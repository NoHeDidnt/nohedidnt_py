# -*- coding: utf-8 -*-
from tests.context import *


# Lists ---------------------------------------


@pytest.fixture
def duplicates_list():
    return ["TestString", "TestString"]


@pytest.fixture
def empties_list():
    return ["TestString", ""]


# Strings -------------------------------------


@pytest.fixture
def bool_string():
    return "True"


@pytest.fixture
def caller_string():
    return "Testing"


@pytest.fixture
def camel_string():
    return "TestString"


@pytest.fixture
def float_string():
    return "420.69"


@pytest.fixture
def int_string():
    return "69"


@pytest.fixture
def msg_string():
    return "Test Message"


@pytest.fixture
def path_string():
    return "."


# Others --------------------------------------


@pytest.fixture
def nhd_int():
    return 69
