#!/bin/env python

import sys
from FXPy.fox import *

class DataTargetWindow(FXMainWindow):
    # Message identifiers for this class
    ID_TIMER, ID_QUIT = range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+2)

    def __init__(self, app):
        # Call base class __init__() first
        FXMainWindow.__init__(self, app, "Data Target Test", opts=DECOR_ALL,
                              x=20, y=20, w=700, h=460)

        # Initialize the data targets for this example
        self.intTarget      = FXDataTarget(10)
        self.floatTarget    = FXDataTarget(3.1415927)
        self.stringTarget   = FXDataTarget("FOX")
        self.colorTarget    = FXRGB(255, 0, 0)
        self.optionTarget   = FXDataTarget(1)
        self.progressTarget = FXDataTarget(0)

        # Menu bar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
  
        # File menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, "&Quit\tCtl-Q", None, self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, "&File", None, filemenu)
  
        # Option menu
        optionmenu = FXMenuPane(self)
        FXMenuCommand(optionmenu, "Option 1", None, self.optionTarget, FXDataTarget.ID_OPTION+1)
        FXMenuCommand(optionmenu, "Option 2", None, self.optionTarget, FXDataTarget.ID_OPTION+2)
        FXMenuCommand(optionmenu, "Option 3", None, self.optionTarget, FXDataTarget.ID_OPTION+3)
        FXMenuCommand(optionmenu, "Option 4", None, self.optionTarget, FXDataTarget.ID_OPTION+4)
        FXMenuTitle(menubar, "&Option", None, optionmenu)
  
        # Lone progress bar at the bottom
        FXProgressBar(self, self.progressTarget, FXDataTarget.ID_VALUE,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|FRAME_SUNKEN|FRAME_THICK)
  
        FXHorizontalSeparator(self, LAYOUT_SIDE_TOP|SEPARATOR_GROOVE|LAYOUT_FILL_X)
  
        FXLabel(self,
    "FXDataTarget can be used to connect a Widget to an application variable without any of the\n"
    "tradional \"glue\" programming code.\n\n"
    "The widgets below are connected (via FXDataTarget) to an integer, real, string, option, and\n"
    "color variable, respectively.\n\n"
    "Changing one of them will cause all widgets connected to the same FXDataTarget to \n"
    "update so as to reflect the value of the application variable.\n\n"
    "The progress bar below shows a time-varying variable, demonstrating that widgets\n"
    "can be updated via FXDataTarget's regardless how the variables are changed.\n\n"
    "Note that the \"Option\" pulldown menu is also connected to the option variable!",  
    NULL,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|JUSTIFY_LEFT);
    
        FXHorizontalSeparator(self, LAYOUT_SIDE_TOP|SEPARATOR_GROOVE|LAYOUT_FILL_X)
        FXSlider(self, self.intTarget, FXDataTarget.ID_VALUE,
            SLIDER_VERTICAL|SLIDER_INSIDE_BAR|LAYOUT_SIDE_RIGHT|LAYOUT_FILL_Y|LAYOUT_FIX_WIDTH,
            0, 0, 20, 0)
  
        # Arrange nicely
        matrix = FXMatrix(self, 7, MATRIX_BY_COLUMNS|LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)
  
        # First row
        FXLabel(matrix, "&Integer", None, LAYOUT_CENTER_Y|LAYOUT_CENTER_X|JUSTIFY_RIGHT|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.intTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.intTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXSlider(matrix, self.intTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_ROW|LAYOUT_FIX_WIDTH, 0, 0, 100)
        FXDial(matrix, self.intTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_ROW|LAYOUT_FIX_WIDTH|DIAL_HORIZONTAL|DIAL_HAS_NOTCH, 0, 0, 100)
        FXSpinner(matrix, 5, self.intTarget, FXDataTarget.ID_VALUE,
            SPIN_CYCLIC|FRAME_SUNKEN|FRAME_THICK|LAYOUT_CENTER_Y|LAYOUT_FILL_ROW)
        FXProgressBar(matrix, self.intTarget, FXDataTarget.ID_VALUE, (LAYOUT_CENTER_Y|LAYOUT_FILL_X|
            FRAME_SUNKEN|FRAME_THICK|PROGRESSBAR_PERCENTAGE|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW))
  
        # Second row
        FXLabel(matrix, "&Real", None, LAYOUT_CENTER_Y|LAYOUT_CENTER_X|JUSTIFY_RIGHT|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.floatTarget, FXDataTarget.ID_VALUE,
            TEXTFIELD_REAL|LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.floatTarget, FXDataTarget.ID_VALUE,
            TEXTFIELD_REAL|LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXSlider(matrix, self.floatTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_X|LAYOUT_FILL_ROW|LAYOUT_FIX_WIDTH, 0, 0, 100)
        FXDial(matrix, self.floatTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_X|LAYOUT_FILL_ROW|LAYOUT_FIX_WIDTH|DIAL_HORIZONTAL|DIAL_HAS_NOTCH, 0, 0, 100)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
  
        # Third row
        FXLabel(matrix, "&String", None, LAYOUT_CENTER_Y|LAYOUT_CENTER_X|JUSTIFY_RIGHT|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.stringTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.stringTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
  
	# Fourth row
        FXLabel(matrix, "&Option", None, LAYOUT_CENTER_Y|LAYOUT_CENTER_X|JUSTIFY_RIGHT|LAYOUT_FILL_ROW)
        FXTextField(matrix, 10, self.optionTarget, FXDataTarget.ID_VALUE,
            TEXTFIELD_INTEGER|LAYOUT_CENTER_Y|LAYOUT_CENTER_X|FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_ROW)
        FXRadioButton(matrix, "Option &1", self.optionTarget, FXDataTarget.ID_OPTION+1,
            LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW|ICON_BEFORE_TEXT)
        FXRadioButton(matrix, "Option &2", self.optionTarget, FXDataTarget.ID_OPTION+2,
            LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW|ICON_BEFORE_TEXT)
        FXRadioButton(matrix, "Option &3", self.optionTarget, FXDataTarget.ID_OPTION+3,
            LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW|ICON_BEFORE_TEXT)
        FXRadioButton(matrix, "Option &4", self.optionTarget, FXDataTarget.ID_OPTION+4,
            LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW|ICON_BEFORE_TEXT)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
  
        # Fifth
        FXLabel(matrix, "&Color", None, LAYOUT_CENTER_Y|LAYOUT_CENTER_X|JUSTIFY_RIGHT|LAYOUT_FILL_ROW)
        FXColorWell(matrix, 0, self.colorTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_X|LAYOUT_FILL_ROW, 0, 0, 0, 0, 0, 0, 0, 0)
        FXColorWell(matrix, 0, self.colorTarget, FXDataTarget.ID_VALUE,
            LAYOUT_CENTER_Y|LAYOUT_FILL_X|LAYOUT_FILL_ROW, 0, 0, 0, 0, 0, 0, 0, 0)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
        FXFrame(matrix, LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)
  
        # Install an accelerator
        self.getAccelTable().addAccel(fxparseaccel("Ctl-Q"), self.getApp(), MKUINT(FXApp.ID_QUIT, SEL_COMMAND))

        # Set up the message map
        FXMAPFUNC(self, SEL_TIMEOUT, DataTargetWindow.ID_TIMER, DataTargetWindow.onCmdTimer)

    def create(self):
        # Create the windows
        FXMainWindow.create(self)

        # Kick off the timer
        self.getApp().addTimeout(80, self, DataTargetWindow.ID_TIMER)

        # Show the main window centered on the screen
        self.show(PLACEMENT_SCREEN)

    def onCmdTimer(self, sender, sel, ptr):
        """Increment progress in response to timer firing."""
        self.progressTarget.setValue((self.progressTarget.getValue() + 1) % 100)
        self.getApp().addTimeout(80, self, DataTargetWindow.ID_TIMER)

def run():
    # Make application
    application = FXApp("DataTarget", "FoxTest")

    # Open display
    application.init(sys.argv)

    # Create the main window
    window = DataTargetWindow(application)

    # Create application
    application.create()

    # Run
    return application.run()

if __name__ == "__main__":
    run()
