class PyFlworError(Exception):
    """Base pyflwor Exception"""


class PyflworSyntaxError(PyFlworError):
    def __init__(self, msg, lineno):
        self.lineno =  lineno
        super(PyflworSyntaxError, self).__init__(msg)


