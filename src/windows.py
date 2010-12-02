# This file was created automatically by SWIG.
import windowsc

from misc import *
import fox
class FX_WindowPtr(FX_DrawablePtr):
    ID_NONE = windowsc.FX_Window_ID_NONE
    ID_HIDE = windowsc.FX_Window_ID_HIDE
    ID_SHOW = windowsc.FX_Window_ID_SHOW
    ID_TOGGLESHOWN = windowsc.FX_Window_ID_TOGGLESHOWN
    ID_LOWER = windowsc.FX_Window_ID_LOWER
    ID_RAISE = windowsc.FX_Window_ID_RAISE
    ID_DELETE = windowsc.FX_Window_ID_DELETE
    ID_DISABLE = windowsc.FX_Window_ID_DISABLE
    ID_ENABLE = windowsc.FX_Window_ID_ENABLE
    ID_UNCHECK = windowsc.FX_Window_ID_UNCHECK
    ID_CHECK = windowsc.FX_Window_ID_CHECK
    ID_UNKNOWN = windowsc.FX_Window_ID_UNKNOWN
    ID_UPDATE = windowsc.FX_Window_ID_UPDATE
    ID_AUTOSCROLL = windowsc.FX_Window_ID_AUTOSCROLL
    ID_HSCROLLED = windowsc.FX_Window_ID_HSCROLLED
    ID_VSCROLLED = windowsc.FX_Window_ID_VSCROLLED
    ID_SETVALUE = windowsc.FX_Window_ID_SETVALUE
    ID_SETINTVALUE = windowsc.FX_Window_ID_SETINTVALUE
    ID_SETREALVALUE = windowsc.FX_Window_ID_SETREALVALUE
    ID_SETSTRINGVALUE = windowsc.FX_Window_ID_SETSTRINGVALUE
    ID_SETINTRANGE = windowsc.FX_Window_ID_SETINTRANGE
    ID_SETREALRANGE = windowsc.FX_Window_ID_SETREALRANGE
    ID_GETINTVALUE = windowsc.FX_Window_ID_GETINTVALUE
    ID_GETREALVALUE = windowsc.FX_Window_ID_GETREALVALUE
    ID_GETSTRINGVALUE = windowsc.FX_Window_ID_GETSTRINGVALUE
    ID_GETINTRANGE = windowsc.FX_Window_ID_GETINTRANGE
    ID_GETREALRANGE = windowsc.FX_Window_ID_GETREALRANGE
    ID_QUERY_TIP = windowsc.FX_Window_ID_QUERY_TIP
    ID_QUERY_HELP = windowsc.FX_Window_ID_QUERY_HELP
    ID_QUERY_MENU = windowsc.FX_Window_ID_QUERY_MENU
    ID_HOTKEY = windowsc.FX_Window_ID_HOTKEY
    ID_ACCEL = windowsc.FX_Window_ID_ACCEL
    ID_UNPOST = windowsc.FX_Window_ID_UNPOST
    ID_POST = windowsc.FX_Window_ID_POST
    ID_MDI_TILEHORIZONTAL = windowsc.FX_Window_ID_MDI_TILEHORIZONTAL
    ID_MDI_TILEVERTICAL = windowsc.FX_Window_ID_MDI_TILEVERTICAL
    ID_MDI_CASCADE = windowsc.FX_Window_ID_MDI_CASCADE
    ID_MDI_MAXIMIZE = windowsc.FX_Window_ID_MDI_MAXIMIZE
    ID_MDI_MINIMIZE = windowsc.FX_Window_ID_MDI_MINIMIZE
    ID_MDI_RESTORE = windowsc.FX_Window_ID_MDI_RESTORE
    ID_MDI_CLOSE = windowsc.FX_Window_ID_MDI_CLOSE
    ID_MDI_WINDOW = windowsc.FX_Window_ID_MDI_WINDOW
    ID_MDI_MENUWINDOW = windowsc.FX_Window_ID_MDI_MENUWINDOW
    ID_MDI_MENUMINIMIZE = windowsc.FX_Window_ID_MDI_MENUMINIMIZE
    ID_MDI_MENURESTORE = windowsc.FX_Window_ID_MDI_MENURESTORE
    ID_MDI_MENUCLOSE = windowsc.FX_Window_ID_MDI_MENUCLOSE
    ID_MDI_NEXT = windowsc.FX_Window_ID_MDI_NEXT
    ID_MDI_PREV = windowsc.FX_Window_ID_MDI_PREV
    ID_CLOSE_DOCUMENT = windowsc.FX_Window_ID_CLOSE_DOCUMENT
    ID_CLOSE_ALL_DOCUMENTS = windowsc.FX_Window_ID_CLOSE_ALL_DOCUMENTS
    ID_LAST = windowsc.FX_Window_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onPaint,(self,) + _args, _kwargs)
        return val
    def onMap(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onMap,(self,) + _args, _kwargs)
        return val
    def onUnmap(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onUnmap,(self,) + _args, _kwargs)
        return val
    def onConfigure(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onConfigure,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onUpdate,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onMotion,(self,) + _args, _kwargs)
        return val
    def onMouseWheel(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onMouseWheel,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onLeave,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onBeginDrag(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onBeginDrag,(self,) + _args, _kwargs)
        return val
    def onEndDrag(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onEndDrag,(self,) + _args, _kwargs)
        return val
    def onDragged(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDragged,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onDestroy(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDestroy,(self,) + _args, _kwargs)
        return val
    def onFocusSelf(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onFocusSelf,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onSelectionLost(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onSelectionLost,(self,) + _args, _kwargs)
        return val
    def onSelectionGained(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onSelectionGained,(self,) + _args, _kwargs)
        return val
    def onSelectionRequest(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onSelectionRequest,(self,) + _args, _kwargs)
        return val
    def onClipboardLost(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onClipboardLost,(self,) + _args, _kwargs)
        return val
    def onClipboardGained(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onClipboardGained,(self,) + _args, _kwargs)
        return val
    def onClipboardRequest(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onClipboardRequest,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDRequest(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onDNDRequest,(self,) + _args, _kwargs)
        return val
    def onCmdShow(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdShow,(self,) + _args, _kwargs)
        return val
    def onCmdHide(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdHide,(self,) + _args, _kwargs)
        return val
    def onUpdToggleShown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onUpdToggleShown,(self,) + _args, _kwargs)
        return val
    def onCmdToggleShown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdToggleShown,(self,) + _args, _kwargs)
        return val
    def onCmdRaise(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdRaise,(self,) + _args, _kwargs)
        return val
    def onCmdLower(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdLower,(self,) + _args, _kwargs)
        return val
    def onCmdEnable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdEnable,(self,) + _args, _kwargs)
        return val
    def onCmdDisable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdDisable,(self,) + _args, _kwargs)
        return val
    def onCmdUpdate(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdUpdate,(self,) + _args, _kwargs)
        return val
    def onUpdYes(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onUpdYes,(self,) + _args, _kwargs)
        return val
    def onCmdDelete(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_onCmdDelete,(self,) + _args, _kwargs)
        return val
    def getParent(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getParent,(self,) + _args, _kwargs)
        return val
    def getOwner(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getOwner,(self,) + _args, _kwargs)
        return val
    def getShell(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getShell,(self,) + _args, _kwargs)
        return val
    def getRoot(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getRoot,(self,) + _args, _kwargs)
        return val
    def getNext(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getNext,(self,) + _args, _kwargs)
        return val
    def getPrev(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getPrev,(self,) + _args, _kwargs)
        return val
    def getFirst(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getFirst,(self,) + _args, _kwargs)
        return val
    def getLast(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getLast,(self,) + _args, _kwargs)
        return val
    def getFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getFocus,(self,) + _args, _kwargs)
        return val
    def setKey(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setKey,(self,) + _args, _kwargs)
        return val
    def getKey(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getKey,(self,) + _args, _kwargs)
        return val
    def setTarget(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setTarget,(self,) + _args, _kwargs)
        return val
    def getTarget(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getTarget,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def setSelector(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setSelector,(self,) + _args, _kwargs)
        return val
    def getSelector(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getSelector,(self,) + _args, _kwargs)
        return val
    def getX(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getX,(self,) + _args, _kwargs)
        return val
    def getY(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getY,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def setX(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setX,(self,) + _args, _kwargs)
        return val
    def setY(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setY,(self,) + _args, _kwargs)
        return val
    def setWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setWidth,(self,) + _args, _kwargs)
        return val
    def setHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setHeight,(self,) + _args, _kwargs)
        return val
    def setLayoutHints(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setLayoutHints,(self,) + _args, _kwargs)
        return val
    def getLayoutHints(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getLayoutHints,(self,) + _args, _kwargs)
        return val
    def getAccelTable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getAccelTable,(self,) + _args, _kwargs)
        if val: val = FX_AccelTablePtr(val) 
        return val
    def setAccelTable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setAccelTable,(self,) + _args, _kwargs)
        return val
    def addHotKey(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_addHotKey,(self,) + _args, _kwargs)
        return val
    def remHotKey(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_remHotKey,(self,) + _args, _kwargs)
        return val
    def isShell(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isShell,(self,) + _args, _kwargs)
        return val
    def isChildOf(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isChildOf,(self,) + _args, _kwargs)
        return val
    def containsChild(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_containsChild,(self,) + _args, _kwargs)
        return val
    def getChildAt(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getChildAt,(self,) + _args, _kwargs)
        return val
    def numChildren(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_numChildren,(self,) + _args, _kwargs)
        return val
    def indexOfChild(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_indexOfChild,(self,) + _args, _kwargs)
        return val
    def childAtIndex(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_childAtIndex,(self,) + _args, _kwargs)
        return val
    def setDefaultCursor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setDefaultCursor,(self,) + _args, _kwargs)
        return val
    def getDefaultCursor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getDefaultCursor,(self,) + _args, _kwargs)
        return val
    def setDragCursor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setDragCursor,(self,) + _args, _kwargs)
        return val
    def getDragCursor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getDragCursor,(self,) + _args, _kwargs)
        return val
    def getCursorPosition(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getCursorPosition,(self,) + _args, _kwargs)
        return val
    def setCursorPosition(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setCursorPosition,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_canFocus,(self,) + _args, _kwargs)
        return val
    def isEnabled(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isEnabled,(self,) + _args, _kwargs)
        return val
    def isActive(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isActive,(self,) + _args, _kwargs)
        return val
    def hasFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_hasFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setDefault,(self,) + _args, _kwargs)
        return val
    def isDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isDefault,(self,) + _args, _kwargs)
        return val
    def setInitial(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setInitial,(self,) + _args, _kwargs)
        return val
    def isInitial(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isInitial,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_disable,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_destroy,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_move,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_resize,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_position,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_recalc,(self,) + _args, _kwargs)
        return val
    def forceRefresh(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_forceRefresh,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_reparent,(self,) + _args, _kwargs)
        return val
    def scroll(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_scroll,(self,) + _args, _kwargs)
        return val
    def update2(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_update2,(self,) + _args, _kwargs)
        return val
    def update(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_Window_update,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_Window_update2,(self,) + _args, _kwargs)
            return val
    def repaint2(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_repaint2,(self,) + _args, _kwargs)
        return val
    def repaint(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_Window_repaint,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_Window_repaint2,(self,) + _args, _kwargs)
            return val
    def grab(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_grab,(self,) + _args, _kwargs)
        return val
    def ungrab(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_ungrab,(self,) + _args, _kwargs)
        return val
    def grabbed(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_grabbed,(self,) + _args, _kwargs)
        return val
    def grabKeyboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_grabKeyboard,(self,) + _args, _kwargs)
        return val
    def ungrabKeyboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_ungrabKeyboard,(self,) + _args, _kwargs)
        return val
    def grabbedKeyboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_grabbedKeyboard,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_hide,(self,) + _args, _kwargs)
        return val
    def shown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_shown,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isComposite,(self,) + _args, _kwargs)
        return val
    def underCursor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_underCursor,(self,) + _args, _kwargs)
        return val
    def hasSelection(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_hasSelection,(self,) + _args, _kwargs)
        return val
    def acquireSelection(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_acquireSelection,(self,) + _args, _kwargs)
        return val
    def releaseSelection(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_releaseSelection,(self,) + _args, _kwargs)
        return val
    def hasClipboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_hasClipboard,(self,) + _args, _kwargs)
        return val
    def acquireClipboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_acquireClipboard,(self,) + _args, _kwargs)
        return val
    def releaseClipboard(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_releaseClipboard,(self,) + _args, _kwargs)
        return val
    def dropEnable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_dropEnable,(self,) + _args, _kwargs)
        return val
    def dropDisable(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_dropDisable,(self,) + _args, _kwargs)
        return val
    def isDropEnabled(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isDropEnabled,(self,) + _args, _kwargs)
        return val
    def isDragging(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isDragging,(self,) + _args, _kwargs)
        return val
    def beginDrag(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_beginDrag,(self,) + _args, _kwargs)
        return val
    def handleDrag(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_handleDrag,(self,) + _args, _kwargs)
        return val
    def endDrag(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_endDrag,(self,) + _args, _kwargs)
        return val
    def isDropTarget(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_isDropTarget,(self,) + _args, _kwargs)
        return val
    def setDragRectangle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setDragRectangle,(self,) + _args, _kwargs)
        return val
    def clearDragRectangle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_clearDragRectangle,(self,) + _args, _kwargs)
        return val
    def acceptDrop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_acceptDrop,(self,) + _args, _kwargs)
        return val
    def didAccept(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_didAccept,(self,) + _args, _kwargs)
        return val
    def inquireDNDTypes(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_inquireDNDTypes,(self,) + _args, _kwargs)
        return val
    def offeredDNDType(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_offeredDNDType,(self,) + _args, _kwargs)
        return val
    def inquireDNDAction(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_inquireDNDAction,(self,) + _args, _kwargs)
        return val
    def setDNDData(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setDNDData,(self,) + _args, _kwargs)
        return val
    def getDNDData(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getDNDData,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_contains,(self,) + _args, _kwargs)
        return val
    def translateCoordinatesFrom(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_translateCoordinatesFrom,(self,) + _args, _kwargs)
        return val
    def translateCoordinatesTo(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_translateCoordinatesTo,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_setBackColor,(self,) + _args, _kwargs)
        return val
    def getBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_getBackColor,(self,) + _args, _kwargs)
        return val
    def linkBefore(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_linkBefore,(self,) + _args, _kwargs)
        return val
    def linkAfter(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_linkAfter,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Window_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Window instance at %s>" % (self.this,)
class FX_Window(FX_WindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_Window,_args,_kwargs)
        self.thisown = 1




class FXWindowPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXWindow_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXWindow instance at %s>" % (self.this,)
class FXWindow(FXWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXWindow,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CompositePtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onCmdUpdate(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_onCmdUpdate,(self,) + _args, _kwargs)
        return val
    def maxChildWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_maxChildWidth,(self,) + _args, _kwargs)
        return val
    def maxChildHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Composite_maxChildHeight,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Composite instance at %s>" % (self.this,)
class FX_Composite(FX_CompositePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_Composite,_args,_kwargs)
        self.thisown = 1




class FXCompositePtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXComposite_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXComposite instance at %s>" % (self.this,)
class FXComposite(FXCompositePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXComposite,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_FramePtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_onPaint,(self,) + _args, _kwargs)
        return val
    def setFrameStyle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setFrameStyle,(self,) + _args, _kwargs)
        return val
    def getFrameStyle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getFrameStyle,(self,) + _args, _kwargs)
        return val
    def getBorderWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getBorderWidth,(self,) + _args, _kwargs)
        return val
    def getPadTop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getPadTop,(self,) + _args, _kwargs)
        return val
    def getPadBottom(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getPadBottom,(self,) + _args, _kwargs)
        return val
    def getPadLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getPadLeft,(self,) + _args, _kwargs)
        return val
    def getPadRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getPadRight,(self,) + _args, _kwargs)
        return val
    def setPadTop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setPadTop,(self,) + _args, _kwargs)
        return val
    def setPadBottom(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setPadBottom,(self,) + _args, _kwargs)
        return val
    def setPadLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setPadLeft,(self,) + _args, _kwargs)
        return val
    def setPadRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setPadRight,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getShadowColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getBorderColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_getBaseColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setShadowColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setBorderColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Frame_setBaseColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Frame instance at %s>" % (self.this,)
