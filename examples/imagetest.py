#! /usr/bin/env python

from FXPy.fox import *
from array import array

# Main window class
class ImageWindow(FXMainWindow):
    # Message IDs
    ID_CANVAS   = FXMainWindow.ID_LAST
    ID_WELL     = ID_CANVAS + 1

    # Initializer
    def __init__(self, app):
        FXMainWindow.__init__(self,app,'Image Application',w=800,h=600)

        FXMAPFUNC(self,SEL_PAINT,ImageWindow.ID_CANVAS,ImageWindow.onPaint)
        FXMAPFUNC(self,SEL_COMMAND,ImageWindow.ID_WELL,ImageWindow.onCmdWell)

        colordlg = FXColorDialog(self,'Color Dialog')

        contents = FXHorizontalFrame(self,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0)

        # LEFT pane to contain the canvas
        canvasFrame = FXVerticalFrame(contents,
            FRAME_SUNKEN|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10)

        # Label above the canvas
        FXLabel(canvasFrame,'Canvas Frame',opts=JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(canvasFrame,SEPARATOR_GROOVE|LAYOUT_FILL_X)

        # Drawing canvas
        self.canvas = FXCanvas(canvasFrame, self, self.ID_CANVAS,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)

        # RIGHT pane for the buttons
        buttonFrame = FXVerticalFrame(contents,
            FRAME_SUNKEN|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,10,10)

        # Label above the buttons
        FXLabel(buttonFrame,"Button Frame",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(buttonFrame,SEPARATOR_RIDGE|LAYOUT_FILL_X)

        FXLabel(buttonFrame,"&Background\nColor well",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        self.backwell = FXColorWell(buttonFrame,FXRGB(255,255,255),self,self.ID_WELL,LAYOUT_CENTER_X|LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,100,30)

        FXLabel(buttonFrame,"B&order\nColor well",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        self.borderwell = FXColorWell(buttonFrame,FXRGB(0,0,0),self,self.ID_WELL,LAYOUT_CENTER_X|LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,100,30)

        FXLabel(buttonFrame,"&Text\nColor well",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)
        self.textwell = FXColorWell(buttonFrame,FXRGB(0,0,0),self,self.ID_WELL,LAYOUT_CENTER_X|LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,100,30)

        # Button to draw
        FXButton(buttonFrame,"&Colors...\tPop the color dialog",None,colordlg,FXWindow.ID_SHOW,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)

        # Exit button
        FXButton(buttonFrame, 'E&xit\tQuit ImageApp', None,
            self.getApp(), FXApp.ID_QUIT,
            FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,
            0,0,0,0,10,10,5,5)

        # Create images
        w, h = 512, 50
        grey, red, green, blue = self.makeColorRamps(w, h)

        self.grey = FXImage(self.getApp(),None,IMAGE_OWNED,w,h)
        self.red = FXImage(self.getApp(),None,IMAGE_OWNED,w,h)
        self.green = FXImage(self.getApp(),None,IMAGE_OWNED,w,h)
        self.blue = FXImage(self.getApp(),None,IMAGE_OWNED,w,h)

        # Make the font
        self.font = FXFont(self.getApp(), "times", 36, FONTWEIGHT_BOLD)

        # Make a tooltip
        FXTooltip(self.getApp())

    def makeColorRamps(self, w, h):
        size = 3*w*h
        grey = array('c', size*'\0')
        red = array('c', size*'\0')
        green = array('c', size*'\0')
        blue = array('c', size*'\0')
        for x in xrange(w):
            for y in xrange(h):
                grey[3*(y*w+x)] = chr(x/2)
                grey[3*(y*w+x)+1] = chr(x/2)
                grey[3*(y*w+x)+2] = chr(x/2)
            for y in xrange(h):
                red[3*(y*w+x)] = chr(x/2)
                red[3*(y*w+x)+1] = chr(0)
                red[3*(y*w+x)+2] = chr(0)
            for y in xrange(h):
                green[3*(y*w+x)] = chr(0)
                green[3*(y*w+x)+1] = chr(x/2)
                green[3*(y*w+x)+2] = chr(0)
            for y in xrange(h):
                blue[3*(y*w+x)] = chr(0)
                blue[3*(y*w+x)+1] = chr(0)
                blue[3*(y*w+x)+2] = chr(x/2)
        grey = grey.tostring()
        red = red.tostring()
        green = green.tostring()
        blue = blue.tostring()
        return grey, red, green, blue

    # Create and initialize
    def create(self):
        FXMainWindow.create(self)

        # Create images
        self.grey.create()
        self.red.create()
        self.green.create()
        self.blue.create()

        # Font too
        self.font.create()

        # Show it
        self.show(PLACEMENT_SCREEN)

    # Expose
    def onPaint(self, sender, sel, event):
        canvas = self.canvas
        dc = FXDCWindow(canvas, event)

        # Erase canvas to background color
        dc.setForeground(self.backwell.getRGBA())
        dc.fillRectangle(0, 0, canvas.getWidth(), canvas.getHeight())

        # Draw images
        dc.drawImage(self.grey, 10, 50)
        dc.drawImage(self.red, 10, 150)
        dc.drawImage(self.green, 10, 250)
        dc.drawImage(self.blue, 10, 350)

        # Draw patterns
        dc.setFillStyle(FILL_OPAQUESTIPPLED)
        dc.setForeground(FXRGB(0,0,0))
        dc.setBackground(FXRGB(255,255,255))
        for pat in xrange(STIPPLE_0,STIPPLE_16):
            dc.setStipple(pat)
            dc.fillRectangle(10+(512*pat)/17, 450, 31, 50)
        dc.setFillStyle(FILL_SOLID);

        # Draw borders
        dc.setForeground(self.borderwell.getRGBA())
        dc.drawRectangle(10, 50, 512, 50)
        dc.drawRectangle(10, 150, 512, 50)
        dc.drawRectangle(10, 250, 512, 50)
        dc.drawRectangle(10, 350, 512, 50)
        dc.drawRectangle(10, 450, 512, 50)

        # Draw text
        dc.setTextFont(self.font)
        dc.setForeground(self.textwell.getRGBA())
        dc.drawText(540, 90, "Grey", 4)
        dc.drawText(540, 190, "Red", 3)
        dc.drawText(540, 290, "Green", 5)
        dc.drawText(540, 390, "Blue", 4)
        dc.drawText(540, 490, "Patterns", 8)

    # Color well changed
    def onCmdWell(self, sender, sel, ptr):
        self.canvas.update()

def runme():
    import sys
    app = FXApp()
    app.init(sys.argv)
    ImageWindow(app)
    app.create()
    app.run()

# Main program starts here
if __name__ == '__main__':
    runme()
