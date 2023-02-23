# -*- coding: utf-8 -*-
from nohedidnt_py.enums import *


# Defaults
dirty_pkg_names: StrList = ["common", "constants", "core"]
home_dir: Path = Path.home()
pkg_abbr: str = "nhd"
pkg_author: str = "NoHeDidn't"
pkg_dir: Path = Path().resolve()
pkg_name: str = str()

if not pkg_dir.exists() or not pkg_dir.is_dir():
    raise ValueError("Invalid pkg_dir")

if not home_dir.exists() or not home_dir.is_dir():
    raise ValueError("Invalid home_dir")

# Name
if pkg_dir.stem in dirty_pkg_names:
    while pkg_dir.stem in dirty_pkg_names:
        pkg_dir = pkg_dir.parent
        if pkg_dir.stem not in dirty_pkg_names:
            break

pkg_name = pkg_dir.stem
if not isinstance(pkg_name, str):
    raise ValueError("Invalid pkg_name")

# Count
name_count = pkg_dir.parts.count(pkg_name)
while name_count > 1:
    pkg_dir = pkg_dir.parent
    name_count = pkg_dir.parts.count(pkg_name)
    
    if name_count <= 1:
        break

if not pkg_dir.is_dir() or home_dir not in pkg_dir.parents:
    raise ValueError("Invalid pkg_dir")

# Enums
int_enums: EnumList = [NhdBoxType, NhdContinent]
str_enums: EnumList = []

all_enums: EnumList = int_enums + str_enums

# Environment
env_values = Box(os.environ.copy())

if pkg_dir is not None:
    env_values.merge_update(dotenv_values())

if not isinstance(env_values, dict):
    raise ValueError("Invalid env_values")
