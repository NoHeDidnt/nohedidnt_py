# -*- coding: utf-8 -*-
from nohedidnt_py.helpers import *


# Model
NhdCatalogueStack = create_model("NhdCatalogueStack", __config__=NhdConfig, **nhd_catalogues_box())

nhd_catalogue_stack = NhdCatalogueStack()
