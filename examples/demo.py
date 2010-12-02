#!/usr/bin/env python

import os, string, sys, thread, xml.sax, gzip, tempfile
try:
    import zipfile
    has_zipfile = 1
except ImportError:
    has_zipfile = 0

from FXPy.fox import *

class DemoList(xml.sax.ContentHandler):
    def __init__(self, filename):
        self._files = {}
        self._descriptions = {}
        self._currentFile = None
        self._currentDescription = None
        xml.sax.parse(filename, self)

    def startElement(self, name, attrs):
        if name == 'demo':
            file = str(attrs['file'])
            title = str(attrs['title'])
            self._files[title] = file
            self._currentFile = file
            self._currentDescription = ''

    def endElement(self, name):
        if name == 'demo':
            self._descriptions[self._currentFile] = self.cleanupDescription(self._currentDescription)
            self._currentFile = None
            self._currentDescription = None

    def cleanupDescription(self, text):
        lines = text.split('\n')
        for lineIndex in range(len(lines)):
            lines[lineIndex] = string.strip(lines[lineIndex])
        lines = filter(lambda x: len(x) > 0, lines)
        return string.join(lines, ' ')

    def characters(self, content):
        if self._currentFile:
            self._currentDescription = self._currentDescription + str(content)

    def getTitles(self):
        """Return a sorted list of the demo case titles"""
        titles = self._files.keys()
        titles.sort()
        return titles

    def getFilename(self, title):
        """Returns the file name associated with this demo case title"""
        return self._files[title]

    def getDescription(self, filename):
        """Returns the description text associated with this file name"""
        return self._descriptions[filename]

def threadFunc(filename, delete):
    os.system(sys.executable + ' ' + filename)
    if delete:
        os.remove(filename)

