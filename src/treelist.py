# This file was created automatically by SWIG.
import treelistc

from misc import *

from windows import *

from containers import *
import fox
class FX_TreeItemPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getParent(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getParent,(self,) + _args, _kwargs)
        return val
    def getNext(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getNext,(self,) + _args, _kwargs)
        return val
    def getPrev(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getPrev,(self,) + _args, _kwargs)
        return val
    def getFirst(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getFirst,(self,) + _args, _kwargs)
        return val
    def getLast(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getLast,(self,) + _args, _kwargs)
        return val
    def getBelow(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getBelow,(self,) + _args, _kwargs)
        return val
    def getAbove(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getAbove,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_destroy,(self,) + _args, _kwargs)
        return val
    def getNumChildren(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getNumChildren,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setText,(self,) + _args, _kwargs)
        return val
    def getOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getOpenIcon,(self,) + _args, _kwargs)
        return val
    def setOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setOpenIcon,(self,) + _args, _kwargs)
        return val
    def getClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getClosedIcon,(self,) + _args, _kwargs)
        return val
    def setClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setClosedIcon,(self,) + _args, _kwargs)
        return val
    def setData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setData,(self,) + _args, _kwargs)
        return val
    def getData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_getData,(self,) + _args, _kwargs)
        return val
    def hasFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_hasFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setFocus,(self,) + _args, _kwargs)
        return val
    def isSelected(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isSelected,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setSelected,(self,) + _args, _kwargs)
        return val
    def isOpened(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isOpened,(self,) + _args, _kwargs)
        return val
    def setOpened(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setOpened,(self,) + _args, _kwargs)
        return val
    def isExpanded(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isExpanded,(self,) + _args, _kwargs)
        return val
    def setExpanded(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setExpanded,(self,) + _args, _kwargs)
        return val
    def isEnabled(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isEnabled,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def isDraggable(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isDraggable,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def isIconOwned(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_isIconOwned,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TreeItem instance at %s>" % (self.this,)
class FX_TreeItem(FX_TreeItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FX_TreeItem,_args,_kwargs)
        self.thisown = 1




class FXTreeItemPtr(FX_TreeItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setText,(self,) + _args, _kwargs)
        return val
    def setOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setOpenIcon,(self,) + _args, _kwargs)
        return val
    def setClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setClosedIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setOpened(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setOpened,(self,) + _args, _kwargs)
        return val
    def setExpanded(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setExpanded,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTreeItem instance at %s>" % (self.this,)
class FXTreeItem(FXTreeItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FXTreeItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TreeListPtr(FX_ScrollAreaPtr):
    ID_TIPTIMER = treelistc.FX_TreeList_ID_TIPTIMER
    ID_LOOKUPTIMER = treelistc.FX_TreeList_ID_LOOKUPTIMER
    ID_LAST = treelistc.FX_TreeList_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onLeave,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onMotion,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onTipTimer(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onTipTimer,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onCommand,(self,) + _args, _kwargs)
        return val
    def onSelected(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onSelected,(self,) + _args, _kwargs)
        return val
    def onDeselected(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onDeselected,(self,) + _args, _kwargs)
        return val
    def onOpened(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onOpened,(self,) + _args, _kwargs)
        return val
    def onClosed(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onClosed,(self,) + _args, _kwargs)
        return val
    def onExpanded(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onExpanded,(self,) + _args, _kwargs)
        return val
    def onCollapsed(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onCollapsed,(self,) + _args, _kwargs)
        return val
    def onLookupTimer(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_onLookupTimer,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getNumVisible,(self,) + _args, _kwargs)
        return val
    def setNumVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setNumVisible,(self,) + _args, _kwargs)
        return val
    def getFirstItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getFirstItem,(self,) + _args, _kwargs)
        return val
    def getLastItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getLastItem,(self,) + _args, _kwargs)
        return val
    def addItemFirst(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemFirst,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemFirst2,(self,) + _args, _kwargs)
            return val
    def addItemFirst2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_addItemFirst2,(self,) + _args, _kwargs)
        return val
    def addItemLast(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemLast,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemLast2,(self,) + _args, _kwargs)
            return val
    def addItemLast2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_addItemLast2,(self,) + _args, _kwargs)
        return val
    def addItemBefore(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemBefore,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemBefore2,(self,) + _args, _kwargs)
            return val
    def addItemAfter(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemAfter,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemAfter2,(self,) + _args, _kwargs)
            return val
    def addItemBefore2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_addItemBefore2,(self,) + _args, _kwargs)
        return val
    def addItemAfter2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_addItemAfter2,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_removeItem,(self,) + _args, _kwargs)
        return val
    def removeItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_removeItems,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_clearItems,(self,) + _args, _kwargs)
        return val
    def getItemWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemWidth,(self,) + _args, _kwargs)
        return val
    def getItemHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemHeight,(self,) + _args, _kwargs)
        return val
    def getItemAt(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemAt,(self,) + _args, _kwargs)
        return val
    def findItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_findItem,(self,) + _args, _kwargs)
        return val
    def makeItemVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_makeItemVisible,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setItemOpenIcon,(self,) + _args, _kwargs)
        return val
    def getItemOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemOpenIcon,(self,) + _args, _kwargs)
        return val
    def setItemClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setItemClosedIcon,(self,) + _args, _kwargs)
        return val
    def getItemClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemClosedIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getItemData,(self,) + _args, _kwargs)
        return val
    def isItemSelected(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemSelected,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def isItemVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemVisible,(self,) + _args, _kwargs)
        return val
    def isItemOpened(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemOpened,(self,) + _args, _kwargs)
        return val
    def isItemExpanded(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemExpanded,(self,) + _args, _kwargs)
        return val
    def isItemLeaf(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemLeaf,(self,) + _args, _kwargs)
        return val
    def isItemEnabled(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_isItemEnabled,(self,) + _args, _kwargs)
        return val
    def hitItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_hitItem,(self,) + _args, _kwargs)
        return val
    def updateItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_updateItem,(self,) + _args, _kwargs)
        return val
    def enableItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_enableItem,(self,) + _args, _kwargs)
        return val
    def disableItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_disableItem,(self,) + _args, _kwargs)
        return val
    def selectItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_selectItem,(self,) + _args, _kwargs)
        return val
    def deselectItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_deselectItem,(self,) + _args, _kwargs)
        return val
    def toggleItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_toggleItem,(self,) + _args, _kwargs)
        return val
    def openItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_openItem,(self,) + _args, _kwargs)
        return val
    def closeItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_closeItem,(self,) + _args, _kwargs)
        return val
    def collapseTree(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_collapseTree,(self,) + _args, _kwargs)
        return val
    def expandTree(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_expandTree,(self,) + _args, _kwargs)
        return val
    def reparentItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_reparentItem,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def setAnchorItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setAnchorItem,(self,) + _args, _kwargs)
        return val
    def getAnchorItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getAnchorItem,(self,) + _args, _kwargs)
        return val
    def getCursorItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getCursorItem,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_killSelection,(self,) + _args, _kwargs)
        return val
    def sortItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_sortItems,(self,) + _args, _kwargs)
        return val
    def sortChildItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_sortChildItems,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setTextColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getLineColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getLineColor,(self,) + _args, _kwargs)
        return val
    def setLineColor(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setLineColor,(self,) + _args, _kwargs)
        return val
    def setIndent(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setIndent,(self,) + _args, _kwargs)
        return val
    def getIndent(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getIndent,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getHelpText,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setSortFunc,(self,) + _args, _kwargs)
        return val
    def getListStyle(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_getListStyle,(self,) + _args, _kwargs)
        return val
    def setListStyle(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeList_setListStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TreeList instance at %s>" % (self.this,)
class FX_TreeList(FX_TreeListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FX_TreeList,_args,_kwargs)
        self.thisown = 1




class FXTreeListPtr(FX_TreeListPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeList_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTreeList instance at %s>" % (self.this,)
class FXTreeList(FXTreeListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FXTreeList,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TreeListBoxPtr(FX_PackerPtr):
    ID_TREE = treelistc.FX_TreeListBox_ID_TREE
    ID_FIELD = treelistc.FX_TreeListBox_ID_FIELD
    ID_LAST = treelistc.FX_TreeListBox_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onChanged(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onChanged,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onCommand,(self,) + _args, _kwargs)
        return val
    def onFieldButton(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onFieldButton,(self,) + _args, _kwargs)
        return val
    def onTreeChanged(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onTreeChanged,(self,) + _args, _kwargs)
        return val
    def onTreeClicked(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onTreeClicked,(self,) + _args, _kwargs)
        return val
    def onUpdFmTree(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_onUpdFmTree,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getNumVisible,(self,) + _args, _kwargs)
        return val
    def setNumVisible(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setNumVisible,(self,) + _args, _kwargs)
        return val
    def getFirstItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getFirstItem,(self,) + _args, _kwargs)
        return val
    def getLastItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getLastItem,(self,) + _args, _kwargs)
        return val
    def addItemFirst(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemFirst,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemFirst2,(self,) + _args, _kwargs)
            return val
    def addItemFirst2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_addItemFirst2,(self,) + _args, _kwargs)
        return val
    def addItemLast(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemLast,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemLast2,(self,) + _args, _kwargs)
            return val
    def addItemLast2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_addItemLast2,(self,) + _args, _kwargs)
        return val
    def addItemAfter(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemAfter,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemAfter2,(self,) + _args, _kwargs)
            return val
    def addItemBefore(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemBefore,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemBefore2,(self,) + _args, _kwargs)
            return val
    def addItemAfter2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_addItemAfter2,(self,) + _args, _kwargs)
        return val
    def addItemBefore2(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_addItemBefore2,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_removeItem,(self,) + _args, _kwargs)
        return val
    def removeItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_removeItems,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_clearItems,(self,) + _args, _kwargs)
        return val
    def findItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_findItem,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def isItemLeaf(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_isItemLeaf,(self,) + _args, _kwargs)
        return val
    def sortChildItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_sortChildItems,(self,) + _args, _kwargs)
        return val
    def sortItems(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_sortItems,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setItemOpenIcon,(self,) + _args, _kwargs)
        return val
    def getItemOpenIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getItemOpenIcon,(self,) + _args, _kwargs)
        return val
    def setItemClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setItemClosedIcon,(self,) + _args, _kwargs)
        return val
    def getItemClosedIcon(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getItemClosedIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getItemData,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setSortFunc,(self,) + _args, _kwargs)
        return val
    def isPaneShown(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_isPaneShown,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getFont,(self,) + _args, _kwargs)
        return val
    def getListStyle(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getListStyle,(self,) + _args, _kwargs)
        return val
    def setListStyle(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setListStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(treelistc.FX_TreeListBox_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TreeListBox instance at %s>" % (self.this,)
class FX_TreeListBox(FX_TreeListBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FX_TreeListBox,_args,_kwargs)
        self.thisown = 1




class FXTreeListBoxPtr(FX_TreeListBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(treelistc.FXTreeListBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTreeListBox instance at %s>" % (self.this,)
class FXTreeListBox(FXTreeListBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(treelistc.new_FXTreeListBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

TREELIST_EXTENDEDSELECT = treelistc.TREELIST_EXTENDEDSELECT
TREELIST_SINGLESELECT = treelistc.TREELIST_SINGLESELECT
TREELIST_BROWSESELECT = treelistc.TREELIST_BROWSESELECT
TREELIST_MULTIPLESELECT = treelistc.TREELIST_MULTIPLESELECT
TREELIST_AUTOSELECT = treelistc.TREELIST_AUTOSELECT
TREELIST_SHOWS_LINES = treelistc.TREELIST_SHOWS_LINES
TREELIST_SHOWS_BOXES = treelistc.TREELIST_SHOWS_BOXES
TREELIST_ROOT_BOXES = treelistc.TREELIST_ROOT_BOXES
TREELIST_NORMAL = treelistc.TREELIST_NORMAL
TREELISTBOX_NORMAL = treelistc.TREELISTBOX_NORMAL
