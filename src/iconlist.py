# This file was created automatically by SWIG.
import iconlistc

from misc import *

from windows import *

from containers import *
import fox
class FX_IconItemPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setText,(self,) + _args, _kwargs)
        return val
    def getBigIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getBigIcon,(self,) + _args, _kwargs)
        return val
    def setBigIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setBigIcon,(self,) + _args, _kwargs)
        return val
    def getMiniIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getMiniIcon,(self,) + _args, _kwargs)
        return val
    def setMiniIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setMiniIcon,(self,) + _args, _kwargs)
        return val
    def setData(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setData,(self,) + _args, _kwargs)
        return val
    def getData(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getData,(self,) + _args, _kwargs)
        return val
    def hasFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_hasFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setFocus,(self,) + _args, _kwargs)
        return val
    def isSelected(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_isSelected,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setSelected,(self,) + _args, _kwargs)
        return val
    def isEnabled(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_isEnabled,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def isDraggable(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_isDraggable,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def isIconOwned(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_isIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_IconItem instance at %s>" % (self.this,)
class FX_IconItem(FX_IconItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(iconlistc.new_FX_IconItem,_args,_kwargs)
        self.thisown = 1




class FXIconItemPtr(FX_IconItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setText,(self,) + _args, _kwargs)
        return val
    def setBigIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setBigIcon,(self,) + _args, _kwargs)
        return val
    def setMiniIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setMiniIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXIconItem instance at %s>" % (self.this,)
class FXIconItem(FXIconItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(iconlistc.new_FXIconItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_IconListPtr(FX_ScrollAreaPtr):
    ID_SHOW_DETAILS = iconlistc.FX_IconList_ID_SHOW_DETAILS
    ID_SHOW_MINI_ICONS = iconlistc.FX_IconList_ID_SHOW_MINI_ICONS
    ID_SHOW_BIG_ICONS = iconlistc.FX_IconList_ID_SHOW_BIG_ICONS
    ID_ARRANGE_BY_ROWS = iconlistc.FX_IconList_ID_ARRANGE_BY_ROWS
    ID_ARRANGE_BY_COLUMNS = iconlistc.FX_IconList_ID_ARRANGE_BY_COLUMNS
    ID_HEADER_CHANGE = iconlistc.FX_IconList_ID_HEADER_CHANGE
    ID_TIPTIMER = iconlistc.FX_IconList_ID_TIPTIMER
    ID_LOOKUPTIMER = iconlistc.FX_IconList_ID_LOOKUPTIMER
    ID_SELECT_ALL = iconlistc.FX_IconList_ID_SELECT_ALL
    ID_DESELECT_ALL = iconlistc.FX_IconList_ID_DESELECT_ALL
    ID_SELECT_INVERSE = iconlistc.FX_IconList_ID_SELECT_INVERSE
    ID_LAST = iconlistc.FX_IconList_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onLeave,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onMotion,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onTipTimer(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onTipTimer,(self,) + _args, _kwargs)
        return val
    def onCmdSelectAll(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdSelectAll,(self,) + _args, _kwargs)
        return val
    def onCmdDeselectAll(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdDeselectAll,(self,) + _args, _kwargs)
        return val
    def onCmdSelectInverse(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdSelectInverse,(self,) + _args, _kwargs)
        return val
    def onCmdArrangeByRows(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdArrangeByRows,(self,) + _args, _kwargs)
        return val
    def onUpdArrangeByRows(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUpdArrangeByRows,(self,) + _args, _kwargs)
        return val
    def onCmdArrangeByColumns(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdArrangeByColumns,(self,) + _args, _kwargs)
        return val
    def onUpdArrangeByColumns(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUpdArrangeByColumns,(self,) + _args, _kwargs)
        return val
    def onCmdShowDetails(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdShowDetails,(self,) + _args, _kwargs)
        return val
    def onUpdShowDetails(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUpdShowDetails,(self,) + _args, _kwargs)
        return val
    def onCmdShowBigIcons(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdShowBigIcons,(self,) + _args, _kwargs)
        return val
    def onUpdShowBigIcons(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUpdShowBigIcons,(self,) + _args, _kwargs)
        return val
    def onCmdShowMiniIcons(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdShowMiniIcons,(self,) + _args, _kwargs)
        return val
    def onUpdShowMiniIcons(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onUpdShowMiniIcons,(self,) + _args, _kwargs)
        return val
    def onHeaderChanged(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onHeaderChanged,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCommand,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onLookupTimer(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onLookupTimer,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumRows(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getNumRows,(self,) + _args, _kwargs)
        return val
    def getNumCols(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getNumCols,(self,) + _args, _kwargs)
        return val
    def getHeader(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getHeader,(self,) + _args, _kwargs)
        return val
    def appendHeader(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_appendHeader,(self,) + _args, _kwargs)
        return val
    def removeHeader(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_removeHeader,(self,) + _args, _kwargs)
        return val
    def setHeaderText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setHeaderText,(self,) + _args, _kwargs)
        return val
    def getHeaderText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getHeaderText,(self,) + _args, _kwargs)
        return val
    def setHeaderIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setHeaderIcon,(self,) + _args, _kwargs)
        return val
    def getHeaderIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getHeaderIcon,(self,) + _args, _kwargs)
        return val
    def setHeaderSize(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setHeaderSize,(self,) + _args, _kwargs)
        return val
    def getHeaderSize(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getHeaderSize,(self,) + _args, _kwargs)
        return val
    def getNumHeaders(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getNumHeaders,(self,) + _args, _kwargs)
        return val
    def retrieveItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_retrieveItem,(self,) + _args, _kwargs)
        return val
    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_insertItemStr,(self,) + _args, _kwargs)
            return val
    def insertItemStr(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_insertItemStr,(self,) + _args, _kwargs)
        return val
    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_replaceItemStr,(self,) + _args, _kwargs)
            return val
    def replaceItemStr(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_replaceItemStr,(self,) + _args, _kwargs)
        return val
    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_appendItemStr,(self,) + _args, _kwargs)
            return val
    def appendItemStr(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_appendItemStr,(self,) + _args, _kwargs)
        return val
    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_prependItemStr,(self,) + _args, _kwargs)
            return val
    def prependItemStr(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_prependItemStr,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_removeItem,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_clearItems,(self,) + _args, _kwargs)
        return val
    def getItemWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemWidth,(self,) + _args, _kwargs)
        return val
    def getItemHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemHeight,(self,) + _args, _kwargs)
        return val
    def getItemAt(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemAt,(self,) + _args, _kwargs)
        return val
    def findItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_findItem,(self,) + _args, _kwargs)
        return val
    def makeItemVisible(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_makeItemVisible,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemBigIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setItemBigIcon,(self,) + _args, _kwargs)
        return val
    def getItemBigIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemBigIcon,(self,) + _args, _kwargs)
        return val
    def setItemMiniIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setItemMiniIcon,(self,) + _args, _kwargs)
        return val
    def getItemMiniIcon(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemMiniIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemData,(self,) + _args, _kwargs)
        return val
    def isItemSelected(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_isItemSelected,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def isItemVisible(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_isItemVisible,(self,) + _args, _kwargs)
        return val
    def isItemEnabled(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_isItemEnabled,(self,) + _args, _kwargs)
        return val
    def enableItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_enableItem,(self,) + _args, _kwargs)
        return val
    def disableItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_disableItem,(self,) + _args, _kwargs)
        return val
    def hitItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_hitItem,(self,) + _args, _kwargs)
        return val
    def updateItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_updateItem,(self,) + _args, _kwargs)
        return val
    def selectInRectangle(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_selectInRectangle,(self,) + _args, _kwargs)
        return val
    def selectItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_selectItem,(self,) + _args, _kwargs)
        return val
    def deselectItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_deselectItem,(self,) + _args, _kwargs)
        return val
    def toggleItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_toggleItem,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def setAnchorItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setAnchorItem,(self,) + _args, _kwargs)
        return val
    def getAnchorItem(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getAnchorItem,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_killSelection,(self,) + _args, _kwargs)
        return val
    def sortItems(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_sortItems,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setTextColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def setItemSpace(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setItemSpace,(self,) + _args, _kwargs)
        return val
    def getItemSpace(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getItemSpace,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setSortFunc,(self,) + _args, _kwargs)
        return val
    def getListStyle(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getListStyle,(self,) + _args, _kwargs)
        return val
    def setListStyle(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setListStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(iconlistc.FX_IconList_getHelpText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_IconList instance at %s>" % (self.this,)
class FX_IconList(FX_IconListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(iconlistc.new_FX_IconList,_args,_kwargs)
        self.thisown = 1




class FXIconListPtr(FX_IconListPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(iconlistc.FXIconList_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXIconList instance at %s>" % (self.this,)
class FXIconList(FXIconListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(iconlistc.new_FXIconList,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

ICONLIST_EXTENDEDSELECT = iconlistc.ICONLIST_EXTENDEDSELECT
ICONLIST_SINGLESELECT = iconlistc.ICONLIST_SINGLESELECT
ICONLIST_BROWSESELECT = iconlistc.ICONLIST_BROWSESELECT
ICONLIST_MULTIPLESELECT = iconlistc.ICONLIST_MULTIPLESELECT
ICONLIST_AUTOSIZE = iconlistc.ICONLIST_AUTOSIZE
ICONLIST_DETAILED = iconlistc.ICONLIST_DETAILED
ICONLIST_MINI_ICONS = iconlistc.ICONLIST_MINI_ICONS
ICONLIST_BIG_ICONS = iconlistc.ICONLIST_BIG_ICONS
ICONLIST_ROWS = iconlistc.ICONLIST_ROWS
ICONLIST_COLUMNS = iconlistc.ICONLIST_COLUMNS
ICONLIST_NORMAL = iconlistc.ICONLIST_NORMAL
