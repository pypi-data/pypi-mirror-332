import json
import logging
import os
import pathlib
import shutil
import traceback
import uuid
from asyncio import Future
import websockets
import malevich_app.export.secondary.LogHelper as lh
import malevich_app.export.secondary.const as C
from typing import Optional, Union, Dict, Any, Callable, Tuple
from malevich_coretools import AUTH, get_collection_object, get_collection_objects, get_ws_app, create_ws_app, JsonImage
from malevich_app.export.abstract.abstract import InitPipeline, InitRun, RunPipeline, FunMetadata, AppFunctionsInfo, \
    LocalRunStruct, Image, PipelineStructureUpdate, Cfg, LocalScheme, FailStructure, WSMessage, WSInitSettings
from malevich_app.export.abstract.pipeline import Pipeline, Processor, AlternativeArgument, Result, Condition, \
    BaseArgument
from malevich_app.export.jls.JuliusPipeline import JuliusPipeline
from malevich_app.export.jls.JuliusRegistry import JuliusRegistry
from malevich_app.export.jls.LocalLogsBuffer import LocalLogsBuffer
from malevich_app.export.secondary.State import states, State
from malevich_app.export.secondary.collection.ObjectCollection import ObjectCollection
from malevich_app.export.secondary.const import MOUNT_PATH_OBJ, FAILS_DIR
from malevich_app.export.secondary.endpoints import reset_core_endpoints
from malevich_app.export.secondary.fail_storage import FailStorage
from malevich_app.export.secondary.helpers import send_background_task
from malevich_app.export.secondary.logger import logfile
from malevich_app.export.secondary.zip import unzip_files
from malevich_app.local.LocalStorage import LocalStorage
from malevich_app.local.log import base_logger_fun
from malevich_app.local.utils import init_settings, scheme_class_columns, fix_cfg
from malevich_app.ws.EventWaiter import waiter
from malevich_app.ws.mapping import operations_mapping
from malevich_app.ws.utils import ws_call


