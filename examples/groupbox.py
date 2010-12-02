#! /usr/bin/env python

from FXPy.fox import *
from thread import start_new_thread
from time import localtime, sleep, strftime, time, localtime
import os

def updateClock(clockLabel):
    """Continuously updates the clock label"""
    while 1:
        clockLabel.setText(strftime("%I:%M:%S %p", localtime(time())))
        sleep(1)

class GroupWindow(FXMainWindow):

    ID_DOWNSIZE = FXMainWindow.ID_LAST
    ID_POPUP    = ID_DOWNSIZE + 1
    ID_ABOUT    = ID_POPUP + 1
    ID_DELETE   = ID_ABOUT + 1
    ID_OPEN     = ID_DELETE + 1
    ID_OPTION1  = ID_OPEN + 1
    ID_OPTION2  = ID_OPTION1 + 1
    ID_OPTION3  = ID_OPTION2 + 1
    ID_OPTION4  = ID_OPTION3 + 1
    ID_RADIO1   = ID_OPTION4 + 1
    ID_RADIO2   = ID_RADIO1 + 1
    ID_RADIO3   = ID_RADIO2 + 1

    def loadIcon(self, filename):
        filename = os.path.join('icons', filename)
        return FXPNGIcon(self.getApp(), open(filename, 'rb').read())

    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Group Box Test", w=800, h=600)

        FXMAPFUNC(self, SEL_COMMAND, GroupWindow.ID_DOWNSIZE, GroupWindow.onCmdDownSize)
        FXMAPFUNC(self, SEL_COMMAND, GroupWindow.ID_DELETE, GroupWindow.onCmdDelete)
        FXMAPFUNCS(self, SEL_COMMAND, GroupWindow.ID_RADIO1, GroupWindow.ID_RADIO3, GroupWindow.onCmdRadio)
        FXMAPFUNCS(self, SEL_UPDATE, GroupWindow.ID_RADIO1, GroupWindow.ID_RADIO3, GroupWindow.onUpdRadio)
        FXMAPFUNC(self, SEL_COMMAND, GroupWindow.ID_POPUP, GroupWindow.onCmdPopup)
        FXMAPFUNC(self, SEL_COMMAND, GroupWindow.ID_ABOUT, GroupWindow.onCmdAbout)
        FXMAPFUNC(self, SEL_COMMAND, GroupWindow.ID_OPEN, GroupWindow.onCmdOpen)
        FXMAPFUNCS(self, SEL_COMMAND, GroupWindow.ID_OPTION1, GroupWindow.ID_OPTION4, GroupWindow.onCmdOption)

        FXTooltip(self.getApp(), 0, 100, 100)

        doc = self.loadIcon('minidoc.png')
        folder_open = self.loadIcon('minifolderopen.png')
        folder_closed = self.loadIcon('minifolder.png')

        # Menubar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
        self.filemenu = FXMenuPane(self)
        FXMenuCommand(self.filemenu, "&Open\tCtl-O\tOpen a file.",
            None, self, self.ID_OPEN)
        FXMenuCommand(self.filemenu, "Radio&1", None, self, self.ID_RADIO1)
        FXMenuCommand(self.filemenu, "Radio&2", None, self, self.ID_RADIO2)
        FXMenuCommand(self.filemenu, "Radio&3", None, self, self.ID_RADIO3)
        FXMenuCommand(self.filemenu, "Delete\tCtl-X", None, self, self.ID_DELETE)
        FXMenuCommand(self.filemenu, "Downsize", None, self, self.ID_DOWNSIZE)
        FXMenuCommand(self.filemenu, "&Size", None, self, self.ID_DOWNSIZE)
        FXMenuCommand(self.filemenu, "Dump Widgets", None, self.getApp(), FXApp.ID_DUMP)

        # Make edit popup menu
        editmenu = FXMenuPane(self)
        FXMenuCommand(editmenu, "Undo")
        FXMenuCommand(editmenu, "Cut")
        submenu1 = FXMenuPane(editmenu)
        FXMenuCommand(submenu1, "&One")
        FXMenuCommand(submenu1, "&Two")
        FXMenuCommand(submenu1, "Th&ree")
        FXMenuCommand(submenu1, "&Four")
        FXMenuCascade(editmenu, "&Submenu1", None, submenu1)
        FXMenuCascade(self.filemenu, "&Edit", None, editmenu)
        FXMenuCommand(self.filemenu, "&Quit", None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, self.filemenu)

        # Help menu
        helpmenu = FXMenuPane(self)
        FXMenuCommand(helpmenu, "&About FOX...", None, self, self.ID_ABOUT)
        FXMenuTitle(menubar, "&Help", None, helpmenu, LAYOUT_RIGHT)

        # Status bar
        status = FXStatusbar(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)
        self.clockLabel = FXLabel(status,
            strftime("%I:%M:%S %p", localtime(time())), None,
            LAYOUT_FILL_Y|LAYOUT_RIGHT|FRAME_SUNKEN)

        # Contents
        contents = FXHorizontalFrame(self, LAYOUT_SIDE_TOP|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        group1 = FXGroupBox(contents, "Title Left", GROUPBOX_TITLE_LEFT|FRAME_RIDGE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        group2 = FXGroupBox(contents, "Slider Tests", GROUPBOX_TITLE_CENTER|FRAME_RIDGE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        group3 = FXGroupBox(contents, "Title Right", GROUPBOX_TITLE_RIGHT|FRAME_RIDGE|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        testlabel = FXLabel(group1, "&This is a multi-line\nlabel widget\nwith a big font", None, LAYOUT_CENTER_X|JUSTIFY_CENTER_X)
        #testlabel.setFont(FXFont(self.getApp(),"helvetica",24,FONTWEIGHT_BOLD,FONTSLANT_ITALIC,FONTENCODING_DEFAULT))

        FXButton(group1, "Small &Button", opts=LAYOUT_BOTTOM|FRAME_RAISED|FRAME_THICK)
        FXButton(group1, "Downsize", None, self, self.ID_DOWNSIZE, FRAME_RAISED|FRAME_THICK)
        FXButton(group1, "Big Fat Wide Button\nComprising\nthree lines", None, None, 0, FRAME_RAISED|FRAME_THICK)

        pop = FXPopup(self)
        FXOption(pop, "First\tTip #1\tHelp first", None, self, self.ID_OPTION1, JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop, "Second\tTip #2\tHelp second", None, self, self.ID_OPTION2, JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop, "Third\tTip #3\tHelp third", None, self, self.ID_OPTION3, JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOption(pop, "Fourth\tTip #4\tHelp fourth", None, self, self.ID_OPTION4, JUSTIFY_HZ_APART|ICON_AFTER_TEXT)
        FXOptionMenu(group1, pop, LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|JUSTIFY_HZ_APART|ICON_AFTER_TEXT)

        FXLabel(group1, "Te&kstje", None, LAYOUT_TOP|JUSTIFY_LEFT)
        FXButton(group1, "Add an `&&' by doubling\tTooltip\tHelp text for status", None, None, 0, LAYOUT_TOP|FRAME_RAISED|FRAME_THICK)
        FXButton(group1, "Te&kstje", None, self, self.ID_POPUP, LAYOUT_TOP|FRAME_RAISED|FRAME_THICK)

        FXMenuButton(group1, "&Menu", None, self.filemenu, MENUBUTTON_ATTACH_BOTH|MENUBUTTON_DOWN|JUSTIFY_HZ_APART|LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|ICON_AFTER_TEXT)
        FXMenuButton(group1, "&Menu", None, self.filemenu, MENUBUTTON_UP|LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|ICON_AFTER_TEXT)

        coolpop = FXPopup(self, POPUP_HORIZONTAL)
        FXButton(coolpop, "A\tTipA", opts=FRAME_THICK|FRAME_RAISED|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, w=30, h=30)
        FXButton(coolpop, "B\tTipB", opts=FRAME_THICK|FRAME_RAISED|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, w=30, h=30)
        FXButton(coolpop, "C\tTipC", opts=FRAME_THICK|FRAME_RAISED|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, w=30, h=30)
        FXButton(coolpop, "D\tTipD", opts=FRAME_THICK|FRAME_RAISED|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, w=30, h=30)
        FXMenuButton(group1, "&S\tSideways", None, coolpop, MENUBUTTON_ATTACH_BOTH|MENUBUTTON_RIGHT|MENUBUTTON_NOARROWS|LAYOUT_TOP|FRAME_RAISED|FRAME_THICK|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT, w=30, h=30)

        matrix = FXMatrix(group1, 3, FRAME_RAISED|LAYOUT_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXButton(matrix,"A",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW)
        FXButton(matrix,"&Wide button",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)
        FXButton(matrix,"A",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)

        FXButton(matrix,"BB",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW|LAYOUT_FILL_COLUMN)
        FXButton(matrix,"B",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)
        FXButton(matrix,"BB",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_COLUMN)

        FXButton(matrix,"C",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_Y|LAYOUT_CENTER_X|LAYOUT_FILL_ROW)
        FXButton(matrix,"&wide",opts=FRAME_RAISED|FRAME_THICK)
        FXButton(matrix,"CC",opts=FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT)

        FXLabel(group2,"No Arrow")
        FXSlider(group2,opts=LAYOUT_TOP|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|SLIDER_HORIZONTAL,w=200,h=30)

        FXLabel(group2,"Up Arrow")
        FXSlider(group2,None,0,LAYOUT_TOP|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|SLIDER_HORIZONTAL|SLIDER_ARROW_UP,0,0,200,30)

        FXLabel(group2,"Down Arrow")
        FXSlider(group2,None,0,LAYOUT_TOP|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|SLIDER_HORIZONTAL|SLIDER_ARROW_DOWN,0,0,200,30)

        FXLabel(group2, "Inside Bar");
        slider = FXSlider(group2,None,0,LAYOUT_TOP|LAYOUT_FILL_X|LAYOUT_FIX_HEIGHT|SLIDER_HORIZONTAL|SLIDER_INSIDE_BAR,0,0,200,20)
        slider.setRange(0, 3)

        frame = FXHorizontalFrame(group2,LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXSlider(frame,None,0,LAYOUT_FIX_HEIGHT|SLIDER_VERTICAL,0,0,30,200)
        FXSlider(frame,None,0,LAYOUT_FIX_HEIGHT|SLIDER_VERTICAL|SLIDER_ARROW_RIGHT,0,0,30,200)
        FXSlider(frame,None,0,LAYOUT_FIX_HEIGHT|SLIDER_VERTICAL|SLIDER_ARROW_LEFT,0,0,30,200)
        FXSlider(frame,None,0,LAYOUT_FIX_HEIGHT|SLIDER_VERTICAL|SLIDER_INSIDE_BAR,0,0,20,200)

        vframe1 = FXVerticalFrame(frame,LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXArrowButton(vframe1,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_UP)
        FXArrowButton(vframe1,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_DOWN)
        FXArrowButton(vframe1,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_LEFT)
        FXArrowButton(vframe1,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_RIGHT)
        vframe2 = FXVerticalFrame(frame,LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXArrowButton(vframe2,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_UP|ARROW_TOOLBAR)
        FXArrowButton(vframe2,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_DOWN|ARROW_TOOLBAR)
        FXArrowButton(vframe2,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_LEFT|ARROW_TOOLBAR)
        FXArrowButton(vframe2,opts=LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_RAISED|FRAME_THICK|ARROW_RIGHT|ARROW_TOOLBAR)

        gp = FXGroupBox(group3,"Group Box",LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        FXRadioButton(gp,"Hilversum 1",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXRadioButton(gp,"Hilversum 2",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXRadioButton(gp,"One multi-line\nRadiobox Widget",opts=JUSTIFY_LEFT|JUSTIFY_TOP|ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXRadioButton(gp,"Radio Stad Amsterdam",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)

        vv = FXGroupBox(group3,"Group Box",LAYOUT_SIDE_TOP|FRAME_GROOVE|LAYOUT_FILL_X, 0,0,0,0)
        FXCheckButton(vv,"Hilversum 1",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXCheckButton(vv,"Hilversum 2",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXCheckButton(vv,"One multi-line\nCheckbox Widget",opts=JUSTIFY_LEFT|JUSTIFY_TOP|ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)
        FXCheckButton(vv,"Radio Stad Amsterdam",opts=ICON_BEFORE_TEXT|LAYOUT_SIDE_TOP)

        spinner = FXSpinner(group3,20,opts=SPIN_NORMAL|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        spinner.setRange(0, 1000)

        combobox = FXComboBox(group3,5,5,opts=COMBOBOX_INSERT_LAST|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        combobox.appendItem("Very Wide Item")
        for i in xrange(3): combobox.appendItem("%04d" % i)

        treebox = FXTreeListBox(group3, 10, None, 0,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP, 0, 0, 200, 0)
        topmost = treebox.addItemLast(None,"Top",folder_open,folder_closed)
        topmost2 = treebox.addItemLast(None,"Top2",folder_open,folder_closed)
        treebox.addItemLast(topmost2,"First",doc,doc)
        treebox.addItemLast(topmost,"First",doc,doc)
        treebox.addItemLast(topmost,"Second",doc,doc)
        treebox.addItemLast(topmost,"Third",doc,doc)
        branch = treebox.addItemLast(topmost,"Fourth",folder_open,folder_closed)
        treebox.addItemLast(branch,"Fourth-First",doc,doc)
        treebox.addItemLast(branch,"Fourth-Second",doc,doc)
        twig = treebox.addItemLast(branch,"Fourth-Third",folder_open,folder_closed)
        treebox.addItemLast(twig,"Fourth-Third-First",doc,doc)
        treebox.addItemLast(twig,"Fourth-Third-Second",doc,doc)
        treebox.addItemLast(twig,"Fourth-Third-Third",doc,doc)
        leaf = treebox.addItemLast(twig,"Fourth-Third-Fourth",folder_open,folder_closed)
        treebox.addItemLast(leaf,"Fourth-Third-Fourth-First",doc,doc)
        treebox.addItemLast(leaf,"Fourth-Third-Fourth-Second",doc,doc)
        treebox.addItemLast(leaf,"Fourth-Third-Fourth-Third",doc,doc)
        twig = treebox.addItemLast(branch,"Fourth-Fourth",folder_open,folder_closed)
        treebox.addItemLast(twig,"Fourth-Fourth-First",doc,doc)
        treebox.addItemLast(twig,"Fourth-Fourth-Second",doc,doc)
        treebox.addItemLast(twig,"Fourth-Fourth-Third",doc,doc)

        FXLabel(group3,"H&it the hotkey",None,LAYOUT_CENTER_X|JUSTIFY_CENTER_X|FRAME_RAISED)
        textfield1 = FXTextField(group3,20,opts=JUSTIFY_RIGHT|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        textfield1.setText("Normal Text Field")
        textfield2 = FXTextField(group3,20,opts=JUSTIFY_RIGHT|TEXTFIELD_PASSWD|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        textfield2.setText("Password")
        textfield3 = FXTextField(group3,20,opts=TEXTFIELD_READONLY|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        textfield3.setText("Read Only")
        textfield4 = FXTextField(group3,20,opts=TEXTFIELD_READONLY|FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP)
        textfield4.setText("Grayed out")
        textfield4.disable()

        FXTextField(group3,20,None,0,FRAME_SUNKEN|FRAME_THICK|LAYOUT_SIDE_TOP|LAYOUT_FIX_HEIGHT,0,0,0,30)

        dial2 = FXDial(group3,None,0,DIAL_CYCLIC|DIAL_HAS_NOTCH|DIAL_HORIZONTAL|LAYOUT_FILL_X|FRAME_RAISED|FRAME_THICK,0,0,120,0)

        pbar = FXProgressBar(group3,opts=LAYOUT_FILL_X|FRAME_SUNKEN|FRAME_THICK|PROGRESSBAR_PERCENTAGE)
        pbar.setProgress(48)
        pbar.setTotal(360)
        pbar2 = FXProgressBar(group3,opts=LAYOUT_FILL_Y|FRAME_SUNKEN|FRAME_THICK|PROGRESSBAR_VERTICAL|PROGRESSBAR_PERCENTAGE|LAYOUT_SIDE_LEFT)
        pbar2.setTotal(360)
        dial1 = FXDial(group3,opts=DIAL_CYCLIC|DIAL_HAS_NOTCH|DIAL_VERTICAL|FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_Y|LAYOUT_SIDE_LEFT)
        pbar2.setProgress(48)
        dial1.setTarget(pbar2)
        dial1.setSelector(FXWindow.ID_SETVALUE)
        dial2.setTarget(pbar)
        dial2.setSelector(FXWindow.ID_SETVALUE)

        self.choice = 0

    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

        # Create a new thread, to update the clock
        start_new_thread(updateClock, (self.clockLabel,))

    # Open file dialog test
    def onCmdOpen(self, sender, sel, ptr):
        open = FXFileDialog(self, "Open some file")
        open.setPatternList("All Files (*)")
        if open.execute(): print "User selected file", open.getFilename()

    # Test window resizing
    def onCmdDownSize(self, sender, sel, ptr):
        self.resize(self.getDefaultWidth(), self.getDefaultHeight())

    # Still not sure how to make this work!
    def onCmdDelete(self, sender, sel, ptr):
        self.group2 = None

    # About
    def onCmdAbout(self, sender, sel, ptr):
        showModalInformationBox(self,MBOX_OK, "About FOX:- An intentionally long title","FOX is a really, really cool C++ library!\nExample written by Jeroen")

    # Set choice
    def onCmdRadio(self, sender, sel, ptr):
        self.choice = SELID(sel)

    # Show a popup menu
    def onCmdPopup(self, sender, sel, ptr):
        x, y, buttons = self.getRoot().getCursorPosition()
        self.filemenu.popup(None, x, y)

    # Update menu
    def onUpdRadio(self, sender, sel, ptr):
        if SELID(sel) == self.choice:
            sender.checkRadio()
        else:
            sender.uncheckRadio()

    def onCmdOption(self, sender, sel, ptr):
        print "Chose option", SELID(sel) - self.ID_OPTION1 + 1

def runme():
    import sys
    application = FXApp("Groupbox", "Test")
    application.init(sys.argv)
    GroupWindow(application)
    application.create()
    application.run()

# Main program starts here
if __name__ == '__main__':
    runme()
