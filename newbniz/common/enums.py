"""Enums for the newbniz project."""
from django_enumfield.enum import Enum as DjangoEnuM

class CommonFunctions(DjangoEnuM, int):
    """Common functions."""
    SIN = 1
    COS = 2
    TAN = 3
    EXP = 4
    LOG10 = 5
    LN = 6
    POLINOMIAL = 7
