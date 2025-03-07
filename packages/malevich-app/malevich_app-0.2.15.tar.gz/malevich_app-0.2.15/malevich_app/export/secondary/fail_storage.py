import os
import shutil
from pathlib import Path
from typing import Optional, Dict, Any, List, Union, Callable
from malevich_app.export.abstract.abstract import FailStructure, FixScheme, LocalScheme
from malevich_app.export.secondary.collection.CompositeCollection import CompositeCollection
from malevich_app.export.secondary.collection.LocalCollection import LocalCollection
from malevich_app.export.secondary.collection.ObjectCollection import ObjectCollection
from malevich_app.export.secondary.helpers import save_collection_json, save_collection_pandas, coll_obj_path


class FailStorage:
    collections_dir = "collections"
    objects_dir = "objects"
    fail_struct_name = "fail.json"

    def __init__(self, path: str, copy_obj: bool = False, schemes: Optional[Dict[str, LocalScheme]] = None):
        self.__path = path
        self.__copy_obj = copy_obj
        self.__schemes: Optional[Dict[str, LocalScheme]] = schemes

    def __collection(self, julius_app, coll: Union[LocalCollection, ObjectCollection, CompositeCollection], operation_id: str, path_by_operation_id: Callable[[str], str], path_objs: str) -> Union[str, List[str]]:
        if isinstance(coll, LocalCollection):
            coll_id = coll.get()
            data, scheme_name = julius_app.local_dfs.get(coll_id)

            scheme = None if scheme_name is None else FixScheme(schemeName=scheme_name).dict()
            if coll.is_doc():
                save_collection_json(data, operation_id, scheme, coll_id=coll_id, path_by_operation_id=path_by_operation_id)
            else:
                save_collection_pandas(data, operation_id, scheme, coll_id=coll_id, path_by_operation_id=path_by_operation_id, save_format="csv")   # force save csv
            return str(coll_id)
        elif isinstance(coll, ObjectCollection):
            if self.__copy_obj:
                path = coll_obj_path(julius_app, coll.get())
                path_to = os.path.join(path_objs, path)
                if Path(path).is_file():
                    shutil.copy(path, path_to)
                elif Path(path).is_dir():
                    shutil.copytree(path, path_to)
            return coll.get(with_prefix=True)
        elif isinstance(coll, CompositeCollection):
            res = []
            for subcoll in coll:
                res.append(self.__collection(julius_app, subcoll, operation_id, path_by_operation_id, path_objs))
            return res
        else:
            raise Exception(f"unexpected collection type: {type(coll)}")

    @staticmethod
    def prefix(path: str, operation_id: str, run_id: str, bind_id: str) -> str:
        return os.path.join(path, operation_id, run_id, bind_id)

    def save(self, julius_app, operation_id: str, run_id: str, bind_id: str, iteration: int, is_processor: bool, err_msg: str, cfg: Optional[Dict[str, Any]], collections_list: List[List[Union[LocalCollection, ObjectCollection, CompositeCollection, List[Union[LocalCollection, ObjectCollection, CompositeCollection]]]]]):
        prefix = self.prefix(self.__path, operation_id, run_id, bind_id)
        prefix_collections = os.path.join(prefix, self.collections_dir)
        prefix_objects = os.path.join(prefix, self.objects_dir)
        os.makedirs(prefix_collections, exist_ok=True)
        path_by_operation_id = lambda _: prefix_collections

        args: List[List[Union[Union[str, List[str]], List[Union[str, List[str]]]]]] = []
        for collections in collections_list:
            subargs = []
            for collection in collections:
                if isinstance(collection, List):
                    subsubargs = []
                    for subcollection in collection:
                        subsubargs.append(self.__collection(julius_app, subcollection, operation_id, path_by_operation_id, prefix_objects))
                    subargs.append(subsubargs)
                else:
                    subargs.append(self.__collection(julius_app, collection, operation_id, path_by_operation_id, prefix_objects))
            args.append(subargs)

        struct = FailStructure(
            operationId=operation_id,
            runId=run_id,
            bindId=bind_id,
            funId=julius_app.fun_id,
            iteration=iteration,
            is_processor=is_processor,
            err=err_msg,
            cfg=cfg,
            schemes=self.__schemes,
            args=args,
            args_names=list(julius_app.fun_arguments),
        )
        with open(os.path.join(prefix, self.fail_struct_name), 'w') as f:
            f.write(struct.model_dump_json())
