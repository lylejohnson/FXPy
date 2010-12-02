# This file was created automatically by SWIG.
import dialogsc

from windows import *

from misc import *

from containers import *

from controls import *

from treelist import *

from iconlist import *
import fox
class FX_DialogBoxPtr(FX_TopWindowPtr):
    ID_CANCEL = dialogsc.FX_DialogBox_ID_CANCEL
    ID_ACCEPT = dialogsc.FX_DialogBox_ID_ACCEPT
    ID_LAST = dialogsc.FX_DialogBox_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onClose(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_onClose,(self,) + _args, _kwargs)
        return val
    def onCmdAccept(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_onCmdAccept,(self,) + _args, _kwargs)
        return val
    def onCmdCancel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_onCmdCancel,(self,) + _args, _kwargs)
        return val
    def execute(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DialogBox_execute,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DialogBox instance at %s>" % (self.this,)
class FX_DialogBox(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this




class FXDialogBoxPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXDialogBox_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXDialogBox_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDialogBox_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDialogBox instance at %s>" % (self.this,)
class FXDialogBox(FXDialogBoxPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(dialogsc.CreateOwnedDialogBox,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(dialogsc.CreateFreeDialogBox,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_DirBoxPtr(FX_TreeListBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onChanged(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_onChanged,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_onCommand,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirBox_getDirectory,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DirBox instance at %s>" % (self.this,)
class FX_DirBox(FX_DirBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_DirBox,_args,_kwargs)
        self.thisown = 1




class FXDirBoxPtr(FX_DirBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDirBox instance at %s>" % (self.this,)
class FXDirBox(FXDirBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXDirBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FileItemPtr(FX_IconItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def isFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isFile,(self,) + _args, _kwargs)
        return val
    def isDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isDirectory,(self,) + _args, _kwargs)
        return val
    def isExecutable(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isExecutable,(self,) + _args, _kwargs)
        return val
    def isSymlink(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isSymlink,(self,) + _args, _kwargs)
        return val
    def isChardev(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isChardev,(self,) + _args, _kwargs)
        return val
    def isBlockdev(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isBlockdev,(self,) + _args, _kwargs)
        return val
    def isFifo(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isFifo,(self,) + _args, _kwargs)
        return val
    def isSocket(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_isSocket,(self,) + _args, _kwargs)
        return val
    def getAssoc(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_getAssoc,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def getSize(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_getSize,(self,) + _args, _kwargs)
        return val
    def getDate(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileItem_getDate,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_FileItem instance at %s>" % (self.this,)
class FX_FileItem(FX_FileItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FileItem,_args,_kwargs)
        self.thisown = 1




class FXFileItemPtr(FX_FileItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setText,(self,) + _args, _kwargs)
        return val
    def setBigIcon(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setBigIcon,(self,) + _args, _kwargs)
        return val
    def setMiniIcon(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setMiniIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFileItem instance at %s>" % (self.this,)
class FXFileItem(FXFileItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFileItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FileListPtr(FX_IconListPtr):
    ID_SORT_BY_NAME = dialogsc.FX_FileList_ID_SORT_BY_NAME
    ID_SORT_BY_TYPE = dialogsc.FX_FileList_ID_SORT_BY_TYPE
    ID_SORT_BY_SIZE = dialogsc.FX_FileList_ID_SORT_BY_SIZE
    ID_SORT_BY_TIME = dialogsc.FX_FileList_ID_SORT_BY_TIME
    ID_SORT_BY_USER = dialogsc.FX_FileList_ID_SORT_BY_USER
    ID_SORT_BY_GROUP = dialogsc.FX_FileList_ID_SORT_BY_GROUP
    ID_SORT_REVERSE = dialogsc.FX_FileList_ID_SORT_REVERSE
    ID_DIRECTORY_UP = dialogsc.FX_FileList_ID_DIRECTORY_UP
    ID_SET_PATTERN = dialogsc.FX_FileList_ID_SET_PATTERN
    ID_SET_DIRECTORY = dialogsc.FX_FileList_ID_SET_DIRECTORY
    ID_SHOW_HIDDEN = dialogsc.FX_FileList_ID_SHOW_HIDDEN
    ID_HIDE_HIDDEN = dialogsc.FX_FileList_ID_HIDE_HIDDEN
    ID_TOGGLE_HIDDEN = dialogsc.FX_FileList_ID_TOGGLE_HIDDEN
    ID_REFRESHTIMER = dialogsc.FX_FileList_ID_REFRESHTIMER
    ID_OPENTIMER = dialogsc.FX_FileList_ID_OPENTIMER
    ID_LAST = dialogsc.FX_FileList_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onRefreshTimer(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onRefreshTimer,(self,) + _args, _kwargs)
        return val
    def onOpenTimer(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onOpenTimer,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDRequest(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDNDRequest,(self,) + _args, _kwargs)
        return val
    def onBeginDrag(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onBeginDrag,(self,) + _args, _kwargs)
        return val
    def onEndDrag(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onEndDrag,(self,) + _args, _kwargs)
        return val
    def onDragged(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onDragged,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdDirectoryUp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdDirectoryUp,(self,) + _args, _kwargs)
        return val
    def onUpdDirectoryUp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdDirectoryUp,(self,) + _args, _kwargs)
        return val
    def onCmdSortByName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortByName,(self,) + _args, _kwargs)
        return val
    def onUpdSortByName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortByName,(self,) + _args, _kwargs)
        return val
    def onCmdSortByType(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortByType,(self,) + _args, _kwargs)
        return val
    def onUpdSortByType(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortByType,(self,) + _args, _kwargs)
        return val
    def onCmdSortBySize(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortBySize,(self,) + _args, _kwargs)
        return val
    def onUpdSortBySize(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortBySize,(self,) + _args, _kwargs)
        return val
    def onCmdSortByTime(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortByTime,(self,) + _args, _kwargs)
        return val
    def onUpdSortByTime(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortByTime,(self,) + _args, _kwargs)
        return val
    def onCmdSortByUser(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortByUser,(self,) + _args, _kwargs)
        return val
    def onUpdSortByUser(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortByUser,(self,) + _args, _kwargs)
        return val
    def onCmdSortByGroup(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortByGroup,(self,) + _args, _kwargs)
        return val
    def onUpdSortByGroup(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortByGroup,(self,) + _args, _kwargs)
        return val
    def onCmdSortReverse(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSortReverse,(self,) + _args, _kwargs)
        return val
    def onUpdSortReverse(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSortReverse,(self,) + _args, _kwargs)
        return val
    def onCmdSetPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSetPattern,(self,) + _args, _kwargs)
        return val
    def onUpdSetPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSetPattern,(self,) + _args, _kwargs)
        return val
    def onCmdSetDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdSetDirectory,(self,) + _args, _kwargs)
        return val
    def onUpdSetDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdSetDirectory,(self,) + _args, _kwargs)
        return val
    def onCmdToggleHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdToggleHidden,(self,) + _args, _kwargs)
        return val
    def onUpdToggleHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdToggleHidden,(self,) + _args, _kwargs)
        return val
    def onCmdShowHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdShowHidden,(self,) + _args, _kwargs)
        return val
    def onUpdShowHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdShowHidden,(self,) + _args, _kwargs)
        return val
    def onCmdHideHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdHideHidden,(self,) + _args, _kwargs)
        return val
    def onUpdHideHidden(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdHideHidden,(self,) + _args, _kwargs)
        return val
    def onCmdHeader(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onCmdHeader,(self,) + _args, _kwargs)
        return val
    def onUpdHeader(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_onUpdHeader,(self,) + _args, _kwargs)
        return val
    def setCurrentFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_setCurrentFile,(self,) + _args, _kwargs)
        return val
    def getCurrentFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getCurrentFile,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getDirectory,(self,) + _args, _kwargs)
        return val
    def setPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_setPattern,(self,) + _args, _kwargs)
        return val
    def getPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getPattern,(self,) + _args, _kwargs)
        return val
    def isItemDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_isItemDirectory,(self,) + _args, _kwargs)
        return val
    def isItemFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_isItemFile,(self,) + _args, _kwargs)
        return val
    def isItemExecutable(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_isItemExecutable,(self,) + _args, _kwargs)
        return val
    def getItemFilename(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getItemFilename,(self,) + _args, _kwargs)
        return val
    def getItemPathname(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getItemPathname,(self,) + _args, _kwargs)
        return val
    def getItemAssoc(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getItemAssoc,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def getMatchMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getMatchMode,(self,) + _args, _kwargs)
        return val
    def setMatchMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_setMatchMode,(self,) + _args, _kwargs)
        return val
    def showHiddenFiles(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FX_FileList_showHiddenFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FX_FileList_showHiddenFiles2,(self,) + _args, _kwargs)
            return val
    def showHiddenFiles2(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_showHiddenFiles2,(self,) + _args, _kwargs)
        return val
    def setAssociations(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_setAssociations,(self,) + _args, _kwargs)
        return val
    def getAssociations(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_getAssociations,(self,) + _args, _kwargs)
        if val: val = FX_FileDictPtr(val) 
        return val
    def showOnlyDirectories(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FX_FileList_showOnlyDirectories,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FX_FileList_showOnlyDirectories2,(self,) + _args, _kwargs)
            return val
    def showOnlyDirectories2(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileList_showOnlyDirectories2,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_FileList instance at %s>" % (self.this,)
class FX_FileList(FX_FileListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FileList,_args,_kwargs)
        self.thisown = 1




class FXFileListPtr(FX_FileListPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileList_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFileList instance at %s>" % (self.this,)
class FXFileList(FXFileListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFileList,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FileSelectorPtr(FX_PackerPtr):
    ID_FILEFILTER = dialogsc.FX_FileSelector_ID_FILEFILTER
    ID_ACCEPT = dialogsc.FX_FileSelector_ID_ACCEPT
    ID_FILELIST = dialogsc.FX_FileSelector_ID_FILELIST
    ID_DIRECTORY_UP = dialogsc.FX_FileSelector_ID_DIRECTORY_UP
    ID_DIRTREE = dialogsc.FX_FileSelector_ID_DIRTREE
    ID_HOME = dialogsc.FX_FileSelector_ID_HOME
    ID_WORK = dialogsc.FX_FileSelector_ID_WORK
    ID_BOOKMARK = dialogsc.FX_FileSelector_ID_BOOKMARK
    ID_VISIT = dialogsc.FX_FileSelector_ID_VISIT
    ID_NEW = dialogsc.FX_FileSelector_ID_NEW
    ID_DELETE = dialogsc.FX_FileSelector_ID_DELETE
    ID_MOVE = dialogsc.FX_FileSelector_ID_MOVE
    ID_COPY = dialogsc.FX_FileSelector_ID_COPY
    ID_LINK = dialogsc.FX_FileSelector_ID_LINK
    ID_LAST = dialogsc.FX_FileSelector_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdAccept(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdAccept,(self,) + _args, _kwargs)
        return val
    def onCmdFilter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdFilter,(self,) + _args, _kwargs)
        return val
    def onCmdItemDblClicked(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdItemDblClicked,(self,) + _args, _kwargs)
        return val
    def onCmdItemSelected(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdItemSelected,(self,) + _args, _kwargs)
        return val
    def onCmdItemDeselected(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdItemDeselected,(self,) + _args, _kwargs)
        return val
    def onCmdDirectoryUp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdDirectoryUp,(self,) + _args, _kwargs)
        return val
    def onUpdDirectoryUp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onUpdDirectoryUp,(self,) + _args, _kwargs)
        return val
    def onCmdDirTree(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdDirTree,(self,) + _args, _kwargs)
        return val
    def onCmdHome(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdHome,(self,) + _args, _kwargs)
        return val
    def onCmdWork(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdWork,(self,) + _args, _kwargs)
        return val
    def onCmdBookmark(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdBookmark,(self,) + _args, _kwargs)
        return val
    def onCmdVisit(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdVisit,(self,) + _args, _kwargs)
        return val
    def onCmdNew(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdNew,(self,) + _args, _kwargs)
        return val
    def onUpdNew(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onUpdNew,(self,) + _args, _kwargs)
        return val
    def onCmdMove(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdMove,(self,) + _args, _kwargs)
        return val
    def onCmdCopy(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdCopy,(self,) + _args, _kwargs)
        return val
    def onCmdLink(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdLink,(self,) + _args, _kwargs)
        return val
    def onCmdDelete(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onCmdDelete,(self,) + _args, _kwargs)
        return val
    def onUpdSelected(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onUpdSelected,(self,) + _args, _kwargs)
        return val
    def onPopupMenu(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_onPopupMenu,(self,) + _args, _kwargs)
        return val
    def acceptButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_acceptButton,(self,) + _args, _kwargs)
        return val
    def cancelButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_cancelButton,(self,) + _args, _kwargs)
        return val
    def setFilename(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setFilename,(self,) + _args, _kwargs)
        return val
    def getFilename(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getFilename,(self,) + _args, _kwargs)
        return val
    def getFilenames(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getFilenames,(self,) + _args, _kwargs)
        return val
    def setPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setPattern,(self,) + _args, _kwargs)
        return val
    def getPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getPattern,(self,) + _args, _kwargs)
        return val
    def setPatternList(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setPatternList,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getDirectory,(self,) + _args, _kwargs)
        return val
    def setCurrentPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setCurrentPattern,(self,) + _args, _kwargs)
        return val
    def getCurrentPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getCurrentPattern,(self,) + _args, _kwargs)
        return val
    def getPatternText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getPatternText,(self,) + _args, _kwargs)
        return val
    def setPatternText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setPatternText,(self,) + _args, _kwargs)
        return val
    def setItemSpace(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setItemSpace,(self,) + _args, _kwargs)
        return val
    def getItemSpace(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getItemSpace,(self,) + _args, _kwargs)
        return val
    def setFileBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setFileBoxStyle,(self,) + _args, _kwargs)
        return val
    def getFileBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getFileBoxStyle,(self,) + _args, _kwargs)
        return val
    def setSelectMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setSelectMode,(self,) + _args, _kwargs)
        return val
    def getSelectMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getSelectMode,(self,) + _args, _kwargs)
        return val
    def showReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_showReadOnly,(self,) + _args, _kwargs)
        return val
    def shownReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_shownReadOnly,(self,) + _args, _kwargs)
        return val
    def setReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_setReadOnly,(self,) + _args, _kwargs)
        return val
    def getReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileSelector_getReadOnly,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_FileSelector instance at %s>" % (self.this,)
