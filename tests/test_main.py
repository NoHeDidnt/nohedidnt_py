# -*- coding: utf-8 -*-
from tests.context import *


# Catalogues ----------------------------------


def test_configs_catalogue():
    assert isinstance(configs_catalogue, Registry)
    assert len(configs_catalogue.get_all()) > 0
    assert "default" in configs_catalogue


def test_enums_catalogue():
    assert isinstance(enums_catalogue, Registry)
    assert len(enums_catalogue.get_all()) > 0
    assert "box_type" in enums_catalogue
    assert "continent" in enums_catalogue


def test_helpers_catalogue():
    assert isinstance(helpers_catalogue, Registry)
    assert len(helpers_catalogue.get_all()) > 0
    assert "nhd_debug" in helpers_catalogue


# Constants -----------------------------------


def test_strict_constants():
    assert const is not None

    with pytest.raises(FrozenInstanceError):
        const.PKG_ABBR = "test"
