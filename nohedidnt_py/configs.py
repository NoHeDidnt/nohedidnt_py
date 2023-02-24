# -*- coding: utf-8 -*-
from nohedidnt_py.aliases import *


@configs_catalogue.register("default")
class NhdConfig(BaseConfig):
    allow_population_by_field_name = True
    anystr_strip_whitespace = True
    arbitrary_types_allowed = True
    smart_union = True
    underscore_attrs_are_private = True
    use_enum_values = True
    validate_assignment = True
    # IDEA anystr_lower = True
