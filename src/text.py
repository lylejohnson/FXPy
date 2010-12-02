# This file was created automatically by SWIG.
import textc

from misc import *

from windows import *

from containers import *
import fox
class FX_CharsetPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def has(self, *_args, **_kwargs):
        val = apply(textc.FX_Charset_has,(self,) + _args, _kwargs)
        return val
    def clear(self, *_args, **_kwargs):
        val = apply(textc.FX_Charset_clear,(self,) + _args, _kwargs)
        if val: val = FX_CharsetPtr(val) 
        return val
    def __repr__(self):
        return "<C FX_Charset instance at %s>" % (self.this,)
class FX_Charset(FX_CharsetPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(textc.new_FX_Charset,_args,_kwargs)
        self.thisown = 1




class FXHiliteStylePtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "normalForeColor" :
            textc.FXHiliteStyle_normalForeColor_set(self,value)
            return
        if name == "normalBackColor" :
            textc.FXHiliteStyle_normalBackColor_set(self,value)
            return
        if name == "selectForeColor" :
            textc.FXHiliteStyle_selectForeColor_set(self,value)
            return
        if name == "selectBackColor" :
            textc.FXHiliteStyle_selectBackColor_set(self,value)
            return
        if name == "hiliteForeColor" :
            textc.FXHiliteStyle_hiliteForeColor_set(self,value)
            return
        if name == "hiliteBackColor" :
            textc.FXHiliteStyle_hiliteBackColor_set(self,value)
            return
        if name == "activeBackColor" :
            textc.FXHiliteStyle_activeBackColor_set(self,value)
            return
        if name == "style" :
            textc.FXHiliteStyle_style_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "normalForeColor" : 
            return textc.FXHiliteStyle_normalForeColor_get(self)
        if name == "normalBackColor" : 
            return textc.FXHiliteStyle_normalBackColor_get(self)
        if name == "selectForeColor" : 
            return textc.FXHiliteStyle_selectForeColor_get(self)
        if name == "selectBackColor" : 
            return textc.FXHiliteStyle_selectBackColor_get(self)
        if name == "hiliteForeColor" : 
            return textc.FXHiliteStyle_hiliteForeColor_get(self)
        if name == "hiliteBackColor" : 
            return textc.FXHiliteStyle_hiliteBackColor_get(self)
        if name == "activeBackColor" : 
            return textc.FXHiliteStyle_activeBackColor_get(self)
        if name == "style" : 
            return textc.FXHiliteStyle_style_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXHiliteStyle instance at %s>" % (self.this,)
class FXHiliteStyle(FXHiliteStylePtr):
    def __init__(self,this):
        self.this = this




class FX_TextPtr(FX_ScrollAreaPtr):
    STYLE_UNDERLINE = textc.FX_Text_STYLE_UNDERLINE
    STYLE_STRIKEOUT = textc.FX_Text_STYLE_STRIKEOUT
    ID_CURSOR_TOP = textc.FX_Text_ID_CURSOR_TOP
    ID_CURSOR_BOTTOM = textc.FX_Text_ID_CURSOR_BOTTOM
    ID_CURSOR_HOME = textc.FX_Text_ID_CURSOR_HOME
    ID_CURSOR_END = textc.FX_Text_ID_CURSOR_END
    ID_CURSOR_RIGHT = textc.FX_Text_ID_CURSOR_RIGHT
    ID_CURSOR_LEFT = textc.FX_Text_ID_CURSOR_LEFT
    ID_CURSOR_UP = textc.FX_Text_ID_CURSOR_UP
    ID_CURSOR_DOWN = textc.FX_Text_ID_CURSOR_DOWN
    ID_CURSOR_WORD_LEFT = textc.FX_Text_ID_CURSOR_WORD_LEFT
    ID_CURSOR_WORD_RIGHT = textc.FX_Text_ID_CURSOR_WORD_RIGHT
    ID_CURSOR_PAGEDOWN = textc.FX_Text_ID_CURSOR_PAGEDOWN
    ID_CURSOR_PAGEUP = textc.FX_Text_ID_CURSOR_PAGEUP
    ID_CURSOR_SCRNTOP = textc.FX_Text_ID_CURSOR_SCRNTOP
    ID_CURSOR_SCRNBTM = textc.FX_Text_ID_CURSOR_SCRNBTM
    ID_CURSOR_SCRNCTR = textc.FX_Text_ID_CURSOR_SCRNCTR
    ID_CURSOR_PAR_HOME = textc.FX_Text_ID_CURSOR_PAR_HOME
    ID_CURSOR_PAR_END = textc.FX_Text_ID_CURSOR_PAR_END
    ID_SCROLL_UP = textc.FX_Text_ID_SCROLL_UP
    ID_SCROLL_DOWN = textc.FX_Text_ID_SCROLL_DOWN
    ID_MARK = textc.FX_Text_ID_MARK
    ID_EXTEND = textc.FX_Text_ID_EXTEND
    ID_OVERST_STRING = textc.FX_Text_ID_OVERST_STRING
    ID_INSERT_STRING = textc.FX_Text_ID_INSERT_STRING
    ID_INSERT_NEWLINE = textc.FX_Text_ID_INSERT_NEWLINE
    ID_INSERT_TAB = textc.FX_Text_ID_INSERT_TAB
    ID_CUT_SEL = textc.FX_Text_ID_CUT_SEL
    ID_COPY_SEL = textc.FX_Text_ID_COPY_SEL
    ID_PASTE_SEL = textc.FX_Text_ID_PASTE_SEL
    ID_DELETE_SEL = textc.FX_Text_ID_DELETE_SEL
    ID_SELECT_CHAR = textc.FX_Text_ID_SELECT_CHAR
    ID_SELECT_WORD = textc.FX_Text_ID_SELECT_WORD
    ID_SELECT_LINE = textc.FX_Text_ID_SELECT_LINE
    ID_SELECT_ALL = textc.FX_Text_ID_SELECT_ALL
    ID_SELECT_MATCHING = textc.FX_Text_ID_SELECT_MATCHING
    ID_SELECT_BRACE = textc.FX_Text_ID_SELECT_BRACE
    ID_SELECT_BRACK = textc.FX_Text_ID_SELECT_BRACK
    ID_SELECT_PAREN = textc.FX_Text_ID_SELECT_PAREN
    ID_SELECT_ANG = textc.FX_Text_ID_SELECT_ANG
    ID_DESELECT_ALL = textc.FX_Text_ID_DESELECT_ALL
    ID_BACKSPACE = textc.FX_Text_ID_BACKSPACE
    ID_BACKSPACE_WORD = textc.FX_Text_ID_BACKSPACE_WORD
    ID_BACKSPACE_BOL = textc.FX_Text_ID_BACKSPACE_BOL
    ID_DELETE = textc.FX_Text_ID_DELETE
    ID_DELETE_WORD = textc.FX_Text_ID_DELETE_WORD
    ID_DELETE_EOL = textc.FX_Text_ID_DELETE_EOL
    ID_DELETE_LINE = textc.FX_Text_ID_DELETE_LINE
    ID_TOGGLE_EDITABLE = textc.FX_Text_ID_TOGGLE_EDITABLE
    ID_TOGGLE_OVERSTRIKE = textc.FX_Text_ID_TOGGLE_OVERSTRIKE
    ID_CURSOR_ROW = textc.FX_Text_ID_CURSOR_ROW
    ID_CURSOR_COLUMN = textc.FX_Text_ID_CURSOR_COLUMN
    ID_CLEAN_INDENT = textc.FX_Text_ID_CLEAN_INDENT
    ID_SHIFT_LEFT = textc.FX_Text_ID_SHIFT_LEFT
    ID_SHIFT_RIGHT = textc.FX_Text_ID_SHIFT_RIGHT
    ID_SHIFT_TABLEFT = textc.FX_Text_ID_SHIFT_TABLEFT
    ID_SHIFT_TABRIGHT = textc.FX_Text_ID_SHIFT_TABRIGHT
    ID_UPPER_CASE = textc.FX_Text_ID_UPPER_CASE
    ID_LOWER_CASE = textc.FX_Text_ID_LOWER_CASE
    ID_GOTO_MATCHING = textc.FX_Text_ID_GOTO_MATCHING
    ID_GOTO_SELECTED = textc.FX_Text_ID_GOTO_SELECTED
    ID_GOTO_LINE = textc.FX_Text_ID_GOTO_LINE
    ID_SEARCH_FORW_SEL = textc.FX_Text_ID_SEARCH_FORW_SEL
    ID_SEARCH_BACK_SEL = textc.FX_Text_ID_SEARCH_BACK_SEL
    ID_SEARCH = textc.FX_Text_ID_SEARCH
    ID_REPLACE = textc.FX_Text_ID_REPLACE
    ID_LEFT_BRACE = textc.FX_Text_ID_LEFT_BRACE
    ID_LEFT_BRACK = textc.FX_Text_ID_LEFT_BRACK
    ID_LEFT_PAREN = textc.FX_Text_ID_LEFT_PAREN
    ID_LEFT_ANG = textc.FX_Text_ID_LEFT_ANG
    ID_RIGHT_BRACE = textc.FX_Text_ID_RIGHT_BRACE
    ID_RIGHT_BRACK = textc.FX_Text_ID_RIGHT_BRACK
    ID_RIGHT_PAREN = textc.FX_Text_ID_RIGHT_PAREN
    ID_RIGHT_ANG = textc.FX_Text_ID_RIGHT_ANG
    ID_BLINK = textc.FX_Text_ID_BLINK
    ID_FLASH = textc.FX_Text_ID_FLASH
    ID_LAST = textc.FX_Text_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdate,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onMotion,(self,) + _args, _kwargs)
        return val
    def onBeginDrag(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onBeginDrag,(self,) + _args, _kwargs)
        return val
    def onEndDrag(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onEndDrag,(self,) + _args, _kwargs)
        return val
    def onDragged(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDragged,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDRequest(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onDNDRequest,(self,) + _args, _kwargs)
        return val
    def onSelectionLost(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onSelectionLost,(self,) + _args, _kwargs)
        return val
    def onSelectionGained(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onSelectionGained,(self,) + _args, _kwargs)
        return val
    def onSelectionRequest(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onSelectionRequest,(self,) + _args, _kwargs)
        return val
    def onClipboardLost(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onClipboardLost,(self,) + _args, _kwargs)
        return val
    def onClipboardGained(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onClipboardGained,(self,) + _args, _kwargs)
        return val
    def onClipboardRequest(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onClipboardRequest,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onBlink(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onBlink,(self,) + _args, _kwargs)
        return val
    def onFlash(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onFlash,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdToggleEditable(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdToggleEditable,(self,) + _args, _kwargs)
        return val
    def onUpdToggleEditable(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdToggleEditable,(self,) + _args, _kwargs)
        return val
    def onCmdToggleOverstrike(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdToggleOverstrike,(self,) + _args, _kwargs)
        return val
    def onUpdToggleOverstrike(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdToggleOverstrike,(self,) + _args, _kwargs)
        return val
    def onCmdCursorRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorRow,(self,) + _args, _kwargs)
        return val
    def onUpdCursorRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdCursorRow,(self,) + _args, _kwargs)
        return val
    def onCmdCursorColumn(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorColumn,(self,) + _args, _kwargs)
        return val
    def onUpdCursorColumn(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdCursorColumn,(self,) + _args, _kwargs)
        return val
    def onUpdHaveSelection(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onUpdHaveSelection,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSearchSel(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSearchSel,(self,) + _args, _kwargs)
        return val
    def onCmdSearch(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSearch,(self,) + _args, _kwargs)
        return val
    def onCmdReplace(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdReplace,(self,) + _args, _kwargs)
        return val
    def onCmdCursorTop(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorTop,(self,) + _args, _kwargs)
        return val
    def onCmdCursorBottom(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorBottom,(self,) + _args, _kwargs)
        return val
    def onCmdCursorHome(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorHome,(self,) + _args, _kwargs)
        return val
    def onCmdCursorEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorEnd,(self,) + _args, _kwargs)
        return val
    def onCmdCursorRight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorRight,(self,) + _args, _kwargs)
        return val
    def onCmdCursorLeft(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorLeft,(self,) + _args, _kwargs)
        return val
    def onCmdCursorUp(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorUp,(self,) + _args, _kwargs)
        return val
    def onCmdCursorDown(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorDown,(self,) + _args, _kwargs)
        return val
    def onCmdCursorWordLeft(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorWordLeft,(self,) + _args, _kwargs)
        return val
    def onCmdCursorWordRight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorWordRight,(self,) + _args, _kwargs)
        return val
    def onCmdCursorPageDown(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorPageDown,(self,) + _args, _kwargs)
        return val
    def onCmdCursorPageUp(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorPageUp,(self,) + _args, _kwargs)
        return val
    def onCmdCursorScreenTop(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorScreenTop,(self,) + _args, _kwargs)
        return val
    def onCmdCursorScreenBottom(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorScreenBottom,(self,) + _args, _kwargs)
        return val
    def onCmdCursorScreenCenter(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorScreenCenter,(self,) + _args, _kwargs)
        return val
    def onCmdCursorParHome(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorParHome,(self,) + _args, _kwargs)
        return val
    def onCmdCursorParEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCursorParEnd,(self,) + _args, _kwargs)
        return val
    def onCmdBlockBeg(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdBlockBeg,(self,) + _args, _kwargs)
        return val
    def onCmdBlockEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdBlockEnd,(self,) + _args, _kwargs)
        return val
    def onCmdGotoMatching(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdGotoMatching,(self,) + _args, _kwargs)
        return val
    def onCmdGotoSelected(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdGotoSelected,(self,) + _args, _kwargs)
        return val
    def onCmdGotoLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdGotoLine,(self,) + _args, _kwargs)
        return val
    def onCmdScrollUp(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdScrollUp,(self,) + _args, _kwargs)
        return val
    def onCmdScrollDown(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdScrollDown,(self,) + _args, _kwargs)
        return val
    def onCmdMark(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdMark,(self,) + _args, _kwargs)
        return val
    def onCmdExtend(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdExtend,(self,) + _args, _kwargs)
        return val
    def onCmdOverstString(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdOverstString,(self,) + _args, _kwargs)
        return val
    def onCmdInsertString(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdInsertString,(self,) + _args, _kwargs)
        return val
    def onCmdInsertNewline(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdInsertNewline,(self,) + _args, _kwargs)
        return val
    def onCmdInsertTab(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdInsertTab,(self,) + _args, _kwargs)
        return val
    def onCmdCutSel(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCutSel,(self,) + _args, _kwargs)
        return val
    def onCmdCopySel(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdCopySel,(self,) + _args, _kwargs)
        return val
    def onCmdPasteSel(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdPasteSel,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteSel(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDeleteSel,(self,) + _args, _kwargs)
        return val
    def onCmdChangeCase(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdChangeCase,(self,) + _args, _kwargs)
        return val
    def onCmdShiftText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdShiftText,(self,) + _args, _kwargs)
        return val
    def onCmdSelectChar(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectChar,(self,) + _args, _kwargs)
        return val
    def onCmdSelectWord(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectWord,(self,) + _args, _kwargs)
        return val
    def onCmdSelectLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectLine,(self,) + _args, _kwargs)
        return val
    def onCmdSelectAll(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectAll,(self,) + _args, _kwargs)
        return val
    def onCmdSelectMatching(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectMatching,(self,) + _args, _kwargs)
        return val
    def onCmdSelectBlock(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdSelectBlock,(self,) + _args, _kwargs)
        return val
    def onCmdDeselectAll(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDeselectAll,(self,) + _args, _kwargs)
        return val
    def onCmdBackspace(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdBackspace,(self,) + _args, _kwargs)
        return val
    def onCmdBackspaceWord(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdBackspaceWord,(self,) + _args, _kwargs)
        return val
    def onCmdBackspaceBol(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdBackspaceBol,(self,) + _args, _kwargs)
        return val
    def onCmdDelete(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDelete,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteWord(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDeleteWord,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteEol(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDeleteEol,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_onCmdDeleteLine,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_moveContents,(self,) + _args, _kwargs)
        return val
    def setMarginTop(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setMarginTop,(self,) + _args, _kwargs)
        return val
    def getMarginTop(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getMarginTop,(self,) + _args, _kwargs)
        return val
    def setMarginBottom(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setMarginBottom,(self,) + _args, _kwargs)
        return val
    def getMarginBottom(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getMarginBottom,(self,) + _args, _kwargs)
        return val
    def setMarginLeft(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setMarginLeft,(self,) + _args, _kwargs)
        return val
    def getMarginLeft(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getMarginLeft,(self,) + _args, _kwargs)
        return val
    def setMarginRight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setMarginRight,(self,) + _args, _kwargs)
        return val
    def getMarginRight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getMarginRight,(self,) + _args, _kwargs)
        return val
    def getWrapColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getWrapColumns,(self,) + _args, _kwargs)
        return val
    def setWrapColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setWrapColumns,(self,) + _args, _kwargs)
        return val
    def getTabColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getTabColumns,(self,) + _args, _kwargs)
        return val
    def setTabColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setTabColumns,(self,) + _args, _kwargs)
        return val
    def getBarColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getBarColumns,(self,) + _args, _kwargs)
        return val
    def setBarColumns(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setBarColumns,(self,) + _args, _kwargs)
        return val
    def isModified(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_isModified,(self,) + _args, _kwargs)
        return val
    def setModified(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setModified,(self,) + _args, _kwargs)
        return val
    def isEditable(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_isEditable,(self,) + _args, _kwargs)
        return val
    def setEditable(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setEditable,(self,) + _args, _kwargs)
        return val
    def setStyled(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setStyled,(self,) + _args, _kwargs)
        return val
    def isStyled(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_isStyled,(self,) + _args, _kwargs)
        return val
    def setDelimiters(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setDelimiters,(self,) + _args, _kwargs)
        return val
    def getDelimiters(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getDelimiters,(self,) + _args, _kwargs)
        if val: val = FX_CharsetPtr(val) ; val.thisown = 1
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getFont,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getTextColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setHiliteTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHiliteTextColor,(self,) + _args, _kwargs)
        return val
    def getHiliteTextColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getHiliteTextColor,(self,) + _args, _kwargs)
        return val
    def setHiliteBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHiliteBackColor,(self,) + _args, _kwargs)
        return val
    def getHiliteBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getHiliteBackColor,(self,) + _args, _kwargs)
        return val
    def setActiveBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setActiveBackColor,(self,) + _args, _kwargs)
        return val
    def getActiveBackColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getActiveBackColor,(self,) + _args, _kwargs)
        return val
    def setCursorColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setCursorColor,(self,) + _args, _kwargs)
        return val
    def getCursorColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getCursorColor,(self,) + _args, _kwargs)
        return val
    def setNumberColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setNumberColor,(self,) + _args, _kwargs)
        return val
    def getNumberColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getNumberColor,(self,) + _args, _kwargs)
        return val
    def setBarColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setBarColor,(self,) + _args, _kwargs)
        return val
    def getBarColor(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getBarColor,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getTipText,(self,) + _args, _kwargs)
        return val
    def getChar(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getChar,(self,) + _args, _kwargs)
        return val
    def getStyle(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getStyle,(self,) + _args, _kwargs)
        return val
    def extractText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_extractText,(self,) + _args, _kwargs)
        return val
    def extractStyle(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_extractStyle,(self,) + _args, _kwargs)
        return val
    def replaceText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_replaceText,(self,) + _args, _kwargs)
        return val
    def replaceStyledText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_replaceStyledText,(self,) + _args, _kwargs)
        return val
    def appendText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_appendText,(self,) + _args, _kwargs)
        return val
    def appendStyledText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_appendStyledText,(self,) + _args, _kwargs)
        return val
    def insertText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_insertText,(self,) + _args, _kwargs)
        return val
    def insertStyledText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_insertStyledText,(self,) + _args, _kwargs)
        return val
    def removeText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_removeText,(self,) + _args, _kwargs)
        return val
    def changeStyle(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_changeStyle,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setText,(self,) + _args, _kwargs)
        return val
    def setStyledText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setStyledText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getText,(self,) + _args, _kwargs)
        return val
    def getLength(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getLength,(self,) + _args, _kwargs)
        return val
    def shiftText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_shiftText,(self,) + _args, _kwargs)
        return val
    def findText(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_findText,(self,) + _args, _kwargs)
        return val
    def isPosSelected(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_isPosSelected,(self,) + _args, _kwargs)
        return val
    def isPosVisible(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_isPosVisible,(self,) + _args, _kwargs)
        return val
    def getPosAt(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getPosAt,(self,) + _args, _kwargs)
        return val
    def lineStart(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_lineStart,(self,) + _args, _kwargs)
        return val
    def lineEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_lineEnd,(self,) + _args, _kwargs)
        return val
    def nextLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_nextLine,(self,) + _args, _kwargs)
        return val
    def prevLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_prevLine,(self,) + _args, _kwargs)
        return val
    def rowStart(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_rowStart,(self,) + _args, _kwargs)
        return val
    def rowEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_rowEnd,(self,) + _args, _kwargs)
        return val
    def nextRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_nextRow,(self,) + _args, _kwargs)
        return val
    def prevRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_prevRow,(self,) + _args, _kwargs)
        return val
    def leftWord(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_leftWord,(self,) + _args, _kwargs)
        return val
    def rightWord(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_rightWord,(self,) + _args, _kwargs)
        return val
    def wordStart(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_wordStart,(self,) + _args, _kwargs)
        return val
    def wordEnd(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_wordEnd,(self,) + _args, _kwargs)
        return val
    def validPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_validPos,(self,) + _args, _kwargs)
        return val
    def setTopLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setTopLine,(self,) + _args, _kwargs)
        return val
    def getTopLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getTopLine,(self,) + _args, _kwargs)
        return val
    def setBottomLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setBottomLine,(self,) + _args, _kwargs)
        return val
    def getBottomLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getBottomLine,(self,) + _args, _kwargs)
        return val
    def setCenterLine(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setCenterLine,(self,) + _args, _kwargs)
        return val
    def setAnchorPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setAnchorPos,(self,) + _args, _kwargs)
        return val
    def getAnchorPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getAnchorPos,(self,) + _args, _kwargs)
        return val
    def setCursorPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setCursorPos,(self,) + _args, _kwargs)
        return val
    def setCursorRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setCursorRow,(self,) + _args, _kwargs)
        return val
    def getCursorRow(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getCursorRow,(self,) + _args, _kwargs)
        return val
    def setCursorCol(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setCursorCol,(self,) + _args, _kwargs)
        return val
    def getCursorCol(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getCursorCol,(self,) + _args, _kwargs)
        return val
    def getCursorPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getCursorPos,(self,) + _args, _kwargs)
        return val
    def getSelStartPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getSelStartPos,(self,) + _args, _kwargs)
        return val
    def getSelEndPos(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getSelEndPos,(self,) + _args, _kwargs)
        return val
    def selectAll(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_selectAll,(self,) + _args, _kwargs)
        return val
    def setSelection(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setSelection,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_killSelection,(self,) + _args, _kwargs)
        return val
    def setHighlight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHighlight,(self,) + _args, _kwargs)
        return val
    def killHighlight(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_killHighlight,(self,) + _args, _kwargs)
        return val
    def makePositionVisible(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_makePositionVisible,(self,) + _args, _kwargs)
        return val
    def setTextStyle(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setTextStyle,(self,) + _args, _kwargs)
        return val
    def getTextStyle(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getTextStyle,(self,) + _args, _kwargs)
        return val
    def setVisRows(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setVisRows,(self,) + _args, _kwargs)
        return val
    def getVisRows(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getVisRows,(self,) + _args, _kwargs)
        return val
    def setVisCols(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setVisCols,(self,) + _args, _kwargs)
        return val
    def getVisCols(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getVisCols,(self,) + _args, _kwargs)
        return val
    def setHiliteMatchTime(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHiliteMatchTime,(self,) + _args, _kwargs)
        return val
    def getHiliteMatchTime(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getHiliteMatchTime,(self,) + _args, _kwargs)
        return val
    def setHiliteStyles(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_setHiliteStyles,(self,) + _args, _kwargs)
        return val
    def getHiliteStyles(self, *_args, **_kwargs):
        val = apply(textc.FX_Text_getHiliteStyles,(self,) + _args, _kwargs)
        if val: val = FXHiliteStylePtr(val) 
        return val
    def __repr__(self):
        return "<C FX_Text instance at %s>" % (self.this,)
