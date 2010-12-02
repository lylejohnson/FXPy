#! /usr/bin/env python

from FXPy.fox import *
import os

try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except:
    print "Sorry, couldn't import the PyOpenGL module."
    raise SystemExit


# Subclass of tab book
class TabBook(FXTabBook):
    def __init__(self, frame, parent):
        FXTabBook.__init__(self, frame)
        self.makeAnglesTab(parent)
        self.makeColorsTab(parent)
        self.makeSwitchesTab(parent)

    def makeAnglesTab(self, parent):
        FXTabItem(self, "Angles\tCamera Angles\tSwitch to camera angles panel.")
        angles = FXMatrix(self, 2, FRAME_THICK|FRAME_RAISED|MATRIX_BY_COLUMNS|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)

        FXLabel(angles,"X:")
        x_dial = FXDial(angles,parent.mdiclient,FXGLViewer.ID_DIAL_X,FRAME_SUNKEN|FRAME_THICK|DIAL_CYCLIC|DIAL_HORIZONTAL|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|LAYOUT_CENTER_Y,0,0,150,14,0,0,0,0)
        x_dial.setTipText("Rotate about X")

        FXLabel(angles,"Y:")
        y_dial = FXDial(angles,parent.mdiclient,FXGLViewer.ID_DIAL_Y,FRAME_SUNKEN|FRAME_THICK|DIAL_CYCLIC|DIAL_HORIZONTAL|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|LAYOUT_CENTER_Y,0,0,150,14,0,0,0,0)
        y_dial.setTipText("Rotate about Y")

        FXLabel(angles,"Z:")
        z_dial = FXDial(angles,parent.mdiclient,FXGLViewer.ID_DIAL_Z,FRAME_SUNKEN|FRAME_THICK|DIAL_CYCLIC|DIAL_HORIZONTAL|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT|LAYOUT_CENTER_Y,0,0,150,14,0,0,0,0)
        z_dial.setTipText("Rotate about Z")

        FXLabel(angles,"FOV:")
        fov = FXTextField(angles,10,parent.mdiclient,FXGLViewer.ID_FOV,JUSTIFY_RIGHT|FRAME_SUNKEN|FRAME_THICK)
        fov.setTipText("Field of view")

        FXLabel(angles,"Zoom:")
        zz = FXTextField(angles,10,parent.mdiclient,FXGLViewer.ID_ZOOM,JUSTIFY_RIGHT|FRAME_SUNKEN|FRAME_THICK)
        zz.setTipText("Zooming")

    def makeColorsTab(self, parent):
        FXTabItem(self, "Colors\tColors\tSwitch to color panel.")
        colors = FXMatrix(self,2,MATRIX_BY_COLUMNS|FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_Y|LAYOUT_CENTER_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)
        FXLabel(colors,"Background:",None,LAYOUT_RIGHT|LAYOUT_CENTER_Y|JUSTIFY_RIGHT)
        FXColorWell(colors,0,parent.mdiclient,FXGLViewer.ID_BACK_COLOR,LAYOUT_TOP|LAYOUT_LEFT, 0,0,0,0 ,0,0,0,0)
        FXLabel(colors,"Ambient:",None,LAYOUT_RIGHT|LAYOUT_CENTER_Y|JUSTIFY_RIGHT)
        FXColorWell(colors,0,parent.mdiclient,FXGLViewer.ID_AMBIENT_COLOR,LAYOUT_TOP|LAYOUT_LEFT, 0,0,0,0 ,0,0,0,0)


        FXLabel(colors,"Light Amb:",None,LAYOUT_RIGHT|LAYOUT_CENTER_Y|JUSTIFY_RIGHT)
        FXColorWell(colors,0,parent.mdiclient,FXGLViewer.ID_LIGHT_AMBIENT,LAYOUT_TOP|LAYOUT_LEFT, 0,0,0,0 ,0,0,0,0)
        FXLabel(colors,"Light Diff:",None,LAYOUT_RIGHT|LAYOUT_CENTER_Y|JUSTIFY_RIGHT)
        FXColorWell(colors,0,parent.mdiclient,FXGLViewer.ID_LIGHT_DIFFUSE,LAYOUT_TOP|LAYOUT_LEFT, 0,0,0,0 ,0,0,0,0)
        FXLabel(colors,"Light Spec:",None,LAYOUT_RIGHT|LAYOUT_CENTER_Y|JUSTIFY_RIGHT)
        FXColorWell(colors,0,parent.mdiclient,FXGLViewer.ID_LIGHT_SPECULAR,LAYOUT_TOP|LAYOUT_LEFT, 0,0,0,0 ,0,0,0,0)

    def makeSwitchesTab(self, parent):
        # Switches
        FXTabItem(self,"Settings\tSettings\tSwitch to settings panel.")
        settings = FXVerticalFrame(self,FRAME_THICK|FRAME_RAISED|LAYOUT_FILL_Y|LAYOUT_CENTER_X|LAYOUT_TOP|LAYOUT_LEFT,0,0,0,0,10,10,10,10)
        FXCheckButton(settings,"Lighting",parent.mdiclient,FXGLViewer.ID_LIGHTING,ICON_BEFORE_TEXT)
        FXCheckButton(settings,"Fog",parent.mdiclient,FXGLViewer.ID_FOG,ICON_BEFORE_TEXT)
        FXCheckButton(settings,"Dither",parent.mdiclient,FXGLViewer.ID_DITHER,ICON_BEFORE_TEXT)
        FXCheckButton(settings,"Lock",parent.mdiclient,FXGLViewer.ID_LOCK,ICON_BEFORE_TEXT)
        FXCheckButton(settings,"Turbo",parent.mdiclient,FXGLViewer.ID_TURBO,ICON_BEFORE_TEXT)

