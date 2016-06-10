from json import loads
from core.const import CONFIG_PATH

def get_version ():
    STR = ''
    with open (CONFIG_PATH, 'r') as f:
        for i in f.readlines ():
            STR += i

    f.close ()

    return (loads (STR) ['developer'], loads (STR) ['num'], loads (STR) ['codename'])