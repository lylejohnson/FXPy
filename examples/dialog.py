#! /usr/bin/env python

from FXPy.fox import *

# Our dialog box
class FXTestDialog(FXDialogBox):
    def __init__(self, owner):
        FXDialogBox.__init__(self,owner,"Test of Dialog Box",DECOR_TITLE|DECOR_BORDER)

        # Bottom buttons
        buttons = FXHorizontalFrame(self,LAYOUT_SIDE_BOTTOM|FRAME_NONE|LAYOUT_FILL_X|PACK_UNIFORM_WIDTH,0,0,0,0,40,40,20,20)

        # Separator
        FXHorizontalSeparator(self,LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|SEPARATOR_GROOVE)

        # Contents
        contents = FXHorizontalFrame(self,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

        submenu = FXMenuPane(self)
        FXMenuCommand(submenu,"One")
        FXMenuCommand(submenu,"Two")
        FXMenuCommand(submenu,"Three")

        # Menu
        menu = FXMenuPane(self)
        FXMenuCommand(menu,"&Accept",None,self,self.ID_ACCEPT)
        FXMenuCommand(menu,"&Cancel",None,self,self.ID_CANCEL)
        FXMenuCascade(menu,"Submenu",None,submenu)
        FXMenuCommand(menu,"&Quit",None,self.getApp(),FXApp.ID_QUIT)

        # Popup menu
        pop = FXPopup(self)
        FXOption(pop,"One",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Two",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Three",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Four",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Five",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Six",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Seven",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Eight",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Nine",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop,"Ten",opts=JUSTIFY_HZ_APART|ICON_AFTER_TEXT)

        # Option menu
        FXOptionMenu(contents,pop,FRAME_RAISED|FRAME_THICK|JUSTIFY_HZ_APART|ICON_AFTER_TEXT|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)

        # Button to pop menu
        FXMenuButton(contents,"&Menu",None,menu,MENUBUTTON_DOWN|JUSTIFY_LEFT|LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|ICON_AFTER_TEXT|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)

        # Accept
        FXButton(buttons,"&Accept",None,self,self.ID_ACCEPT,FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT|LAYOUT_CENTER_Y)

        # Cancel
        FXButton(buttons,"&Cancel",None,self,self.ID_CANCEL,FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT|LAYOUT_CENTER_Y);

# Main window class
class DialogTester(FXMainWindow):
    ID_SHOWDIALOG = FXMainWindow.ID_LAST
    ID_SHOWDIALOGMODAL = ID_SHOWDIALOG + 1

    def __init__(self, app):
        FXMainWindow.__init__(self,app,"Dialog Box Test",w=400,h=200)

        # Message map
        FXMAPFUNC(self,SEL_COMMAND,DialogTester.ID_SHOWDIALOG,DialogTester.onCmdShowDialog)
        FXMAPFUNC(self,SEL_COMMAND,DialogTester.ID_SHOWDIALOGMODAL,DialogTester.onCmdShowDialogModal)

        # Tooltip
        FXTooltip(self.getApp())

        # Menubar
        menubar = FXMenubar(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Separator
        FXHorizontalSeparator(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|SEPARATOR_GROOVE)

        # File Menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu,"&Quit",None,self.getApp(),FXApp.ID_QUIT,0)
        FXMenuTitle(menubar,"&File",None,filemenu)

        # Contents
        contents = FXHorizontalFrame(self,LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

        # Button to pop normal dialog
        FXButton(contents,"&Non-Modal Dialog...\tDisplay normal dialog",None,self,self.ID_SHOWDIALOG,FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)

        # Button to pop modal dialog
        FXButton(contents,"&Modal Dialog...\tDisplay modal dialog",None,self,self.ID_SHOWDIALOGMODAL,FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_X|LAYOUT_CENTER_Y)

        # Build a dialog box
        self.dialog = FXTestDialog(self)

    # Display modelessly
    def onCmdShowDialog(self,sender,sel,ptr):
        self.dialog.show()

    # Display modally
    def onCmdShowDialogModal(self,sender,sel,ptr):
        self.dialog.execute()

    # Start
    def create(self):
        FXMainWindow.create(self)
        self.show()

def runme():
    import sys
    app = FXApp("Dialog", "Test")
    app.init(sys.argv)
    DialogTester(app)
    app.create()
    app.run()

if __name__ == '__main__':
    runme()
