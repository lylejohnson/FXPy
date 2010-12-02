#! /usr/bin/env python

from FXPy.fox import *
import os

class ImageWindow(FXMainWindow):
    (ID_ABOUT,
     ID_OPEN,
     ID_SAVE,
     ID_TITLE,
     ID_QUIT,
     ID_FILELIST,
     ID_RECENTFILE,
     ID_ROTATE_90,
     ID_ROTATE_180,
     ID_ROTATE_270,
     ID_MIRROR_HOR,
     ID_MIRROR_VER,
     ID_SCALE,
     ID_CROP) = range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+14)

    def loadIcon(self, filename):
        filename = os.path.join('icons', filename)
        return FXPNGIcon(self.getApp(), open(filename, 'rb').read())

    def __init__(self, app):
        FXMainWindow.__init__(self, app, 'FOX Image Viewer: - untitled', w=850, h=600)

        # Set up message map
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_ABOUT, ImageWindow.onCmdAbout)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_OPEN, ImageWindow.onCmdOpen)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_SAVE, ImageWindow.onCmdSave)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_TITLE, ImageWindow.onUpdTitle)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_QUIT, ImageWindow.onCmdQuit)
        FXMAPFUNC(self, SEL_SIGNAL,        ImageWindow.ID_QUIT, ImageWindow.onCmdQuit)
        FXMAPFUNC(self, SEL_CLOSE,         ImageWindow.ID_TITLE, ImageWindow.onCmdQuit)
        FXMAPFUNC(self, SEL_DOUBLECLICKED, ImageWindow.ID_FILELIST, ImageWindow.onCmdFileList)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_RECENTFILE, ImageWindow.onCmdRecentFile)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_ROTATE_90, ImageWindow.onCmdRotate)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_ROTATE_180, ImageWindow.onCmdRotate)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_ROTATE_270, ImageWindow.onCmdRotate)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_MIRROR_HOR, ImageWindow.onCmdMirror)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_MIRROR_VER, ImageWindow.onCmdMirror)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_SCALE, ImageWindow.onCmdScale)
        FXMAPFUNC(self, SEL_COMMAND,       ImageWindow.ID_CROP, ImageWindow.onCmdCrop)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_ROTATE_90, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_ROTATE_180, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_ROTATE_270, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_MIRROR_HOR, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_MIRROR_VER, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_SCALE, ImageWindow.onUpdImage)
        FXMAPFUNC(self, SEL_UPDATE,        ImageWindow.ID_CROP, ImageWindow.onUpdImage)

        # Make color dialog
        self.colordlg = FXColorDialog(self, 'Color Dialog')

        # Make menu bar
        dragShell1 = FXToolbarShell(self, 0)
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X|FRAME_RAISED)
        FXToolbarGrip(menubar, menubar, FXMenubar.ID_TOOLBARGRIP,
                      TOOLBARGRIP_DOUBLE)

        # Toolbar
        dragShell2 = FXToolbarShell(self, 0)
        toolbar = FXToolbar(self, dragShell2,
            LAYOUT_SIDE_TOP|PACK_UNIFORM_WIDTH|PACK_UNIFORM_HEIGHT|FRAME_RAISED|LAYOUT_FILL_X)
        FXToolbarGrip(toolbar, toolbar, FXToolbar.ID_TOOLBARGRIP,
                      TOOLBARGRIP_DOUBLE)

        # Status bar
        statusbar = FXStatusbar(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuTitle(menubar, '&File', None, filemenu)

        # Edit menu
        editmenu = FXMenuPane(self)
        FXMenuTitle(menubar, '&Edit', None, editmenu)

        # Manipulation menu
        manipmenu = FXMenuPane(self)
        FXMenuTitle(menubar, '&Manipulation', None, manipmenu)

        # View menu
        viewmenu = FXMenuPane(self)
        FXMenuTitle(menubar, '&View', None, viewmenu)

        # Help menu
        helpmenu = FXMenuPane(self)
        FXMenuTitle(menubar, '&Help', None, helpmenu)

        # Splitter
        splitter = FXSplitter(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y|SPLITTER_TRACKING|SPLITTER_VERTICAL|SPLITTER_REVERSED)

        # Sunken border for the image widget
        imagebox = FXHorizontalFrame(splitter, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0, 0, 0, 0, 0, 0, 0, 0)

        # Make image widget
        self.imageview = FXImageView(imagebox, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Sunken border for the file list
        self.filebox = FXHorizontalFrame(splitter, LAYOUT_FILL_X|LAYOUT_FILL_Y, 0, 0, 0, 0, 0, 0, 0, 0)

        # Make the file list
        fileframe = FXHorizontalFrame(self.filebox, FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.filelist = FXFileList(fileframe, self, self.ID_FILELIST, LAYOUT_FILL_X|LAYOUT_FILL_Y|ICONLIST_MINI_ICONS|ICONLIST_AUTOSIZE)
        FXButton(self.filebox, '\tUp one level\tGo up to higher directory.', self.loadIcon('tbuplevel.png'), self.filelist, FXFileList.ID_DIRECTORY_UP, BUTTON_TOOLBAR|FRAME_RAISED|LAYOUT_FILL_Y)

        # Toolbar buttons: File manipulation
        FXButton(toolbar, '&Open\tOpen Image\tOpen image file',
            self.loadIcon('fileopen.png'), self, self.ID_OPEN,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
        FXButton(toolbar, '&Save\tSave Image\tSave image file',
            self.loadIcon('filesave.png'), self, self.ID_SAVE,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)

        # Toolbar buttons: Editing
        FXButton(toolbar, 'Cut\tCut',
            self.loadIcon('cut.png'), None, 0,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
        FXButton(toolbar, 'Copy\tCopy',
            self.loadIcon('copy.png'), None, 0,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)
        FXButton(toolbar, 'Paste\tPaste',
            self.loadIcon('paste.png'), None, 0,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED)

        # Color
        FXButton(toolbar, '&Colors\tColors\tDisplay color dialog.',
            self.loadIcon('colorpal.png'), self.colordlg, FXWindow.ID_SHOW,
            ICON_ABOVE_TEXT|BUTTON_TOOLBAR|FRAME_RAISED|LAYOUT_RIGHT)

        # File menu entries
        FXMenuCommand(filemenu, '&Open...\tCtl-O\tOpen image file.',
            self.loadIcon('fileopen.png'), self, self.ID_OPEN)
        FXMenuCommand(filemenu, '&Save...\tCtl-S\tSave image file.',
            self.loadIcon('filesave.png'), self, self.ID_SAVE)

        # Edit menu entries
        FXMenuCommand(editmenu, '&Undo\tCtl-Z\tUndo last change.')
        FXMenuCommand(editmenu, '&Redo\tCtl-R\tRedo last undo.')
        FXMenuCommand(editmenu, '&Copy\tCtl-C\tCopy selection to clipboard.',
            self.loadIcon('copy.png'))
        FXMenuCommand(editmenu, 'C&ut\tCtl-X\tCut selection to clipboard.',
            self.loadIcon('cut.png'))
        FXMenuCommand(editmenu, '&Paste\tCtl-V\tPaste from clipboard.',
            self.loadIcon('paste.png'))
        FXMenuCommand(editmenu, '&Delete\t\tDelete selection.',
            self.loadIcon('paste.png'), None, 0)

        # Manipulation menu entries
        FXMenuCommand(manipmenu, 'Rotate 90\t\tRotate image 90 degrees.',
            None, self, self.ID_ROTATE_90)
        FXMenuCommand(manipmenu, 'Rotate 180\t\tRotate image 180 degrees.',
            None, self, self.ID_ROTATE_180)
        FXMenuCommand(manipmenu, 'Rotate -90\t\tRotate image -90 degrees.',
            None, self, self.ID_ROTATE_270)
        FXMenuCommand(manipmenu, 'Mirror Hor.\t\tMirror horizontally.',
            None, self, self.ID_MIRROR_HOR)
        FXMenuCommand(manipmenu, 'Mirror Ver.\t\tMirror vertically.',
            None, self, self.ID_MIRROR_VER)
        FXMenuCommand(manipmenu, 'Scale...\t\tScale image.',
            None, self, self.ID_SCALE)
        FXMenuCommand(manipmenu, 'Crop...\t\tCrop image.',
            None, self, self.ID_CROP)

        # View menu entries
        FXMenuCommand(viewmenu, 'File List\t\tDisplay file list.',
            None, self.filebox, FXWindow.ID_TOGGLESHOWN)
        FXMenuCommand(viewmenu,
            'Show Hidden\t\tShow hidden files and directories.',
            None, self.filelist, FXFileList.ID_TOGGLE_HIDDEN)
        FXMenuCommand(viewmenu,
            'Show small icons\t\tShow directories with small icons',
            None, self.filelist, FXFileList.ID_SHOW_MINI_ICONS)
        FXMenuCommand(viewmenu,
            'Show big icons\t\tDisplay directory with big icons.',
            None, self.filelist, FXFileList.ID_SHOW_BIG_ICONS)
        FXMenuCommand(viewmenu,
            'Show details view\t\tDisplay detailed directory listing.',
            None, self.filelist, FXFileList.ID_SHOW_DETAILS)
        FXMenuCommand(viewmenu, 'Rows of icons\t\tView row-wise.',
            None, self.filelist, FXFileList.ID_ARRANGE_BY_ROWS)
        FXMenuCommand(viewmenu, 'Columns of icons\t\tView column-wise.',
            None, self.filelist, FXFileList.ID_ARRANGE_BY_COLUMNS)
        FXMenuCommand(viewmenu, 'Toolbar\t\tDisplay toolbar.',
            None, toolbar, FXWindow.ID_TOGGLESHOWN)
        FXMenuCommand(viewmenu, 'Status line\t\tDisplay status line.',
            None, statusbar, FXWindow.ID_TOGGLESHOWN)

        # Help menu entries
        FXMenuCommand(helpmenu, '&About FOX...', None, self, self.ID_ABOUT)

        # Make a tool tip
        FXTooltip(self.getApp(), 0)

        # Recent files
        self.mrufiles = FXRecentFiles()
        self.mrufiles.setTarget(self)
        self.mrufiles.setSelector(self.ID_RECENTFILE)

        # Initialize the file name
        self.filename = 'untitled'

    def onCmdAbout(self, sender, sel, ptr):
        about = FXMessageBox(self, 'About Image Viewer',
            'Image Viewer demonstrates the FOX ImageView widget.\n\nUsing the FOX C++ GUI Library (http://www.cfdrc.com/FOX/fox.html)\n\nCopyright (c) 2000 Jeroen van der Zijp (jvz@cfdrc.com)',
            None, MBOX_OK|DECOR_TITLE|DECOR_BORDER)
        about.execute()

    def loadImage(self, file):
        root, ext = os.path.splitext(file)
        img = None
        if ext == '.png':
            img = FXGIFImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.bmp':
            img = FXBMPImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.xpm':
            img = FXXPMImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.png':
            img = FXPNGImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.jpg':
            img = FXJPGImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.pcx':
            img = FXPCXImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.tif':
            img = FXTIFImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.ico':
            img = FXICOImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)
        elif ext == '.tga':
            img = FXTGAImage(self.getApp(), None, IMAGE_KEEP|IMAGE_SHMI|IMAGE_SHMP)

        if not img:
            showModalErrorBox(self, MBOX_OK, 'Error loading image', 'Unsupported type: ' + ext)
            return 0

        stream = FXFileStream()
        if stream.open(file, FXStreamLoad):
            self.getApp().beginWaitCursor()
            img.loadPixels(stream)
            stream.close()
            img.create()
            old = self.imageview.getImage()     # How to ensure this resource gets destroyed?
            self.imageview.setImage(img)
            self.getApp().endWaitCursor()

    def saveImage(self, file):
        stream = FXFileStream()
        if stream.open(file, FXStreamSave):
            self.getApp().beginWaitCursor()
            img = self.imageview.getImage()     # We may want to save in another format...
            img.savePixels(stream)
            stream.close()
            self.getApp().endWaitCursor()

    def onCmdOpen(self, sender, sel, ptr):
        open = FXFileDialog(self, 'Open Image')
        open.setFilename(self.filename)
        patterns = "All Files (*)\n" + \
                   "GIF Images (*.png)\n" + \
                   "BMP Images (*.bmp)\n" + \
                   "XPM Images (*.xpm)\n" + \
                   "PNG Images (*.png)\n" + \
                   "JPG Images (*.jpg)\n" + \
                   "TIF Images (*.tif)\n" + \
                   "TGA Images (*.tga)\n" + \
                   "ICO Images (*.ico)\n" + \
                   "PCX Images (*.pcx)"
        open.setPatternList(patterns)
        if open.execute():
            self.filename = open.getFilename()
            self.filelist.setCurrentFile(self.filename)
            self.mrufiles.appendFile(self.filename)
            self.loadImage(self.filename)

    def onCmdSave(self, sender, sel, ptr):
        saveDialog = FXFileDialog(self, 'Save Image')
        saveDialog.setFilename(self.filename)
        if saveDialog.execute():
            if os.path.exists(saveDialog.getFilename()):
                if MBOX_CLICKED_NO == showModalQuestionBox(self,
                    MBOX_YES_NO, 'Overwrite Image',
                    'Overwrite existing image?'): return 1
            self.filename = saveDialog.getFilename()
            self.filelist.setCurrentFile(self.filename)
            self.mrufiles.appendFile(self.filename)
            self.saveImage(self.filename)

    def onCmdQuit(self, sender, sel, ptr):
        # Write new window size back to the registry
        self.getApp().reg().writeIntEntry('SETTINGS', 'x', self.getX())
        self.getApp().reg().writeIntEntry('SETTINGS', 'y', self.getY())
        self.getApp().reg().writeIntEntry('SETTINGS', 'w', self.getWidth())
        self.getApp().reg().writeIntEntry('SETTINGS', 'h', self.getHeight())

        # Height of file box
        self.getApp().reg().writeIntEntry('SETTINGS', 'fileheight', self.filebox.getHeight())

        # Was the file box shown?
        self.getApp().reg().writeIntEntry('SETTINGS', 'filesshown', self.filebox.shown())

        dir = self.filelist.getDirectory()
        self.getApp().reg().writeStringEntry('SETTINGS', 'directory', dir)

        self.getApp().exit(0)

    def onUpdTitle(self, sender, sel, ptr):
        title = 'FOX Image Viewer:- ' + self.filename
        image = self.imageview.getImage()
        if image:
            title = title + ' (%d x %d)' % (image.getWidth(), image.getHeight())
        sender.setText(title)

    def onCmdRecentFile(self, sender, sel, ptr):
        print 'onCmdRecentFile(): not implemented'

    def onCmdFileList(self, sender, sel, index):
        if index >= 0:
            if self.filelist.isItemDirectory(index):
                self.filelist.setDirectory(self.filelist.getItemPathname(index))
            elif self.filelist.isItemFile(index):
                self.filename = self.filelist.getItemPathname(index)
                self.mrufiles.appendFile(self.filename)
                self.loadImage(self.filename)

    def onCmdRotate(self, sender, sel, ptr):
        image = self.imageview.getImage();
        if SELID(sel) == ImageWindow.ID_ROTATE_90:
            image.rotate(90)
        elif SELID(sel) == ImageWindow.ID_ROTATE_180:
            image.rotate(180)
        elif SELID(sel) == ImageWindow.ID_ROTATE_270:
            image.rotate(270)
        self.imageview.setImage(image)

    def onUpdImage(self, sender, sel, ptr):
        if self.imageview.getImage():
            sender.handle(self, MKUINT(FXWindow.ID_ENABLE, SEL_COMMAND), ptr)
        else:
            sender.handle(self, MKUINT(FXWindow.ID_DISABLE, SEL_COMMAND), ptr)

    def onCmdMirror(self, sender, sel, ptr):
        image = self.imageview.getImage()
        if SELID(sel) == ImageWindow.ID_MIRROR_HOR:
            image.mirror(1, 0)
        elif SELID(sel) == ImageWindow.ID_MIRROR_VER:
            image.mirror(0, 1)
        self.imageview.setImage(image)

    def onCmdScale(self, sender, sel, ptr):
        image = self.imageview.getImage()
        sx = image.getWidth()
        sy = image.getHeight()
        scalepanel = FXDialogBox(self, "Scale Image To Size")
        frame = FXHorizontalFrame(scalepanel,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXLabel(frame, "W:", None, LAYOUT_CENTER_Y)
        sxText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        sxText.setText(str(sx))
        FXLabel(frame, "H:", None, LAYOUT_CENTER_Y)
        syText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        syText.setText(str(sy))
        FXButton(frame, "Cancel", None, scalepanel, FXDialogBox.ID_CANCEL,
            LAYOUT_CENTER_Y|FRAME_RAISED|FRAME_THICK,
            0, 0, 0, 0, 20, 20, 4, 4)
        FXButton(frame, "OK", None, scalepanel, FXDialogBox.ID_ACCEPT,
            LAYOUT_CENTER_Y|FRAME_RAISED|FRAME_THICK,
            0, 0, 0, 0, 30, 30, 4, 4)
        if not scalepanel.execute():
            return 1
        sx, sy = int(sxText.getText()), int(syText.getText())
        if sx < 1 or sy < 1:
            return 1
        image.scale(sx, sy)
        self.imageview.setImage(image)

    def onCmdCrop(self, sender, sel, ptr):
        image = self.imageview.getImage()
        cx = 0
        cy = 0
        cw = image.getWidth()
        ch = image.getHeight()
        croppanel = FXDialogBox(self, "Crop image")
        frame = FXHorizontalFrame(croppanel,
            LAYOUT_SIDE_TOP|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        FXLabel(frame, "X:", None, LAYOUT_CENTER_Y)
        cxText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        FXLabel(frame, "Y:", None, LAYOUT_CENTER_Y)
        cyText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        FXLabel(frame, "W:", None, LAYOUT_CENTER_Y)
        cwText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        FXLabel(frame, "H:", None, LAYOUT_CENTER_Y)
        chText = FXTextField(frame, 5, None, 0,
            LAYOUT_CENTER_Y|FRAME_SUNKEN|FRAME_THICK|JUSTIFY_RIGHT)
        FXButton(frame, "Cancel", None, croppanel, FXDialogBox.ID_CANCEL,
            LAYOUT_CENTER_Y|FRAME_RAISED|FRAME_THICK,
            0, 0, 0, 0, 20, 20, 4, 4)
        FXButton(frame, "OK", None, croppanel, FXDialogBox.ID_ACCEPT,
            LAYOUT_CENTER_Y|FRAME_RAISED|FRAME_THICK,
            0, 0, 0, 0, 30, 30, 4, 4)

        cxText.setText(str(cx))
        cyText.setText(str(cy))
        cwText.setText(str(cw))
        chText.setText(str(ch))

        if not croppanel.execute():
            return 1

        cx, cy = int(cxText.getText()), int(cyText.getText())
        cw, ch = int(cwText.getText()), int(chText.getText())

        if cx < 0 or cy < 0:
            return 1
        if cx+cw > image.getWidth() or cy+ch > image.getHeight():
            return 1
        image.crop(cx, cy, cw, ch)
        self.imageview.setImage(image)

    def create(self):
        xx = self.getApp().reg().readIntEntry('SETTINGS','x',5)
        yy = self.getApp().reg().readIntEntry('SETTINGS','y',5)
        ww = self.getApp().reg().readIntEntry('SETTINGS','w',600)
        hh = self.getApp().reg().readIntEntry('SETTINGS','h',400)

        fh = self.getApp().reg().readIntEntry('SETTINGS','fileheight',100)
        fs = self.getApp().reg().readIntEntry('SETTINGS','filesshown',1)

        dir = self.getApp().reg().readStringEntry('SETTINGS','directory','~')
        self.filelist.setDirectory(dir)

        self.filebox.setHeight(fh)
        if not fs:
            self.filebox.hide()

        self.position(xx,yy,ww,hh)

        FXMainWindow.create(self)
        self.show()

if __name__ == '__main__':
    import sys
    app = FXApp("ImageView", "Test")
    app.init(sys.argv)
    window = ImageWindow(app)
    app.create()
    app.run()