class FX_Frame(FX_FramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_Frame,_args,_kwargs)
        self.thisown = 1




class FXFramePtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXFrame_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFrame instance at %s>" % (self.this,)
class FXFrame(FXFramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXFrame,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RootWindowPtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_RootWindow instance at %s>" % (self.this,)
class FX_RootWindow(FX_RootWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_RootWindow,_args,_kwargs)
        self.thisown = 1




class FXRootWindowPtr(FX_RootWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXRootWindow_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXRootWindow instance at %s>" % (self.this,)
class FXRootWindow(FXRootWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXRootWindow,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CanvasPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Canvas_onPaint,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Canvas_onMotion,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Canvas_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Canvas_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Canvas instance at %s>" % (self.this,)
class FX_Canvas(FX_CanvasPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_Canvas,_args,_kwargs)
        self.thisown = 1




class FXCanvasPtr(FX_CanvasPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXCanvas_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXCanvas instance at %s>" % (self.this,)
class FXCanvas(FXCanvasPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXCanvas,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ShellPtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onConfigure(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Shell_onConfigure,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Shell_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Shell_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Shell_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Shell_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Shell instance at %s>" % (self.this,)
class FX_Shell(FX_ShellPtr):
    def __init__(self,this):
        self.this = this




class FXShellPtr(FX_ShellPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXShell_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXShell instance at %s>" % (self.this,)
class FXShell(FXShellPtr):
    def __init__(self,this):
        self.this = this




class FX_PopupPtr(FX_ShellPtr):
    ID_CHOICE = windowsc.FX_Popup_ID_CHOICE
    ID_LAST = windowsc.FX_Popup_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusRight,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onLeave,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onMotion,(self,) + _args, _kwargs)
        return val
    def onMap(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onMap,(self,) + _args, _kwargs)
        return val
    def onButtonPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onButtonPress,(self,) + _args, _kwargs)
        return val
    def onButtonRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onButtonRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdChoice(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_onCmdChoice,(self,) + _args, _kwargs)
        return val
    def setFrameStyle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setFrameStyle,(self,) + _args, _kwargs)
        return val
    def getFrameStyle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getFrameStyle,(self,) + _args, _kwargs)
        return val
    def getBorderWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getBorderWidth,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setBorderColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getBorderColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setBaseColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getBaseColor,(self,) + _args, _kwargs)
        return val
    def popup(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_popup,(self,) + _args, _kwargs)
        return val
    def popdown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_popdown,(self,) + _args, _kwargs)
        return val
    def getGrabOwner(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getGrabOwner,(self,) + _args, _kwargs)
        return val
    def getOrientation(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getOrientation,(self,) + _args, _kwargs)
        return val
    def setOrientation(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setOrientation,(self,) + _args, _kwargs)
        return val
    def getShrinkWrap(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_getShrinkWrap,(self,) + _args, _kwargs)
        return val
    def setShrinkWrap(self, *_args, **_kwargs):
        val = apply(windowsc.FX_Popup_setShrinkWrap,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Popup instance at %s>" % (self.this,)
class FX_Popup(FX_PopupPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_Popup,_args,_kwargs)
        self.thisown = 1




class FXPopupPtr(FX_PopupPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_setBackColor,(self,) + _args, _kwargs)
        return val
    def popup(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_popup,(self,) + _args, _kwargs)
        return val
    def popdown(self, *_args, **_kwargs):
        val = apply(windowsc.FXPopup_popdown,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPopup instance at %s>" % (self.this,)
class FXPopup(FXPopupPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXPopup,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TopWindowPtr(FX_ShellPtr):
    ID_ICONIFY = windowsc.FX_TopWindow_ID_ICONIFY
    ID_DEICONIFY = windowsc.FX_TopWindow_ID_DEICONIFY
    ID_QUERY_DOCK = windowsc.FX_TopWindow_ID_QUERY_DOCK
    ID_LAST = windowsc.FX_TopWindow_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onClose(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onClose,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdIconify(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onCmdIconify,(self,) + _args, _kwargs)
        return val
    def onCmdDeiconify(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onCmdDeiconify,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_onFocusRight,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_show2,(self,) + _args, _kwargs)
        return val
    def place(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_place,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_deiconify,(self,) + _args, _kwargs)
        return val
    def isIconified(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_isIconified,(self,) + _args, _kwargs)
        return val
    def setTitle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setTitle,(self,) + _args, _kwargs)
        return val
    def getTitle(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getTitle,(self,) + _args, _kwargs)
        return val
    def setPadTop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setPadTop,(self,) + _args, _kwargs)
        return val
    def getPadTop(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getPadTop,(self,) + _args, _kwargs)
        return val
    def setPadBottom(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setPadBottom,(self,) + _args, _kwargs)
        return val
    def getPadBottom(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getPadBottom,(self,) + _args, _kwargs)
        return val
    def setPadLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setPadLeft,(self,) + _args, _kwargs)
        return val
    def getPadLeft(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getPadLeft,(self,) + _args, _kwargs)
        return val
    def setPadRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setPadRight,(self,) + _args, _kwargs)
        return val
    def getPadRight(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getPadRight,(self,) + _args, _kwargs)
        return val
    def getHSpacing(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getHSpacing,(self,) + _args, _kwargs)
        return val
    def getVSpacing(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getVSpacing,(self,) + _args, _kwargs)
        return val
    def setHSpacing(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setHSpacing,(self,) + _args, _kwargs)
        return val
    def setVSpacing(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setVSpacing,(self,) + _args, _kwargs)
        return val
    def setPackingHints(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setPackingHints,(self,) + _args, _kwargs)
        return val
    def getPackingHints(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getPackingHints,(self,) + _args, _kwargs)
        return val
    def setDecorations(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setDecorations,(self,) + _args, _kwargs)
        return val
    def getDecorations(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getDecorations,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getIcon,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setIcon,(self,) + _args, _kwargs)
        return val
    def getMiniIcon(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_getMiniIcon,(self,) + _args, _kwargs)
        return val
    def setMiniIcon(self, *_args, **_kwargs):
        val = apply(windowsc.FX_TopWindow_setMiniIcon,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TopWindow instance at %s>" % (self.this,)
class FX_TopWindow(FX_TopWindowPtr):
    def __init__(self,this):
        self.this = this




class FXTopWindowPtr(FX_TopWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_TopWindow_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_TopWindow_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(windowsc.FXTopWindow_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTopWindow instance at %s>" % (self.this,)
class FXTopWindow(FXTopWindowPtr):
    def __init__(self,this):
        self.this = this




class FX_MainWindowPtr(FX_TopWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onClose(self, *_args, **_kwargs):
        val = apply(windowsc.FX_MainWindow_onClose,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MainWindow instance at %s>" % (self.this,)
class FX_MainWindow(FX_MainWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FX_MainWindow,_args,_kwargs)
        self.thisown = 1




class FXMainWindowPtr(FX_MainWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FXMainWindow_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FXMainWindow_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(windowsc.FXMainWindow_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMainWindow instance at %s>" % (self.this,)
class FXMainWindow(FXMainWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(windowsc.new_FXMainWindow,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def FX_Window_commonAncestor(*_args, **_kwargs):
    val = apply(windowsc.FX_Window_commonAncestor,_args,_kwargs)
    return val



#-------------- VARIABLE WRAPPERS ------------------

POPUP_VERTICAL = windowsc.POPUP_VERTICAL
POPUP_HORIZONTAL = windowsc.POPUP_HORIZONTAL
POPUP_SHRINKWRAP = windowsc.POPUP_SHRINKWRAP
LAYOUT_NORMAL = windowsc.LAYOUT_NORMAL
LAYOUT_SIDE_TOP = windowsc.LAYOUT_SIDE_TOP
LAYOUT_SIDE_BOTTOM = windowsc.LAYOUT_SIDE_BOTTOM
LAYOUT_SIDE_LEFT = windowsc.LAYOUT_SIDE_LEFT
LAYOUT_SIDE_RIGHT = windowsc.LAYOUT_SIDE_RIGHT
LAYOUT_FILL_COLUMN = windowsc.LAYOUT_FILL_COLUMN
LAYOUT_FILL_ROW = windowsc.LAYOUT_FILL_ROW
LAYOUT_LEFT = windowsc.LAYOUT_LEFT
LAYOUT_RIGHT = windowsc.LAYOUT_RIGHT
LAYOUT_CENTER_X = windowsc.LAYOUT_CENTER_X
LAYOUT_FIX_X = windowsc.LAYOUT_FIX_X
LAYOUT_TOP = windowsc.LAYOUT_TOP
LAYOUT_BOTTOM = windowsc.LAYOUT_BOTTOM
LAYOUT_CENTER_Y = windowsc.LAYOUT_CENTER_Y
LAYOUT_FIX_Y = windowsc.LAYOUT_FIX_Y
LAYOUT_RESERVED_1 = windowsc.LAYOUT_RESERVED_1
LAYOUT_RESERVED_2 = windowsc.LAYOUT_RESERVED_2
LAYOUT_FIX_WIDTH = windowsc.LAYOUT_FIX_WIDTH
LAYOUT_FIX_HEIGHT = windowsc.LAYOUT_FIX_HEIGHT
LAYOUT_MIN_WIDTH = windowsc.LAYOUT_MIN_WIDTH
LAYOUT_MIN_HEIGHT = windowsc.LAYOUT_MIN_HEIGHT
LAYOUT_FILL_X = windowsc.LAYOUT_FILL_X
LAYOUT_FILL_Y = windowsc.LAYOUT_FILL_Y
LAYOUT_EXPLICIT = windowsc.LAYOUT_EXPLICIT
FRAME_NONE = windowsc.FRAME_NONE
FRAME_SUNKEN = windowsc.FRAME_SUNKEN
FRAME_RAISED = windowsc.FRAME_RAISED
FRAME_THICK = windowsc.FRAME_THICK
FRAME_GROOVE = windowsc.FRAME_GROOVE
FRAME_RIDGE = windowsc.FRAME_RIDGE
FRAME_LINE = windowsc.FRAME_LINE
FRAME_NORMAL = windowsc.FRAME_NORMAL
PACK_NORMAL = windowsc.PACK_NORMAL
PACK_UNIFORM_HEIGHT = windowsc.PACK_UNIFORM_HEIGHT
PACK_UNIFORM_WIDTH = windowsc.PACK_UNIFORM_WIDTH
DEFAULT_PAD = windowsc.DEFAULT_PAD
DECOR_NONE = windowsc.DECOR_NONE
DECOR_TITLE = windowsc.DECOR_TITLE
DECOR_MINIMIZE = windowsc.DECOR_MINIMIZE
DECOR_MAXIMIZE = windowsc.DECOR_MAXIMIZE
DECOR_CLOSE = windowsc.DECOR_CLOSE
DECOR_BORDER = windowsc.DECOR_BORDER
DECOR_RESIZE = windowsc.DECOR_RESIZE
DECOR_MENU = windowsc.DECOR_MENU
DECOR_ALL = windowsc.DECOR_ALL
PLACEMENT_DEFAULT = windowsc.PLACEMENT_DEFAULT
PLACEMENT_VISIBLE = windowsc.PLACEMENT_VISIBLE
PLACEMENT_CURSOR = windowsc.PLACEMENT_CURSOR
PLACEMENT_OWNER = windowsc.PLACEMENT_OWNER
PLACEMENT_SCREEN = windowsc.PLACEMENT_SCREEN
PLACEMENT_MAXIMIZED = windowsc.PLACEMENT_MAXIMIZED
cvar = windowsc.cvar
