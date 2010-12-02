#!/usr/bin/env python

"""
A demonstration of the FXTable widget, contributed by
Robert Schweikert (rjschwei@mindspring.com).
"""

from FXPy.fox import *

import sys

class TableWindow(FXMainWindow):

    # Setup message identifiers
    ID_TEST = FXMainWindow.ID_LAST
    ID_RESIZETABLE = ID_TEST + 1

    def __init__ (self, app):
        FXMainWindow.__init__(self, app, "Table Widget Test")

        # Set up the message map.
        FXMAPFUNC(self, SEL_COMMAND,TableWindow.ID_TEST, TableWindow.onCmdTest)
        FXMAPFUNC(self, SEL_COMMAND, TableWindow.ID_RESIZETABLE,
                  TableWindow.onCmdResizeTable)

        # Add tool tips
        FXTooltip(self.getApp())

        # Add a manu bar
        menubar = FXMenubar(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)

        # Separator
        FXHorizontalSeparator(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X|\
                              SEPARATOR_GROOVE)

        # Window Contents
        # Use a vertical frame layout manager
        contents = FXVerticalFrame(self, LAYOUT_SIDE_TOP|FRAME_NONE|\
                                   LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Add a vertical fram layout manager
        frame = FXVerticalFrame(contents, FRAME_SUNKEN|FRAME_THICK|\
                                LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 0,0,0,0)

        # Add a table to the frame
        self.table = FXTable(frame, 20, 8, None, 0,
                             LAYOUT_FILL_X|LAYOUT_FILL_Y, 0,0,0,0, 2,2,2,2)

        # Set the table attributes
        self.table.setTableSize(50,14)
        self.table.setLeadingRows(1)
        self.table.setLeadingCols(1)

        months = ['January', 'Feburary', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November',
                  'December']

        # Set the first and last fixed rows in the table
        row = 1
        for month in months:
            self.table.setItemText(0, row, month)
            self.table.setItemText(49, row, month)
            row = row + 1

        # Set the first and last fixed columns in the table
        for row in range(48):
            self.table.setItemText(row+1,  0, '%i' %(row+1))
            self.table.setItemText(row+1, 13, '%i' %(row+1))

        # Set the scrollable part of the table
        for row in range(48):
            for column in range(len(months)):
                self.table.setItemText(row+1, column+1,
                                       "row %i; column %i" %(row+1, column+1))


        # Add file menu bar item
        filemenu = FXMenuPane(self)
        FXMenuCommand(filemenu, "&Quit\tCtl-Q", None, self.getApp(),
                      FXApp.ID_QUIT)
        FXMenuTitle(menubar,"&File",NULL,filemenu)

        # Add options menu bar item
        optMenu = FXMenuPane(self)
        FXMenuCommand(optMenu, "Horizontal grid", None, self.table,
                      FXTable.ID_HORZ_GRID)
        FXMenuCommand(optMenu, "Vertical grid", None, self.table,
                      FXTable.ID_VERT_GRID)
        FXMenuTitle(menubar, "&Options", None, optMenu)

        # Add table manipulation menu bar entry
        manipMenu = FXMenuPane(self)
        FXMenuCommand(manipMenu, "Delete Column\tCtl-C", None, self.table,
                      FXTable.ID_DELETE_COLUMN)
        FXMenuCommand(manipMenu, "Delete Row\tCtl-R", None, self.table,
                      FXTable.ID_DELETE_ROW)
        FXMenuCommand(manipMenu, "Insert Column\tCtl-Shift-C", None,
                      self.table, FXTable.ID_INSERT_COLUMN)
        FXMenuCommand(manipMenu, "Insert Row\tCtl-Shift-R", None, self.table,
                      FXTable.ID_INSERT_ROW)
        FXMenuCommand(manipMenu, "Resize table...", None, self,
                      TableWindow.ID_RESIZETABLE)
        FXMenuTitle(menubar, "&Manipulations", None, manipMenu)

        # Add selection menu bar entry
        selectMenu = FXMenuPane(self)
        FXMenuCommand(selectMenu, "Select All", None, self.table,
                      FXTable.ID_SELECT_ALL)
        FXMenuCommand(selectMenu, "Select Cell", None, self.table,
                      FXTable.ID_SELECT_CELL)
        FXMenuCommand(selectMenu, "Select Row", None, self.table,
                      FXTable.ID_SELECT_ROW)
        FXMenuCommand(selectMenu, "Select Column", None, self.table,
                      FXTable.ID_SELECT_COLUMN)
        FXMenuCommand(selectMenu, "Deselect All", None, self.table,
                      FXTable.ID_DESELECT_ALL)
        FXMenuTitle(menubar, "&Selections", None, selectMenu)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onCmdTest(self, sel):
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onCmdResizeTable(self, sel):

        # Create a dialog box
        dlg = FXDialogBox(self, "Resize Table")

        # Add a horizontal frame layout manager to the dialog box
        frame = FXHorizontalFrame(dlg, LAYOUT_FILL_X|LAYOUT_FILL_Y)

        # Add the "Rows" label
        FXLabel(frame, "Rows :", None, LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y)

        # Add a text filed
        rows = FXTextFiled(frame, 5, None, 0, JUSTIFY_RIGHT|FRAME_SUNKEN|\
                           FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y)

        # Add the "Columns" label
        FXLabel(frame, "Columns:", None, (LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))

        # Add atext field
        cols = FXTextFiled(frame, 5, None, 0, JUSTIFY_RIGHT|FRAME_SUNKEN|\
                           FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y)

        # Add a Cancle button
        FXButton(frame, "Cancle", None, dlg, FXDialogBox.ID_CANCLE,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))

        # Add an OK button
        FXButton(frame, "  OK  ", None, dlg, FXDialogBox.ID_ACCEPT,
                 (FRAME_RAISED|FRAME_THICK|LAYOUT_SIDE_LEFT|LAYOUT_CENTER_Y))

        # Get the curretn number of rows and columns in the table
        curNoRows = self.table.getNumRows()
        curNoCols = self.table.getNumCols()

        # Set the number of current rows and columns in the appropriate
        #text field
        rows.setText('%i' %curNoRows)
        cols.setText('%i' %curNoCols)

        # When the OK button is pushed this evaluates to TRUE
        if dlg.execute():

            # Get the new number of rows and columns
            newNoRows = rows.getText()
            newNoCols = cols.getText()

            if newNoRows < 0:
                newNoRows = 0
            if newNoCols < 0:
                newNoCols = 0

            self.table.setTableSize(newNoRows, newNoCols) 
            for row in range(newNoRows):
                for col in range(newNoCols):
                    if row > curNoRows or col > curNoCols:
                        self.table.setItemText(row, col,
                                       "row %i; column %i" %(row+1, column+1))

        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def create(self):
        """Create and display the dialog box"""
        
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)


application = FXApp("TableApp","Test")
application.init(sys.argv)
TableWindow(application)
application.create()
application.run()
