# -*- coding: utf-8 -*-
from __future__ import annotations


import difflib
import json
import locale
import logging
import math
import os
import re
import sys
import typing
import urllib.parse
import uuid

from argparse import ArgumentParser as ArgParser, SUPPRESS
from collections import Counter
from dataclasses import FrozenInstanceError
from datetime import datetime, timedelta
from enum import Enum, IntEnum
from logging import Logger, NullHandler, StreamHandler
from logging.handlers import RotatingFileHandler
from pathlib import Path
from re import Pattern
from typing import Any, AnyStr, Callable, ClassVar, Dict, ForwardRef, Generic, IO, Iterable, Iterator, List, Mapping, MutableMapping, NoReturn, Optional, \
    Sequence, Set, Tuple, Type, TypeVar, Union


import catalogue
import chardet
import pycountry
import pycountry_convert
import pytz
import pytz_deprecation_shim as pds
import requests

from babel import Locale
from box import Box, BoxList
from charset_normalizer import from_bytes, from_path
from codetiming import Timer
from colour import Color
from deepdiff import DeepDiff, Delta
from devtools import debug
from dotenv import dotenv_values
from pydantic import AnyHttpUrl, BaseConfig, BaseModel, BaseSettings, create_model, DirectoryPath, EmailStr, Field, FilePath, FutureDate, Json, NameEmail, \
    NegativeFloat, NegativeInt, NoneBytes, NoneStr, NoneStrBytes, NonNegativeFloat, NonNegativeInt, NonPositiveFloat, NonPositiveInt, PastDate, PositiveFloat, \
    PositiveInt, PrivateAttr, root_validator, SecretStr, StrBytes, UUID4, validate_arguments, ValidationError, validator
from pydantic.color import Color as PyColor
from pydantic.dataclasses import dataclass
from pydantic.env_settings import SettingsSourceCallable
from pytz import BaseTzInfo, timezone, utc as UtcTz
from pytz_deprecation_shim._impl import _PytzShimTimezone as ShimTimezone
from typeguard import typechecked, typeguard_ignore
from typeguard.importhook import install_import_hook
from typing_extensions import Final, Literal, TypedDict
from tzlocal import get_localzone, get_localzone_name


# Any -----------------------------------------

AnyBox = Union[Box, "AnyDict"]
AnyBytes = Union[bytes, bytearray]
AnyCallable = Callable[..., Any]
AnyData = Union[AnyBox, "AnyList", "AnyTupl"]
AnyDateTime = Union[datetime, str]
AnyDict = Dict[str, Any]
AnyDiffData = Union[DeepDiff, Delta]
AnyEnum = Union[Enum, IntEnum, "StrEnum"]
AnyEnumValue = Union[int, str]
AnyFileData = Union[AnyBox, AnyStr]
AnyKeys = Union["StrList", str]
AnyList = Union[BoxList, List[Any]]
AnyLogHandler = Union[NullHandler, RotatingFileHandler, StreamHandler]
AnyNhdDate = Union[AnyDateTime, "AnyTimeDelta", "AnyNum"]
AnyNhdVal = Union[AnyData, AnyNhdDate, "AnyPath", "AnyTimezone", "AnyVal", Locale, Timer, type]
AnyNum = Union[float, int]
AnyPath = Union[Path, str]
AnyTimeDelta = Union[timedelta, AnyNum]
AnyTimezone = Union[BaseTzInfo, ShimTimezone]
AnyTupl = Tuple[Any, ...]
AnyVal = Union[AnyDateTime, AnyNum, AnyStr, property]


# TypeVar(s) ----------------------------------

StrEnum = TypeVar("StrEnum", str, Enum)


# Tuple(s) ------------------------------------

HelperTupl = Tuple[AnyCallable, type]
ListTupl = Tuple[AnyList, ...]
PatternTuple = Tuple[Pattern, AnyCallable]
PkgTupl = Tuple[str, str, AnyPath, str]
ReplTupl = Tuple[str, str]
StrTupl = Tuple[str, ...]


# Dict(s) -------------------------------------

HelperDict = Dict[str, HelperTupl]


# List(s) -------------------------------------

DateTimeList = List[AnyDateTime]
EnumList = List[Type[AnyEnum]]
PathList = List[AnyPath]
ReplList = Union[List[ReplTupl], bool]
StrList = List[str]


# Optional ------------------------------------

OptBaseSettings = Optional[BaseSettings]
OptBool = Optional[bool]
OptBox = Optional[AnyBox]
OptBytes = Optional[AnyBytes]
OptCallable = Optional[AnyCallable]
OptColor = Optional[Color]
OptData = Optional[AnyData]
OptDateTime = Optional[AnyDateTime]
OptDict = Optional[AnyDict]
OptDiffData = Optional[AnyDiffData]
OptEnumValue = Optional[AnyEnumValue]
OptFileData = Optional[AnyFileData]
OptHttpUrl = Optional[AnyHttpUrl]
OptInt = Optional[int]
OptKeys = Optional[AnyKeys]
OptList = Optional[AnyList]
OptLocale = Optional[Locale]
OptLogger = Optional[Logger]
OptLogHandler = Optional[AnyLogHandler]
OptNhdDate = Optional[AnyNhdDate]
OptNhdVal = Optional[AnyNhdVal]
OptNum = Optional[AnyNum]
OptPath = Optional[AnyPath]
OptReplList = Optional[ReplList]
OptReplTupl = Optional[ReplTupl]
OptStr = Optional[str]
OptTimeDelta = Optional[AnyTimeDelta]
OptTimer = Optional[Timer]
OptTimezone = Optional[AnyTimezone]
OptTupl = Optional[AnyTupl]
OptType = Optional[type]
OptTzInfo = Optional[BaseTzInfo]
OptVal = Optional[AnyVal]
