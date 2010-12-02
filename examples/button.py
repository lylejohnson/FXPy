#! /usr/bin/env python

import os
from FXPy.fox import *

class ButtonWindow(FXMainWindow):
    (ID_ICON_BEFORE_TEXT,
    ID_ICON_AFTER_TEXT,
    ID_ICON_CENTER_HOR,
    ID_ICON_ABOVE_TEXT,
    ID_ICON_BELOW_TEXT,
    ID_ICON_CENTER_VER,
    ID_JUST_CENTER_X,
    ID_JUST_LEFT,
    ID_JUST_RIGHT,
    ID_JUST_HOR_APART,
    ID_JUST_CENTER_Y,
    ID_JUST_TOP,
    ID_JUST_BOTTOM,
    ID_JUST_VER_APART,
    ID_TOOLBAR_STYLE,
    ID_DEBUG) = range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+16)

    # Constructor
    def __init__(self, app):
        FXMainWindow.__init__(self, app, "Button Test")

        # Set up the message map
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_BEFORE_TEXT,ButtonWindow.onCmdIconBeforeText)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_AFTER_TEXT,ButtonWindow.onCmdIconAfterText)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_CENTER_HOR,ButtonWindow.onCmdIconCenterHor)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_ABOVE_TEXT,ButtonWindow.onCmdIconAboveText)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_BELOW_TEXT,ButtonWindow.onCmdIconBelowText)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_ICON_CENTER_VER,ButtonWindow.onCmdIconCenterVer)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_CENTER_X,ButtonWindow.onCmdJustCenterX)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_LEFT,ButtonWindow.onCmdJustLeft)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_RIGHT,ButtonWindow.onCmdJustRight)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_HOR_APART,ButtonWindow.onCmdJustHorApart)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_CENTER_Y,ButtonWindow.onCmdJustCenterY)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_TOP,ButtonWindow.onCmdJustTop)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_BOTTOM,ButtonWindow.onCmdJustBottom)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_JUST_VER_APART,ButtonWindow.onCmdJustVerApart)
        FXMAPFUNC(self,SEL_COMMAND,ButtonWindow.ID_TOOLBAR_STYLE,ButtonWindow.onCmdToolbarStyle)

        # Make a tool tip
        FXTooltip(app)

        # Status bar
        statusbar = FXStatusbar(self, LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)

        # Controls on the right
        controls = FXVerticalFrame(self, LAYOUT_SIDE_RIGHT|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH)

        # Contents
        contents = FXHorizontalFrame(self, LAYOUT_SIDE_LEFT|FRAME_NONE|LAYOUT_FILL_X|LAYOUT_FILL_Y|PACK_UNIFORM_WIDTH,0,0,0,0,20,20,20,20)

        # The button
        bigpenguin = open(os.path.join('icons', 'bigpenguin.png'), 'rb').read();
        self.button = FXButton(contents,
                      "&This is a multi-line label on\na button to show off the full\ncapabilities of the button object\tIt also has a tooltip\n[which by the way can be multi-line also]\tAnd some helpful message for the status line.",
                      FXPNGIcon(self.getApp(),bigpenguin),
                      opts=FRAME_RAISED|FRAME_THICK|LAYOUT_CENTER_X|LAYOUT_CENTER_Y|LAYOUT_FIX_WIDTH|LAYOUT_FIX_HEIGHT,
                      w=300, h=200)

        self.checkButton = FXCheckButton(controls, 'Toolbar Style\tCool "poppy" style buttons', self, self.ID_TOOLBAR_STYLE)

        group1 = FXGroupBox(controls,"Horizontal Placement",GROUPBOX_TITLE_CENTER|FRAME_RIDGE)
        FXRadioButton(group1,"Before Text",self,self.ID_ICON_BEFORE_TEXT)
        FXRadioButton(group1,"After Text",self,self.ID_ICON_AFTER_TEXT)
        FXRadioButton(group1,"Centered",self,self.ID_ICON_CENTER_HOR)

        group2 = FXGroupBox(controls,"Vertical Placement",GROUPBOX_TITLE_CENTER|FRAME_RIDGE)
        FXRadioButton(group2,"Above Text",self,self.ID_ICON_ABOVE_TEXT)
        FXRadioButton(group2,"Below Text",self,self.ID_ICON_BELOW_TEXT)
        FXRadioButton(group2,"Centered",self,self.ID_ICON_CENTER_VER)

        group3 = FXGroupBox(controls,"Horizontal Justify",GROUPBOX_TITLE_CENTER|FRAME_RIDGE)
        FXRadioButton(group3,"Center",self,self.ID_JUST_CENTER_X)
        FXRadioButton(group3,"Left",self,self.ID_JUST_LEFT)
        FXRadioButton(group3,"Right",self,self.ID_JUST_RIGHT)
        FXRadioButton(group3,"Apart",self,self.ID_JUST_HOR_APART)

        group4 = FXGroupBox(controls,"Vertical Justify",GROUPBOX_TITLE_CENTER|FRAME_RIDGE)
        FXRadioButton(group4,"Center",self,self.ID_JUST_CENTER_Y)
        FXRadioButton(group4,"Top",self,self.ID_JUST_TOP)
        FXRadioButton(group4,"Bottom",self,self.ID_JUST_BOTTOM)
        FXRadioButton(group4,"Apart",self,self.ID_JUST_VER_APART)

    def onCmdIconBeforeText(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style|ICON_BEFORE_TEXT
        style = style & ~ICON_AFTER_TEXT
        self.button.setIconPosition(style)

    def onCmdIconAfterText(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style|ICON_AFTER_TEXT
        style = style & ~ICON_BEFORE_TEXT
        self.button.setIconPosition(style)

    def onCmdIconCenterHor(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style & ~ICON_AFTER_TEXT
        style = style & ~ICON_BEFORE_TEXT
        self.button.setIconPosition(style)

    def onCmdIconAboveText(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style | ICON_ABOVE_TEXT
        style = style & ~ICON_BELOW_TEXT
        self.button.setIconPosition(style)

    def onCmdIconBelowText(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style | ICON_BELOW_TEXT
        style = style & ~ICON_ABOVE_TEXT
        self.button.setIconPosition(style)

    def onCmdIconCenterVer(self,sender,sel,ptr):
        style = self.button.getIconPosition()
        style = style & ~ICON_ABOVE_TEXT
        style = style & ~ICON_BELOW_TEXT
        self.button.setIconPosition(style)

    def onCmdJustCenterX(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_HZ_APART
        self.button.setJustify(style)

    def onCmdJustLeft(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_HZ_APART
        style = style|JUSTIFY_LEFT
        self.button.setJustify(style)

    def onCmdJustRight(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_HZ_APART
        style = style|JUSTIFY_RIGHT
        self.button.setJustify(style)

    def onCmdJustHorApart(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style|JUSTIFY_HZ_APART
        self.button.setJustify(style)

    def onCmdJustCenterY(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_VT_APART
        self.button.setJustify(style)

    def onCmdJustTop(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_VT_APART
        style = style|JUSTIFY_TOP
        self.button.setJustify(style)

    def onCmdJustBottom(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style&~JUSTIFY_VT_APART
        style = style|JUSTIFY_BOTTOM
        self.button.setJustify(style)

    def onCmdJustVerApart(self,sender,sel,ptr):
        style = self.button.getJustify()
        style = style|JUSTIFY_VT_APART
        self.button.setJustify(style)

    def onCmdToolbarStyle(self,sender,sel,ptr):
        style = self.button.getButtonStyle()
        if self.checkButton.getCheck():
            style = style|BUTTON_TOOLBAR
            self.button.setFrameStyle(FRAME_RAISED)
        else:
            style = style&~BUTTON_TOOLBAR
            self.button.setFrameStyle(FRAME_RAISED|FRAME_THICK)
        self.button.setButtonStyle(style)


    # Create and show the main window
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

# Main program starts here
if __name__ == "__main__":
    import sys
    application = FXApp("Button", "Test")
    application.init(sys.argv)
    ButtonWindow(application)
    application.create()
    application.run()
