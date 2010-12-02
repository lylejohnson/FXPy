# This file was created automatically by SWIG.
import dirlistc

from misc import *

from windows import *

from containers import *

from treelist import *
import fox
class FX_DirItemPtr(FX_TreeItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def isDirectory(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isDirectory,(self,) + _args, _kwargs)
        return val
    def isExecutable(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isExecutable,(self,) + _args, _kwargs)
        return val
    def isSymlink(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isSymlink,(self,) + _args, _kwargs)
        return val
    def isChardev(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isChardev,(self,) + _args, _kwargs)
        return val
    def isBlockdev(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isBlockdev,(self,) + _args, _kwargs)
        return val
    def isFifo(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isFifo,(self,) + _args, _kwargs)
        return val
    def isSocket(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_isSocket,(self,) + _args, _kwargs)
        return val
    def getAssoc(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_getAssoc,(self,) + _args, _kwargs)
        return val
    def getSize(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_getSize,(self,) + _args, _kwargs)
        return val
    def getDate(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirItem_getDate,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DirItem instance at %s>" % (self.this,)
class FX_DirItem(FX_DirItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dirlistc.new_FX_DirItem,_args,_kwargs)
        self.thisown = 1




class FXDirItemPtr(FX_DirItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setText,(self,) + _args, _kwargs)
        return val
    def setOpenIcon(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setOpenIcon,(self,) + _args, _kwargs)
        return val
    def setClosedIcon(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setClosedIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setOpened(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setOpened,(self,) + _args, _kwargs)
        return val
    def setExpanded(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setExpanded,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDirItem instance at %s>" % (self.this,)
class FXDirItem(FXDirItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dirlistc.new_FXDirItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DirListPtr(FX_TreeListPtr):
    ID_REFRESH = dirlistc.FX_DirList_ID_REFRESH
    ID_SHOW_FILES = dirlistc.FX_DirList_ID_SHOW_FILES
    ID_HIDE_FILES = dirlistc.FX_DirList_ID_HIDE_FILES
    ID_TOGGLE_FILES = dirlistc.FX_DirList_ID_TOGGLE_FILES
    ID_SHOW_HIDDEN = dirlistc.FX_DirList_ID_SHOW_HIDDEN
    ID_HIDE_HIDDEN = dirlistc.FX_DirList_ID_HIDE_HIDDEN
    ID_TOGGLE_HIDDEN = dirlistc.FX_DirList_ID_TOGGLE_HIDDEN
    ID_SET_PATTERN = dirlistc.FX_DirList_ID_SET_PATTERN
    ID_SORT_REVERSE = dirlistc.FX_DirList_ID_SORT_REVERSE
    ID_LAST = dirlistc.FX_DirList_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onRefresh(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onRefresh,(self,) + _args, _kwargs)
        return val
    def onBeginDrag(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onBeginDrag,(self,) + _args, _kwargs)
        return val
    def onEndDrag(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onEndDrag,(self,) + _args, _kwargs)
        return val
    def onDragged(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDragged,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDRequest(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onDNDRequest,(self,) + _args, _kwargs)
        return val
    def onOpened(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onOpened,(self,) + _args, _kwargs)
        return val
    def onClosed(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onClosed,(self,) + _args, _kwargs)
        return val
    def onExpanded(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onExpanded,(self,) + _args, _kwargs)
        return val
    def onCollapsed(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCollapsed,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdToggleHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdToggleHidden,(self,) + _args, _kwargs)
        return val
    def onUpdToggleHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdToggleHidden,(self,) + _args, _kwargs)
        return val
    def onCmdShowHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdShowHidden,(self,) + _args, _kwargs)
        return val
    def onUpdShowHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdShowHidden,(self,) + _args, _kwargs)
        return val
    def onCmdHideHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdHideHidden,(self,) + _args, _kwargs)
        return val
    def onUpdHideHidden(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdHideHidden,(self,) + _args, _kwargs)
        return val
    def onCmdToggleFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdToggleFiles,(self,) + _args, _kwargs)
        return val
    def onUpdToggleFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdToggleFiles,(self,) + _args, _kwargs)
        return val
    def onCmdShowFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdShowFiles,(self,) + _args, _kwargs)
        return val
    def onUpdShowFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdShowFiles,(self,) + _args, _kwargs)
        return val
    def onCmdHideFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdHideFiles,(self,) + _args, _kwargs)
        return val
    def onUpdHideFiles(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdHideFiles,(self,) + _args, _kwargs)
        return val
    def onCmdSetPattern(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdSetPattern,(self,) + _args, _kwargs)
        return val
    def onUpdSetPattern(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdSetPattern,(self,) + _args, _kwargs)
        return val
    def onCmdSortReverse(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onCmdSortReverse,(self,) + _args, _kwargs)
        return val
    def onUpdSortReverse(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_onUpdSortReverse,(self,) + _args, _kwargs)
        return val
    def isItemDirectory(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_isItemDirectory,(self,) + _args, _kwargs)
        return val
    def isItemFile(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_isItemFile,(self,) + _args, _kwargs)
        return val
    def isItemExecutable(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_isItemExecutable,(self,) + _args, _kwargs)
        return val
    def setCurrentFile(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_setCurrentFile,(self,) + _args, _kwargs)
        return val
    def getCurrentFile(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getCurrentFile,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getDirectory,(self,) + _args, _kwargs)
        return val
    def getItemFilename(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getItemFilename,(self,) + _args, _kwargs)
        return val
    def getItemPathname(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getItemPathname,(self,) + _args, _kwargs)
        return val
    def setPattern(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_setPattern,(self,) + _args, _kwargs)
        return val
    def getPattern(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getPattern,(self,) + _args, _kwargs)
        return val
    def getMatchMode(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getMatchMode,(self,) + _args, _kwargs)
        return val
    def setMatchMode(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_setMatchMode,(self,) + _args, _kwargs)
        return val
    def showFiles(self, *_args, **_kwargs):
        try:
            val = apply(dirlistc.FX_DirList_showFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dirlistc.FX_DirList_showFiles2,(self,) + _args, _kwargs)
            return val
    def showFiles2(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_showFiles2,(self,) + _args, _kwargs)
        return val
    def showHiddenFiles(self, *_args, **_kwargs):
        try:
            val = apply(dirlistc.FX_DirList_showHiddenFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dirlistc.FX_DirList_showHiddenFiles2,(self,) + _args, _kwargs)
            return val
    def showHiddenFiles2(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_showHiddenFiles2,(self,) + _args, _kwargs)
        return val
    def setAssociations(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_setAssociations,(self,) + _args, _kwargs)
        return val
    def getAssociations(self, *_args, **_kwargs):
        val = apply(dirlistc.FX_DirList_getAssociations,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DirList instance at %s>" % (self.this,)
class FX_DirList(FX_DirListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dirlistc.new_FX_DirList,_args,_kwargs)
        self.thisown = 1




class FXDirListPtr(FX_DirListPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(dirlistc.FXDirList_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDirList instance at %s>" % (self.this,)
class FXDirList(FXDirListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dirlistc.new_FXDirList,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

FX_DirList_cmpFName = dirlistc.FX_DirList_cmpFName

FX_DirList_cmpRName = dirlistc.FX_DirList_cmpRName



#-------------- VARIABLE WRAPPERS ------------------

DIRLIST_SHOWFILES = dirlistc.DIRLIST_SHOWFILES
DIRLIST_SHOWHIDDEN = dirlistc.DIRLIST_SHOWHIDDEN
DIRLIST_NO_OWN_ASSOC = dirlistc.DIRLIST_NO_OWN_ASSOC