class FX_FileSelector(FX_FileSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FileSelector,_args,_kwargs)
        self.thisown = 1




class FXFileSelectorPtr(FX_FileSelectorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileSelector_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFileSelector instance at %s>" % (self.this,)
class FXFileSelector(FXFileSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFileSelector,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FileDialogPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setFilename(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setFilename,(self,) + _args, _kwargs)
        return val
    def getFilename(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getFilename,(self,) + _args, _kwargs)
        return val
    def getFilenames(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getFilenames,(self,) + _args, _kwargs)
        return val
    def setPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setPattern,(self,) + _args, _kwargs)
        return val
    def getPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getPattern,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getDirectory,(self,) + _args, _kwargs)
        return val
    def setPatternList(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setPatternList,(self,) + _args, _kwargs)
        return val
    def setCurrentPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setCurrentPattern,(self,) + _args, _kwargs)
        return val
    def getCurrentPattern(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getCurrentPattern,(self,) + _args, _kwargs)
        return val
    def getPatternText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getPatternText,(self,) + _args, _kwargs)
        return val
    def setPatternText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setPatternText,(self,) + _args, _kwargs)
        return val
    def setItemSpace(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setItemSpace,(self,) + _args, _kwargs)
        return val
    def getItemSpace(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getItemSpace,(self,) + _args, _kwargs)
        return val
    def setFileBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setFileBoxStyle,(self,) + _args, _kwargs)
        return val
    def getFileBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getFileBoxStyle,(self,) + _args, _kwargs)
        return val
    def setSelectMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setSelectMode,(self,) + _args, _kwargs)
        return val
    def getSelectMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getSelectMode,(self,) + _args, _kwargs)
        return val
    def showReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_showReadOnly,(self,) + _args, _kwargs)
        return val
    def shownReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_shownReadOnly,(self,) + _args, _kwargs)
        return val
    def setReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_setReadOnly,(self,) + _args, _kwargs)
        return val
    def getReadOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDialog_getReadOnly,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_FileDialog instance at %s>" % (self.this,)
