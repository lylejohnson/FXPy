#! /usr/bin/env python

"""
This is the "Cadillac" version of the classical "Hello World" example.
It has not only an icon, but also a tooltip, and an accelerator.

For this example (and all of the FXPy examples) icon images are loaded
directly from GIF/BMP/XPM/PNG/JPG disk files into strings. Another approach
(the one commonly used in C++ FOX applications) is to use the reswrap.py
utility to convert these images into coded strings; with this approach you
would not need to distribute the individual image files.

Executing an FXIcon's constructor will cause it to deserialize the pixel-
data by associating a memory stream with the data array; the resulting icon
object will contain a pixel-array, which will be converted to an off-screen
X pixmap when the icons create() method is called.  At that point, the
temporary (client-side) pixel storage will be freed.
"""

from FXPy.fox import *
import os
import sys

if __name__ == '__main__':
    # Create and initialize the application object
    app = FXApp('Hello2', 'Test')
    app.init(sys.argv)

    # Create the main window
    main = FXMainWindow(app, 'Hello', None, None, DECOR_ALL)

    # Create an icon object from disk file
    icon = FXPNGIcon(app, open(os.path.join('icons', 'fox.png'), 'rb').read())

    # Create a button using this icon
    button = FXButton(main, '&Hello, Guido!\tWow, FOX is really cool!\nClick on the icon to quit the application.', icon, app, FXApp.ID_QUIT, ICON_UNDER_TEXT|JUSTIFY_BOTTOM)

    # Create a tooltip object
    tooltip = FXTooltip(app)

    # Create all application windows
    app.create()

    # Show the main window
    main.show(PLACEMENT_SCREEN)

    # Go into main event loop
    app.run()
