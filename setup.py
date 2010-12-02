#!/usr/bin/env python

import sys

# Location of the FOX library and header files.
if sys.platform == 'win32':
    FXLIBDIR = r'..\fox-1.0.5\lib'
    FXINCDIR = r'..\fox-1.0.5\include'
else:
    FXLIBDIR = '/usr/local/lib'
    FXINCDIR = '/usr/local/include/fox'

# Location of X libraries
if sys.platform == 'win32':
    XLIBDIR = []
else:
    XLIBDIR = ['/usr/X11R6/lib']

# Other libraries
OLIBDIRS = ['c:\cygwin\usr\local\lib']

# Source files for this extension
SOURCES = [
    'src/FXPy.cpp',
    'src/FXPyApp.cpp',
    'src/FXPyDataTarget.cpp',
    'src/containers.cpp',
    'src/controls.cpp',
    'src/dialogs.cpp',
    'src/dirlist.cpp',
    'src/fox.cpp',
    'src/fox3d.cpp',
    'src/graphics.cpp',
    'src/iconlist.cpp',
    'src/mdi.cpp',
    'src/menus.cpp',
    'src/misc.cpp',
    'src/table.cpp',
    'src/text.cpp',
    'src/treelist.cpp',
    'src/windows.cpp',
    'src/libpy.c'
    ]

# All required include file directories
INCDIRS = [FXINCDIR]

# All required library file directories
LIBDIRS = [FXLIBDIR] + XLIBDIR + OLIBDIRS

import sys
if sys.platform == 'win32':
    MACROS = [('NDEBUG', None), ('WIN32', None), ('__WIN32__', None),
	('WIN32_LEAN_AND_MEAN', None), ('FXPy_USE_THREADS', None)]
    LIBS = ['fox', 'user32', 'gdi32', 'advapi32', 'comctl32', 'winspool', 'shell32', 'wsock32', 'mpr', 'opengl32', 'glu32', 'libpng', 'zlib', 'libjpeg', 'libtiff']
else:
    MACROS = [('NDEBUG', None), ('FXPy_USE_THREADS', None)]
    LIBS = ['FOX', 'GL', 'GLU', 'jpeg', 'png', 'z']

# Some last-minute checks before we get started...
import os

if not os.path.exists(os.path.join(FXINCDIR, 'fx.h')):
    print """I couldn't find the file "fx.h" in this directory:"""
    print '\n    %s\n' % FXINCDIR
    print "Please check the value of FXINCDIR in the FXPy setup.py script to make sure"
    print "it's pointing to your FOX include files directory."
    raise SystemExit

if sys.platform == 'win32':
    foxlibname = 'fox.lib'
else:
    foxlibname = 'libFOX.a'

if not os.path.exists(os.path.join(FXLIBDIR, foxlibname)):
    print """I couldn't find the file "%s" in this directory:""" % foxlibname
    print '\n    %s\n' % FXLIBDIR
    print "Please check the value of FXLIBDIR in the FXPy setup.py script to make sure"
    print "it's pointing to your FOX library directory."
    raise SystemExit

from distutils.core import setup, Extension

setup (name = "FXPy",
       version = "1.0.5",
       description = "FOX Extensions for Python",
       author = "Lyle Johnson",
       author_email = "lyle@users.sourceforge.net",
       url = "http://fxpy.sourceforge.net",

       packages = ['FXPy'],
       package_dir = {'FXPy' : 'src'},

       ext_modules = [Extension('FXPy.foxc',
                                sources = SOURCES,
                                define_macros = MACROS,
                                include_dirs = INCDIRS,
                                library_dirs = LIBDIRS,
                                libraries = LIBS,
                               )
                     ]
      )
