#! /usr/bin/env python

from FXPy.fox import *

class TabBookWindow(FXMainWindow):

    ID_TABS_TOP         = FXMainWindow.ID_LAST
    ID_TABS_BOTTOM      = ID_TABS_TOP + 1
    ID_TABS_LEFT        = ID_TABS_BOTTOM + 1
    ID_TABS_RIGHT       = ID_TABS_LEFT + 1

    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Tab Book Test", w=600, h=400)

        FXMAPFUNC(self, SEL_COMMAND, TabBookWindow.ID_TABS_TOP,
            TabBookWindow.onCmdTabOrient)
        FXMAPFUNC(self, SEL_COMMAND, TabBookWindow.ID_TABS_BOTTOM,
            TabBookWindow.onCmdTabOrient)
        FXMAPFUNC(self, SEL_COMMAND, TabBookWindow.ID_TABS_LEFT,
            TabBookWindow.onCmdTabOrient)
        FXMAPFUNC(self, SEL_COMMAND, TabBookWindow.ID_TABS_RIGHT,
            TabBookWindow.onCmdTabOrient)

        FXTooltip(self.getApp())
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
        FXHorizontalSeparator(self,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)
        contents = FXHorizontalFrame(self, LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

        # Switcher
        self.tabbook = FXTabBook(contents, None, 0,
            LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_RIGHT)

        # First item is a list
        self.tab1 = FXTabItem(self.tabbook, "&Simple List", None)
        listframe = FXHorizontalFrame(self.tabbook, FRAME_THICK|FRAME_RAISED)
        simplelist = FXList(listframe, 1, None, 0,
            LIST_EXTENDEDSELECT|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        simplelist.appendItem("First Entry")
        simplelist.appendItem("Second Entry")
        simplelist.appendItem("Third Entry")
        simplelist.appendItem("Fourth Entry")

        # Second item is a file list
        self.tab2 = FXTabItem(self.tabbook, "F&ile List", None)
        fileframe = FXHorizontalFrame(self.tabbook, FRAME_THICK|FRAME_RAISED)
        filelist = FXFileList(fileframe, None, 0,
            ICONLIST_EXTENDEDSELECT|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Third item is a directory list
        self.tab3 = FXTabItem(self.tabbook, "T&ree List", None)
        dirframe = FXHorizontalFrame(self.tabbook, FRAME_THICK|FRAME_RAISED)
        dirlist = FXDirList(dirframe, 0,
            opts=DIRLIST_SHOWFILES|TREELIST_SHOWS_LINES|TREELIST_SHOWS_BOXES|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # File Menu
        filemenu = FXMenuPane(menubar)
        FXMenuCommand(filemenu, "&Simple List", None, self.tabbook,
            FXTabBar.ID_OPEN_FIRST+0)
        FXMenuCommand(filemenu, "F&ile List", None, self.tabbook,
            FXTabBar.ID_OPEN_FIRST+1)
        FXMenuCommand(filemenu, "T&ree List", None, self.tabbook,
            FXTabBar.ID_OPEN_FIRST+2)
        FXMenuCommand(filemenu, "&Quit", None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, filemenu)

        # Tab side
        tabmenu = FXMenuPane(menubar)
        FXMenuCommand(tabmenu, "&Top Tabs", None, self,
            TabBookWindow.ID_TABS_TOP)
        FXMenuCommand(tabmenu, "&Bottom Tabs", None, self,
            TabBookWindow.ID_TABS_BOTTOM)
        FXMenuCommand(tabmenu, "&Left Tabs", None, self,
            TabBookWindow.ID_TABS_LEFT)
        FXMenuCommand(tabmenu, "&Right Tabs", None, self,
            TabBookWindow.ID_TABS_RIGHT)
        FXMenuTitle(menubar, "&Tab Placement", None, tabmenu)

    def onCmdTabOrient(self, sender, sel, ptr):
        id = SELID(sel)

        if id == TabBookWindow.ID_TABS_TOP:
            tabStyle = TABBOOK_TOPTABS
            tabOrient = TAB_TOP
        elif id == TabBookWindow.ID_TABS_BOTTOM:
            tabStyle = TABBOOK_BOTTOMTABS
            tabOrient = TAB_BOTTOM
        elif id == TabBookWindow.ID_TABS_LEFT:
            tabStyle = TABBOOK_LEFTTABS
            tabOrient = TAB_LEFT
        elif id == TabBookWindow.ID_TABS_RIGHT:
            tabStyle = TABBOOK_RIGHTTABS
            tabOrient = TAB_RIGHT
        else:
            raise SystemExit

        self.tabbook.setTabStyle(tabStyle)
        self.tab1.setTabOrientation(tabOrient)
        self.tab2.setTabOrientation(tabOrient)
        self.tab3.setTabOrientation(tabOrient)

    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

def runme():
    application = FXApp()
    import sys
    application.init(sys.argv)
    TabBookWindow(application)
    application.create()
    application.run()

# Main program starts here
if __name__ == '__main__':
    runme()
