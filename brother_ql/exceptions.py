"""
This module contains all the classes of exceptions that may be raised by brother_ql
"""

class BrotherQLError(Exception):
    """ Base class for exceptions from this package """
    pass

class BrotherQLUnsupportedCmd(BrotherQLError):
    """ Raised when a raster command is not supported with a given printer/label combination """
    pass

class BrotherQLUnknownModel(BrotherQLError):
    """ Unrecognized printer model """
    pass

class BrotherQLRasterError(BrotherQLError):
    """ Raised when invalid data is passed to functions on ``brother_ql.raster.BrotherQLRaster`` """
    pass
