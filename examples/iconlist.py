#! /usr/bin/env python

from FXPy.fox import *
import os

class IconListWindow(FXMainWindow):

    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Icon List Test", w=800, h=600)

        # Menu bar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, "&Quit", None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, filemenu);

        # Status bar
        status = FXStatusbar(self,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # Main window interior
        group = FXVerticalFrame(self, LAYOUT_FILL_X|LAYOUT_FILL_Y,
            0,0,0,0, 0,0,0,0)

        # Files
        FXLabel(group, "Icon List Widget", None,
            LAYOUT_TOP|LAYOUT_FILL_X|FRAME_SUNKEN)
        subgroup = FXVerticalFrame(group,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y,
            0, 0, 0, 0, 0, 0, 0, 0)

        # Icon list on the right
        iconlist = FXIconList(subgroup, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|ICONLIST_MINI_ICONS)

        iconlist.appendHeader("Name", None, 200)
        iconlist.appendHeader("Type", None, 100)
        iconlist.appendHeader("Size", None, 60)
        iconlist.appendHeader("Modified Date", None, 150)
        iconlist.appendHeader("User", None, 50)
        iconlist.appendHeader("Group", None, 50)

        big_folder = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'bigfolder.png'), 'rb').read())
        mini_folder = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'minifolder.png'), 'rb').read())

        iconlist.appendItem("Really BIG and wide item to test\tDocument\t10000\tJune 13, 1999\tUser\tSoftware", big_folder, mini_folder)
        for i in xrange(1,100):
            iconlist.appendItem("Filename_%d\tDocument\t10000\tJune 13, 1999\tUser\tSoftware" % i, big_folder, mini_folder);

        # Arrange menu
        arrangemenu = FXMenuPane(self)
        FXMenuCommand(arrangemenu, "&Details", None, iconlist,
            FXIconList.ID_SHOW_DETAILS)
        FXMenuCommand(arrangemenu, "&Small Icons", None, iconlist,
            FXIconList.ID_SHOW_MINI_ICONS)
        FXMenuCommand(arrangemenu, "&Big Icons", None, iconlist,
            FXIconList.ID_SHOW_BIG_ICONS)
        FXMenuCommand(arrangemenu, "&Rows", None, iconlist,
            FXIconList.ID_ARRANGE_BY_ROWS)
        FXMenuCommand(arrangemenu, "&Columns", None, iconlist,
            FXIconList.ID_ARRANGE_BY_COLUMNS)
        FXMenuTitle(menubar, "&Arrange", None, arrangemenu)

        # Sort menu
        sortmenu = FXMenuPane(self)
        FXMenuCommand(sortmenu,"&Name",None,iconlist,
            FXFileList.ID_SORT_BY_NAME)
        FXMenuCommand(sortmenu,"&Type",None,iconlist,
            FXFileList.ID_SORT_BY_TYPE)
        FXMenuCommand(sortmenu,"&Size",None,iconlist,
            FXFileList.ID_SORT_BY_SIZE)
        FXMenuCommand(sortmenu,"T&ime",None,iconlist,
            FXFileList.ID_SORT_BY_TIME)
        FXMenuCommand(sortmenu,"&User",None,iconlist,
            FXFileList.ID_SORT_BY_USER)
        FXMenuCommand(sortmenu,"&Group",None,iconlist,
            FXFileList.ID_SORT_BY_GROUP)
        FXMenuCommand(sortmenu,"&Reverse",None,iconlist,
            FXFileList.ID_SORT_REVERSE)
        FXMenuCommand(sortmenu,"Hide status",None,status,
            FXWindow.ID_HIDE)
        FXMenuCommand(sortmenu,"Show status",None,status,
            FXWindow.ID_SHOW)
        FXMenuTitle(menubar, "&Sort", None, sortmenu)

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

# Main program starts here
if __name__ == '__main__':
    import sys
    application = FXApp("IconList", "Test")
    application.init(sys.argv)
    IconListWindow(application)
    application.create()
    application.run()