class FX_FileDialog(FX_FileDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FileDialog,_args,_kwargs)
        self.thisown = 1




class FXFileDialogPtr(FX_FileDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXFileDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXFileDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFileDialog instance at %s>" % (self.this,)
class FXFileDialog(FXFileDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFileDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ColorSelectorPtr(FX_PackerPtr):
    ID_CUSTOM_FIRST = dialogsc.FX_ColorSelector_ID_CUSTOM_FIRST
    ID_CUSTOM_LAST = dialogsc.FX_ColorSelector_ID_CUSTOM_LAST
    ID_RGB_RED_SLIDER = dialogsc.FX_ColorSelector_ID_RGB_RED_SLIDER
    ID_RGB_GREEN_SLIDER = dialogsc.FX_ColorSelector_ID_RGB_GREEN_SLIDER
    ID_RGB_BLUE_SLIDER = dialogsc.FX_ColorSelector_ID_RGB_BLUE_SLIDER
    ID_RGB_RED_TEXT = dialogsc.FX_ColorSelector_ID_RGB_RED_TEXT
    ID_RGB_GREEN_TEXT = dialogsc.FX_ColorSelector_ID_RGB_GREEN_TEXT
    ID_RGB_BLUE_TEXT = dialogsc.FX_ColorSelector_ID_RGB_BLUE_TEXT
    ID_HSV_HUE_SLIDER = dialogsc.FX_ColorSelector_ID_HSV_HUE_SLIDER
    ID_HSV_SATURATION_SLIDER = dialogsc.FX_ColorSelector_ID_HSV_SATURATION_SLIDER
    ID_HSV_VALUE_SLIDER = dialogsc.FX_ColorSelector_ID_HSV_VALUE_SLIDER
    ID_HSV_HUE_TEXT = dialogsc.FX_ColorSelector_ID_HSV_HUE_TEXT
    ID_HSV_SATURATION_TEXT = dialogsc.FX_ColorSelector_ID_HSV_SATURATION_TEXT
    ID_HSV_VALUE_TEXT = dialogsc.FX_ColorSelector_ID_HSV_VALUE_TEXT
    ID_CMY_CYAN_SLIDER = dialogsc.FX_ColorSelector_ID_CMY_CYAN_SLIDER
    ID_CMY_MAGENTA_SLIDER = dialogsc.FX_ColorSelector_ID_CMY_MAGENTA_SLIDER
    ID_CMY_YELLOW_SLIDER = dialogsc.FX_ColorSelector_ID_CMY_YELLOW_SLIDER
    ID_CMY_CYAN_TEXT = dialogsc.FX_ColorSelector_ID_CMY_CYAN_TEXT
    ID_CMY_MAGENTA_TEXT = dialogsc.FX_ColorSelector_ID_CMY_MAGENTA_TEXT
    ID_CMY_YELLOW_TEXT = dialogsc.FX_ColorSelector_ID_CMY_YELLOW_TEXT
    ID_DIAL_WHEEL = dialogsc.FX_ColorSelector_ID_DIAL_WHEEL
    ID_COLOR_BAR = dialogsc.FX_ColorSelector_ID_COLOR_BAR
    ID_COLOR_LIST = dialogsc.FX_ColorSelector_ID_COLOR_LIST
    ID_WELL_CHANGED = dialogsc.FX_ColorSelector_ID_WELL_CHANGED
    ID_COLOR = dialogsc.FX_ColorSelector_ID_COLOR
    ID_ACTIVEPANE = dialogsc.FX_ColorSelector_ID_ACTIVEPANE
    ID_ALPHA_SLIDER = dialogsc.FX_ColorSelector_ID_ALPHA_SLIDER
    ID_ALPHA_TEXT = dialogsc.FX_ColorSelector_ID_ALPHA_TEXT
    ID_ALPHA_LABEL = dialogsc.FX_ColorSelector_ID_ALPHA_LABEL
    ID_COLORPICK = dialogsc.FX_ColorSelector_ID_COLORPICK
    ID_LAST = dialogsc.FX_ColorSelector_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdColor,(self,) + _args, _kwargs)
        return val
    def onChgColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onChgColor,(self,) + _args, _kwargs)
        return val
    def onCmdWell(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdWell,(self,) + _args, _kwargs)
        return val
    def onChgWell(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onChgWell,(self,) + _args, _kwargs)
        return val
    def onCmdRGBSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdRGBSlider,(self,) + _args, _kwargs)
        return val
    def onUpdRGBSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdRGBSlider,(self,) + _args, _kwargs)
        return val
    def onCmdRGBText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdRGBText,(self,) + _args, _kwargs)
        return val
    def onUpdRGBText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdRGBText,(self,) + _args, _kwargs)
        return val
    def onCmdHSVSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdHSVSlider,(self,) + _args, _kwargs)
        return val
    def onUpdHSVSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdHSVSlider,(self,) + _args, _kwargs)
        return val
    def onCmdHSVText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdHSVText,(self,) + _args, _kwargs)
        return val
    def onUpdHSVText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdHSVText,(self,) + _args, _kwargs)
        return val
    def onCmdCMYSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdCMYSlider,(self,) + _args, _kwargs)
        return val
    def onUpdCMYSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdCMYSlider,(self,) + _args, _kwargs)
        return val
    def onCmdCMYText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdCMYText,(self,) + _args, _kwargs)
        return val
    def onUpdCMYText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdCMYText,(self,) + _args, _kwargs)
        return val
    def onCmdList(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdList,(self,) + _args, _kwargs)
        return val
    def onCmdCustomWell(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdCustomWell,(self,) + _args, _kwargs)
        return val
    def onChgCustomWell(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onChgCustomWell,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdActivePane(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdActivePane,(self,) + _args, _kwargs)
        return val
    def onCmdAlphaSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdAlphaSlider,(self,) + _args, _kwargs)
        return val
    def onUpdAlphaSlider(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdAlphaSlider,(self,) + _args, _kwargs)
        return val
    def onCmdAlphaText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdAlphaText,(self,) + _args, _kwargs)
        return val
    def onUpdAlphaText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdAlphaText,(self,) + _args, _kwargs)
        return val
    def onUpdAlphaLabel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdAlphaLabel,(self,) + _args, _kwargs)
        return val
    def onCmdWheel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdWheel,(self,) + _args, _kwargs)
        return val
    def onUpdWheel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdWheel,(self,) + _args, _kwargs)
        return val
    def onCmdBar(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdBar,(self,) + _args, _kwargs)
        return val
    def onUpdBar(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onUpdBar,(self,) + _args, _kwargs)
        return val
    def onCmdColorPick(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_onCmdColorPick,(self,) + _args, _kwargs)
        return val
    def acceptButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_acceptButton,(self,) + _args, _kwargs)
        return val
    def cancelButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_cancelButton,(self,) + _args, _kwargs)
        return val
    def setRGBA(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_setRGBA,(self,) + _args, _kwargs)
        return val
    def getRGBA(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_getRGBA,(self,) + _args, _kwargs)
        return val
    def isOpaqueOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_isOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def setOpaqueOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorSelector_setOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ColorSelector instance at %s>" % (self.this,)
