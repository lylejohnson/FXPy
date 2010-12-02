#! /usr/bin/env python

import os
from FXPy.fox import *

class PeriodicWindow(FXMainWindow):
    def loadIcon(self, filename):
        filename = os.path.join('icons', filename)
        return FXPNGIcon(self.getApp(), open(filename, 'rb').read())

    def __init__(self, app):
        FXMainWindow.__init__(self, app, 'Periodic Table', w=800, h=600)

        # Make a few icons
        labelicon = self.loadIcon('bigfolder.png')
        buttonicon = self.loadIcon('tbuplevel.png')

        # Folder icons
        folder_open = self.loadIcon('minifolderopen.png')
        folder_closed = self.loadIcon('minifolder.png')

        # Document icon
        doc = self.loadIcon('minidoc.png')

        # Make menubar
        menubar = FXMenubar(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Make status bar
        FXStatusbar(self,LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # Make file popup menu
        filemenu = FXMenuPane(menubar)
        FXMenuCommand(filemenu,"Open",None,None,0)
        FXMenuCommand(filemenu,"Close")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"aaaaa")
        FXMenuCommand(filemenu,"Exit",tgt=app)

        # Hang it under menu bar
        FXMenuTitle(menubar, "File", None, filemenu)

        # Make Edit popup menu
        editmenu = FXMenuPane(menubar)
        FXMenuCommand(editmenu,"Undo")
        FXMenuCommand(editmenu,"Cut")
        FXMenuCommand(editmenu,"aaaaa")
        FXMenuCommand(editmenu,"bbbbb")
        FXMenuCommand(editmenu,"ccccc")
        FXMenuCommand(editmenu,"dddddd")
        FXMenuSeparator(editmenu)
        FXMenuCommand(editmenu,"Copy")

        submenu1 = FXMenuPane(menubar)
        FXMenuCommand(submenu1,"One")
        FXMenuCommand(submenu1,"Two",None,None,0)
        FXMenuCommand(submenu1,"Three",None,None,0)
        FXMenuCommand(submenu1,"Four")
        FXMenuCommand(submenu1,"Three",None,None,0)
        FXMenuCommand(submenu1,"Three",None,None,0)
        FXMenuCommand(submenu1,"Three",None,None,0)
        FXMenuCommand(submenu1,"Four")
        FXMenuCommand(submenu1,"Four")
        FXMenuCommand(submenu1,"Four")

        FXMenuCascade(editmenu,"Submenu1",None,submenu1)

        submenu2 = FXMenuPane(menubar)
        FXMenuCommand(submenu2,"Aaaa")
        FXMenuCommand(submenu2,"Bbbb")
        FXMenuCommand(submenu2,"Cccc")
        FXMenuCascade(editmenu,"Submenu2",None,submenu2)

        submenu3 = FXMenuPane(menubar)
        FXMenuCommand(submenu3,"11111")
        FXMenuCommand(submenu3,"22222")

        submenu4 = FXMenuPane(menubar)
        FXMenuCommand(submenu4,"QQQQQQ")
        FXMenuCommand(submenu4,"RRRRRR")
        FXMenuCommand(submenu4,"SSSSSS")
        FXMenuCommand(submenu4,"TTTTTT")
        FXMenuCommand(submenu4,"UUUUUU")
        FXMenuCommand(submenu4,"VVVVVV")

        FXMenuCascade(submenu3,"subsub",None,submenu4)
        FXMenuCommand(submenu3,"33333")
        FXMenuCascade(editmenu,"Submenu3",None,submenu3)

        # Hang it under menu bar
        FXMenuTitle(menubar, "Edit", None, editmenu)

        # Make Help menu
        helpmenu = FXMenuPane(menubar)
        FXMenuCommand(helpmenu, "About")
        FXMenuTitle(menubar, "Help", None, helpmenu)

        # Make Periodic Table
        periodictable = FXHorizontalFrame(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0)

        # Labels
        labels = FXGroupBox(periodictable,"Labels",FRAME_RIDGE|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,5,5,5,5)
        FXLabel(labels,"Label Types",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(labels,SEPARATOR_LINE|LAYOUT_FILL_X)
        FXHorizontalSeparator(labels,SEPARATOR_GROOVE|LAYOUT_FILL_X|LAYOUT_FIX_HEIGHT,0,0,0,10)
        FXHorizontalSeparator(labels,SEPARATOR_RIDGE|LAYOUT_FILL_X|LAYOUT_FIX_HEIGHT,0,0,0,10)
        FXHorizontalSeparator(labels,SEPARATOR_LINE|LAYOUT_FILL_X|LAYOUT_FIX_HEIGHT,0,0,0,10)
        FXLabel(labels,"Text Label")
        FXLabel(labels,"Label met een icoontje",labelicon,TEXT_OVER_ICON|FRAME_RAISED)
        FXLabel(labels,"TEXT and ICON",buttonicon)

        FXButton(labels,"Popup",opts=FRAME_RAISED|FRAME_THICK)

        text = FXTextField(labels,10,opts=FRAME_SUNKEN|FRAME_THICK)

        text = FXTextField(labels,10,opts=FRAME_SUNKEN|FRAME_THICK)

        simplelist = FXList(labels,10,opts=LIST_EXTENDEDSELECT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_RIGHT)
        simplelist.appendItem("One very long list entry")
        simplelist.appendItem("Another entry")
        for i in xrange(30):
            simplelist.appendItem("%d" % i,folder_open)

        # Buttons
        buttons = FXVerticalFrame(periodictable,FRAME_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)
        FXLabel(buttons,"Button Types",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(buttons,SEPARATOR_LINE|LAYOUT_FILL_X)
        FXButton(buttons,"Click Me",opts=FRAME_RAISED|FRAME_THICK)
        FXCheckButton(buttons,"Check Button")
        FXRadioButton(buttons,"Radio Button")
        FXButton(buttons,None,buttonicon,opts=FRAME_RAISED|FRAME_THICK)
        FXArrowButton(buttons,None,0,FRAME_RAISED|FRAME_THICK|ARROW_UP|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,10,10,0,0,0,0)
        FXArrowButton(buttons,opts=FRAME_RAISED|FRAME_THICK|ARROW_DOWN)
        FXArrowButton(buttons,opts=FRAME_RAISED|FRAME_THICK|ARROW_LEFT)
        FXArrowButton(buttons,opts=FRAME_RAISED|FRAME_THICK|ARROW_RIGHT)

        tree = FXTreeList(buttons,0,opts=TREELIST_ROOT_BOXES|TREELIST_SHOWS_BOXES|TREELIST_SHOWS_LINES|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_RIGHT)
        topmost = tree.addItemLast(None, "Top", folder_open, folder_closed)
        topmost2 = tree.addItemLast(None, "Top2", folder_open, folder_closed)
        tree.addItemLast(topmost2, "First", doc, doc)

        tree.addItemLast(topmost,"First",doc,doc)
        tree.addItemLast(topmost,"Second",doc,doc)
        tree.addItemLast(topmost,"Third",doc,doc)
        branch = tree.addItemLast(topmost,"Fourth",folder_open,folder_closed)
        tree.addItemLast(branch,"Fourth-First",doc,doc)
        tree.addItemLast(branch,"Fourth-Second",doc,doc)
        twig = tree.addItemLast(branch,"Fourth-Third",folder_open,folder_closed)
        tree.addItemLast(twig,"Fourth-Third-First",doc,doc)
        tree.addItemLast(twig,"Fourth-Third-Second",doc,doc)
        tree.addItemLast(twig,"Fourth-Third-Third",doc,doc)
        leaf = tree.addItemLast(twig,"Fourth-Third-Fourth",folder_open,folder_closed)
        tree.addItemLast(leaf,"Fourth-Third-Fourth-First",doc,doc)
        tree.addItemLast(leaf,"Fourth-Third-Fourth-Second",doc,doc)
        tree.addItemLast(leaf,"Fourth-Third-Fourth-Third",doc,doc)
        twig = tree.addItemLast(branch,"Fourth-Fourth",folder_open,folder_closed)
        tree.addItemLast(twig,"Fourth-Fourth-First",doc,doc)
        tree.addItemLast(twig,"Fourth-Fourth-Second",doc,doc)
        tree.addItemLast(twig,"Fourth-Fourth-Third",doc,doc)
        for i in xrange(10):
            tree.addItemLast(twig,"%09d" % i,doc,doc)

        twig = tree.addItemLast(branch,"Fourth-Fifth",folder_open,folder_closed)
        tree.addItemLast(twig,"Fourth-Fifth-First",doc,doc)
        tree.addItemLast(twig,"Fourth-Fifth-Second",doc,doc)
        tree.addItemLast(twig,"Fourth-Fifth-Third",doc,doc)
        for i in xrange(10):
            tree.addItemLast(twig,"%09d" % i,doc,doc)
        tree.addItemLast(topmost,"Fifth",doc,doc)
        tree.addItemLast(topmost,"Sixth",doc,doc)
        branch = tree.addItemLast(topmost,"Seventh",folder_open,folder_closed)
        tree.addItemLast(branch,"Seventh-First",doc,doc)
        tree.addItemLast(branch,"Seventh-Second",doc,doc)
        tree.addItemLast(branch,"Seventh-Third",doc,doc)
        tree.addItemLast(topmost,"Eighth",doc,doc)

        # Switcher windows
        switchers = FXVerticalFrame(periodictable,FRAME_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)
        FXLabel(switchers,"Switcher Windows",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(switchers,SEPARATOR_LINE|LAYOUT_FILL_X)

        tabbook = FXTabBook(switchers,opts=LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXTabItem(tabbook,"One")
        FXLabel(tabbook,"Tab Book Page 1",None,FRAME_THICK|FRAME_RAISED)

        FXTabItem(tabbook,"Two")
        FXLabel(tabbook,"Tab Book Page 2",None,FRAME_THICK|FRAME_RAISED)

        FXTabItem(tabbook,"Three",buttonicon)
        FXLabel(tabbook,"Tabs can be on all sides",None,FRAME_THICK|FRAME_RAISED)

        FXTabItem(tabbook,None,buttonicon)
        page = FXVerticalFrame(tabbook,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)
        FXLabel(page,"Switch Page",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXButton(page,"Text Button",opts=LAYOUT_TOP)
        FXCheckButton(page,"Check Button",opts=LAYOUT_TOP|ICON_BEFORE_TEXT)
        FXRadioButton(page,"Radio Button",opts=LAYOUT_TOP|ICON_BEFORE_TEXT)
        FXButton(page,None,buttonicon,opts=FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|ICON_BEFORE_TEXT)

        # Scroll windows
        scrollwin = FXVerticalFrame(periodictable,FRAME_NORMAL|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)
        FXLabel(scrollwin,"Scrolled Window",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        FXHorizontalSeparator(scrollwin,SEPARATOR_LINE|LAYOUT_FILL_X)

        scrolledwindow = FXScrollWindow(scrollwin,LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXLabel(scrolledwindow,"TEXT and ICON",buttonicon,ICON_ABOVE_TEXT|FRAME_RAISED)

    # Overrides the base class version of create()
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

if __name__ == '__main__':
    app = FXApp("Window", "Test")
    import sys
    app.init(sys.argv)
    PeriodicWindow(app)
    app.create()
    app.run()
