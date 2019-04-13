import sys

# Use sys.version_info[0] instead of sys.version_info.major so we can run these
# checks in versions < 2.7. Source: https://stackoverflow.com/a/9079062
_py_major = sys.version_info[0]
_py_minor = sys.version_info[1]

_is_py_supported = True
_infinity = None

if _py_major == 2:
    if _py_minor < 7:
        _is_py_supported = False
    else:
        # Using Python2 >= 2.7
        _infinity = sys.maxint

elif _py_major == 3:
    if _py_minor < 4:
        _is_py_supported = False
    else:
        # Using Python3 >= 3.4
        _infinity = sys.maxsize
else:
    # Using an unknown Python (not 2 or 3)
    _is_py_supported = False

if not _is_py_supported:
    raise Exception(
        'gt-tsp cannot be used with your Python version: %d.%d'
        % (_py_major, _py_minor))


INFINITY = _infinity
