#! /usr/bin/env python

from FXPy.fox import *

class FourSplitWindow(FXMainWindow):
    def __init__(self, app):
        # Base class constructor
        FXMainWindow.__init__(self, app, "4-Way Splitter Test",
            w=800, h=600, hs=0, vs=0)

        # Menu bar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X);

        # Status bar
        FXStatusbar(self,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER);

        # Create the split
        splitter = FX4Splitter(self,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y|FOURSPLITTER_TRACKING);

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, "&Quit\t\tQuit the application.",
            None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, filemenu)

        # Expand menu
        expandmenu = FXMenuPane(self)
        FXMenuCommand(expandmenu, 'All four', None,
            splitter, FX4Splitter.ID_EXPAND_ALL)
        FXMenuCommand(expandmenu, 'Top/left', None,
            splitter, FX4Splitter.ID_EXPAND_TOPLEFT)
        FXMenuCommand(expandmenu, 'Top/right', None,
            splitter, FX4Splitter.ID_EXPAND_TOPRIGHT)
        FXMenuCommand(expandmenu, 'Bottom/left', None,
            splitter, FX4Splitter.ID_EXPAND_BOTTOMLEFT)
        FXMenuCommand(expandmenu, 'Bottom/right', None,
            splitter, FX4Splitter.ID_EXPAND_BOTTOMRIGHT)
        FXMenuTitle(menubar, '&Expand', None, expandmenu)

        # Four widgets in the four splitter
        FXButton(splitter, "Top &Left\tThis splitter tracks",
            opts=FRAME_RAISED|FRAME_THICK)
        FXButton(splitter, "Top &Right\tThis splitter tracks",
            opts=FRAME_RAISED|FRAME_THICK)
        FXButton(splitter, "&Bottom Left\tThis splitter tracks",
            opts=FRAME_SUNKEN|FRAME_THICK)
        subsplitter = FX4Splitter(splitter, LAYOUT_FILL_X|LAYOUT_FILL_Y)
        temp = FXButton(subsplitter,"&Of course\tThis splitter does NOT track",
            opts=FRAME_SUNKEN|FRAME_THICK)
        temp.setBackColor(FXRGB(0,128,0))
        temp.setTextColor(FXRGB(255,255,255))
        temp = FXButton(subsplitter,"the&y CAN\tThis splitter does NOT track",
            opts=FRAME_SUNKEN|FRAME_THICK)
        temp.setBackColor(FXRGB(128,0,0))
        temp.setTextColor(FXRGB(255,255,255))

        temp = FXButton(subsplitter,"be &NESTED\tThis splitter does NOT track",
            opts=FRAME_SUNKEN|FRAME_THICK)
        temp.setBackColor(FXRGB(0,0,200));
        temp.setTextColor(FXRGB(255,255,255));
        temp = FXButton(subsplitter,
            "&arbitrarily!\tThis splitter does NOT track",
            opts=FRAME_SUNKEN|FRAME_THICK)
        temp.setBackColor(FXRGB(128,128,0))
        temp.setTextColor(FXRGB(255,255,255))

        tooltip = FXTooltip(self.getApp())

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

def runme():
    import sys
    application = FXApp("FourSplit", "FoxTest")
    application.init(sys.argv)
    FourSplitWindow(application)
    application.create()
    application.run()

# Main program starts here
if __name__ == "__main__":
    runme()
