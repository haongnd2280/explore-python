# Python 3.11.2

from typing import NewType, AnyStr

UserId = NewType("UserId", int)

class AdminUserId(UserId):
    pass
