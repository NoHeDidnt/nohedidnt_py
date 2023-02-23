# -*- coding: utf-8 -*-
from tests.context import *


def test_find_empty_values():
    if not callable(find_empty_values):
        raise ValueError("Invalid find_empty_values")
    
    search_result = find_empty_values()
    assert isinstance(search_result, list)
    assert "None" in search_result
    assert None in search_result


# Dates & Times -------------------------------


def test_datetime_now():
    """Includes: format_datetime"""
    
    if not callable(datetime_now):
        raise ValueError("Invalid datetime_now")
    
    result = datetime_now()
    format_result = datetime_now(frmt=const.DT_FORMAT)
    
    assert isinstance(result, datetime)
    assert isinstance(format_result, str)


# Factories -----------------------------------


def test_nhd_box():
    value = nhd_box(box_type=NhdBoxType.default)
    assert isinstance(value, Box)


def test_nhd_timer():
    timer = nhd_timer(logger=None)

    assert isinstance(timer, Timer)
    assert isinstance(timer.stop(), float)


# Formatting ----------------------------------


def test_format_msg(msg_string):
    formatted_msg = format_msg(msg_string)

    assert isinstance(formatted_msg, str)
    assert msg_string in formatted_msg
    assert const.PKG_ABBR in formatted_msg


# Logging -------------------------------------


def test_nhd_debug(msg_string):
    """
    GIVEN msg_string
    WHEN nhd_debug is called
    THEN None is returned
    """

    assert nhd_debug(msg_string) is None


# Parsing -------------------------------------


def test_detect_encoding():
    """Includes: request_data"""
    rawdata = request_data(content=True)
    
    if not isinstance(rawdata, (bytes, bytearray)):
        raise ValueError("Invalid rawdata")
    
    data_encoding = detect_encoding(rawdata)
    
    assert isinstance(data_encoding, str)


def test_kill_duplicates(camel_string, duplicates_list):
    if not callable(kill_duplicates):
        raise ValueError("Invalid kill_duplicates")
    
    result = kill_duplicates(duplicates_list)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert camel_string in result


def test_kill_empties(camel_string, empties_list):
    if not callable(kill_empties):
        raise ValueError("Invalid kill_empties")
    
    result = kill_empties(empties_list)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert camel_string in result


# TypeConversions -----------------------------


def test_bool_from_value(bool_string):
    assert callable(bool_from_value)
    assert isinstance(bool_from_value(bool_string), bool)


def test_continent_name_from_value():
    assert callable(continent_from_value)
    
    continent = continent_from_value("Germany")
    
    assert isinstance(continent, NhdContinent)
    assert continent == NhdContinent.europe


def test_float_from_value(float_string):
    assert callable(float_from_value)
    assert isinstance(float_from_value(float_string), float)


def test_int_from_value(int_string):
    assert callable(int_from_value)
    assert isinstance(int_from_value(int_string), int)


def test_path_from_value(path_string):
    assert callable(path_from_value)
    assert isinstance(path_from_value(path_string), Path)


def test_string_from_value(nhd_int):
    assert callable(string_from_value)
    assert isinstance(string_from_value(nhd_int), str)
