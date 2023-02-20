# -*- coding: utf-8 -*-
import os

from pathlib import Path
from typing import Any, AnyStr, Callable, Dict, List, Optional, Tuple, Union


from box import Box, BoxList
from devtools import debug
from dotenv import dotenv_values
from typeguard.importhook import install_import_hook


# Any -----------------------------------------

AnyBox = Union[Box, "AnyDict"]
AnyCallable = Callable[..., Any]
AnyDict = Dict[str, Any]
AnyList = Union[BoxList, List[Any]]
AnyNum = Union[float, int]
AnyPath = Union[Path, str]
AnyTupl = Tuple[Any, ...]


# Tuple(s) ------------------------------------

ListTupl = Tuple[AnyList, ...]
PkgTupl = Tuple[str, str, AnyPath, str]
StrTupl = Tuple[str, ...]


# List(s) -------------------------------------

PathList = List[AnyPath]
StrList = List[str]


# Optional ------------------------------------

OptBool = Optional[bool]
OptBox = Optional[AnyBox]
OptCallable = Optional[AnyCallable]
OptDict = Optional[AnyDict]
OptInt = Optional[int]
OptList = Optional[AnyList]
OptNum = Optional[AnyNum]
OptPath = Optional[AnyPath]
OptStr = Optional[str]
OptTupl = Optional[AnyTupl]
OptType = Optional[type]
