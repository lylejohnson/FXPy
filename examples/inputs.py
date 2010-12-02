#!/usr/bin/env python

import os
import sys
from FXPy.fox import *

class InputHandlerWindow(FXMainWindow):

    # Message identifiers
    ID_PIPE = FXMainWindow.ID_LAST
    ID_TEXT = FXMainWindow.ID_LAST + 1

    def __init__(self, app):
        # Calls the base class constructor first
        FXMainWindow.__init__(self, app, "Input Handlers Test", w=400, h=300)

        # Set up the message map for this class
        FXMAPFUNC(self, SEL_COMMAND, InputHandlerWindow.ID_TEXT,
                  InputHandlerWindow.onCmdText)
        FXMAPFUNC(self, SEL_IO_READ, InputHandlerWindow.ID_PIPE,
                  InputHandlerWindow.onPipeRead)
        FXMAPFUNC(self, SEL_IO_EXCEPT, InputHandlerWindow.ID_PIPE,
                  InputHandlerWindow.onPipeException)

        # Text area plus a button
        commands = FXHorizontalFrame(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)
        FXLabel(commands, "Command:")
        self.cmdInput = FXTextField(commands, 30,
            self, InputHandlerWindow.ID_TEXT,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X) 
        FXHorizontalSeparator(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X)
        textFrame = FXVerticalFrame(self,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Output will be displayed in a multiline text area
        self.cmdOutput = FXText(textFrame, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Initialize the pipe
        self.pipe = None

    def create(self):
        """Create and show the main window."""
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    def onCmdText(self, sender, sel, ptr):
        """User typed a new command for us to try."""

        # Remove previous input (if any)
        if self.pipe:
            self.getApp().removeInput(self.pipe, INPUT_READ|INPUT_EXCEPT)

        # Clean up the output window
        self.cmdOutput.setText("")

        # Open a new pipe
        self.pipe = os.popen(self.cmdInput.getText(), "r")

        # Register input callbacks and return
        self.getApp().addInput(self.pipe, INPUT_READ|INPUT_EXCEPT,
                               self, InputHandlerWindow.ID_PIPE)
        return 1

    def onPipeRead(self, sender, sel, ptr):
        """This handler should get called when there's input waiting."""
        latest = self.pipe.read()
        if not latest:
            self.getApp().removeInput(self.pipe, INPUT_READ|INPUT_EXCEPT)
            self.pipe = None
        self.cmdOutput.appendText(latest, len(latest))
        return 1

    def onPipeException(self, sender, sel, ptr):
        """An exception occurred on the input source."""
        print 'onPipeExcept'
        return 1

def run():
    # Construct an application
    application = FXApp("InputHandler", "FoxTest")

    # Open the display
    application.init(sys.argv)

    # Construct the main window
    InputHandlerWindow(application)

    # Create and show the window
    application.create()

    # Run it
    return application.run()

# Main program starts here
if __name__ == "__main__":
    run()
