import json
import logging
import os
import sys
import nest_asyncio
import pandas as pd
from typing import List, Dict, Any, Type, Set, Tuple, Union
from pydantic import BaseModel
import malevich_app.export.secondary.const as C
import malevich_app.jls_lib.utils as lib
from malevich_app.export.abstract.abstract import LocalRunStruct, Cfg


def init_settings(local_settings: LocalRunStruct):
    assert len(local_settings.import_dirs) > 0, "empty import dirs"
    if local_settings.workdir is None:
        workdir = local_settings.import_dirs[0]
    else:
        workdir = local_settings.workdir
    if workdir is not None:
        C.WORKDIR = workdir
        C.APP_DIR = f"{workdir}/apps"
        lib.APP_DIR = C.WORKDIR
        lib.WORKDIR = C.APP_DIR

    if local_settings.mount_path is not None:
        C.MOUNT_PATH = local_settings.mount_path
    if local_settings.mount_path_obj is not None:
        C.MOUNT_PATH_OBJ = local_settings.mount_path_obj

    os.makedirs(C.MOUNT_PATH, exist_ok=True)
    os.makedirs(C.MOUNT_PATH_OBJ, exist_ok=True)
    os.makedirs(local_settings.results_dir, exist_ok=True)

    sys.path.append("/")

    logging.getLogger().handlers.clear()

    pd.set_option('display.max_columns', None)
    nest_asyncio.apply()


def fix_cfg(cfg: Union[Dict[str, Any], str, Cfg]) -> str:
    if isinstance(cfg, Cfg):
        for app_setting in cfg.app_settings:
            if isinstance(app_setting.saveCollectionsName, str):
                app_setting.saveCollectionsName = [app_setting.saveCollectionsName]
        cfg_json = cfg.model_dump_json()
    else:
        if isinstance(cfg, str):
            cfg = json.loads(cfg)
        assert isinstance(cfg, dict), "wrong cfg type"
        for app_setting in cfg.get("app_settings", []):
            if isinstance(name := app_setting.get("saveCollectionsName"), str):
                app_setting["saveCollectionsName"] = [name]
        cfg_json = json.dumps(cfg)
    return cfg_json


def filter_columns(names: List[str]) -> List[str]:
    columns = []
    for column in names:
        if column != "__name__" and column != "__id__":
            columns.append(column)
    return columns


def scheme_class_columns(scheme_class: Type[BaseModel]) -> Tuple[List[str], Set[str]]:
    res = scheme_class.model_json_schema()
    return __scheme_dict_columns(res)


def scheme_json_columns(scheme: Union[str, Dict[str, Any]]) -> Tuple[List[str], Set[str]]:
    if isinstance(scheme, str):
        scheme = json.loads(scheme)
    return __scheme_dict_columns(scheme)


def __scheme_dict_columns(scheme_dict: Dict[str, Any]) -> Tuple[List[str], Set[str]]:
    keys = []
    optional_keys = set()
    for k, v in scheme_dict["properties"].items():
        keys.append(k)

        if v.get("optional"):
            optional_keys.add(k)
            continue

        for variant in v.get("anyOf", []):
            if variant.get("type") == "null":
                optional_keys.add(k)
                break
    return keys, optional_keys


def schemes_mapping_by_columns(keys_from: Set[str], keys_to: List[str], optional_keys_to: Set[str]) -> Dict[str, str]:
    res = {}
    if len(keys_from) == len(keys_to):
        equal = True
        for k in keys_to:
            if k not in keys_from:
                equal = False
                break

        if equal:
            for k in keys_to:
                res[k] = k
        else:
            for i, k in enumerate(keys_from):
                res[k] = keys_to[i]
    else:
        contains = False
        for k in keys_to:
            if k not in keys_from:
                contains = False
                break
            res[k] = k

        if not contains:
            if len(keys_from) + len(optional_keys_to) == len(keys_to):
                req_keys_to = []
                for k in keys_to:
                    if k not in optional_keys_to:
                        req_keys_to.append(k)

                return schemes_mapping_by_columns(keys_from, req_keys_to, None)
            else:
                raise Exception(''.join(["schemes mapping fail: [", "|".join(keys_from), "] -> [", "|".join(keys_to), "]"]))

    return res


def remapping(path_prefix: str, coll_id: str, new_coll_id: str, mapping: Dict[str, str], collection_name: str):
    path = os.path.join(path_prefix, coll_id, collection_name)
    new_path = os.path.join(path_prefix, new_coll_id, collection_name)

    df = pd.read_csv(path)
    df = df[list(mapping.keys())].rename(columns=mapping)
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    df.to_csv(new_path, header=True, index=False)

