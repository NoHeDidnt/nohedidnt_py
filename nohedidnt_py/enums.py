# -*- coding: utf-8 -*-
from nohedidnt_py.aliases import *


class NhdBoxType(IntEnum):
    none = -99
    test = -69
    default = 1


class NhdContinent(IntEnum):
    none = -99
    africa = 1
    asia = 2
    europe = 3
    north_america = 4
    oceania = 5
    south_america = 6
