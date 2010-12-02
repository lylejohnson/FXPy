#! /usr/bin/env python

import glob, os, string

# First get the set of class names
clsdict = {}
for file in glob.glob('*.ii'):
    for line in os.popen('grep -h "^class FX" ' + file).readlines():
        words = string.split(line)
        classname = words[1]
	clsdict[classname] = file

classes = clsdict.keys()
classes.sort()
f = open('renames.i', 'w')
for cls in classes:
    if cls[:4] != 'FXPy':
        newname = string.replace(cls, "FX", "FX_")
        f.write('%%rename %s %s;\n' % (cls, newname))

f.write('\n')

for cls in classes:
    if cls[:4] == 'FXPy':
        newname = string.replace(cls, "FXPy", "FX")
        f.write('%%rename %s %s;\n' % (cls, newname))
