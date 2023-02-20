# -*- coding: utf-8 -*-
from tests.context import *


def test_format_msg(msg_string):
    formatted_msg = format_msg(msg_string)
    
    assert isinstance(formatted_msg, str)
    assert msg_string in formatted_msg
    assert PKG_ABBR in formatted_msg


def test_nhd_debug(msg_string):
    """
        GIVEN msg_string
        WHEN nhd_debug is called
        THEN None is returned
    """
    
    assert nhd_debug(msg_string) is None
