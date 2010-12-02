# This file was created automatically by SWIG.
import tablec

from misc import *

from windows import *

from containers import *
import fox
class FXTablePosPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "row" :
            tablec.FXTablePos_row_set(self,value)
            return
        if name == "col" :
            tablec.FXTablePos_col_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "row" : 
            return tablec.FXTablePos_row_get(self)
        if name == "col" : 
            return tablec.FXTablePos_col_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXTablePos instance at %s>" % (self.this,)
class FXTablePos(FXTablePosPtr):
    def __init__(self,this):
        self.this = this




class FXTableRangePtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "fm" :
            tablec.FXTableRange_fm_set(self,value.this)
            return
        if name == "to" :
            tablec.FXTableRange_to_set(self,value.this)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "fm" : 
            return FXTablePosPtr(tablec.FXTableRange_fm_get(self))
        if name == "to" : 
            return FXTablePosPtr(tablec.FXTableRange_to_get(self))
        raise AttributeError,name
    def __repr__(self):
        return "<C FXTableRange instance at %s>" % (self.this,)
class FXTableRange(FXTableRangePtr):
    def __init__(self,this):
        self.this = this




class FX_TableItemPtr(FX_ObjectPtr):
    RIGHT = tablec.FX_TableItem_RIGHT
    LEFT = tablec.FX_TableItem_LEFT
    TOP = tablec.FX_TableItem_TOP
    BOTTOM = tablec.FX_TableItem_BOTTOM
    BEFORE = tablec.FX_TableItem_BEFORE
    AFTER = tablec.FX_TableItem_AFTER
    ABOVE = tablec.FX_TableItem_ABOVE
    BELOW = tablec.FX_TableItem_BELOW
    LBORDER = tablec.FX_TableItem_LBORDER
    RBORDER = tablec.FX_TableItem_RBORDER
    TBORDER = tablec.FX_TableItem_TBORDER
    BBORDER = tablec.FX_TableItem_BBORDER
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getText(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setText,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getIcon,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setIcon,(self,) + _args, _kwargs)
        return val
    def hasFocus(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_hasFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setFocus,(self,) + _args, _kwargs)
        return val
    def isSelected(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isSelected,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setSelected,(self,) + _args, _kwargs)
        return val
    def isEnabled(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isEnabled,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def isDraggable(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isDraggable,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def getJustify(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getJustify,(self,) + _args, _kwargs)
        return val
    def setJustify(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setJustify,(self,) + _args, _kwargs)
        return val
    def getIconPosition(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getIconPosition,(self,) + _args, _kwargs)
        return val
    def setIconPosition(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setIconPosition,(self,) + _args, _kwargs)
        return val
    def getBorders(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getBorders,(self,) + _args, _kwargs)
        return val
    def setBorders(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setBorders,(self,) + _args, _kwargs)
        return val
    def getStipple(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getStipple,(self,) + _args, _kwargs)
        return val
    def setStipple(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setStipple,(self,) + _args, _kwargs)
        return val
    def isButton(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isButton,(self,) + _args, _kwargs)
        return val
    def setButton(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setButton,(self,) + _args, _kwargs)
        return val
    def isPressed(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isPressed,(self,) + _args, _kwargs)
        return val
    def setPressed(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setPressed,(self,) + _args, _kwargs)
        return val
    def isIconOwned(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_isIconOwned,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def setData(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_setData,(self,) + _args, _kwargs)
        return val
    def getData(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getData,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(tablec.FX_TableItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TableItem instance at %s>" % (self.this,)
class FX_TableItem(FX_TableItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(tablec.new_FX_TableItem,_args,_kwargs)
        self.thisown = 1




class FXTableItemPtr(FX_TableItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setText,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setJustify(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_setJustify,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(tablec.FXTableItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTableItem instance at %s>" % (self.this,)
class FXTableItem(FXTableItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(tablec.new_FXTableItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TablePtr(FX_ScrollAreaPtr):
    ID_HORZ_GRID = tablec.FX_Table_ID_HORZ_GRID
    ID_VERT_GRID = tablec.FX_Table_ID_VERT_GRID
    ID_DELETE_COLUMN = tablec.FX_Table_ID_DELETE_COLUMN
    ID_DELETE_ROW = tablec.FX_Table_ID_DELETE_ROW
    ID_INSERT_COLUMN = tablec.FX_Table_ID_INSERT_COLUMN
    ID_INSERT_ROW = tablec.FX_Table_ID_INSERT_ROW
    ID_SELECT_COLUMN = tablec.FX_Table_ID_SELECT_COLUMN
    ID_SELECT_ROW = tablec.FX_Table_ID_SELECT_ROW
    ID_SELECT_CELL = tablec.FX_Table_ID_SELECT_CELL
    ID_SELECT_ALL = tablec.FX_Table_ID_SELECT_ALL
    ID_DESELECT_ALL = tablec.FX_Table_ID_DESELECT_ALL
    ID_MOVE_LEFT = tablec.FX_Table_ID_MOVE_LEFT
    ID_MOVE_RIGHT = tablec.FX_Table_ID_MOVE_RIGHT
    ID_MOVE_UP = tablec.FX_Table_ID_MOVE_UP
    ID_MOVE_DOWN = tablec.FX_Table_ID_MOVE_DOWN
    ID_MOVE_HOME = tablec.FX_Table_ID_MOVE_HOME
    ID_MOVE_END = tablec.FX_Table_ID_MOVE_END
    ID_MOVE_TOP = tablec.FX_Table_ID_MOVE_TOP
    ID_MOVE_BOTTOM = tablec.FX_Table_ID_MOVE_BOTTOM
    ID_MOVE_PAGEDOWN = tablec.FX_Table_ID_MOVE_PAGEDOWN
    ID_MOVE_PAGEUP = tablec.FX_Table_ID_MOVE_PAGEUP
    ID_MARK = tablec.FX_Table_ID_MARK
    ID_EXTEND = tablec.FX_Table_ID_EXTEND
    ID_CUT_SEL = tablec.FX_Table_ID_CUT_SEL
    ID_COPY_SEL = tablec.FX_Table_ID_COPY_SEL
    ID_PASTE_SEL = tablec.FX_Table_ID_PASTE_SEL
    ID_BLINK = tablec.FX_Table_ID_BLINK
    ID_LAST = tablec.FX_Table_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onPaint,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onMotion,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onBlink(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onBlink,(self,) + _args, _kwargs)
        return val
    def onSelectionLost(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onSelectionLost,(self,) + _args, _kwargs)
        return val
    def onSelectionGained(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onSelectionGained,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCommand,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onCmdHorzGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdHorzGrid,(self,) + _args, _kwargs)
        return val
    def onUpdHorzGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onUpdHorzGrid,(self,) + _args, _kwargs)
        return val
    def onCmdVertGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdVertGrid,(self,) + _args, _kwargs)
        return val
    def onUpdVertGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onUpdVertGrid,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdDeleteColumn,(self,) + _args, _kwargs)
        return val
    def onUpdDeleteColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onUpdDeleteColumn,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdDeleteRow,(self,) + _args, _kwargs)
        return val
    def onUpdDeleteRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onUpdDeleteRow,(self,) + _args, _kwargs)
        return val
    def onCmdInsertColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdInsertColumn,(self,) + _args, _kwargs)
        return val
    def onCmdInsertRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdInsertRow,(self,) + _args, _kwargs)
        return val
    def onCmdMoveRight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveRight,(self,) + _args, _kwargs)
        return val
    def onCmdMoveLeft(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveLeft,(self,) + _args, _kwargs)
        return val
    def onCmdMoveUp(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveUp,(self,) + _args, _kwargs)
        return val
    def onCmdMoveDown(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveDown,(self,) + _args, _kwargs)
        return val
    def onCmdMoveHome(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveHome,(self,) + _args, _kwargs)
        return val
    def onCmdMoveEnd(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveEnd,(self,) + _args, _kwargs)
        return val
    def onCmdMoveTop(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveTop,(self,) + _args, _kwargs)
        return val
    def onCmdMoveBottom(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMoveBottom,(self,) + _args, _kwargs)
        return val
    def onCmdMovePageDown(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMovePageDown,(self,) + _args, _kwargs)
        return val
    def onCmdMovePageUp(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMovePageUp,(self,) + _args, _kwargs)
        return val
    def onCmdMark(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdMark,(self,) + _args, _kwargs)
        return val
    def onCmdExtend(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdExtend,(self,) + _args, _kwargs)
        return val
    def onCmdSelectCell(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdSelectCell,(self,) + _args, _kwargs)
        return val
    def onCmdSelectRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdSelectRow,(self,) + _args, _kwargs)
        return val
    def onCmdSelectColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdSelectColumn,(self,) + _args, _kwargs)
        return val
    def onCmdSelectAll(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdSelectAll,(self,) + _args, _kwargs)
        return val
    def onCmdDeselectAll(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_onCmdDeselectAll,(self,) + _args, _kwargs)
        return val
    def setVisibleRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setVisibleRows,(self,) + _args, _kwargs)
        return val
    def getVisibleRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getVisibleRows,(self,) + _args, _kwargs)
        return val
    def setVisibleCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setVisibleCols,(self,) + _args, _kwargs)
        return val
    def getVisibleCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getVisibleCols,(self,) + _args, _kwargs)
        return val
    def isHorzGridShown(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isHorzGridShown,(self,) + _args, _kwargs)
        return val
    def isVertGridShown(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isVertGridShown,(self,) + _args, _kwargs)
        return val
    def showHorzGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_showHorzGrid,(self,) + _args, _kwargs)
        return val
    def showVertGrid(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_showVertGrid,(self,) + _args, _kwargs)
        return val
    def setTableSize(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setTableSize,(self,) + _args, _kwargs)
        return val
    def getNumRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getNumRows,(self,) + _args, _kwargs)
        return val
    def getNumCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getNumCols,(self,) + _args, _kwargs)
        return val
    def setMarginTop(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setMarginTop,(self,) + _args, _kwargs)
        return val
    def getMarginTop(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getMarginTop,(self,) + _args, _kwargs)
        return val
    def setMarginBottom(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setMarginBottom,(self,) + _args, _kwargs)
        return val
    def getMarginBottom(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getMarginBottom,(self,) + _args, _kwargs)
        return val
    def setMarginLeft(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setMarginLeft,(self,) + _args, _kwargs)
        return val
    def getMarginLeft(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getMarginLeft,(self,) + _args, _kwargs)
        return val
    def setMarginRight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setMarginRight,(self,) + _args, _kwargs)
        return val
    def getMarginRight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getMarginRight,(self,) + _args, _kwargs)
        return val
    def getTableStyle(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getTableStyle,(self,) + _args, _kwargs)
        return val
    def setTableStyle(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setTableStyle,(self,) + _args, _kwargs)
        return val
    def setLeadingRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setLeadingRows,(self,) + _args, _kwargs)
        return val
    def getLeadingRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getLeadingRows,(self,) + _args, _kwargs)
        return val
    def setLeadingCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setLeadingCols,(self,) + _args, _kwargs)
        return val
    def getLeadingCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getLeadingCols,(self,) + _args, _kwargs)
        return val
    def setTrailingRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setTrailingRows,(self,) + _args, _kwargs)
        return val
    def getTrailingRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getTrailingRows,(self,) + _args, _kwargs)
        return val
    def setTrailingCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setTrailingCols,(self,) + _args, _kwargs)
        return val
    def getTrailingCols(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getTrailingCols,(self,) + _args, _kwargs)
        return val
    def rowAtY(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_rowAtY,(self,) + _args, _kwargs)
        return val
    def colAtX(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_colAtX,(self,) + _args, _kwargs)
        return val
    def getItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getItem,(self,) + _args, _kwargs)
        if val: val = FX_TableItemPtr(val) 
        return val
    def setItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setItem,(self,) + _args, _kwargs)
        return val
    def insertRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_insertRows,(self,) + _args, _kwargs)
        return val
    def insertColumns(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_insertColumns,(self,) + _args, _kwargs)
        return val
    def removeRows(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_removeRows,(self,) + _args, _kwargs)
        return val
    def removeColumns(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_removeColumns,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_removeItem,(self,) + _args, _kwargs)
        return val
    def makePositionVisible(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_makePositionVisible,(self,) + _args, _kwargs)
        return val
    def setColumnWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setColumnWidth,(self,) + _args, _kwargs)
        return val
    def getColumnWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getColumnWidth,(self,) + _args, _kwargs)
        return val
    def setRowHeight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setRowHeight,(self,) + _args, _kwargs)
        return val
    def getRowHeight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getRowHeight,(self,) + _args, _kwargs)
        return val
    def setColumnX(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setColumnX,(self,) + _args, _kwargs)
        return val
    def getColumnX(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getColumnX,(self,) + _args, _kwargs)
        return val
    def setRowY(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setRowY,(self,) + _args, _kwargs)
        return val
    def getRowY(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getRowY,(self,) + _args, _kwargs)
        return val
    def setDefColumnWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setDefColumnWidth,(self,) + _args, _kwargs)
        return val
    def getDefColumnWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getDefColumnWidth,(self,) + _args, _kwargs)
        return val
    def setDefRowHeight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setDefRowHeight,(self,) + _args, _kwargs)
        return val
    def getDefRowHeight(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getDefRowHeight,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemIcon(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setItemIcon,(self,) + _args, _kwargs)
        return val
    def getItemIcon(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getItemIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getItemData,(self,) + _args, _kwargs)
        return val
    def isItemSelected(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isItemSelected,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def isItemVisible(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isItemVisible,(self,) + _args, _kwargs)
        return val
    def isItemEnabled(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_isItemEnabled,(self,) + _args, _kwargs)
        return val
    def updateRange(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_updateRange,(self,) + _args, _kwargs)
        return val
    def updateItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_updateItem,(self,) + _args, _kwargs)
        return val
    def enableItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_enableItem,(self,) + _args, _kwargs)
        return val
    def disableItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_disableItem,(self,) + _args, _kwargs)
        return val
    def selectItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_selectItem,(self,) + _args, _kwargs)
        return val
    def deselectItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_deselectItem,(self,) + _args, _kwargs)
        return val
    def toggleItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_toggleItem,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getCurrentRow,(self,) + _args, _kwargs)
        return val
    def getCurrentColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getCurrentColumn,(self,) + _args, _kwargs)
        return val
    def setAnchorItem(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setAnchorItem,(self,) + _args, _kwargs)
        return val
    def getAnchorRow(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getAnchorRow,(self,) + _args, _kwargs)
        return val
    def getAnchorColumn(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getAnchorColumn,(self,) + _args, _kwargs)
        return val
    def selectRange(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_selectRange,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_killSelection,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getFont,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getTextColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setBaseColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getBaseColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setBorderColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getBorderColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setGridColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setGridColor,(self,) + _args, _kwargs)
        return val
    def getGridColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getGridColor,(self,) + _args, _kwargs)
        return val
    def setStippleColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setStippleColor,(self,) + _args, _kwargs)
        return val
    def getStippleColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getStippleColor,(self,) + _args, _kwargs)
        return val
    def setCellBorderColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setCellBorderColor,(self,) + _args, _kwargs)
        return val
    def getCellBorderColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getCellBorderColor,(self,) + _args, _kwargs)
        return val
    def setCellColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setCellColor,(self,) + _args, _kwargs)
        return val
    def getCellColor(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getCellColor,(self,) + _args, _kwargs)
        return val
    def setCellBorderWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setCellBorderWidth,(self,) + _args, _kwargs)
        return val
    def getCellBorderWidth(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getCellBorderWidth,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(tablec.FX_Table_getHelpText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Table instance at %s>" % (self.this,)
class FX_Table(FX_TablePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(tablec.new_FX_Table,_args,_kwargs)
        self.thisown = 1




class FXTablePtr(FX_TablePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(tablec.FXTable_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTable instance at %s>" % (self.this,)
class FXTable(FXTablePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(tablec.new_FXTable,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

DEFAULT_MARGIN = tablec.DEFAULT_MARGIN
TABLE_COL_SIZABLE = tablec.TABLE_COL_SIZABLE
TABLE_ROW_SIZABLE = tablec.TABLE_ROW_SIZABLE
TABLE_NO_COLSELECT = tablec.TABLE_NO_COLSELECT
TABLE_NO_ROWSELECT = tablec.TABLE_NO_ROWSELECT
