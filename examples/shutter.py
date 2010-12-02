#! /usr/bin/env python

from FXPy.fox import *
import os

class ShutterWindow(FXMainWindow):
    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Shutter Widget Test", w=800, h=600)
        foldericon = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'shutter1.png'), 'rb').read())
        compressicon = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'shutter2.png'), 'rb').read())

        contents = FXHorizontalFrame(self, LAYOUT_FILL_X|LAYOUT_FILL_Y)
        listFrame = FXVerticalFrame(contents, LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)
        FXLabel(listFrame, "Tree List", None, JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(listFrame, SEPARATOR_GROOVE|LAYOUT_FILL_X);
        tree = FXTreeList(listFrame, 10,
            opts=FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_RIGHT|TREELIST_SHOWS_LINES|TREELIST_SHOWS_BOXES)

        buttonFrame = FXVerticalFrame(contents,
            FRAME_RAISED|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10)
        FXLabel(buttonFrame,"Button Frame",opts=JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(buttonFrame, SEPARATOR_RIDGE|LAYOUT_FILL_X)

        shutterFrame = FXShutter(buttonFrame, None, 0,
            FRAME_SUNKEN|LAYOUT_FILL_Y|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,0,0,0,0,0,0)
        shutterItem = FXShutterItem(shutterFrame, "Test 1", None,
            LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10,10,10)
        FXButton(shutterItem.getContent(), None, foldericon, self.getApp(),
            FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, compressicon, self.getApp(),
            FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, compressicon, self.getApp(),
            FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, foldericon, self.getApp(),
            FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        shutterItem = FXShutterItem(shutterFrame, "Test 2", None,
            LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10,10,10)
        FXButton(shutterItem.getContent(), None, foldericon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, compressicon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, foldericon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        shutterItem = FXShutterItem(shutterFrame, "Test 3", None,
            LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10,10,10)
        FXButton(shutterItem.getContent(), None, foldericon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, compressicon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        shutterItem = FXShutterItem(shutterFrame, "Test 4", None,
            LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10,10,10)
        FXButton(shutterItem.getContent(), None, foldericon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)
        FXButton(shutterItem.getContent(), None, compressicon,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

# Main program begins here
if __name__ == '__main__':
    import sys
    application = FXApp("Shutter", "Test")
    application.init(sys.argv)
    ShutterWindow(application)
    application.create()
    application.run()
