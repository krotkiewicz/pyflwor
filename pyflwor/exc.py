class PyFlworError(Exception):
    """Base pyflwor Exception"""


class PyFlworException(PyFlworError):
    """
    Exception rised on all parsing errors, including:
    - operator not found
    - object has no attribute
    etc.
    """


class PyflworSyntaxError(PyFlworError):
    def __init__(self, msg, lineno):
        self.lineno =  lineno
        super(PyflworSyntaxError, self).__init__(msg)


