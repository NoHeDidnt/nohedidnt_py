# -*- coding: utf-8 -*-
from nohedidnt_py.aliases import *


CALL_CHR = " > "
JOIN_CHR = ", "

ABBR_LEN = 6
CALL_LEN = ABBR_LEN * 2
KEY_LEN = CALL_LEN * 2

DFLT_COLS = 80
DISPLAY_COLS = DFLT_COLS * 2


# Formats -------------------------------------

CALL_FORMAT = str(CALL_LEN).join(["{:>", "}"])
MSG_FORMAT = CALL_CHR.join([CALL_FORMAT, "{}"])


# Package -------------------------------------

PKG_ABBR = "nhd"
PKG_AUTHOR = "NoHeDidn't"
PKG_NAME = "nohedidnt_py"


# Paths ---------------------------------------

DATA_DIR, DEBUG_FILE, ENV_FILE, LOG_FILE, PROJS_DIR = None, None, None, None, None


""" Helpers ------------------------------- """


def nhd_pkg_env_info(value: OptPath = None) -> StrTupl:
    env_values = Box(os.environ.copy())

    if value is not None:
        env_values.merge_update(dotenv_values())

    return env_values.get("PKG_ABBR", PKG_ABBR), env_values.get("PKG_AUTHOR", PKG_AUTHOR)


def nhd_pkg_name(value: Path) -> str:
    """
    Get package name
    
    DOCS Description
    
    :param value: a Path
    :return: package name
    :rtype: str
    """
    
    if not value.is_dir():
        raise ValueError("Invalid value")

    if value.stem == "core":
        value = value.parent

    return value.stem


def nhd_pkg_info(value: OptPath = None) -> PkgTupl:
    if value is None:
        value = Path().resolve()

    if not isinstance(value, Path) or not value.exists() or not value.is_dir():
        raise ValueError("Invalid value")

    home_dir = Path.home()
    if not isinstance(home_dir, Path) or not home_dir.exists() or not home_dir.is_dir():
        raise ValueError("Invalid home_dir")

    name = nhd_pkg_name(value)
    name_count = value.parts.count(name)

    while name_count > 1:
        value = value.parent
        name_count = value.parts.count(name)

        if name_count <= 1:
            break

    if not value.is_dir() or home_dir not in value.parents:
        raise ValueError("Invalid value")

    env_info = nhd_pkg_env_info(value.joinpath(".env"))
    
    return env_info[0], env_info[1], value, name


""" Dynamic ------------------------------- """


pkg_info = nhd_pkg_info()
if not isinstance(pkg_info, tuple) or not len(pkg_info) == 4:
    raise ValueError("Invalid pkg_info")

PKG_ABBR, PKG_AUTHOR, PKG_DIR, PKG_NAME = pkg_info
if isinstance(PKG_DIR, Path) and isinstance(PKG_NAME, str):
    PROJS_DIR = PKG_DIR.parent
    DATA_DIR = PKG_DIR.joinpath("data")
    ENV_FILE = PKG_DIR.joinpath(".env")
    DEBUG_FILE = DATA_DIR.joinpath("debug.json")
    LOG_FILE = DATA_DIR.joinpath("logs", f"{PKG_NAME}.log")
    
    # TypeGuard
    install_import_hook(PKG_NAME)
