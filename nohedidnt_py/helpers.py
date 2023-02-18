# -*- coding: utf-8 -*-
from nohedidnt_py.constants import *


def nhd_debug(msg: str, caller: str = PKG_ABBR) -> None:
    msg = format_msg(msg, caller, length=DISPLAY_COLS)
    debug(msg)


def format_msg(msg: str, caller: str = PKG_ABBR, length: OptInt = None, msg_format: str = MSG_FORMAT, title: bool = False) -> str:
    # Caller
    if caller in msg:
        msg = msg.replace(caller, "").strip()

    if len(caller) > CALL_LEN:
        caller = caller[:CALL_LEN]

    # Convert to Title
    if title is True and caller.istitle() is False:
        caller = caller.title()

    # Shorten Message
    if length is not None:
        length -= len(caller) + len(CALL_CHR)

        if len(msg) > length:
            msg = msg[:length]

    return msg_format.format(caller, msg)
