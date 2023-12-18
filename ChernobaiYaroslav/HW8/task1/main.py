from utils import *
from models import *

print(list(filter(lambda str: not ("__" in str), dir())))
# Output is ['create_admin', 'create_user', 'format_string', 'log_in_file']