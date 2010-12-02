#! /usr/bin/env python

from FXPy.fox import *
import sys

def runme():
    app = FXApp('Hello', 'Test')
    app.init(sys.argv)
    main = FXMainWindow(app, 'Hello', None, None, DECOR_ALL)
    button = FXButton(main, '&Hello, World!', None, app, FXApp.ID_QUIT);
    app.create()
    main.show(PLACEMENT_SCREEN)
    app.run()

if __name__ == '__main__':
    runme()
