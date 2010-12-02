#
# Extra goodies appended to the end
#

# This call gives the C++ code layer access to Python's namespace
FXPySetDict(vars())

def FXMAPTYPES(self, typelo, typehi, func):
    if not hasattr(self, "FXMSGMAP"):
	self.FXMSGMAP = []
    keylo = MKUINT(MINKEY, typelo)
    keyhi = MKUINT(MAXKEY, typehi)
    tup = (keylo, keyhi, func)
    self.FXMSGMAP.append(tup)

def FXMAPTYPE(self, type, func):
    if not hasattr(self, "FXMSGMAP"):
	self.FXMSGMAP = []
    keylo = MKUINT(MINKEY, type)
    keyhi = MKUINT(MAXKEY, type)
    tup = (keylo, keyhi, func)
    self.FXMSGMAP.append(tup)

# Here's how we handle mapping message identifiers to method calls at
# the Python level. Each object instance has a list member called
# FXMSGMAP which maps a range of identifiers to a method call.
def FXMAPFUNC(self, type, id, func):
    if not hasattr(self, "FXMSGMAP"):
	self.FXMSGMAP = []
    keylo = MKUINT(id, type)
    keyhi = MKUINT(id, type)
    tup = (keylo, keyhi, func)
    self.FXMSGMAP.append(tup)

def FXMAPFUNCS(self, type, keylo, keyhi, func):
    if not hasattr(self, "FXMSGMAP"):
	self.FXMSGMAP = []
    keylo = MKUINT(keylo, type)
    keyhi = MKUINT(keyhi, type)
    tup = (keylo, keyhi, func)
    self.FXMSGMAP.append(tup)

