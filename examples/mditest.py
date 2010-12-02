#! /usr/bin/env python

from FXPy.fox import *
import os

# Main window class
class MDITestWindow(FXMainWindow):
    ID_ABOUT = FXMainWindow.ID_LAST + 1
    ID_NEW = ID_ABOUT + 1

    # Constructor
    def __init__(self, app):
        FXMainWindow.__init__(self,app,"MDI Widget Test",w=800,h=600)
        FXMAPFUNC(self,SEL_COMMAND,MDITestWindow.ID_ABOUT,MDITestWindow.onCmdAbout)
        FXMAPFUNC(self,SEL_COMMAND,MDITestWindow.ID_NEW,MDITestWindow.onCmdNew)

        # Menubar
        menubar = FXMenubar(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Status bar
        FXStatusbar(self,LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # MDI Client
        self.mdiclient = FXMDIClient(self,LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Icon for MDI Child
        self.mdiicon = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'penguin.png'), 'rb').read())

        # Make MDI Menu
        self.mdimenu = FXMDIMenu(self,self.mdiclient)

        # MDI buttons in menu
        FXMDIWindowButton(menubar,self.mdiclient,FXMDIClient.ID_MDI_MENUWINDOW,LAYOUT_LEFT)
        FXMDIDeleteButton(menubar,self.mdiclient,FXMDIClient.ID_MDI_MENUCLOSE,FRAME_RAISED|LAYOUT_RIGHT)
        FXMDIRestoreButton(menubar,self.mdiclient,FXMDIClient.ID_MDI_MENURESTORE,FRAME_RAISED|LAYOUT_RIGHT)
        FXMDIMinimizeButton(menubar,self.mdiclient,FXMDIClient.ID_MDI_MENUMINIMIZE,FRAME_RAISED|LAYOUT_RIGHT)

        # Create three child windows to get started
        mdichild = FXMDIChild(self.mdiclient,"TEST1",self.mdiicon,self.mdimenu,LAYOUT_FIX_X|LAYOUT_FIX_Y,10,10,300,200)
        FXScrollWindow(mdichild,HSCROLLER_ALWAYS|VSCROLLER_ALWAYS)

        mdichild = FXMDIChild(self.mdiclient,"TEST2",self.mdiicon,self.mdimenu,LAYOUT_FIX_X|LAYOUT_FIX_Y,20,20,300,200)
        FXScrollWindow(mdichild,HSCROLLER_ALWAYS|VSCROLLER_ALWAYS)

        mdichild = FXMDIChild(self.mdiclient,"TEST3",self.mdiicon,self.mdimenu,LAYOUT_FIX_X|LAYOUT_FIX_Y,30,30,300,200)
        FXButton(mdichild,"Hello",opts=FRAME_THICK|FRAME_RAISED|JUSTIFY_CENTER_X|JUSTIFY_CENTER_Y)

        # Make that last one the active window
        self.mdiclient.setActiveChild(mdichild)

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu,"&New\t\tCreate new document.",None,self,self.ID_NEW)
        FXMenuCommand(filemenu,"&Open\t\tOpen document.")
        FXMenuCommand(filemenu,"&Quit\t\tQuit application.",None,self.getApp(),FXApp.ID_QUIT,0)
        FXMenuTitle(menubar,"&File",None,filemenu)

        # Window menu
        windowmenu = FXMenuPane(self)
        FXMenuCommand(windowmenu,"Tile &Horizontally",None,self.mdiclient,FXWindow.ID_MDI_TILEHORIZONTAL)
        FXMenuCommand(windowmenu,"Tile &Vertically",None,self.mdiclient,FXWindow.ID_MDI_TILEVERTICAL)
        FXMenuCommand(windowmenu,"C&ascade",None,self.mdiclient,FXWindow.ID_MDI_CASCADE)
        FXMenuCommand(windowmenu,"&Close",None,self.mdiclient,FXWindow.ID_MDI_CLOSE)
        FXMenuCommand(windowmenu,"Close &All",None,self.mdiclient,FXMDIClient.ID_CLOSE_ALL_DOCUMENTS)
        FXMenuTitle(menubar,"&Window",None,windowmenu)

        # Help menu
        helpmenu = FXMenuPane(self)
        FXMenuCommand(helpmenu,"&About FOX...",None,self,self.ID_ABOUT,0)
        FXMenuTitle(menubar,"&Help",None,helpmenu,LAYOUT_RIGHT)

    # Create & show main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    # Show the "About" dialog
    def onCmdAbout(self, sender, sel, ptr):
        showModalInformationBox(self,MBOX_OK, "About MDI Test", "Test of the FOX MDI Widgets\nWritten by Jeroen van der Zijp")

    # Create a new child window
    def onCmdNew(self, sender, sel, ptr):
        mdichild = FXMDIChild(self.mdiclient,"Child",self.mdiicon,self.mdimenu,0,20,20,300,200)
        FXScrollWindow(mdichild,HSCROLLER_ALWAYS|VSCROLLER_ALWAYS)
        mdichild.create()

# Main program starts here...
if __name__ == '__main__':
    import sys
    app = FXApp("MDIApp","Test")
    app.init(sys.argv)
    MDITestWindow(app)
    app.create()
    app.run()
