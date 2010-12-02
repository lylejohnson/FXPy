#! /usr/bin/env python

from FXPy.fox import *
import os

# Main window class
class SplitterWindow(FXMainWindow):
    ID_REVERSE, ID_NORMAL, ID_HORIZONTAL, ID_VERTICAL, ID_TRACKING = \
        range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+5)

    # Constructor
    def __init__(self, app):
        FXMainWindow.__init__(self, app, 'Splitter Test', w=800, h=600)

        FXMAPFUNC(self, SEL_COMMAND, SplitterWindow.ID_REVERSE,
            SplitterWindow.onCmdReverse)
        FXMAPFUNC(self, SEL_COMMAND, SplitterWindow.ID_NORMAL,
            SplitterWindow.onCmdNormal)
        FXMAPFUNC(self, SEL_COMMAND, SplitterWindow.ID_HORIZONTAL,
            SplitterWindow.onCmdHorizontal)
        FXMAPFUNC(self, SEL_COMMAND, SplitterWindow.ID_VERTICAL,
            SplitterWindow.onCmdVertical)
        FXMAPFUNC(self, SEL_COMMAND, SplitterWindow.ID_TRACKING,
            SplitterWindow.onCmdTracking)
        FXMAPFUNC(self, SEL_UPDATE,  SplitterWindow.ID_TRACKING,
            SplitterWindow.onUpdTracking)

        # Icons for tree list
        folder_open = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'minifolderopen.png'), 'rb').read())
        folder_closed = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'minifolder.png'), 'rb').read())
        doc = FXPNGIcon(self.getApp(),
            open(os.path.join('icons', 'minidoc.png'), 'rb').read())

        # Menu bar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Status bar
        status = FXStatusbar(self,
            LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # File menu
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, 'Quit\tCtl-Q', None,
            self.getApp(), FXApp.ID_QUIT)
        FXMenuTitle(menubar, '&File', None, filemenu)

        # Mode menu
        modemenu = FXMenuPane(self)
        FXMenuCommand(modemenu, 'Reverse\t\tReverse split order', None,
            self, SplitterWindow.ID_REVERSE)
        FXMenuCommand(modemenu, 'Normal\t\tNormal split order', None,
            self, SplitterWindow.ID_NORMAL)
        FXMenuCommand(modemenu, 'Horizontal\t\tHorizontal split', None,
            self, SplitterWindow.ID_HORIZONTAL)
        FXMenuCommand(modemenu, 'Vertical\t\tVertical split', None,
            self, SplitterWindow.ID_VERTICAL)
        FXMenuCommand(modemenu, 'Tracking\t\tToggle continuous tracking mode',
            None, self, SplitterWindow.ID_TRACKING)
        FXMenuTitle(menubar, '&Mode', None, modemenu)

        # Main window interior
        self.splitter = FXSplitter(self,
            LAYOUT_FILL_X|LAYOUT_FILL_Y|SPLITTER_REVERSED|SPLITTER_TRACKING)
        group1 = FXVerticalFrame(self.splitter,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y,
            0, 0, 0, 0, 0, 0, 0, 0)
        group2 = FXVerticalFrame(self.splitter,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        group3 = FXVerticalFrame(self.splitter,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)

        tree = FXTreeList(group1, 0,
            opts=FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_TOP|LAYOUT_RIGHT|TREELIST_SHOWS_LINES|TREELIST_SHOWS_BOXES)

        topItem = FXTreeItem('Top', folder_open, folder_closed)
        topmost = tree.addItemLast(None, topItem)
        tree.expandTree(topmost)
        tree.addItemLast(topmost, 'First', doc, doc)
        tree.addItemLast(topmost, 'Second', doc, doc)
        tree.addItemLast(topmost, 'Third', doc, doc)
        branch = tree.addItemLast(topmost, 'Fourth', folder_open, folder_closed)
        tree.expandTree(branch)
        tree.addItemLast(branch, FXTreeItem('Fourth-First', doc, doc))
        tree.addItemLast(branch, 'Fourth-Second', doc, doc)
        twig = tree.addItemLast(branch, 'Fourth-Third', folder_open,
            folder_closed)
        tree.addItemLast(twig, 'Fourth-Third-First', doc, doc)
        tree.addItemLast(twig, 'Fourth-Third-Second', doc, doc)
        tree.addItemLast(twig, 'Fourth-Third-Third', doc, doc)
        leaf = tree.addItemLast(twig, 'Fourth-Third-Fourth',
            folder_open, folder_closed)
        tree.addItemLast(leaf, 'Fourth-Third-Fourth-First', doc, doc)
        tree.addItemLast(leaf, 'Fourth-Third-Fourth-Second', doc, doc)
        tree.addItemLast(leaf, 'Fourth-Third-Fourth-Third', doc, doc)
        twig = tree.addItemLast(branch, 'Fourth-Fourth',
            folder_open, folder_closed)
        tree.expandTree(twig)
        tree.addItemLast(twig, 'Fourth-Fourth-First', doc, doc)
        tree.addItemLast(twig, 'Fourth-Fourth-Second', doc, doc)
        tree.addItemLast(twig, 'Fourth-Fourth-Third', doc, doc)
        for i in xrange(10):
            tree.addItemLast(twig, '%09d' % i, doc, doc)
        twig = tree.addItemLast(branch, 'Fourth-Fifth',
            folder_open, folder_closed)
        tree.addItemLast(twig, 'Fourth-Fifth-First', doc, doc)
        tree.addItemLast(twig, 'Fourth-Fifth-Second', doc, doc)
        tree.addItemLast(twig, 'Fourth-Fifth-Third', doc, doc)
        for i in xrange(10):
            tree.addItemLast(twig, '%09d' % i, doc, doc)
        tree.addItemLast(topmost, 'Fifth', doc, doc)
        tree.addItemLast(topmost, 'Sixth', doc, doc)
        branch = tree.addItemLast(topmost, 'Seventh',
            folder_open, folder_closed)
        tree.addItemLast(branch, 'Seventh-First', doc, doc)
        tree.addItemLast(branch, 'Seventh-Second', doc, doc)
        tree.addItemLast(branch, 'Seventh-Third', doc, doc)
        tree.addItemLast(topmost, 'Eighth', doc, doc)

        # Add a matrix to the second section
        FXLabel(group2, 'Matrix', None, LAYOUT_CENTER_X)
        FXHorizontalSeparator(group2, SEPARATOR_GROOVE|LAYOUT_FILL_X)
        matrix = FXMatrix(group2, 2, MATRIX_BY_COLUMNS|LAYOUT_FILL_X)

        FXLabel(matrix, 'Alpha:', None, JUSTIFY_RIGHT|LAYOUT_FILL_X|LAYOUT_CENTER_Y);
        FXTextField(matrix, 2, opts = FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN)
        FXLabel(matrix, 'Beta:', None, JUSTIFY_RIGHT|LAYOUT_FILL_X|LAYOUT_CENTER_Y)
        FXTextField(matrix, 2, opts = FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN)
        FXLabel(matrix, 'Gamma:', None, JUSTIFY_RIGHT|LAYOUT_FILL_X|LAYOUT_CENTER_Y)
        FXTextField(matrix, 2, opts = FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_CENTER_Y|LAYOUT_FILL_COLUMN)

        FXCheckButton(group2, 'Continuous Tracking\tSplitter continuously tracks split changes', self, SplitterWindow.ID_TRACKING)

        FXLabel(group3, 'Quite a Stretch', None, LAYOUT_CENTER_X)
        FXHorizontalSeparator(group3, SEPARATOR_GROOVE|LAYOUT_FILL_X)
        mat = FXMatrix(group3, 3, LAYOUT_FILL_X|LAYOUT_FILL_Y)

        FXButton(mat, 'One\nStretch the row\nStretch in Y\nStretch in X\tThe possibilities are endless..',
            opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW)
        FXButton(mat, 'Two\nStretch in Y\nStretch in X\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X)
        FXButton(mat, 'Three\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW)

        FXButton(mat, 'Four\nStretch the column\nStretch the row\nStretch in Y\nStretch in X\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_ROW|LAYOUT_FILL_COLUMN)
        FXButton(mat, 'Five\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_COLUMN)
        FXButton(mat, 'Six\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y|LAYOUT_FILL_COLUMN|LAYOUT_FILL_ROW)

        FXButton(mat, 'Seven\nStretch the column\nStretch the row\nCenter in Y\nCenter in X\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_Y|LAYOUT_CENTER_X|LAYOUT_FILL_ROW|LAYOUT_FILL_COLUMN)
        FXButton(mat, 'Eight\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_COLUMN)
        FXButton(mat, 'Nine\nStretch the column\nStretch the row\nStretch in Y\tThe possibilities are endless..', opts = FRAME_RAISED|FRAME_THICK|LAYOUT_RIGHT|LAYOUT_FILL_Y|LAYOUT_FILL_ROW|LAYOUT_FILL_COLUMN)

        # Make a tool tip
        FXTooltip(self.getApp())

    def onCmdReverse(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle() | SPLITTER_REVERSED
        self.splitter.setSplitterStyle(style)

    def onCmdNormal(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle() & ~SPLITTER_REVERSED
        self.splitter.setSplitterStyle(style)

    def onCmdHorizontal(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle() & ~SPLITTER_VERTICAL
        self.splitter.setSplitterStyle(style)

    def onCmdVertical(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle() | SPLITTER_VERTICAL
        self.splitter.setSplitterStyle(style)

    def onCmdTracking(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle() ^ SPLITTER_TRACKING
        self.splitter.setSplitterStyle(style)

    def onUpdTracking(self, sender, sel, ptr):
        style = self.splitter.getSplitterStyle()
        if style&SPLITTER_TRACKING:
            sender.handle(self, MKUINT(FXWindow.ID_CHECK, SEL_COMMAND), None)
        else:
            sender.handle(self, MKUINT(FXWindow.ID_UNCHECK, SEL_COMMAND), None)

    # Start
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

# Main program starts here
if __name__ == '__main__':
    import sys
    app = FXApp('Splitter', 'Test')
    app.init(sys.argv)
    SplitterWindow(app)
    app.create()
    app.run()
