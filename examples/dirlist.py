from FXPy.fox import *
import sys

# Main window class
class DirListWindow(FXMainWindow):

    ID_ABOUT = FXMainWindow.ID_LAST

    def __init__(self, app):
        # Call base class constructor first
        FXMainWindow.__init__(self, app, "Directory List", w=800, h=600)

        # Setup message map
        FXMAPFUNC(self, SEL_COMMAND, DirListWindow.ID_ABOUT,
            DirListWindow.onCmdAbout)

        # Menu bar
        menubar = FXMenubar(self, LAYOUT_FILL_X)
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, "&Quit", None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, filemenu)
        helpmenu = FXMenuPane(self)
        FXMenuCommand(helpmenu, "&About FOX...", None, self, self.ID_ABOUT, 0)
        FXMenuTitle(menubar, "&Help", None, helpmenu, LAYOUT_RIGHT)

        # Text field at the bottom
        text = FXTextField(self, 10, None, 0,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|FRAME_SUNKEN|FRAME_THICK)

        # Make contents
        contents = FXDirList(self, 0, None, 0, HSCROLLING_OFF|TREELIST_ROOT_BOXES|TREELIST_SHOWS_LINES|TREELIST_SHOWS_BOXES|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0, 0, 0, 0)

        text.setTarget(contents)
        text.setSelector(FXWindow.ID_SETVALUE)

    # Show About box
    def onCmdAbout(self, sender, sel, ptr):
        showModalInformationBox(self, MBOX_OK, "About FOX",
            "FOX is a really, really cool C++ library!")

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

def runme():
    app = FXApp()
    app.init(sys.argv)
    DirListWindow(app)
    app.create()
    app.run()

# Main program starts here
if __name__ == '__main__':
    runme()
