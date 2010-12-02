#!/usr/local/bin/python
#
# This is an enhancement of the standard OpenGL test program for FXPy,
# contributed by John Przybylski (johnp9@bellatlantic.net).
#

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
    ID_CANVAS, ID_SPIN, ID_SPINFAST, ID_STOP, ID_TIMEOUT, ID_CHORE, ID_NUM_UP, ID_NUM_DOWN, ID_INCR_UP, ID_INCR_DOWN, ID_VIEW_UP, ID_VIEW_DOWN, ID_ZOOM_IN, ID_ZOOM_OUT = \
        range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+14)

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
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_NUM_UP,GLTestWindow.onNumUp)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_NUM_DOWN,GLTestWindow.onNumDown)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_INCR_UP,GLTestWindow.onIncrUp)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_INCR_DOWN,GLTestWindow.onIncrDown)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_VIEW_UP,GLTestWindow.onViewUp)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_VIEW_DOWN,GLTestWindow.onViewDown)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_ZOOM_IN,GLTestWindow.onZoomIn)
        FXMAPFUNC(self,SEL_COMMAND,GLTestWindow.ID_ZOOM_OUT,GLTestWindow.onZoomOut)

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
        FXButton(buttonFrame,"Add\tCreate boxes",None,self,self.ID_NUM_UP,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"Del\tRemove boxes",None,self,self.ID_NUM_DOWN,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"+ Spin\tSpeed up box rotation",None,self,self.ID_INCR_UP,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"- Spin\tSlow down box rotation",None,self,self.ID_INCR_DOWN,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"View &Up\tup",None,self,self.ID_VIEW_UP,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"View &Down\tdown",None,self,self.ID_VIEW_DOWN,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"Zoom In\tZoom In",None,self,self.ID_ZOOM_IN,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
        FXButton(buttonFrame,"Zoom Out\tZoom Out",None,self,self.ID_ZOOM_OUT,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,5,5)
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
        self.NUM = 3.0
        self.INCR = 1.0
	self.VIEW = 1.0
        self.dist = 60.0

    # Create and initialize
    def create(self):
        FXMainWindow.create(self)
        self.show()

    # Widget was resized
    def onConfigure(self,sender,sel,ptr):
        if self.glcanvas.makeCurrent():
            glViewport(0,0,self.glcanvas.getWidth(),self.glcanvas.getHeight())
            self.glcanvas.makeNonCurrent()
        return 1

    # Expose
    def onExpose(self,sender,sel,ptr):
        self.drawScene()
        return 1

    # Rotate the boxes whenever timer fires
    def onTimeout(self,sender,sel,ptr):
        self.angle = self.angle + self.INCR
        if self.angle > 360: self.angle = self.angle - 360
        self.drawScene()
        self.timer = self.getApp().addTimeout(50,self,self.ID_TIMEOUT)
        return 1

    # Rotate the boxes when a chore message is received
    def onChore(self,sender,sel,ptr):
        self.angle = self.angle + self.INCR
        if self.angle > 360: self.angle = self.angle - 360
        self.drawScene()
        self.chore = self.getApp().addChore(self,self.ID_CHORE)
        return 1

    # add number of boxes
    def onNumUp(self,sender,sel,ptr):
        self.NUM = self.NUM + 1
        self.drawScene()
        return 1

    # del number of boxes
    def onNumDown(self,sender,sel,ptr):
        self.NUM = self.NUM - 1
        self.drawScene()
        return 1

    # add number of boxes
    def onIncrUp(self,sender,sel,ptr):
        self.INCR = self.INCR + 1
        self.drawScene()
        return 1

    # del number of boxes
    def onIncrDown(self,sender,sel,ptr):
        self.INCR = self.INCR - 1
        self.drawScene()
        return 1

    # add number of boxes
    def onViewUp(self,sender,sel,ptr):
        self.VIEW = self.VIEW + 1
        self.drawScene()
        return 1

    # del number of boxes
    def onViewDown(self,sender,sel,ptr):
        self.VIEW = self.VIEW - 1
        self.drawScene()
        return 1

    # add number of boxes
    def onZoomIn(self,sender,sel,ptr):
        self.dist = self.dist-10
        self.drawScene()
        return 1

    # del number of boxes
    def onZoomOut(self,sender,sel,ptr):
        self.dist = self.dist+10
        self.drawScene()
        return 1


    # Start the boxes spinning
    def onCmdSpin(self,sender,sel,ptr):
        self.spinning = 1
        self.timer = self.getApp().addTimeout(100,self,self.ID_TIMEOUT)
        return 1

    # Enable or disable the spin button
    def onUpdSpin(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)
        return 1

    # Start the boxes spinning
    def onCmdSpinFast(self,sender,sel,ptr):
        self.spinning = 1
        self.chore = self.getApp().addChore(self,self.ID_CHORE)
        return 1

    # Enable or disable the spin button
    def onUpdSpinFast(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)
        return 1

    # If boxes are spinning, stop them
    def onCmdStop(self,sender,sel,ptr):
        self.spinning = 0
        if self.timer:
            self.getApp().removeTimeout(self.timer)
            self.timer = None
        if self.chore:
            self.getApp().removeChore(self.chore)
            self.chore = None
        return 1

    # Enable or disable the stop button
    def onUpdStop(self,sender,sel,ptr):
        if self.spinning:
            sender.handle(self,MKUINT(FXWindow.ID_ENABLE,SEL_COMMAND),ptr)
        else:
            sender.handle(self,MKUINT(FXWindow.ID_DISABLE,SEL_COMMAND),ptr)
        return 1

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
        greenMaterial = [0.,1.,0.,1.]
        blackMaterial = [0.,0.,0.,1.]
        whiteMaterial = [1.,1.,1.,0.]
        magentaMaterial = [1.,0.,1.,1.]

        glcanvas = self.glcanvas
        angle = self.angle
	num = self.NUM
	view = self.VIEW

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
        #gluPerspective(60., aspect, 1., 100.) # dist, angle of view, ?, clipping distance
        #gluPerspective(60., aspect, 1., 200.) # view dist, aspect ration, front clipping, clipping distance
        gluPerspective(self.dist, aspect, 1., 200.) # view dist, aspect ration, front clipping, clipping distance

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #gluLookAt(5.,10.,15.,0.,0.,0.,0.,1.,0.) # Viewer angle?
        gluLookAt(5.,view,15,0.,0.,0.,0.,1.,0.) # Viewer side-to-side, viewer hight, view front-to-back

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
        self.drawBox(-.5, -.5, -.5, .5, .5, .5)
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

        glMaterialfv(GL_FRONT, GL_AMBIENT, greenMaterial)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, greenMaterial)

	a = 1.5
        for i in range(num):
        	glPushMatrix()
        	glRotated(90., 1., 0., 0.)	# puts it on one of the sides of the blue cube
        	glTranslated(0.,a,0.) 		# a distance way from the cube
        	#glRotated(angle, 0., 1., 0.) 	# rotates around the side axis
        	glRotated(0, 0., 1., 0.) 	# stopped rotation around the side axis
        	self.drawBox(-.5,-.5,-.5,.5,.5,.5)
        	glPopMatrix()
		a=a+1.5

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