class FX_ColorSelector(FX_ColorSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_ColorSelector,_args,_kwargs)
        self.thisown = 1




class FXColorSelectorPtr(FX_ColorSelectorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorSelector_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXColorSelector instance at %s>" % (self.this,)
class FXColorSelector(FXColorSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXColorSelector,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ColorDialogPtr(FX_DialogBoxPtr):
    ID_COLORSELECTOR = dialogsc.FX_ColorDialog_ID_COLORSELECTOR
    ID_LAST = dialogsc.FX_ColorDialog_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onChgColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_onChgColor,(self,) + _args, _kwargs)
        return val
    def onCmdColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_onCmdColor,(self,) + _args, _kwargs)
        return val
    def setRGBA(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_setRGBA,(self,) + _args, _kwargs)
        return val
    def getRGBA(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_getRGBA,(self,) + _args, _kwargs)
        return val
    def isOpaqueOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_isOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def setOpaqueOnly(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ColorDialog_setOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ColorDialog instance at %s>" % (self.this,)
class FX_ColorDialog(FX_ColorDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_ColorDialog,_args,_kwargs)
        self.thisown = 1




class FXColorDialogPtr(FX_ColorDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXColorDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXColorDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXColorDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXColorDialog instance at %s>" % (self.this,)
class FXColorDialog(FXColorDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXColorDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FontSelectorPtr(FX_PackerPtr):
    ID_FAMILY = dialogsc.FX_FontSelector_ID_FAMILY
    ID_WEIGHT = dialogsc.FX_FontSelector_ID_WEIGHT
    ID_STYLE = dialogsc.FX_FontSelector_ID_STYLE
    ID_STYLE_TEXT = dialogsc.FX_FontSelector_ID_STYLE_TEXT
    ID_SIZE = dialogsc.FX_FontSelector_ID_SIZE
    ID_SIZE_TEXT = dialogsc.FX_FontSelector_ID_SIZE_TEXT
    ID_CHARSET = dialogsc.FX_FontSelector_ID_CHARSET
    ID_SETWIDTH = dialogsc.FX_FontSelector_ID_SETWIDTH
    ID_PITCH = dialogsc.FX_FontSelector_ID_PITCH
    ID_SCALABLE = dialogsc.FX_FontSelector_ID_SCALABLE
    ID_ALLFONTS = dialogsc.FX_FontSelector_ID_ALLFONTS
    ID_LAST = dialogsc.FX_FontSelector_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdFamily(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdFamily,(self,) + _args, _kwargs)
        return val
    def onCmdWeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdWeight,(self,) + _args, _kwargs)
        return val
    def onCmdStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdStyle,(self,) + _args, _kwargs)
        return val
    def onCmdStyleText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdStyleText,(self,) + _args, _kwargs)
        return val
    def onCmdSize(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdSize,(self,) + _args, _kwargs)
        return val
    def onCmdSizeText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdSizeText,(self,) + _args, _kwargs)
        return val
    def onCmdCharset(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdCharset,(self,) + _args, _kwargs)
        return val
    def onUpdCharset(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onUpdCharset,(self,) + _args, _kwargs)
        return val
    def onCmdSetWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdSetWidth,(self,) + _args, _kwargs)
        return val
    def onUpdSetWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onUpdSetWidth,(self,) + _args, _kwargs)
        return val
    def onCmdPitch(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdPitch,(self,) + _args, _kwargs)
        return val
    def onUpdPitch(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onUpdPitch,(self,) + _args, _kwargs)
        return val
    def onCmdScalable(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdScalable,(self,) + _args, _kwargs)
        return val
    def onUpdScalable(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onUpdScalable,(self,) + _args, _kwargs)
        return val
    def onCmdAllFonts(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onCmdAllFonts,(self,) + _args, _kwargs)
        return val
    def onUpdAllFonts(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_onUpdAllFonts,(self,) + _args, _kwargs)
        return val
    def acceptButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_acceptButton,(self,) + _args, _kwargs)
        return val
    def cancelButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_cancelButton,(self,) + _args, _kwargs)
        return val
    def setFontSelection(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_setFontSelection,(self,) + _args, _kwargs)
        return val
    def getFontSelection(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontSelector_getFontSelection,(self,) + _args, _kwargs)
        if val: val = FXFontDescPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C FX_FontSelector instance at %s>" % (self.this,)
