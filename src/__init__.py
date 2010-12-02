class FXError(Exception):
    pass

from fox import setErrorObject 
setErrorObject(FXError)
