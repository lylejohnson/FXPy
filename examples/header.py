#! /usr/bin/env python

import os
import string
from FXPy.fox import *

# Header Main Window
class HeaderWindow(FXMainWindow):
    ID_ABOUT = FXMainWindow.ID_LAST + 1
    ID_HEADER = ID_ABOUT + 1
    ID_TRACKING = ID_HEADER + 1

    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Header Control Test", w=800, h=600)
        FXMAPFUNC(self,SEL_COMMAND,HeaderWindow.ID_ABOUT,HeaderWindow.onCmdAbout)
        FXMAPFUNC(self,SEL_CHANGED,HeaderWindow.ID_HEADER,HeaderWindow.onCmdHeader)
        FXMAPFUNC(self,SEL_COMMAND,HeaderWindow.ID_HEADER,HeaderWindow.onCmdHeaderButton)
        FXMAPFUNC(self,SEL_COMMAND,HeaderWindow.ID_TRACKING,HeaderWindow.onCmdContinuous)

        menubar = FXMenubar(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
        FXStatusbar(self,LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)

        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu,"&Quit\t\tQuit the application",None,self.getApp(),FXApp.ID_QUIT)
        FXMenuTitle(menubar,"&File",None,filemenu)
        helpmenu = FXMenuPane(self)
        FXMenuCommand(helpmenu,"&About Header...",None,self,self.ID_ABOUT,0)
        FXMenuTitle(menubar,"&Help",None,helpmenu,LAYOUT_RIGHT)

        # Make main window contents
        contents = FXVerticalFrame(self,FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0, 0,0)

        # Make header control
        self.header1 = FXHeader(contents, self, self.ID_HEADER,
            HEADER_BUTTON|FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)

        # Document icon
        doc = FXPNGIcon(self.getApp(), open(os.path.join('icons', 'minidoc.png'), 'rb').read())

        self.header1.appendItem("Name",doc,150)
        self.header1.appendItem("Type",None,120)
        self.header1.appendItem("Layout Option",doc,230)
        self.header1.appendItem("Attributes",None,80)

        # Below header
        panes = FXHorizontalFrame(contents,FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0, 0,0)

        # Make 4 lists
        self.list = []
        self.list.append(FXList(panes,1,None,0,LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH,0,0,150,0))
        self.list.append(FXList(panes,1,None,0,LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH,0,0,120,0))
        self.list.append(FXList(panes,1,None,0,LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH,0,0,230,0))
        self.list.append(FXList(panes,1,None,0,LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH,0,0,80,0))

        self.list[0].setBackColor(FXRGB(255,240,240))
        self.list[1].setBackColor(FXRGB(240,255,240))
        self.list[2].setBackColor(FXRGB(240,240,255))
        self.list[3].setBackColor(FXRGB(255,255,240))

        # Add some contents
        self.list[0].appendItem("Jeroen van der Zijp")
        self.list[0].appendItem("Lyle Johnson")
        self.list[0].appendItem("Freddy Golos")
        self.list[0].appendItem("Charles Warren")
        self.list[0].appendItem("Jonathan Bush")
        self.list[0].appendItem("Guoqing Tian")

        self.list[1].appendItem("Incorrigible Hacker")
        self.list[1].appendItem("Windows Hacker")
        self.list[1].appendItem("Russian Hacker")
        self.list[1].appendItem("Shutter Widget")
        self.list[1].appendItem("Progress Bar")
        self.list[1].appendItem("Dial Widget")

        self.list[2].appendItem("LAYOUT_FILL_X|LAYOUT_FILL_Y")
        self.list[2].appendItem("LAYOUT_FILL_Y")
        self.list[2].appendItem("LAYOUT_NORMAL")
        self.list[2].appendItem("LAYOUT_NORMAL")
        self.list[2].appendItem("LAYOUT_NORMAL")
        self.list[2].appendItem("LAYOUT_NORMAL")

        self.list[3].appendItem("A")
        self.list[3].appendItem("B")
        self.list[3].appendItem("C")
        self.list[3].appendItem("D")
        self.list[3].appendItem("E")
        self.list[3].appendItem("F")

        self.header2 = FXHeader(panes, None, 0,
          HEADER_VERTICAL|HEADER_BUTTON|FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_Y)
        self.header2.appendItem("Example", None, 30)
        self.header2.appendItem("Of", None, 30)
        self.header2.appendItem("Vertical", None, 30)
        self.header2.appendItem("Header", None, 30)

        # Group box with some controls
        groupie = FXGroupBox(panes,"Controls",GROUPBOX_TITLE_CENTER|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        check = FXCheckButton(groupie,"Continuous Tracking\tContinuous\tTrack Header continuously",self,self.ID_TRACKING,ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)

        # Whip out a tooltip control, jeez, that's hard
        FXTooltip(self.getApp())

    # About
    def onCmdAbout(self, sender, sel, ptr):
        showModalInformationBox(self,MBOX_OK,
            "About Header",
            "An example of how to work with the header control\n\n\nAnd some attributes of the developers!")

    # Changed the header control
    def onCmdHeader(self, sender, sel, which):
        self.list[which].setWidth(self.header1.getItemSize(which))

    # Clicked a header button; highlight the entire column
    def onCmdHeaderButton(self, sender, sel, which):
        for i in xrange(self.list[which].getNumItems()):
            self.list[which].selectItem(i)

    # Continuous tracking
    def onCmdContinuous(self, sender, sel, ptr):
        self.header1.setHeaderStyle(HEADER_TRACKING^self.header1.getHeaderStyle())
        self.header2.setHeaderStyle(HEADER_TRACKING^self.header2.getHeaderStyle())

    # Create & show main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

def runme():
    import sys
    app = FXApp("Header", "Test")
    app.init(sys.argv)
    HeaderWindow(app)
    app.create()
    app.run()

# Main program starts here
if __name__ == '__main__':
    runme()
