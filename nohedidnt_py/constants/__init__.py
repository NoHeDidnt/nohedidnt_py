# -*- coding: utf-8 -*-
from nohedidnt_py.configs import *
from nohedidnt_py.constants._dynamic import *


# Constants -----------------------------------


@dataclass(config=NhdConfig, frozen=True)
class NhdConstants:
    # Dynamic
    PKG_ABBR: str = pkg_abbr
    PKG_AUTHOR: str = pkg_author
    PKG_DIR: Path = pkg_dir
    PKG_NAME: str = pkg_name
    # Package
    PKG_TITLE_SHORT: str = f"{PKG_AUTHOR}-Py"
    PKG_TITLE: str = f"{PKG_TITLE_SHORT}thon Library"
    PKG_DESCRIPTION: str = f"{PKG_TITLE} ..."
    # Paths
    PROJS_DIR: Path = PKG_DIR.parent
    DATA_DIR: Path = PKG_DIR.joinpath("data")
    ENV_FILE: Path = PKG_DIR.joinpath(".env")
    DEBUG_FILE: Path = DATA_DIR.joinpath("debug.json")
    LOG_FILE: Path = DATA_DIR.joinpath("logs", f"{PKG_NAME}.log")
    # CLI
    CLI_EPILOG: str = f"Thank you, for using {PKG_TITLE_SHORT}!"
    # Blanks
    OBJ_BLK = object()
    SPC_CHR = " "
    STR_BLK = ""
    TD_BLK = timedelta()
    # Chars
    CALL_CHR = " > "
    DIV_CHR = "-"
    JOIN_CHR = ", "
    SNK_CHR = "_"
    # Numbers
    ABBR_LEN = 6
    CALL_LEN = ABBR_LEN * 2
    DFT_COLS = 80
    DISPLAY_COLS = DFT_COLS * 2
    FACTOR_PRECISION = 10
    KEY_LEN = CALL_LEN * 2
    LOG_BACKUPS = 3
    LOOPS_MAX = 1
    MARGIN_FACTOR = 0.05
    SHORT_COLS = 48
    STR_LEN = 191
    # FileInfos
    ENCODING_ALT = "iso8859_2"
    ENCODING_DFT = "utf-8"
    KB_BS = 1024
    MB_KBS = 1024
    GB_MBS = 1024
    MB_BS = MB_KBS * KB_BS
    GB_BS = GB_MBS * MB_BS
    # Dates & Times
    DAY_HRS = 24
    H_MINS = 60
    DAY_MINS = DAY_HRS * H_MINS
    MONTH_DAYS = 30
    MILSEC_MICSECS = 1000
    MIN_SECS = 60
    DAY_SECS = DAY_MINS * MIN_SECS
    H_SECS = H_MINS * MIN_SECS
    SEC_MILSECS = 1000
    SEC_MICSECS = SEC_MILSECS * MILSEC_MICSECS
    MIN_MILSECS = MIN_SECS * SEC_MILSECS
    MIN_MICSECS = MIN_MILSECS * MILSEC_MICSECS
    WEEK_DAYS = 7
    WEEK_HRS = WEEK_DAYS * DAY_HRS
    YEAR_DAYS = 365
    YEAR_MONTHS = 12
    YEAR_QUARTERS = 4
    YEAR_WEEKS = 52
    QUARTER_WEEKS = round(YEAR_WEEKS / YEAR_QUARTERS)
    # Formats
    CALL_FORMAT = str(CALL_LEN).join(["{:>", "}"])
    DT_FORMAT = "%Y-%m-%d %H:%M:%S"
    DT_FORMAT_SHORT = DT_FORMAT.split(" ")[0]
    LOG_CONSOLE_FORMAT = "%(message)s"
    LOG_DFT_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
    MSG_FORMAT = CALL_CHR.join([CALL_FORMAT, "{}"])
    URL_FORMAT = "{}://{}.{}/{}"
    # Locale
    LOCALE_DFT: Locale = Locale.parse("en_US")
    # Logger
    LOG_DIVIDER_LINE = DIV_CHR * DISPLAY_COLS
    LOG_CONSOLE_LEVEL = "notset"
    LOG_DFT_LEVEL = "info"
    LOG_NONE_LEVEL = "notset"
    # URLs
    URL_STATUS = URL_FORMAT.format("https", "status", "iracing.com", "status.json")
    # Lists
    LOG_LEVELS = ["critical", "error", "exception", "warning", "info", "debug"]
    REPL_CHRS = [
        "'",
    ]
    # Collections
    CONVERSIONS = Box(
        factor=Box(
            bar_hg=29.5299801647,
            bar_kpa=100,
            c_f=1.8,
            ftlb_nm=1.3558179483,
            gal_l=3.7854125343,
            kg_lb=2.2046226218,
            km_mi=0.6213711922,
            m_ft=3.28084,
        ),
        offset=Box(
            c_f=32,
        ),
        precision=Box(
            c_f=1,
            kg_lb=0,
        ),
    )
    DETAILS = Box(),
    DIRTIES = Box(
        cls_name=["Meta"],
        path_name=[".DS_Store", ".git", ".idea", ".venv", "_devel"],
        pkg_name=dirty_pkg_names,
    )
    EMPTIES = Box(
        object=[OBJ_BLK],
        str=[STR_BLK, SPC_CHR, str(None), "N/A"],
        test=["TEST"],
        timedelta=[TD_BLK],
    )
    MARGINS = Box(timedelta=timedelta(minutes=1))
    MESSAGES = Box(timer="Finished in {minutes:.2f} minutes.")
    PATTERNS = Box(
        all_cap=(re.compile("([a-z0-9])([A-Z])"), re.sub),
        email=(re.compile(r"/^.+@.+$/w"), re.match),
        first_cap=(re.compile("(.)([A-Z][a-z]+)"), re.sub),
        hex_color=(re.compile(r"/^#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$/"), re.match),
        numbers=(re.compile(r"^\d+$"), re.fullmatch),
        space_cap=(re.compile("( *_+)(_)"), re.sub),
        url=(re.compile(r"/^((https?|ftp|file):\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$/"), re.match),
        vowels=(re.compile("[aeiou]", flags=re.I), re.sub),
    )
    SUFFIXXES = Box(
        binary=[".jpg", ".jpeg", ".png", ".svg", ".zip"],
        document=[".pdf"],
        encoding_alt=[".csv", ".pdf"],
        images=[".jpg", ".jpeg", ".png", ".svg"],
        logs=[".log"],
        serial=[".csv", ".log"],
    )


# const ---------------------------------------

const = NhdConstants()

# TypeGuard
install_import_hook(const.PKG_NAME)
