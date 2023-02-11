# -*- coding: utf-8 -*-
from tests.context import *


def test_always_fails():
    assert False, "This test fails always."


def test_always_passes():
    assert True