# Test for OpenGL
class GLViewWindow(FXMainWindow):
    (ID_ABOUT, ID_OPEN, ID_NEWVIEWER, ID_QUERY_MODE, ID_GLVIEWER) = \
        range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+5)

    def iconResource(self, filename, transp=0, opts=0):
        return FXPNGIcon(self.getApp(), open(filename, 'rb').read(),
            transp, opts)

    # Constructor
    def __init__(self,app):
        # Must invoke base class constructor explicitly
        FXMainWindow.__init__(self,app,"OpenGL Test Application",w=800,h=600)

        # Message map
        FXMAPFUNC(self, SEL_COMMAND, GLViewWindow.ID_ABOUT,      GLViewWindow.onCmdAbout)
        FXMAPFUNC(self, SEL_COMMAND, GLViewWindow.ID_OPEN,       GLViewWindow.onCmdOpen)
        FXMAPFUNC(self, SEL_COMMAND, GLViewWindow.ID_NEWVIEWER,  GLViewWindow.onCmdNewViewer)
        FXMAPFUNC(self, SEL_UPDATE,  GLViewWindow.ID_QUERY_MODE, GLViewWindow.onUpdMode)
        FXMAPFUNC(self, SEL_COMMAND, FXWindow.ID_QUERY_MENU,     GLViewWindow.onQueryMenu)

        peng = self.iconResource(os.path.join('icons', 'penguin.png'))
        self.setIcon(peng)

        self.getAccelTable().addAccel(fxparseaccel("Ctl-Q"),self.getApp(),MKUINT(FXApp.ID_QUIT,SEL_COMMAND))
        colordlg = FXColorDialog(self,"Color Dialog")

        # Menubar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Tool bar
        FXHorizontalSeparator(self,LAYOUT_SIDE_TOP|SEPARATOR_GROOVE|LAYOUT_FILL_X)
        toolbar = FXHorizontalFrame(self,LAYOUT_SIDE_TOP|LAYOUT_FILL_X,0,0,0,0, 4,4,0,0, 0,0)

        # Make status bar
        statusbar = FXStatusbar(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # Senor Tux
        FXButton(statusbar, "\tHello, I'm Tux...\nThe symbol for the Linux Operating System.\nAnd all it stands for.",
            self.iconResource(os.path.join('icons', 'penguin.png')), opts = LAYOUT_RIGHT)

        # Contents
        frame = FXHorizontalFrame(self,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 0,0,0,0, 0,0)

        # Nice sunken box around the GL viewer
        box = FXVerticalFrame(frame,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y,
            0,0,0,0, 0,0,0,0)

        # MDI client area
        self.mdiclient = FXMDIClient(box, LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # MDI buttons in menu
        FXMDIWindowButton(menubar, self.mdiclient, FXMDIClient.ID_MDI_MENUWINDOW, LAYOUT_LEFT)
        FXMDIDeleteButton(menubar, self.mdiclient, FXMDIClient.ID_MDI_MENUCLOSE, FRAME_RAISED|LAYOUT_RIGHT)
        FXMDIRestoreButton(menubar, self.mdiclient, FXMDIClient.ID_MDI_MENURESTORE, FRAME_RAISED|LAYOUT_RIGHT)
        FXMDIMinimizeButton(menubar, self.mdiclient, FXMDIClient.ID_MDI_MENUMINIMIZE, FRAME_RAISED|LAYOUT_RIGHT)

        # Icon for MDI child windows
        self.mdiicon = self.iconResource(os.path.join('icons', 'winapp.png'))

        # Make MDI window menu
        self.mdimenu = FXMDIMenu(self, self.mdiclient)

        # Make an MDI child window
        mdichild = FXMDIChild(self.mdiclient, "FOX GL Viewer", self.mdiicon, self.mdimenu, MDI_NORMAL, 30, 30, 300, 200)

        # Visual
        self.glvisual = FXGLVisual(self.getApp(), VISUAL_DOUBLEBUFFER)

        # Viewer
        viewer = FXGLViewer(mdichild, self.glvisual, self, self.ID_GLVIEWER,
            LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_LEFT)

        # Tab book with several panels
        panels = TabBook(frame, self)

        # Icons we'll soon need
        newdoc = self.iconResource(os.path.join('icons', 'filenew.png'))
        opendoc = self.iconResource(os.path.join('icons', 'fileopen.png'))
        savedoc = self.iconResource(os.path.join('icons', 'filesave.png'))
        saveasdoc = self.iconResource(os.path.join('icons', 'filesaveas.png'),0,IMAGE_ALPHAGUESS)

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuTitle(menubar,"&File",None,filemenu)
        FXMenuCommand(filemenu,"&New...\tCtl-N\tCreate new document.",newdoc)
        FXMenuCommand(filemenu,"&Open...\tCtl-O\tOpen document file.",opendoc,self,self.ID_OPEN)
        FXMenuCommand(filemenu,"&Save\tCtl-S\tSave document.",savedoc)
        FXMenuCommand(filemenu,"Save &As...\t\tSave document to another file.",saveasdoc)
        FXMenuCommand(filemenu,"&Print...\t\tPrint document.")
        FXMenuCommand(filemenu,"&Dump...\t\tDump widgets.",None,self.getApp(),FXApp.ID_DUMP)
        FXMenuCommand(filemenu,"&Quit\tCtl-Q\tQuit the application.",None,self.getApp(),FXApp.ID_QUIT)

        # Edit Menu
        editmenu = FXMenuPane(self)
        FXMenuTitle(menubar,"&Edit",None,editmenu)
        FXMenuCommand(editmenu,"Undo")
        FXMenuCommand(editmenu,"Copy",None,self.mdiclient,FXGLViewer.ID_COPY_SEL,MENU_AUTOGRAY)
        FXMenuCommand(editmenu,"Cut",None,self.mdiclient,FXGLViewer.ID_CUT_SEL,MENU_AUTOGRAY)
        FXMenuCommand(editmenu,"Paste",None,self.mdiclient,FXGLViewer.ID_PASTE_SEL,MENU_AUTOGRAY)
        FXMenuCommand(editmenu,"Delete",None,self.mdiclient,FXGLViewer.ID_DELETE_SEL,MENU_AUTOGRAY)

        # File manipulation
        FXButton(toolbar,"\tNew\tCreate new document.",newdoc,None,0,FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar,"\tOpen\tOpen document file.",opendoc,self,self.ID_OPEN,FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar,"\tSave\tSave document.",savedoc,None,0,FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar,"\tSave As\tSave document to another file.",saveasdoc,self,self.ID_OPEN,FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tNew Folder\tNo comment",
            self.iconResource(os.path.join('icons', 'newfolder.png')),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Print
        FXFrame(toolbar,LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,4,20)
        FXButton(toolbar, "\tPrint\tPrint document.",
            self.iconResource(os.path.join('icons', 'printicon.png')),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Editing
        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,4,20)
        FXButton(toolbar, "\tCut",
            self.iconResource(os.path.join('icons', 'cut.png')),
            self.mdiclient, FXGLViewer.ID_CUT_SEL,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tCopy",
            self.iconResource(os.path.join('icons', 'copy.png')),
            self.mdiclient, FXGLViewer.ID_COPY_SEL,
            opts=BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tPaste",
            self.iconResource(os.path.join('icons', 'paste.png')),
            self.mdiclient, FXGLViewer.ID_PASTE_SEL,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Projections
        FXFrame(toolbar,LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,8,20)
        FXButton(toolbar, "\tPerspective\tSwitch to perspective projection.",
            self.iconResource(os.path.join('icons', 'perspective.png')),
            self.mdiclient, FXGLViewer.ID_PERSPECTIVE,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tParallel\tSwitch to parallel projection.",
            self.iconResource(os.path.join('icons', 'parallel.png')),
            self.mdiclient, FXGLViewer.ID_PARALLEL,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Shading model
        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,8,20)
        FXButton(toolbar, "\tNo shading\tTurn light sources off.",
            self.iconResource(os.path.join('icons', 'nolight.png')),
            self.mdiclient, FXGLCube.ID_SHADEOFF,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tFlat shading\tTurn on faceted (flat) shading.",
            self.iconResource(os.path.join('icons', 'light.png')),
            self.mdiclient, FXGLCube.ID_SHADEON,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tSmooth shading\tTurn on smooth shading.",
            self.iconResource(os.path.join('icons', 'smoothlight.png')),
            self.mdiclient, FXGLCube.ID_SHADESMOOTH,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,8,20)
        FXToggleButton(toolbar, "\tToggle Light\tToggle light source.", None,
            self.iconResource(os.path.join('icons', 'nolight.png')),
            self.iconResource(os.path.join('icons', 'light.png')),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # View orientation
        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,8,20)
        FXButton(toolbar, "\tFront View\tView objects from the front.",
            self.iconResource(os.path.join('icons', 'frontview.png')),
            self.mdiclient, FXGLViewer.ID_FRONT,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tBack View\tView objects from behind.",
            self.iconResource(os.path.join('icons', 'backview.png')),
            self.mdiclient, FXGLViewer.ID_BACK,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tLeft View\tView objects from the left.",
            self.iconResource(os.path.join('icons', 'leftview.png')),
            self.mdiclient, FXGLViewer.ID_LEFT,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tRight View\tView objects from the right.",
            self.iconResource(os.path.join('icons', 'rightview.png')),
            self.mdiclient, FXGLViewer.ID_RIGHT,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tTop View\tView objects from the top.",
            self.iconResource(os.path.join('icons', 'topview.png'), 0, IMAGE_OPAQUE),
            self.mdiclient, FXGLViewer.ID_TOP,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tBottom View\tView objects from below.",
            self.iconResource(os.path.join('icons', 'bottomview.png'), 0, IMAGE_OPAQUE),
            self.mdiclient, FXGLViewer.ID_BOTTOM,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Miscellaneous buttons
        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,8,20)
        FXButton(toolbar, None,
            self.iconResource(os.path.join('icons', 'zoom.png')),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, "\tColors\tDisplay color dialog.",
            self.iconResource(os.path.join('icons', 'colorpal.png')),
            colordlg, FXWindow.ID_SHOW,
            FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, None,
            self.iconResource(os.path.join('icons', 'camera.png'), 0, IMAGE_OPAQUE),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)
        FXButton(toolbar, None,
            self.iconResource(os.path.join('icons', 'foxicon.png')),
            opts = FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # Dangerous delete a bit on the side
        FXFrame(toolbar,
            LAYOUT_TOP|LAYOUT_LEFT|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,0,0,10,20)
        FXButton(toolbar, "\tDelete\tDelete the selected object.",
            self.iconResource(os.path.join('icons', 'kill.png')),
            self.mdiclient, FXGLViewer.ID_DELETE_SEL,
            BUTTON_AUTOGRAY|FRAME_THICK|FRAME_RAISED|LAYOUT_TOP|LAYOUT_LEFT)

        # View menu
        viewmenu = FXMenuPane(self)
        FXMenuTitle(menubar,"&View",None,viewmenu)
        FXMenuCommand(viewmenu, "Parallel\t\tSwitch to parallel projection.",
            None, self.mdiclient, FXGLViewer.ID_PARALLEL, MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,
            "Perspective\t\tSwitch to perspective projection.", None,
            self.mdiclient,FXGLViewer.ID_PERSPECTIVE,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu, "&Front\t\tFront view.", None,
            self.mdiclient, FXGLViewer.ID_FRONT, MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"&Back\t\tBack view.",None,self.mdiclient,FXGLViewer.ID_BACK,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"&Left\t\tLeft view.",None,self.mdiclient,FXGLViewer.ID_LEFT,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"&Right\t\tRight view.",None,self.mdiclient,FXGLViewer.ID_RIGHT,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"&Top\t\tTop view.",None,self.mdiclient,FXGLViewer.ID_TOP,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"&Bottom\t\tBottom view.",None,self.mdiclient,FXGLViewer.ID_BOTTOM,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"F&it\t\tFit to view.",None,self.mdiclient,FXGLViewer.ID_FITVIEW,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"R&eset\t\tReset all viewing parameters",None,self.mdiclient,FXGLViewer.ID_RESETVIEW,MENU_AUTOGRAY)
        FXMenuCommand(viewmenu, "Zoom...\t\tZoom in on area", None,
            self.mdiclient, FXGLViewer.ID_LASSO_ZOOM, MENU_AUTOGRAY)
        FXMenuCommand(viewmenu, "Select...\t\tZoom in on area", None,
            self.mdiclient, FXGLViewer.ID_LASSO_SELECT, MENU_AUTOGRAY)
        FXMenuCommand(viewmenu,"Lock\t\tLock view orientation",None,self.mdiclient,FXGLViewer.ID_LOCK,MENU_AUTOGRAY)

        # Rendering menu
        rendermenu = FXMenuPane(self)
        FXMenuTitle(menubar, "&Rendering", None, rendermenu)
        FXMenuCommand(rendermenu, "Points\t\tRender as points.", None,
            self.mdiclient, FXGLShape.ID_STYLE_POINTS, MENU_AUTOGRAY)
        FXMenuCommand(rendermenu, "Wire Frame\t\tRender as wire frame.", None,
            self.mdiclient, FXGLShape.ID_STYLE_WIREFRAME, MENU_AUTOGRAY)
        FXMenuCommand(rendermenu, "Surface \t\tRender solid surface.", None,
            self.mdiclient, FXGLShape.ID_STYLE_SURFACE, MENU_AUTOGRAY)
        FXMenuCommand(rendermenu,
            "Bounding Box\t\tRender bounding box only.", None,
            self.mdiclient, FXGLShape.ID_STYLE_BOUNDINGBOX, MENU_AUTOGRAY)

        # Window menu
        windowmenu = FXMenuPane(self)
        FXMenuTitle(menubar,"&Windows",None,windowmenu)
        FXMenuCommand(windowmenu,
            "New Viewer\t\tCreate new viewer window.", None,
            self, self.ID_NEWVIEWER)
        FXMenuCommand(windowmenu,
            "Tile Horizontally\t\tTile windows horizontally.", None,
            self.mdiclient, FXWindow.ID_MDI_TILEHORIZONTAL)
        FXMenuCommand(windowmenu,
            "Tile Vertically\t\tTile windows vertically.", None,
            self.mdiclient, FXWindow.ID_MDI_TILEVERTICAL)
        FXMenuCommand(windowmenu,
            "Cascade\t\tCascade windows.", None,
            self.mdiclient, FXWindow.ID_MDI_CASCADE)
        FXMenuCommand(windowmenu, "Toolbar", None,
            toolbar, FXWindow.ID_TOGGLESHOWN)
        FXMenuCommand(windowmenu, "Control panel", None,
            panels, FXWindow.ID_TOGGLESHOWN)
        FXMenuCommand(windowmenu,
            "Delete\t\tDelete current viewer window.", None,
            self.mdiclient, FXMDIClient.ID_MDI_CLOSE)
        sep1 = FXMenuSeparator(windowmenu)
        sep1.setTarget(self.mdiclient)
        sep1.setSelector(FXMDIClient.ID_MDI_ANY)
        for i in range(4):
            FXMenuCommand(windowmenu, None, None,
                self.mdiclient, FXMDIClient.ID_MDI_1 + i)

        # Help menu
        helpmenu = FXMenuPane(self)
        FXMenuTitle(menubar, "&Help", None, helpmenu, LAYOUT_RIGHT)
        FXMenuCommand(helpmenu,
            "&About FOX...\t\tDisplay FOX about panel.", None,
            self, self.ID_ABOUT)

        # Make a tool tip
        FXTooltip(self.getApp(), 0)

        # Status bar shows the mode
        statusbar.getStatusline().setTarget(self)
        statusbar.getStatusline().setSelector(self.ID_QUERY_MODE)

        # Make a scene!
        self.scene = self.makeScene()

        # Add scene to GL viewer
        viewer.setScene(self.scene)

    # Construct a scene object
    def makeScene(self):
        scene = FXGLGroup()
        scene.append(FXGLPoint(2,0,0))
        scene.append(FXGLPoint(0,2,0))
        scene.append(FXGLPoint(2,2,0))
        scene.append(FXGLPoint(0,0,0))
        scene.append(FXGLLine(0,0,0, 1,0,0))
        scene.append(FXGLLine(0,0,0, 0,1,0))
        scene.append(FXGLLine(0,0,0, 0,0,1))
        scene.append(FXGLLine(0,0,0, 1,1,1))
        gp2 = FXGLGroup()
        scene.append(gp2)
        gp2.append(FXGLCube(-1.0, 0.0, 0.0, 0.5, 0.5, 0.5))
        gp2.append(FXGLCube( 1.0, 0.0, 0.0, 0.5, 0.5, 0.5))
        gp2.append(FXGLCube( 0.0,-1.0, 0.0, 0.5, 0.5, 0.5))
        gp2.append(FXGLCube( 0.0, 1.0, 0.0, 0.5, 0.5, 1.5))
        gp2.append(FXGLCone( 1.0,-1.5, 0.0, 1.0, 0.5))
        gp2.append(FXGLCylinder(-1.0, 0.5, 0.0, 1.0, 0.5))
        gp2.append(FXGLSphere(1.0, 1.0, 0.0, 0.5))
        return scene

    # Create and initialize
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    # About
    def onCmdAbout(self,sender,sel,ptr):
        showModalInformationBox(self,MBOX_OK,"About FOX","FOX OpenGL Example.\nCopyright (C) 1998 Jeroen van der Zijp")

    # Open
    def onCmdOpen(self,sender,sel,ptr):
        patterns = "All Files (*)\n" + \
                   "C++ Source Files (*.[Cc][Pp][Pp])\n" + \
                   "C++ Header Files (*.[Hh])\n" + \
                   "Object Files (*.o)\n" + \
                   "HTML Header Files (*.[Hh][Tt][Mm][Ll])"
        open = FXFileDialog(self, "Open some file")
        open.setPatternList(patterns)
        if open.execute():
            pass

    # Make new viewer
    def onCmdNewViewer(self,sender,sel,ptr):
        # Make a new child window
        mdichild = FXMDIChild(self.mdiclient, "FOX GL Viewer",
            self.mdiicon, self.mdimenu, MDI_NORMAL, 30, 30, 300, 200)

        # Create a new viewer
        viewer = FXGLViewer(mdichild, self.glvisual, self, self.ID_GLVIEWER)

        # Change of scenery
        viewer.setScene(self.scene)

        # Create the child
        mdichild.create()

    # Update status line text
    def onUpdMode(self, sender, sel, ptr):
        sender.setText("Ready.")

    # When the user right-clicks in the GLViewer background, the viewer
    # first sends a SEL_COMMAND message with identifier FXWindow::ID_QUERY_MENU
    # to the selected GLObject (if any). If that message isn't handled, it
    # tries to send it to the GLViewer's target (which in our case is the main
    # window).
    def onQueryMenu(self, sender, sel, event):
        pane = FXMenuPane(self)
        FXMenuCommand(pane,
            "Parallel\t\tSwitch to parallel projection.", None,
            sender, FXGLViewer.ID_PARALLEL)
        FXMenuCommand(pane,
            "Perspective\t\tSwitch to perspective projection.", None,
            sender, FXGLViewer.ID_PERSPECTIVE)
        FXMenuSeparator(pane)
        FXMenuCommand(pane, "&Front\t\tFront view.", None,
            sender, FXGLViewer.ID_FRONT)
        FXMenuCommand(pane, "&Back\t\tBack view.", None,
            sender, FXGLViewer.ID_BACK)
        FXMenuCommand(pane, "&Left\t\tLeft view.", None,
            sender, FXGLViewer.ID_LEFT)
        FXMenuCommand(pane, "&Right\t\tRight view.", None,
            sender, FXGLViewer.ID_RIGHT)
        FXMenuCommand(pane, "&Top\t\tTop view.", None,
            sender, FXGLViewer.ID_TOP)
        FXMenuCommand(pane, "&Bottom\t\tBottom view.", None,
            sender, FXGLViewer.ID_BOTTOM)
        FXMenuSeparator(pane)
        FXMenuCommand(pane, "F&it\t\tFit to view.", None,
            sender, FXGLViewer.ID_FITVIEW)
        FXMenuCommand(pane, "R&eset\t\tReset all viewing parameters", None,
            sender, FXGLViewer.ID_RESETVIEW)
        FXMenuCommand(pane, "Lock\t\tLock view orientation", None,
            sender, FXGLViewer.ID_LOCK)
        pane.create()
        pane.popup(None, event.root_x, event.root_y)
        self.getApp().runModalWhileShown(pane)

# Main program starts here
if __name__ == '__main__':
    import sys
    app = FXApp("GLViewer", "Test")
    app.init(sys.argv)
    GLViewWindow(app)
    app.create()
    app.run()