class LocalRunner:
    def __init__(self, local_settings: LocalRunStruct, logger_fun: Optional[Callable[[str, Optional[str], Optional[str], bool], logging.Logger]] = None):
        init_settings(local_settings)

        self.__local_schemes: Dict[str, LocalScheme] = {}
        self.__logger_fun = logger_fun if logger_fun is not None else base_logger_fun
        self.__registry = JuliusRegistry(local_settings.import_dirs, logger_fun=self.__logger_fun)
        self.__storage: LocalStorage = LocalStorage(local_settings, {k: scheme_class_columns(v) for k, v in self.__registry.schemes().items()}, self.__local_schemes)
        self.__registry._set_local_storage(self.__storage)
        self.__local_settings = local_settings
        self.__secret = str(uuid.uuid4())   # FIXME one secret for operation_id
        self.__fail_dir = None
        lh.log_on = False

    @property
    def app_info(self) -> AppFunctionsInfo:
        with open(os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "version"), 'r') as f:
            version = f.readline()
        try:
            self.__registry.info.version = version
            return self.__registry.info
        except:
            return AppFunctionsInfo(logs=traceback.format_exc(), version=version)

    @property
    def storage(self) -> LocalStorage:
        return self.__storage

    async def __init(self, init: InitPipeline):
        state = states.get(init.operationId)
        assert state is None, f"pipeline already inited, operationId {init.operationId}"

        try:
            state = State(init.operationId, init.schemesNames, init.scale, logs_buffer=LocalLogsBuffer(self.__logger_fun, init.operationId))
            states[init.operationId] = state
            fail_storage = None if (path := self.__storage.fail_dir) is None else FailStorage(path, copy_obj=True, schemes=self.__local_schemes)
            j_pipeline = JuliusPipeline(init, self.__registry, state.logs_buffer, storage=self.__storage, fail_storage=fail_storage)
            state.pipeline = j_pipeline
            state.schemes_names.update(j_pipeline.scheme_aliases())
            j_pipeline.set_exist_schemes(None, state.schemes_names)

            await self.__registry.update_schemes_pipeline(init.operationId)
        except BaseException as ex:
            if state is not None:
                state.logs_buffer.write(f"{traceback.format_exc()}\n")
            states.pop(init.operationId, None)
            raise Exception("init pipeline failed") from ex

        if not await j_pipeline.init():
            states.pop(init.operationId, None)
            raise Exception("init failed")

        self.__registry.save_schemes(init.operationId)  # TODO not need local?

    async def __init_run(self, init: InitRun):
        state = states.get(init.operationId)
        assert state is not None, f"wrong operationId {init.operationId}"

        if state.pipeline is None:
            state.logs_buffer.write("error: init_run pipeline failed before, can't run\n")
        try:
            res = await state.pipeline.init_run(init)
            assert res, "not init"
            state.pipeline.set_exist_schemes(init.runId, state.schemes_names)
        except BaseException as ex:
            raise Exception("init_run failed") from ex

    async def __run(self, run: RunPipeline):
        state = states.get(run.operationId)
        assert state is not None, f"wrong operationId {run.operationId}"

        if not state.pipeline.exist_run(run.runId):
            state.logs_buffer.write(f"/run/pipeline wrong runId {run.runId}\n")
            raise Exception(f"runId {run.runId} already exist")

        state.pipeline.set_index(run.runId, run.index)  # TODO check that it work
        try:
            ok = await state.pipeline.run(run.runId, run.iteration, run.bindId, run.data, run.conditions, run.structureUpdate, run.bindIdsDependencies)
        except BaseException as ex:
            state.logs_buffer.write(traceback.format_exc())
            raise Exception("run failed") from ex
        if not ok:
            raise Exception("run failed")

    async def __finish(self, metadata: FunMetadata):
        state = states.get(metadata.operationId)
        assert state is not None, f"finish wrong operationId {metadata.operationId}"
        if metadata.runId is None:
            states.pop(metadata.operationId)
        else:
            state.pipeline.delete_run(metadata.runId)

    async def prepare(self, pipeline: Pipeline, cfg: Optional[Union[Dict[str, Any], str, Cfg]] = None, debug_mode: bool = False, profile_mode: Optional[str] = None) -> str:
        if cfg is not None:
            cfg = fix_cfg(cfg)

        operation_id = str(uuid.uuid4())

        pipeline = InitPipeline(
            cfg=cfg,
            infoUrl=None,
            debugMode=debug_mode,
            profileMode=profile_mode,
            operationId=operation_id,
            dagHost="",     # TODO ok?

            login=self.__local_settings.login,
            pipeline=pipeline,
            schemesNames=[],
            image=Image(ref=""),
            scale=1,
            processorIds=set(pipeline.processors.keys()),
            secret=self.__secret,
            singlePod=True,
            continueAfterProcessor=False,
        )
        await self.__init(pipeline)
        return operation_id

    async def run(self, operation_id: str, run_id: str, cfg: Optional[Union[Dict[str, Any], str, Cfg]] = None, debug_mode: bool = False, profile_mode: Optional[str] = None):
        if cfg is not None:
            cfg = fix_cfg(cfg)

        init = InitRun(
            cfg=cfg,
            infoUrl=None,
            debugMode=debug_mode,
            profileMode=profile_mode,
            operationId=operation_id,
            dagHost="",

            runId=run_id,
            kafkaInitRun=None,
        )
        await self.__init_run(init)
        run = RunPipeline(
            runId=run_id,
            operationId=operation_id,

            iteration=0,
            bindId="",  # not matter
            data=None,
            conditions=None,
            index=0,
            structureUpdate=PipelineStructureUpdate(),
            bindIdsDependencies=None,
        )
        await self.__run(run)

    async def stop(self, operation_id: str, run_id: Optional[str] = None):
        metadata = FunMetadata(
            runId=run_id,
            operationId=operation_id,
        )
        await self.__finish(metadata)

    async def run_full(self, pipeline: Pipeline, cfg: Optional[Union[Dict[str, Any], str, Cfg]] = None, debug_mode: bool = False, profile_mode: Optional[str] = None) -> str:
        if cfg is not None:
            cfg = fix_cfg(cfg)

        operation_id = await self.prepare(pipeline, None, debug_mode, profile_mode)
        run_id = ""
        await self.run(operation_id, run_id, cfg, debug_mode, profile_mode)
        await self.stop(operation_id, run_id)
        return operation_id

    def __fail_dir_update(self) -> str:
        if self.__fail_dir is None:
            self.__fail_dir = self.__storage.fail_dir
            self.__storage.fail_dir = None
        return self.__fail_dir

    @staticmethod
    def __recognize_run_id_bind_id(prefix: str, run_id: Optional[str], bind_id: Optional[str]) -> Union[str, str]:
        if run_id is None:
            if bind_id is not None:
                if os.path.isfile(os.path.join(prefix, bind_id, FailStorage.fail_struct_name)):
                    return "", bind_id
                else:
                    for name in os.listdir(prefix):
                        if os.path.isdir(os.path.join(prefix, name)) and os.path.isfile(os.path.join(prefix, name, bind_id, FailStorage.fail_struct_name)):
                            return name, bind_id
            else:
                for name in os.listdir(prefix):
                    temp_prefix = os.path.join(prefix, name)
                    if os.path.isdir(temp_prefix):
                        for subname in os.listdir(temp_prefix):
                            if os.path.isfile(os.path.join(temp_prefix, subname)):
                                if subname == FailStorage.fail_struct_name:
                                    return "", name
                            elif os.path.isdir(os.path.join(temp_prefix, subname)) and os.path.isfile(os.path.join(temp_prefix, subname, FailStorage.fail_struct_name)):
                                return name, subname
        else:
            if bind_id is not None:
                if os.path.isfile(os.path.join(prefix, run_id, bind_id, FailStorage.fail_struct_name)):
                    return run_id, bind_id
            else:
                for name in os.listdir(os.path.join(prefix, run_id)):
                    if os.path.isdir(os.path.join(prefix, run_id, name)) and os.path.isfile(os.path.join(prefix, run_id, name, FailStorage.fail_struct_name)):
                        return run_id, name
        raise Exception("Unable to find the configuration of the run, please check if it is correct `run_id` and `bind_id`")

    async def reproduce_prepare(self, operation_id: str, run_id: Optional[str] = None, bind_id: Optional[str] = None, force_reload: bool = False, *, auth: Optional[AUTH] = None, conn_url: Optional[str] = None) -> Tuple[str, str, str]:
        """
        It's worth running once before "reproduce" after a failed non-local run

        Return operation_id, run_id, bind_id
        """
        fail_dir = self.__fail_dir_update()
        assert fail_dir is not None, "results_dir and fail_dir is None in LocalRunStruct"
        prefix = FailStorage.prefix(fail_dir, operation_id, "", "")

        if not force_reload and os.path.exists(prefix):
            try:
                run_id, bind_id = self.__recognize_run_id_bind_id(prefix, run_id, bind_id)
                return operation_id, run_id, bind_id
            except:
                pass    # not found local

        if run_id is not None:
            if bind_id is None:
                files_dirs = get_collection_objects(FailStorage.prefix(FAILS_DIR, operation_id, run_id, ""), recursive=True, auth=auth, conn_url=conn_url)
                for name in files_dirs.files.keys():
                    if name.endswith(f"/{FailStorage.fail_struct_name}"):
                        name = name.removesuffix(f"/{FailStorage.fail_struct_name}")
                        if "/" not in name:
                            bind_id = name
                            break
        else:
            files_dirs = get_collection_objects(FailStorage.prefix(FAILS_DIR, operation_id, "", ""), recursive=True, auth=auth, conn_url=conn_url)
            for name in files_dirs.files.keys():
                if name.endswith(f"/{FailStorage.fail_struct_name}"):
                    name = name.removesuffix(f"/{FailStorage.fail_struct_name}")
                    dirs = name.split("/")
                    if len(dirs) == 1:
                        run_id, bind_id = "", dirs[0]
                        break
                    elif len(dirs) == 2:
                        run_id, bind_id = dirs[0], dirs[1]
                        break
        assert run_id is not None and bind_id is not None, f"not exist fail run"

        zip_bytes = get_collection_object(FailStorage.prefix(FAILS_DIR, operation_id, run_id, bind_id), auth=auth, conn_url=conn_url)
        prefix = os.path.join(prefix, run_id, bind_id)
        if os.path.exists(prefix):
            shutil.rmtree(prefix, ignore_errors=True)
        os.makedirs(prefix)
        fail_zip_path = os.path.join(prefix, "fail.zip")
        with open(fail_zip_path, 'wb') as f:
            f.write(zip_bytes)
        unzip_files(fail_zip_path, prefix)

        return operation_id, run_id, bind_id

    async def reproduce(self, operation_id: str, run_id: Optional[str] = None, bind_id: Optional[str] = None, debug_mode: bool = True, profile_mode: Optional[str] = None, force_copy_objects: bool = False):
        """
        Runs a previously failed run locally (specifically a failed function), it is worth calling "reproduce_prepare" once before to get the necessary files
        """
        fail_dir = self.__fail_dir_update()
        assert fail_dir is not None, "results_dir and fail_dir is None in LocalRunStruct"
        prefix = FailStorage.prefix(fail_dir, operation_id, "", "")
        assert os.path.exists(prefix), f"not exist fail run with operation_id={operation_id}, call reproduce_prepare"

        run_id, bind_id = self.__recognize_run_id_bind_id(prefix, run_id, bind_id)
        prefix = os.path.join(prefix, run_id, bind_id)

        prefix_collections = os.path.join(prefix, FailStorage.collections_dir)
        prefix_objects = os.path.join(prefix, FailStorage.objects_dir)
        real_prefix_objects = os.path.join(MOUNT_PATH_OBJ, self.__local_settings.login)
        if force_copy_objects:
            shutil.copytree(prefix_objects, real_prefix_objects, dirs_exist_ok=True)
        else:
            os.makedirs(real_prefix_objects, exist_ok=True)

        with open(os.path.join(prefix, FailStorage.fail_struct_name), 'r') as f:
            struct = FailStructure.model_validate_json(f.read())
        if struct.schemes is not None:
            self.__storage._schemes_consider(struct.schemes)

        def coll_id(arg: str) -> str:
            if arg.startswith(ObjectCollection.prefix):
                path = os.path.join(real_prefix_objects, arg.removeprefix(ObjectCollection.prefix))
                if not os.path.exists(path):
                    path_from = os.path.join(prefix_objects, arg.removeprefix(ObjectCollection.prefix))
                    assert os.path.exists(path_from), f"object collection not exist: {arg.removeprefix(ObjectCollection.prefix)}"
                    path_from = pathlib.Path(path_from)
                    if path_from.is_file():
                        shutil.copy(path_from, path)
                    elif path_from.is_dir():
                        shutil.copytree(path_from, path)
                coll_id = ObjectCollection.prefix + self.__storage.data(path=path)
            else:
                coll_id = self.__storage.data(path=os.path.join(prefix_collections, arg, "data"))
            return coll_id

        assert len(struct.args_names) == len(struct.args), "wrong arguments count"
        arguments = {}
        for name, arg in zip(struct.args_names, struct.args):   # not supported arg like List[List[str]] and hard dfs case yet
            if len(arg) == 1:
                arg = arg[0]
            if isinstance(arg, str):
                arguments[name] = AlternativeArgument(collectionId=coll_id(arg))
            else:
                group = []
                for subarg in arg:
                    if isinstance(subarg, list) and len(subarg) == 1:
                        subarg = subarg[0]
                    assert isinstance(subarg, str), "not supported hard cases arguments"
                    group.append(BaseArgument(collectionId=coll_id(subarg)))
                arguments[name] = AlternativeArgument(group=group)
        cfg = Cfg()

        if struct.is_processor:
            pipeline = Pipeline(
                pipelineId=f"reproduce_{struct.operationId}",
                processors={
                    struct.bindId: Processor(
                        processorId=struct.funId,
                        cfg=None if struct.cfg is None else json.dumps(struct.cfg),
                        image=JsonImage(ref=""),
                        arguments=arguments,
                    )
                },
                results={
                    struct.bindId: [Result(
                        name=f"reproduce_{struct.operationId}",
                    )],
                }
            )
        else:
            pipeline = Pipeline(
                pipelineId="reproduce",
                conditions={
                    struct.bindId: Condition(
                        processorId=struct.funId,
                        cfg=None if struct.cfg is None else json.dumps(struct.cfg),
                        image=JsonImage(ref=""),
                        arguments=arguments,
                    )
                },
            )
        return await self.run_full(pipeline, cfg, debug_mode=debug_mode, profile_mode=profile_mode)

    def __ws_set_internals(self, ws, id: str, core_host: str, core_port: str, save_df_format: str):
        import malevich_app.export.api.api as api
        api.registry = self.__registry

        C.IS_EXTERNAL = True
        C.LOGS_STREAMING = False
        C.WS = ws
        C.APP_ID = id
        C.CORE_HOST = core_host
        C.CORE_PORT = core_port
        C.CORE_HOST_PORT = f"http://{C.CORE_HOST}:{C.CORE_PORT}"
        C.SAVE_DF_FORMAT = save_df_format
        reset_core_endpoints()
        open(logfile, 'a').close()

    def __ws_unset_internals(self):
        C.WS = None
        C.APP_ID = "app"
        C.IS_EXTERNAL = False
        C.SAVE_DF_FORMAT = "csv"

    async def __sync_objects(self, sync_objects: Optional[Any] = None):
        pass    # TODO init sync objects

    async def ws(self, id: Optional[str] = None, secret: Optional[str] = None, dm_url: str = "localhost:8000", sync_objects: Optional[Any] = None, secure: bool = True):
        if id is not None:
            if secret is None:
                ws_app = get_ws_app(id)
                secret = ws_app.secret
        else:
            assert secret is None, "id not set"
            ws_app = create_ws_app()
            id = ws_app.id
            secret = ws_app.secret

        def future_callback(future: Future[None]):
            if (ex := future.exception()) is not None:
                print(ex)

        async with websockets.connect(f"{'wss' if secure else 'ws'}://{dm_url}/ws/app?id={id}&secret={secret}", ping_interval=3600, ping_timeout=5) as ws:
            data = await ws.recv()
            if data.startswith("internal error: "):
                raise Exception(data)

            init_msg = WSInitSettings.model_validate_json(data)
            assert init_msg.id == id, "wrong id"

            await self.__sync_objects(sync_objects)

            print(id)

            try:
                self.__ws_set_internals(ws, id, init_msg.core_host, init_msg.core_port, init_msg.save_df_format)

                while True:
                    data = await ws.recv()

                    if data.startswith("internal error: "):
                        raise Exception(data)

                    try:
                        msg = WSMessage.model_validate_json(data)
                        handled = waiter.set_result(msg)
                    except:
                        print(traceback.format_exc())
                        continue

                    if not handled:
                        f = operations_mapping.get(msg.operation)
                        if f is None:
                            print(f"unknown operation: {msg.operation}")
                            continue

                        future = send_background_task(ws_call, ws, f, msg, ignore_errors=True)
                        future.add_done_callback(future_callback)
            finally:
                self.__ws_unset_internals()
