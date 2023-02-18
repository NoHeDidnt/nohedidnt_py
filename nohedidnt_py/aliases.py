# -*- coding: utf-8 -*-
import os

from pathlib import Path
from typing import Any, Optional, Tuple, Union


from box import Box, BoxList
from devtools import debug
from dotenv import dotenv_values
from typeguard.importhook import install_import_hook


# Any

AnyPath = Union[Path, str]
AnyTupl = Tuple[Any, ...]

# Tuple

PkgTupl = Tuple[AnyPath, str]
StrTupl = Tuple[str, ...]

# Optional

OptInt = Optional[int]
OptPath = Optional[AnyPath]
OptTupl = Optional[AnyTupl]
