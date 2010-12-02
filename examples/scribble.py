#! /usr/bin/env python

from FXPy.fox import *

# Main window
class ScribbleWindow(FXMainWindow):
    # Message IDs
    ID_CANVAS = FXMainWindow.ID_LAST
    ID_CLEAR = ID_CANVAS + 1
    ID_LAST = ID_CLEAR + 1

    # Constructor
    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Scribble Application", w=800, h=600)

        # Set up message map
        FXMAPFUNC(self, SEL_COMMAND, self.ID_CLEAR, ScribbleWindow.onCmdClear)
        FXMAPFUNC(self, SEL_UPDATE,  self.ID_CLEAR, ScribbleWindow.onUpdClear)
        FXMAPFUNC(self, SEL_PAINT,   self.ID_CANVAS,ScribbleWindow.onPaint)
        FXMAPFUNC(self, SEL_LEFTBUTTONPRESS, self.ID_CANVAS, ScribbleWindow.onMouseDown)
        FXMAPFUNC(self, SEL_LEFTBUTTONRELEASE, self.ID_CANVAS, ScribbleWindow.onMouseUp)
        FXMAPFUNC(self, SEL_MOTION, self.ID_CANVAS, ScribbleWindow.onMouseMove)

        # Main frame
        self.contents = FXHorizontalFrame(self,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0)

        # Left pane to contain the canvas
        self.canvasFrame = FXVerticalFrame(self.contents,
            FRAME_SUNKEN|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10)

        # Label above the canvas
        FXLabel(self.canvasFrame, "Canvas Frame", None,
            JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(self.canvasFrame, SEPARATOR_GROOVE|LAYOUT_FILL_X)

        # Drawing canvas
        self.canvas = FXCanvas(self.canvasFrame, self, self.ID_CANVAS,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)

        # Right pane for the buttons
        self.buttonFrame = FXVerticalFrame(self.contents,
            FRAME_SUNKEN|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10)

        # Label above the buttons
        FXLabel(self.buttonFrame, "Button Frame", None,
            JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(self.buttonFrame, SEPARATOR_RIDGE|LAYOUT_FILL_X)

        # Button to clear
        self.clear = FXButton(self.buttonFrame, "&Clear", None, self,
            self.ID_CLEAR,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        # Exit button
        FXButton(self.buttonFrame, "&Exit", None, app, FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        # Initialize private variables
        self.drawColor = FXRGB(255,0,0)
        self.mdflag = 0
        self.dirty = 0

    # Create and initialize
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    # Mouse button was pressed somewhere
    def onMouseDown(self, sender, sel, ptr):
        self.mdflag = 1

    # Mouse has moved, so draw a line
    def onMouseMove(self, sender, sel, ev):
        if self.mdflag == 1:
            dc = FXDCWindow(self.canvas)
            dc.setForeground(self.drawColor)
            dc.drawLine(ev.last_x, ev.last_y, ev.win_x, ev.win_y)
            self.dirty = 1

    # The mouse button was released again
    def onMouseUp(self, sender, sel, ev):
        if self.mdflag == 1:
            dc = FXDCWindow(self.canvas)
            dc.setForeground(self.drawColor)
            dc.drawLine(ev.last_x, ev.last_y, ev.win_x, ev.win_y)
            self.dirty = 1
            self.mdflag = 0

    # Paint the canvas
    def onPaint(self, sender, sel, ev):
        dc = FXDCWindow(self.canvas, ev)
        dc.setForeground(self.canvas.getBackColor())
        dc.fillRectangle(ev.rect.x, ev.rect.y, ev.rect.w, ev.rect.h)

    # Handle the clear message
    def onCmdClear(self, sender, sel, ptr):
        dc = FXDCWindow(self.canvas)
        dc.setForeground(self.canvas.getBackColor())
        dc.fillRectangle(0, 0, self.canvas.getWidth(), self.canvas.getHeight())
        self.dirty = 0

    # Update the clear button
    def onUpdClear(self, sender, sel, ptr):
        if self.dirty == 1:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),NULL)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),NULL)

def runme():
    # Make application
    application = FXApp("Scribble", "Test")

    # Start app
    import sys
    application.init(sys.argv)

    # Create scribble window
    scribble = ScribbleWindow(application)

    # Create the application's windows
    application.create()

    # Run the application
    application.run()

# Main program begins here
if __name__ == "__main__":
    runme()
