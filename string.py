import re

def search(pattern, x):
    return bool(re.search(pattern, x))