class FX_FontSelector(FX_FontSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FontSelector,_args,_kwargs)
        self.thisown = 1




class FXFontSelectorPtr(FX_FontSelectorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontSelector_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFontSelector instance at %s>" % (self.this,)
class FXFontSelector(FXFontSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFontSelector,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FontDialogPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setFontSelection(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontDialog_setFontSelection,(self,) + _args, _kwargs)
        return val
    def getFontSelection(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FontDialog_getFontSelection,(self,) + _args, _kwargs)
        if val: val = FXFontDescPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C FX_FontDialog instance at %s>" % (self.this,)
class FX_FontDialog(FX_FontDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FontDialog,_args,_kwargs)
        self.thisown = 1




class FXFontDialogPtr(FX_FontDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXFontDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXFontDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFontDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFontDialog instance at %s>" % (self.this,)
class FXFontDialog(FXFontDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFontDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DirSelectorPtr(FX_PackerPtr):
    ID_DIRNAME = dialogsc.FX_DirSelector_ID_DIRNAME
    ID_DIRLIST = dialogsc.FX_DirSelector_ID_DIRLIST
    ID_DRIVEBOX = dialogsc.FX_DirSelector_ID_DRIVEBOX
    ID_LAST = dialogsc.FX_DirSelector_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_onCmdName,(self,) + _args, _kwargs)
        return val
    def onCmdOpened(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_onCmdOpened,(self,) + _args, _kwargs)
        return val
    def onCmdDriveChanged(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_onCmdDriveChanged,(self,) + _args, _kwargs)
        return val
    def acceptButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_acceptButton,(self,) + _args, _kwargs)
        return val
    def cancelButton(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_cancelButton,(self,) + _args, _kwargs)
        return val
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_getDirectory,(self,) + _args, _kwargs)
        return val
    def setDirBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_setDirBoxStyle,(self,) + _args, _kwargs)
        return val
    def getDirBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirSelector_getDirBoxStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DirSelector instance at %s>" % (self.this,)
class FX_DirSelector(FX_DirSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_DirSelector,_args,_kwargs)
        self.thisown = 1