class DemoBrowser(FXMainWindow):
    # Message identifiers
    (ID_ABOUT,
     ID_LIST
    ) = range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+2)

    def __init__(self, app):
        # Call base class constructor first
        FXMainWindow.__init__(self, app, 'FXPy Demo Browser', w=600, h=400)

        # Set up message map
        FXMAPFUNC(self, SEL_COMMAND, DemoBrowser.ID_ABOUT, DemoBrowser.onCmdAbout)
        FXMAPFUNC(self, SEL_COMMAND, DemoBrowser.ID_LIST,  DemoBrowser.onCmdList)

        # Read information about the available demos
        self.demos = DemoList('demos.xml')

        # Menu bar along the top
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
        self.setupMenubar(menubar)

        # Status bar along the bottom
        statusbar = FXStatusbar(self,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # Split pane fills up the middle
        splitter = FXSplitter(self, LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.setupLeftPane(splitter)
        self.setupRightPane(splitter)

    def loadIcon(self, filename):
        filename = os.path.join('icons', filename)
        return FXPNGIcon(self.getApp(), open(filename, 'rb').read())

    def setupMenubar(self, menubar):
        filemenu = FXMenuPane(menubar)
        FXMenuTitle(menubar, '&File', None, filemenu)
        FXMenuCommand(filemenu, '&Quit\tCtrl-Q', None,
            self.getApp(), FXApp.ID_QUIT)

        helpmenu = FXMenuPane(menubar)
        FXMenuTitle(menubar, '&Help', None, helpmenu)
        FXMenuCommand(helpmenu, '&About...', None, self, DemoBrowser.ID_ABOUT)

    def setupLeftPane(self, splitter):
        """Construct and fill the list of demo case names"""
        leftPane = FXVerticalFrame(splitter,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.demoList = FXList(leftPane, 10, self, DemoBrowser.ID_LIST,
            opts=LAYOUT_FILL_X|LAYOUT_FILL_Y)
        titles = self.demos.getTitles()
        for title in titles:
            self.demoList.appendItem(title)

    def resizeLeftPane(self):
        """Resize the left pane to make it wide enough to hold widest item"""
        maxItemWidth = 0
        listFont = self.demoList.getFont()
        for itemIndex in xrange(self.demoList.getNumItems()):
            itemText = self.demoList.getItemText(itemIndex)
            itemWidth = listFont.getTextWidth(itemText, len(itemText))
            maxItemWidth = max(itemWidth, maxItemWidth)
        self.demoList.getParent().setWidth(2*maxItemWidth)

    def getSourceCodeFont(self):
        """Pick a fixed pitch font same size as application's font"""
        appFont = self.getApp().getNormalFont()
        return FXFont(self.getApp(), '', 0.1*appFont.getSize(),
            h=FONTPITCH_FIXED)

    def getDescriptionTextFont(self):
        """Pick a font a little bigger than the application's font"""
        appFontDesc = self.getApp().getNormalFont().getFontDesc()
        appFontDesc.size = 120          # decipoints, remember?
        return FXFont(self.getApp(), appFontDesc)

    def setupRightPane(self, splitter):
        rightPane = FXVerticalFrame(splitter,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        tabBook = FXTabBook(rightPane, None, 0, LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXTabItem(tabBook, 'Description')
        pageFrame = FXHorizontalFrame(tabBook,
            FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        textFrame = FXHorizontalFrame(pageFrame,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.descText = FXText(textFrame,
            opts=TEXT_READONLY|TEXT_WORDWRAP|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.descText.setFont(self.getDescriptionTextFont())

        FXTabItem(tabBook, 'Source Code')
        pageFrame = FXHorizontalFrame(tabBook,
            FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        textFrame = FXHorizontalFrame(pageFrame,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.codeText = FXText(textFrame,
            opts=TEXT_READONLY|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.codeText.setFont(self.getSourceCodeFont())

    def onCmdAbout(self, sender, sel, ptr):
        icon = self.loadIcon('but_line_power.png')
        about = FXMessageBox(self,
            "About DemoBrowser",
            "Demo Browser for the FXPy GUI Toolkit\nhttp://fxpy.sourceforge.net\nCopyright (c) 2000 by Lyle Johnson",
            icon, MBOX_OK|DECOR_TITLE|DECOR_BORDER)
        about.execute()

    def getDemoDescription(self, filename):
        return self.demos.getDescription(filename)

    def getDemoSource(self, filename):
        return open(filename).read()

    def runDemo(self, filename, delete):
        thread.start_new_thread(threadFunc, (filename, delete))

    def onCmdList(self, sender, sel, ptr):
        currentItem = sender.getCurrentItem()
        if currentItem >= 0:
            title = self.demoList.getItemText(currentItem)
            filename = self.demos.getFilename(title)
            delete = 0
            realfile = None
            if os.path.isfile(filename):
                realfile = filename
            elif os.path.isfile(filename+".gz"):
                ifd = gzip.open(filename+".gz")
                realfile = tempfile.mktemp(".py")
                ofd = open(realfile, "w")
                ofd.write(ifd.read())
                delete = 1
            elif os.path.isfile(filename+".zip") and has_zipfile:
                ifd = zipfile.ZipFile(filename+".zip", "r")
                realfile = tempfile.mktemp(".py")
                ofd = open(realfile, "w")
                ofd.write(ifd.read(filename))
                delete = 1
            if realfile is None:
                print "could not open file %s"%filename
                return
            demoDesc = self.getDemoDescription(filename)
            demoSource = self.getDemoSource(realfile)
            self.descText.setText(demoDesc)
            self.codeText.setText(demoSource)
            self.runDemo(realfile, delete)
        else:
            self.descText.setText('')
            self.codeText.setText('')

    def create(self):
        FXMainWindow.create(self)
        self.resizeLeftPane()
        self.show(PLACEMENT_SCREEN)

if __name__ == '__main__':
    app = FXApp()
    app.init(sys.argv)
    demoBrowser = DemoBrowser(app)
    app.create()
    app.run()