class FX_Text(FX_TextPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(textc.new_FX_Text,_args,_kwargs)
        self.thisown = 1




class FXTextPtr(FX_TextPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(textc.FXText_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(textc.FXText_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(textc.FXText_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(textc.FXText_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(textc.FXText_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(textc.FXText_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(textc.FXText_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(textc.FXText_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(textc.FXText_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(textc.FXText_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(textc.FXText_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(textc.FXText_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(textc.FXText_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(textc.FXText_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(textc.FXText_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(textc.FXText_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(textc.FXText_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(textc.FXText_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(textc.FXText_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(textc.FXText_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(textc.FXText_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(textc.FXText_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(textc.FXText_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(textc.FXText_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(textc.FXText_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(textc.FXText_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(textc.FXText_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(textc.FXText_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(textc.FXText_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(textc.FXText_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(textc.FXText_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(textc.FXText_moveContents,(self,) + _args, _kwargs)
        return val
    def setCursorPos(self, *_args, **_kwargs):
        val = apply(textc.FXText_setCursorPos,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(textc.FXText_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(textc.FXText_killSelection,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXText instance at %s>" % (self.this,)
class FXText(FXTextPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(textc.new_FXText,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------



#-------------- VARIABLE WRAPPERS ------------------

TEXT_READONLY = textc.TEXT_READONLY
TEXT_WORDWRAP = textc.TEXT_WORDWRAP
TEXT_OVERSTRIKE = textc.TEXT_OVERSTRIKE
TEXT_FIXEDWRAP = textc.TEXT_FIXEDWRAP
TEXT_NO_TABS = textc.TEXT_NO_TABS
TEXT_AUTOINDENT = textc.TEXT_AUTOINDENT
TEXT_SHOWACTIVE = textc.TEXT_SHOWACTIVE
SELECT_CHARS = textc.SELECT_CHARS
SELECT_WORDS = textc.SELECT_WORDS
SELECT_LINES = textc.SELECT_LINES