class FXDirSelectorPtr(FX_DirSelectorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirSelector_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDirSelector instance at %s>" % (self.this,)
class FXDirSelector(FXDirSelectorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXDirSelector,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DirDialogPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirDialog_setDirectory,(self,) + _args, _kwargs)
        return val
    def getDirectory(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirDialog_getDirectory,(self,) + _args, _kwargs)
        return val
    def setDirBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirDialog_setDirBoxStyle,(self,) + _args, _kwargs)
        return val
    def getDirBoxStyle(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_DirDialog_getDirBoxStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DirDialog instance at %s>" % (self.this,)
class FX_DirDialog(FX_DirDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_DirDialog,_args,_kwargs)
        self.thisown = 1




class FXDirDialogPtr(FX_DirDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXDirDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXDirDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXDirDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDirDialog instance at %s>" % (self.this,)
class FXDirDialog(FXDirDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXDirDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PrintDialogPtr(FX_DialogBoxPtr):
    ID_TO_PRINTER = dialogsc.FX_PrintDialog_ID_TO_PRINTER
    ID_TO_FILE = dialogsc.FX_PrintDialog_ID_TO_FILE
    ID_PRINTER_NAME = dialogsc.FX_PrintDialog_ID_PRINTER_NAME
    ID_FILE_NAME = dialogsc.FX_PrintDialog_ID_FILE_NAME
    ID_LANDSCAPE = dialogsc.FX_PrintDialog_ID_LANDSCAPE
    ID_PORTRAIT = dialogsc.FX_PrintDialog_ID_PORTRAIT
    ID_MEDIA = dialogsc.FX_PrintDialog_ID_MEDIA
    ID_COLLATE_NORMAL = dialogsc.FX_PrintDialog_ID_COLLATE_NORMAL
    ID_COLLATE_REVERSED = dialogsc.FX_PrintDialog_ID_COLLATE_REVERSED
    ID_PAGES_ALL = dialogsc.FX_PrintDialog_ID_PAGES_ALL
    ID_PAGES_EVEN = dialogsc.FX_PrintDialog_ID_PAGES_EVEN
    ID_PAGES_ODD = dialogsc.FX_PrintDialog_ID_PAGES_ODD
    ID_PAGES_RANGE = dialogsc.FX_PrintDialog_ID_PAGES_RANGE
    ID_PAGES_FIRST = dialogsc.FX_PrintDialog_ID_PAGES_FIRST
    ID_PAGES_LAST = dialogsc.FX_PrintDialog_ID_PAGES_LAST
    ID_BROWSE_FILE = dialogsc.FX_PrintDialog_ID_BROWSE_FILE
    ID_PROPERTIES = dialogsc.FX_PrintDialog_ID_PROPERTIES
    ID_COLOR_PRINTER = dialogsc.FX_PrintDialog_ID_COLOR_PRINTER
    ID_GRAY_PRINTER = dialogsc.FX_PrintDialog_ID_GRAY_PRINTER
    ID_NUM_COPIES = dialogsc.FX_PrintDialog_ID_NUM_COPIES
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdToPrinter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdToPrinter,(self,) + _args, _kwargs)
        return val
    def onUpdToPrinter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdToPrinter,(self,) + _args, _kwargs)
        return val
    def onCmdToFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdToFile,(self,) + _args, _kwargs)
        return val
    def onUpdToFile(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdToFile,(self,) + _args, _kwargs)
        return val
    def onCmdBrowse(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdBrowse,(self,) + _args, _kwargs)
        return val
    def onUpdBrowse(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdBrowse,(self,) + _args, _kwargs)
        return val
    def onCmdProps(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdProps,(self,) + _args, _kwargs)
        return val
    def onUpdProps(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdProps,(self,) + _args, _kwargs)
        return val
    def onCmdPortrait(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdPortrait,(self,) + _args, _kwargs)
        return val
    def onUpdPortrait(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdPortrait,(self,) + _args, _kwargs)
        return val
    def onCmdLandscape(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdLandscape,(self,) + _args, _kwargs)
        return val
    def onUpdLandscape(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdLandscape,(self,) + _args, _kwargs)
        return val
    def onCmdPages(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdPages,(self,) + _args, _kwargs)
        return val
    def onUpdPages(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdPages,(self,) + _args, _kwargs)
        return val
    def onCmdColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdColor,(self,) + _args, _kwargs)
        return val
    def onUpdColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdColor,(self,) + _args, _kwargs)
        return val
    def onCmdGray(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdGray,(self,) + _args, _kwargs)
        return val
    def onUpdGray(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdGray,(self,) + _args, _kwargs)
        return val
    def onCmdNumCopies(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdNumCopies,(self,) + _args, _kwargs)
        return val
    def onUpdNumCopies(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdNumCopies,(self,) + _args, _kwargs)
        return val
    def onCmdFirstPage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdFirstPage,(self,) + _args, _kwargs)
        return val
    def onUpdFirstPage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdFirstPage,(self,) + _args, _kwargs)
        return val
    def onCmdLastPage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdLastPage,(self,) + _args, _kwargs)
        return val
    def onUpdLastPage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdLastPage,(self,) + _args, _kwargs)
        return val
    def onCmdCollateNormal(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdCollateNormal,(self,) + _args, _kwargs)
        return val
    def onUpdCollateNormal(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdCollateNormal,(self,) + _args, _kwargs)
        return val
    def onCmdCollateReversed(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdCollateReversed,(self,) + _args, _kwargs)
        return val
    def onUpdCollateReversed(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdCollateReversed,(self,) + _args, _kwargs)
        return val
    def onCmdFileName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdFileName,(self,) + _args, _kwargs)
        return val
    def onUpdFileName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdFileName,(self,) + _args, _kwargs)
        return val
    def onCmdPrinterName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdPrinterName,(self,) + _args, _kwargs)
        return val
    def onUpdPrinterName(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdPrinterName,(self,) + _args, _kwargs)
        return val
    def onCmdAccept(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdAccept,(self,) + _args, _kwargs)
        return val
    def onCmdMedia(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onCmdMedia,(self,) + _args, _kwargs)
        return val
    def onUpdMedia(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_onUpdMedia,(self,) + _args, _kwargs)
        return val
    def setPrinter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_setPrinter,(self,) + _args, _kwargs)
        return val
    def getPrinter(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_PrintDialog_getPrinter,(self,) + _args, _kwargs)
        if val: val = FXPrinterPtr(val) ; val.thisown = 1
        return val
    def __del__(self,dialogsc=dialogsc):
        if self.thisown == 1 :
            dialogsc.delete_FX_PrintDialog(self)
    def __repr__(self):
        return "<C FX_PrintDialog instance at %s>" % (self.this,)
class FX_PrintDialog(FX_PrintDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_PrintDialog,_args,_kwargs)
        self.thisown = 1




