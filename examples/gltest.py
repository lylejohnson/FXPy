#!/usr/local/bin/python

from FXPy.fox import *
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print "Sorry, couldn't import the PyOpenGL module."
    raise SystemExit

# Test for OpenGL
class GLTestWindow(FXMainWindow):
    # Enumerated message identifiers
    ID_CANVAS, ID_SPIN, ID_SPINFAST, ID_STOP, ID_TIMEOUT, ID_CHORE = \
        range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+6)

    # Constructor
    def __init__(self,app):
        # Must invoke base class constructor explicitly
        FXMainWindow.__init__(self,app,"OpenGL Test Application",w=800,h=600)

        # Message map
        FXMAPFUNC(self,SEL_PAINT,GLTestWindow.ID_CANVAS,GLTestWindow.onExpose)
        FXMAPFUNC(self,SEL_CONFIGURE,GLTestWindow.ID_CANVAS,GLTestWindow.onConfigure)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_SPIN,GLTestWindow.onCmdSpin)
        FXMAPFUNC(self,SEL_UPDATE,GLTestWindow.ID_SPIN,GLTestWindow.onUpdSpin)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_SPINFAST,GLTestWindow.onCmdSpinFast)
        FXMAPFUNC(self,SEL_UPDATE,GLTestWindow.ID_SPINFAST,GLTestWindow.onUpdSpinFast)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_STOP,GLTestWindow.onCmdStop)
        FXMAPFUNC(self,SEL_UPDATE,GLTestWindow.ID_STOP,GLTestWindow.onUpdStop)
        FXMAPFUNC(self,SEL_TIMEOUT,GLTestWindow.ID_TIMEOUT,GLTestWindow.onTimeout)
        FXMAPFUNC(self,SEL_CHORE,GLTestWindow.ID_CHORE,GLTestWindow.onChore)

        # Top container
        frame = FXHorizontalFrame(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y,0,0,0,0, 0,0,0,0)

        # LEFT pane to contain the glcanvas
        glcanvasFrame = FXVerticalFrame(frame,LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)

        # Label above the glcanvas
        FXLabel(glcanvasFrame,"OpenGL Canvas Frame",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(glcanvasFrame,SEPARATOR_GROOVE|LAYOUT_FILL_X)

        # Drawing glcanvas
        glpanel = FXVerticalFrame(glcanvasFrame,FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0, 0,0,0,0)

        # A visual to draw OpenGL
        self.glvisual = FXGLVisual(self.getApp(),VISUAL_DOUBLEBUFFER)

        # Drawing glcanvas
        self.glcanvas = FXGLCanvas(glpanel,self.glvisual,self,self.ID_CANVAS,LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)

        # RIGHT pane for the buttons
        buttonFrame = FXVerticalFrame(frame,LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)

        # Label above the buttons
        FXLabel(buttonFrame,"Button Frame",None,JUSTIFY_CENTER_X|LAYOUT_FILL_X)

        # Horizontal divider line
        FXHorizontalSeparator(buttonFrame,SEPARATOR_RIDGE|LAYOUT_FILL_X)

        # Start boxes spinning
        FXButton(buttonFrame,"Spin &Timer\tSpin using interval timers\nNote the app blocks until the interal has elapsed...",None,self,self.ID_SPIN,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"Spin &Chore\tSpin as fast as possible using chores\nNote even though the app is very responsive, it never blocks;\nthere is always something to do...",None,self,self.ID_SPINFAST,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5);

        # Stop the insanity
        FXButton(buttonFrame,"&Stop Spin\tStop this mad spinning, I'm getting dizzy",None,self,self.ID_STOP,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)

        # Exit button
        FXButton(buttonFrame,"Exit",None,self.getApp(),FXApp.ID_QUIT,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)

        # Initialize private variables
        self.spinning=0
        self.timer = None
        self.chore = None
        self.angle = 0.0

    # Create and initialize
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    # Widget was resized
    def onConfigure(self,sender,sel,ptr):
        if self.glcanvas.makeCurrent():
            glViewport(0,0,self.glcanvas.getWidth(),self.glcanvas.getHeight())
            self.glcanvas.makeNonCurrent()

    # Expose
    def onExpose(self,sender,sel,ptr):
        self.drawScene()

    # Rotate the boxes whenever timer fires
    def onTimeout(self,sender,sel,ptr):
        self.angle = self.angle + 2
        if self.angle > 360: self.angle = self.angle - 360
        self.drawScene()
        self.timer = self.getApp().addTimeout(100,self,self.ID_TIMEOUT)

    # Rotate the boxes when a chore message is received
    def onChore(self,sender,sel,ptr):
        self.angle = self.angle + 2
        if self.angle > 360: self.angle = self.angle - 360
        self.drawScene()
        self.chore = self.getApp().addChore(self,self.ID_CHORE)

    # Start the boxes spinning
    def onCmdSpin(self,sender,sel,ptr):
        self.spinning = 1
        self.timer = self.getApp().addTimeout(100,self,self.ID_TIMEOUT)

    # Enable or disable the spin button
    def onUpdSpin(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)

    # Start the boxes spinning
    def onCmdSpinFast(self,sender,sel,ptr):
        self.spinning = 1
        self.chore = self.getApp().addChore(self,self.ID_CHORE)

    # Enable or disable the spin button
    def onUpdSpinFast(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)

    # If boxes are spinning, stop them
    def onCmdStop(self,sender,sel,ptr):
        self.spinning = 0
        if self.timer:
            self.getApp().removeTimeout(self.timer)
            self.timer = None
        if self.chore:
            self.getApp().removeChore(self.chore)
            self.chore = None

    # Enable or disable the stop button
    def onUpdStop(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)

    # Draws a simple box using the given corners
    def drawBox(self, xmin, ymin, zmin, xmax, ymax, zmax):
        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(0.,0.,-1.)
        glVertex3f(xmin, ymin, zmin)
        glVertex3f(xmin, ymax, zmin)
        glVertex3f(xmax, ymin, zmin)
        glVertex3f(xmax, ymax, zmin)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(1.,0.,0.)
        glVertex3f(xmax, ymin, zmin)
        glVertex3f(xmax, ymax, zmin)
        glVertex3f(xmax, ymin, zmax)
        glVertex3f(xmax, ymax, zmax)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(0.,0.,1.)
        glVertex3f(xmax, ymin, zmax)
        glVertex3f(xmax, ymax, zmax)
        glVertex3f(xmin, ymin, zmax)
        glVertex3f(xmin, ymax, zmax)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(-1.,0.,0.)
        glVertex3f(xmin, ymin, zmax)
        glVertex3f(xmin, ymax, zmax)
        glVertex3f(xmin, ymin, zmin)
        glVertex3f(xmin, ymax, zmin)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(0.,1.,0.)
        glVertex3f(xmin, ymax, zmin)
        glVertex3f(xmin, ymax, zmax)
        glVertex3f(xmax, ymax, zmin)
        glVertex3f(xmax, ymax, zmax)
        glEnd()

        glBegin(GL_TRIANGLE_STRIP)
        glNormal3f(0.,-1.,0.)
        glVertex3f(xmax, ymin, zmax)
        glVertex3f(xmax, ymin, zmin)
        glVertex3f(xmin, ymin, zmax)
        glVertex3f(xmin, ymin, zmin)
        glEnd()

    # Draw the scene
    def drawScene(self):
        lightPosition = [15.,10.,5.,1.]
        lightAmbient = [.1,.1,.1,1.]
        lightDiffuse = [.9,.9,.9,1.]
        redMaterial = [1.,0.,0.,1.]
        blueMaterial = [0.,0.,1.,1.]

        glcanvas = self.glcanvas
        angle = self.angle

        width = glcanvas.getWidth()
        height = glcanvas.getHeight()
        aspect = width / height

        # Make context current
        glcanvas.makeCurrent()

        glViewport(0,0,glcanvas.getWidth(),glcanvas.getHeight())

        glClearColor(1.0,1.0,1.0,1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
        glEnable(GL_DEPTH_TEST)

        glDisable(GL_DITHER)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30.,aspect, 1., 100.)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(5.,10.,15.,0.,0.,0.,0.,1.,0.)

        glShadeModel(GL_SMOOTH)
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
        glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbient)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightDiffuse)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)

        glMaterialfv(GL_FRONT, GL_AMBIENT, blueMaterial)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, blueMaterial)

        glPushMatrix()
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-1, -1, -1, 1, 1, 1)
        glMaterialfv(GL_FRONT, GL_AMBIENT, redMaterial)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, redMaterial)

        glPushMatrix()
        glTranslated(0.,1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()

        glPushMatrix()
        glTranslated(0.,-1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()

        glPushMatrix()
        glRotated(90., 1., 0., 0.)
        glTranslated(0.,1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()
        glPushMatrix()
        glRotated(90., -1., 0., 0.)
        glTranslated(0.,1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()

        glPushMatrix()
        glRotated(90., 0., 0., 1.)
        glTranslated(0.,1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()

        glPushMatrix()
        glRotated(90., 0., 0., -1.)
        glTranslated(0.,1.75,0.)
        glRotated(angle, 0., 1., 0.)
        self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        glPopMatrix()

        glPopMatrix()

        # Swap if it is double-buffered
        if self.glvisual.isDoubleBuffer(): glcanvas.swapBuffers()

        # Make context non-current
        self.glcanvas.makeNonCurrent()

def runme():
    import sys
    app = FXApp("GLTest", "Test")
    app.init(sys.argv)
    GLTestWindow(app)
    app.create()
    app.run()

# Main program starts here
if __name__ == '__main__':
    runme()
