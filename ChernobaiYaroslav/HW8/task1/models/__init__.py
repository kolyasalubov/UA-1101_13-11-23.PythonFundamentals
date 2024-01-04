# Have to use import from this modules to get access to their functions

from .admin import *
from .user import *

__all__ = ["create_admin", "create_user"]