class FXPrintDialogPtr(FX_PrintDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXPrintDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXPrintDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXPrintDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPrintDialog instance at %s>" % (self.this,)
class FXPrintDialog(FXPrintDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXPrintDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MessageBoxPtr(FX_DialogBoxPtr):
    ID_CLICKED_YES = dialogsc.FX_MessageBox_ID_CLICKED_YES
    ID_CLICKED_NO = dialogsc.FX_MessageBox_ID_CLICKED_NO
    ID_CLICKED_OK = dialogsc.FX_MessageBox_ID_CLICKED_OK
    ID_CLICKED_CANCEL = dialogsc.FX_MessageBox_ID_CLICKED_CANCEL
    ID_CLICKED_QUIT = dialogsc.FX_MessageBox_ID_CLICKED_QUIT
    ID_CLICKED_SAVE = dialogsc.FX_MessageBox_ID_CLICKED_SAVE
    ID_LAST = dialogsc.FX_MessageBox_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdClicked(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_MessageBox_onCmdClicked,(self,) + _args, _kwargs)
        return val
    def onCmdCancel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_MessageBox_onCmdCancel,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MessageBox instance at %s>" % (self.this,)
class FX_MessageBox(FX_MessageBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_MessageBox,_args,_kwargs)
        self.thisown = 1




class FXMessageBoxPtr(FX_MessageBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXMessageBox_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXMessageBox_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXMessageBox_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMessageBox instance at %s>" % (self.this,)
class FXMessageBox(FXMessageBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXMessageBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FXFileAssocPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "command" :
            dialogsc.FXFileAssoc_command_set(self,value)
            return
        if name == "extension" :
            dialogsc.FXFileAssoc_extension_set(self,value)
            return
        if name == "mimetype" :
            dialogsc.FXFileAssoc_mimetype_set(self,value)
            return
        if name == "bigicon" :
            dialogsc.FXFileAssoc_bigicon_set(self,value.this)
            return
        if name == "bigiconopen" :
            dialogsc.FXFileAssoc_bigiconopen_set(self,value.this)
            return
        if name == "miniicon" :
            dialogsc.FXFileAssoc_miniicon_set(self,value.this)
            return
        if name == "miniiconopen" :
            dialogsc.FXFileAssoc_miniiconopen_set(self,value.this)
            return
        if name == "dragtype" :
            dialogsc.FXFileAssoc_dragtype_set(self,value)
            return
        if name == "flags" :
            dialogsc.FXFileAssoc_flags_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "command" : 
            return dialogsc.FXFileAssoc_command_get(self)
        if name == "extension" : 
            return dialogsc.FXFileAssoc_extension_get(self)
        if name == "mimetype" : 
            return dialogsc.FXFileAssoc_mimetype_get(self)
        if name == "bigicon" : 
            return FX_IconPtr(dialogsc.FXFileAssoc_bigicon_get(self))
        if name == "bigiconopen" : 
            return FX_IconPtr(dialogsc.FXFileAssoc_bigiconopen_get(self))
        if name == "miniicon" : 
            return FX_IconPtr(dialogsc.FXFileAssoc_miniicon_get(self))
        if name == "miniiconopen" : 
            return FX_IconPtr(dialogsc.FXFileAssoc_miniiconopen_get(self))
        if name == "dragtype" : 
            return dialogsc.FXFileAssoc_dragtype_get(self)
        if name == "flags" : 
            return dialogsc.FXFileAssoc_flags_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXFileAssoc instance at %s>" % (self.this,)
class FXFileAssoc(FXFileAssocPtr):
    def __init__(self,this):
        self.this = this




class FX_IconDictPtr(FX_DictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getApp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_getApp,(self,) + _args, _kwargs)
        return val
    def setIconPath(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_setIconPath,(self,) + _args, _kwargs)
        return val
    def getIconPath(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_getIconPath,(self,) + _args, _kwargs)
        return val
    def insert(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_insert,(self,) + _args, _kwargs)
        return val
    def remove(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_remove,(self,) + _args, _kwargs)
        return val
    def find(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_IconDict_find,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_IconDict instance at %s>" % (self.this,)
class FX_IconDict(FX_IconDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_IconDict,_args,_kwargs)
        self.thisown = 1




class FXIconDictPtr(FX_IconDictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXIconDict_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXIconDict instance at %s>" % (self.this,)
class FXIconDict(FXIconDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXIconDict,_args,_kwargs)
        self.thisown = 1




class FX_FileDictPtr(FX_DictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getApp(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_getApp,(self,) + _args, _kwargs)
        return val
    def setIconPath(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_setIconPath,(self,) + _args, _kwargs)
        return val
    def getIconPath(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_getIconPath,(self,) + _args, _kwargs)
        return val
    def replace(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_replace,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def remove(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_remove,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def find(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_find,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def associate(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_associate,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def findFileBinding(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_findFileBinding,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def findDirBinding(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_findDirBinding,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def findExecBinding(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_FileDict_findExecBinding,(self,) + _args, _kwargs)
        if val: val = FXFileAssocPtr(val) 
        return val
    def __repr__(self):
        return "<C FX_FileDict instance at %s>" % (self.this,)
class FX_FileDict(FX_FileDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_FileDict,_args,_kwargs)
        self.thisown = 1




class FXFileDictPtr(FX_FileDictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXFileDict_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFileDict instance at %s>" % (self.this,)
class FXFileDict(FXFileDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXFileDict,_args,_kwargs)
        self.thisown = 1




class FX_ReplaceDialogPtr(FX_DialogBoxPtr):
    ID_NEXT = dialogsc.FX_ReplaceDialog_ID_NEXT
    ID_PREV = dialogsc.FX_ReplaceDialog_ID_PREV
    ID_SEARCH_UP = dialogsc.FX_ReplaceDialog_ID_SEARCH_UP
    ID_SEARCH_DN = dialogsc.FX_ReplaceDialog_ID_SEARCH_DN
    ID_REPLACE_UP = dialogsc.FX_ReplaceDialog_ID_REPLACE_UP
    ID_REPLACE_DN = dialogsc.FX_ReplaceDialog_ID_REPLACE_DN
    ID_ALL = dialogsc.FX_ReplaceDialog_ID_ALL
    ID_DIR = dialogsc.FX_ReplaceDialog_ID_DIR
    ID_SEARCH_TEXT = dialogsc.FX_ReplaceDialog_ID_SEARCH_TEXT
    ID_REPLACE_TEXT = dialogsc.FX_ReplaceDialog_ID_REPLACE_TEXT
    ID_MODE = dialogsc.FX_ReplaceDialog_ID_MODE
    ID_LAST = dialogsc.FX_ReplaceDialog_ID_LAST
    DONE = dialogsc.FX_ReplaceDialog_DONE
    SEARCH = dialogsc.FX_ReplaceDialog_SEARCH
    REPLACE = dialogsc.FX_ReplaceDialog_REPLACE
    SEARCH_NEXT = dialogsc.FX_ReplaceDialog_SEARCH_NEXT
    REPLACE_NEXT = dialogsc.FX_ReplaceDialog_REPLACE_NEXT
    REPLACE_ALL = dialogsc.FX_ReplaceDialog_REPLACE_ALL
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdAll(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdAll,(self,) + _args, _kwargs)
        return val
    def onCmdNext(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdNext,(self,) + _args, _kwargs)
        return val
    def onUpdDir(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onUpdDir,(self,) + _args, _kwargs)
        return val
    def onCmdDir(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdDir,(self,) + _args, _kwargs)
        return val
    def onUpdMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onUpdMode,(self,) + _args, _kwargs)
        return val
    def onCmdMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdMode,(self,) + _args, _kwargs)
        return val
    def onSearchKey(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onSearchKey,(self,) + _args, _kwargs)
        return val
    def onReplaceKey(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onReplaceKey,(self,) + _args, _kwargs)
        return val
    def onCmdSearchHist(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdSearchHist,(self,) + _args, _kwargs)
        return val
    def onCmdReplaceHist(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdReplaceHist,(self,) + _args, _kwargs)
        return val
    def onCmdAccept(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_onCmdAccept,(self,) + _args, _kwargs)
        return val
    def setSearchText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_setSearchText,(self,) + _args, _kwargs)
        return val
    def getSearchText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_getSearchText,(self,) + _args, _kwargs)
        return val
    def setReplaceText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_setReplaceText,(self,) + _args, _kwargs)
        return val
    def getReplaceText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_getReplaceText,(self,) + _args, _kwargs)
        return val
    def setSearchMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_setSearchMode,(self,) + _args, _kwargs)
        return val
    def getSearchMode(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ReplaceDialog_getSearchMode,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ReplaceDialog instance at %s>" % (self.this,)
class FX_ReplaceDialog(FX_ReplaceDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_ReplaceDialog,_args,_kwargs)
        self.thisown = 1




class FXReplaceDialogPtr(FX_ReplaceDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXReplaceDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXReplaceDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXReplaceDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXReplaceDialog instance at %s>" % (self.this,)
class FXReplaceDialog(FXReplaceDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXReplaceDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_SearchDialogPtr(FX_ReplaceDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_SearchDialog instance at %s>" % (self.this,)
class FX_SearchDialog(FX_SearchDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_SearchDialog,_args,_kwargs)
        self.thisown = 1




class FXSearchDialogPtr(FX_SearchDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXSearchDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXSearchDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXSearchDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXSearchDialog instance at %s>" % (self.this,)
class FXSearchDialog(FXSearchDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXSearchDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_InputDialogPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdAccept(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_onCmdAccept,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_setText,(self,) + _args, _kwargs)
        return val
    def setNumColumns(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_setNumColumns,(self,) + _args, _kwargs)
        return val
    def getNumColumns(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_getNumColumns,(self,) + _args, _kwargs)
        return val
    def setLimits(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_setLimits,(self,) + _args, _kwargs)
        return val
    def getLimits(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_getLimits,(self,) + _args, _kwargs)
        return val
    def execute(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_InputDialog_execute,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_InputDialog instance at %s>" % (self.this,)
class FX_InputDialog(FX_InputDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_InputDialog,_args,_kwargs)
        self.thisown = 1




class FXInputDialogPtr(FX_InputDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXInputDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXInputDialog_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXInputDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXInputDialog instance at %s>" % (self.this,)
class FXInputDialog(FXInputDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXInputDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ProgressDialogPtr(FX_DialogBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdCancel(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_onCmdCancel,(self,) + _args, _kwargs)
        return val
    def setMessage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_setMessage,(self,) + _args, _kwargs)
        return val
    def getMessage(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_getMessage,(self,) + _args, _kwargs)
        return val
    def setProgress(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_setProgress,(self,) + _args, _kwargs)
        return val
    def getProgress(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_getProgress,(self,) + _args, _kwargs)
        return val
    def setTotal(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_setTotal,(self,) + _args, _kwargs)
        return val
    def getTotal(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_getTotal,(self,) + _args, _kwargs)
        return val
    def increment(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_increment,(self,) + _args, _kwargs)
        return val
    def isCancelled(self, *_args, **_kwargs):
        val = apply(dialogsc.FX_ProgressDialog_isCancelled,(self,) + _args, _kwargs)
        return val
    def __del__(self,dialogsc=dialogsc):
        if self.thisown == 1 :
            dialogsc.delete_FX_ProgressDialog(self)
    def __repr__(self):
        return "<C FX_ProgressDialog instance at %s>" % (self.this,)
class FX_ProgressDialog(FX_ProgressDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FX_ProgressDialog,_args,_kwargs)
        self.thisown = 1




class FXProgressDialogPtr(FX_ProgressDialogPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(dialogsc.FXProgressDialog_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXProgressDialog instance at %s>" % (self.this,)
class FXProgressDialog(FXProgressDialogPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(dialogsc.new_FXProgressDialog,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateOwnedDialogBox(*_args, **_kwargs):
    val = apply(dialogsc.CreateOwnedDialogBox,_args,_kwargs)
    if val: val = FXDialogBoxPtr(val)
    return val

def CreateFreeDialogBox(*_args, **_kwargs):
    val = apply(dialogsc.CreateFreeDialogBox,_args,_kwargs)
    if val: val = FXDialogBoxPtr(val)
    return val

showModalErrorBox = dialogsc.showModalErrorBox

showModalWarningBox = dialogsc.showModalWarningBox

showModalQuestionBox = dialogsc.showModalQuestionBox

showModalInformationBox = dialogsc.showModalInformationBox

FX_FileDialog_getOpenFilename = dialogsc.FX_FileDialog_getOpenFilename

FX_FileDialog_getOpenFilenames = dialogsc.FX_FileDialog_getOpenFilenames

FX_FileDialog_getSaveFilename = dialogsc.FX_FileDialog_getSaveFilename

FX_FileDialog_getOpenDirectory = dialogsc.FX_FileDialog_getOpenDirectory

FX_InputDialog_getString = dialogsc.FX_InputDialog_getString

FX_InputDialog_getInteger = dialogsc.FX_InputDialog_getInteger

FX_InputDialog_getReal = dialogsc.FX_InputDialog_getReal



#-------------- VARIABLE WRAPPERS ------------------

FILELIST_SHOWHIDDEN = dialogsc.FILELIST_SHOWHIDDEN
FILELIST_SHOWDIRS = dialogsc.FILELIST_SHOWDIRS
FILELIST_NO_OWN_ASSOC = dialogsc.FILELIST_NO_OWN_ASSOC
SELECTFILE_ANY = dialogsc.SELECTFILE_ANY
SELECTFILE_EXISTING = dialogsc.SELECTFILE_EXISTING
SELECTFILE_MULTIPLE = dialogsc.SELECTFILE_MULTIPLE
SELECTFILE_DIRECTORY = dialogsc.SELECTFILE_DIRECTORY
MBOX_OK = dialogsc.MBOX_OK
MBOX_OK_CANCEL = dialogsc.MBOX_OK_CANCEL
MBOX_YES_NO = dialogsc.MBOX_YES_NO
MBOX_YES_NO_CANCEL = dialogsc.MBOX_YES_NO_CANCEL
MBOX_QUIT_CANCEL = dialogsc.MBOX_QUIT_CANCEL
MBOX_QUIT_SAVE_CANCEL = dialogsc.MBOX_QUIT_SAVE_CANCEL
MBOX_CLICKED_YES = dialogsc.MBOX_CLICKED_YES
MBOX_CLICKED_NO = dialogsc.MBOX_CLICKED_NO
MBOX_CLICKED_OK = dialogsc.MBOX_CLICKED_OK
MBOX_CLICKED_CANCEL = dialogsc.MBOX_CLICKED_CANCEL
MBOX_CLICKED_QUIT = dialogsc.MBOX_CLICKED_QUIT
MBOX_CLICKED_SAVE = dialogsc.MBOX_CLICKED_SAVE
INPUTDIALOG_STRING = dialogsc.INPUTDIALOG_STRING
INPUTDIALOG_INTEGER = dialogsc.INPUTDIALOG_INTEGER
INPUTDIALOG_REAL = dialogsc.INPUTDIALOG_REAL
INPUTDIALOG_PASSWORD = dialogsc.INPUTDIALOG_PASSWORD
