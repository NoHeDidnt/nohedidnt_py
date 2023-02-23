# -*- coding: utf-8 -*-
from tests.context import *


def test_catalogue():
    assert isinstance(nhd_catalogue_stack, NhdCatalogueStack)
    assert isinstance(nhd_catalogue_stack.enums, catalogue.Registry)
    assert len(nhd_catalogue_stack.enums.get_all()) == len(const.CATALOGUES.get("enums", list()))
    assert "box_type" in nhd_catalogue_stack.enums


def test_strict_constants():
    assert const is not None

    with pytest.raises(FrozenInstanceError):
        const.PKG_ABBR = "test"
