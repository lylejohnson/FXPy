# This file was created automatically by SWIG.
import controlsc

from misc import *

from windows import *

from containers import *
import fox
class FX_LabelPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onPaint,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_onQueryTip,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setText,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setIcon,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getIcon,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setTextColor,(self,) + _args, _kwargs)
        return val
    def setJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setJustify,(self,) + _args, _kwargs)
        return val
    def getJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getJustify,(self,) + _args, _kwargs)
        return val
    def setIconPosition(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setIconPosition,(self,) + _args, _kwargs)
        return val
    def getIconPosition(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getIconPosition,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Label_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Label instance at %s>" % (self.this,)
class FX_Label(FX_LabelPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Label,_args,_kwargs)
        self.thisown = 1




class FXLabelPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXLabel_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXLabel instance at %s>" % (self.this,)
class FXLabel(FXLabelPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXLabel,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DialPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onPaint,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onMotion,(self,) + _args, _kwargs)
        return val
    def onMouseWheel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onMouseWheel,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdSetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdGetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdSetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdGetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdSetRealRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdSetRealRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetRealRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onCmdGetRealRange,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_onQueryTip,(self,) + _args, _kwargs)
        return val
    def setRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setRange,(self,) + _args, _kwargs)
        return val
    def getRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getRange,(self,) + _args, _kwargs)
        return val
    def setValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setValue,(self,) + _args, _kwargs)
        return val
    def getValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getValue,(self,) + _args, _kwargs)
        return val
    def setRevolutionIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setRevolutionIncrement,(self,) + _args, _kwargs)
        return val
    def getRevolutionIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getRevolutionIncrement,(self,) + _args, _kwargs)
        return val
    def setNotchSpacing(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setNotchSpacing,(self,) + _args, _kwargs)
        return val
    def getNotchSpacing(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getNotchSpacing,(self,) + _args, _kwargs)
        return val
    def setNotchOffset(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setNotchOffset,(self,) + _args, _kwargs)
        return val
    def getNotchOffset(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getNotchOffset,(self,) + _args, _kwargs)
        return val
    def getDialStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getDialStyle,(self,) + _args, _kwargs)
        return val
    def setDialStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setDialStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Dial_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Dial instance at %s>" % (self.this,)
class FX_Dial(FX_DialPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Dial,_args,_kwargs)
        self.thisown = 1




class FXDialPtr(FX_DialPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXDial_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDial instance at %s>" % (self.this,)
class FXDial(FXDialPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXDial,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ColorWellPtr(FX_FramePtr):
    ID_COLORDIALOG = controlsc.FX_ColorWell_ID_COLORDIALOG
    ID_LAST = controlsc.FX_ColorWell_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onMotion,(self,) + _args, _kwargs)
        return val
    def onBeginDrag(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onBeginDrag,(self,) + _args, _kwargs)
        return val
    def onEndDrag(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onEndDrag,(self,) + _args, _kwargs)
        return val
    def onDragged(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDragged,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDRequest(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDNDRequest,(self,) + _args, _kwargs)
        return val
    def onSelectionLost(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onSelectionLost,(self,) + _args, _kwargs)
        return val
    def onSelectionGained(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onSelectionGained,(self,) + _args, _kwargs)
        return val
    def onSelectionRequest(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onSelectionRequest,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdColorWell(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onCmdColorWell,(self,) + _args, _kwargs)
        return val
    def onChgColorWell(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onChgColorWell,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setRGBA(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_setRGBA,(self,) + _args, _kwargs)
        return val
    def getRGBA(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_getRGBA,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_getTipText,(self,) + _args, _kwargs)
        return val
    def isOpaqueOnly(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_isOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def setOpaqueOnly(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWell_setOpaqueOnly,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ColorWell instance at %s>" % (self.this,)
class FX_ColorWell(FX_ColorWellPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ColorWell,_args,_kwargs)
        self.thisown = 1




class FXColorWellPtr(FX_ColorWellPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWell_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXColorWell instance at %s>" % (self.this,)
class FXColorWell(FXColorWellPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXColorWell,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TextFieldPtr(FX_FramePtr):
    ID_CURSOR_HOME = controlsc.FX_TextField_ID_CURSOR_HOME
    ID_CURSOR_END = controlsc.FX_TextField_ID_CURSOR_END
    ID_CURSOR_RIGHT = controlsc.FX_TextField_ID_CURSOR_RIGHT
    ID_CURSOR_LEFT = controlsc.FX_TextField_ID_CURSOR_LEFT
    ID_MARK = controlsc.FX_TextField_ID_MARK
    ID_EXTEND = controlsc.FX_TextField_ID_EXTEND
    ID_SELECT_ALL = controlsc.FX_TextField_ID_SELECT_ALL
    ID_DESELECT_ALL = controlsc.FX_TextField_ID_DESELECT_ALL
    ID_CUT_SEL = controlsc.FX_TextField_ID_CUT_SEL
    ID_COPY_SEL = controlsc.FX_TextField_ID_COPY_SEL
    ID_PASTE_SEL = controlsc.FX_TextField_ID_PASTE_SEL
    ID_DELETE_SEL = controlsc.FX_TextField_ID_DELETE_SEL
    ID_OVERST_STRING = controlsc.FX_TextField_ID_OVERST_STRING
    ID_INSERT_STRING = controlsc.FX_TextField_ID_INSERT_STRING
    ID_BACKSPACE = controlsc.FX_TextField_ID_BACKSPACE
    ID_DELETE = controlsc.FX_TextField_ID_DELETE
    ID_TOGGLE_EDITABLE = controlsc.FX_TextField_ID_TOGGLE_EDITABLE
    ID_TOGGLE_OVERSTRIKE = controlsc.FX_TextField_ID_TOGGLE_OVERSTRIKE
    ID_BLINK = controlsc.FX_TextField_ID_BLINK
    ID_LAST = controlsc.FX_TextField_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onPaint,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onVerify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onVerify,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onMotion,(self,) + _args, _kwargs)
        return val
    def onSelectionLost(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onSelectionLost,(self,) + _args, _kwargs)
        return val
    def onSelectionGained(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onSelectionGained,(self,) + _args, _kwargs)
        return val
    def onSelectionRequest(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onSelectionRequest,(self,) + _args, _kwargs)
        return val
    def onClipboardLost(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onClipboardLost,(self,) + _args, _kwargs)
        return val
    def onClipboardGained(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onClipboardGained,(self,) + _args, _kwargs)
        return val
    def onClipboardRequest(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onClipboardRequest,(self,) + _args, _kwargs)
        return val
    def onFocusSelf(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onFocusSelf,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onBlink(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onBlink,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdSetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdGetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdCursorHome(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCursorHome,(self,) + _args, _kwargs)
        return val
    def onCmdCursorEnd(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCursorEnd,(self,) + _args, _kwargs)
        return val
    def onCmdCursorRight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCursorRight,(self,) + _args, _kwargs)
        return val
    def onCmdCursorLeft(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCursorLeft,(self,) + _args, _kwargs)
        return val
    def onCmdMark(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdMark,(self,) + _args, _kwargs)
        return val
    def onCmdExtend(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdExtend,(self,) + _args, _kwargs)
        return val
    def onCmdSelectAll(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdSelectAll,(self,) + _args, _kwargs)
        return val
    def onCmdDeselectAll(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdDeselectAll,(self,) + _args, _kwargs)
        return val
    def onCmdCutSel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCutSel,(self,) + _args, _kwargs)
        return val
    def onCmdCopySel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdCopySel,(self,) + _args, _kwargs)
        return val
    def onCmdPasteSel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdPasteSel,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteSel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdDeleteSel,(self,) + _args, _kwargs)
        return val
    def onCmdOverstString(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdOverstString,(self,) + _args, _kwargs)
        return val
    def onCmdInsertString(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdInsertString,(self,) + _args, _kwargs)
        return val
    def onCmdBackspace(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdBackspace,(self,) + _args, _kwargs)
        return val
    def onCmdDelete(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdDelete,(self,) + _args, _kwargs)
        return val
    def onCmdToggleEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdToggleEditable,(self,) + _args, _kwargs)
        return val
    def onUpdToggleEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onUpdToggleEditable,(self,) + _args, _kwargs)
        return val
    def onCmdToggleOverstrike(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onCmdToggleOverstrike,(self,) + _args, _kwargs)
        return val
    def onUpdToggleOverstrike(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_onUpdToggleOverstrike,(self,) + _args, _kwargs)
        return val
    def isEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_isEditable,(self,) + _args, _kwargs)
        return val
    def setEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setEditable,(self,) + _args, _kwargs)
        return val
    def setCursorPos(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setCursorPos,(self,) + _args, _kwargs)
        return val
    def getCursorPos(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getCursorPos,(self,) + _args, _kwargs)
        return val
    def setAnchorPos(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setAnchorPos,(self,) + _args, _kwargs)
        return val
    def getAnchorPos(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getAnchorPos,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getText,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getFont,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getTextColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setNumColumns(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setNumColumns,(self,) + _args, _kwargs)
        return val
    def getNumColumns(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getNumColumns,(self,) + _args, _kwargs)
        return val
    def setJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setJustify,(self,) + _args, _kwargs)
        return val
    def getJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getJustify,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getTipText,(self,) + _args, _kwargs)
        return val
    def setTextStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setTextStyle,(self,) + _args, _kwargs)
        return val
    def getTextStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_getTextStyle,(self,) + _args, _kwargs)
        return val
    def selectAll(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_selectAll,(self,) + _args, _kwargs)
        return val
    def setSelection(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_setSelection,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_killSelection,(self,) + _args, _kwargs)
        return val
    def isPosSelected(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_isPosSelected,(self,) + _args, _kwargs)
        return val
    def isPosVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_isPosVisible,(self,) + _args, _kwargs)
        return val
    def makePositionVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TextField_makePositionVisible,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TextField instance at %s>" % (self.this,)
class FX_TextField(FX_TextFieldPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_TextField,_args,_kwargs)
        self.thisown = 1




class FXTextFieldPtr(FX_TextFieldPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXTextField_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTextField instance at %s>" % (self.this,)
class FXTextField(FXTextFieldPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXTextField,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ButtonPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onLeave,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onCheck,(self,) + _args, _kwargs)
        return val
    def onUncheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onUncheck,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_setState,(self,) + _args, _kwargs)
        return val
    def getState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_getState,(self,) + _args, _kwargs)
        return val
    def setButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_setButtonStyle,(self,) + _args, _kwargs)
        return val
    def getButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Button_getButtonStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Button instance at %s>" % (self.this,)
class FX_Button(FX_ButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Button,_args,_kwargs)
        self.thisown = 1




class FXButtonPtr(FX_ButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXButton instance at %s>" % (self.this,)
class FXButton(FXButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ToggleButtonPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onLeave,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onCheck,(self,) + _args, _kwargs)
        return val
    def onUncheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onUncheck,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_setState,(self,) + _args, _kwargs)
        return val
    def getState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_getState,(self,) + _args, _kwargs)
        return val
    def setAltText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_setAltText,(self,) + _args, _kwargs)
        return val
    def getAltText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_getAltText,(self,) + _args, _kwargs)
        return val
    def setAltIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_setAltIcon,(self,) + _args, _kwargs)
        return val
    def getAltIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_getAltIcon,(self,) + _args, _kwargs)
        return val
    def setAltHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_setAltHelpText,(self,) + _args, _kwargs)
        return val
    def getAltHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_getAltHelpText,(self,) + _args, _kwargs)
        return val
    def setAltTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_setAltTipText,(self,) + _args, _kwargs)
        return val
    def getAltTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToggleButton_getAltTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ToggleButton instance at %s>" % (self.this,)
class FX_ToggleButton(FX_ToggleButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ToggleButton,_args,_kwargs)
        self.thisown = 1




class FXToggleButtonPtr(FX_ToggleButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXToggleButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXToggleButton instance at %s>" % (self.this,)
class FXToggleButton(FXToggleButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXToggleButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RadioButtonPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onLeave,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onUncheckRadio(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onUncheckRadio,(self,) + _args, _kwargs)
        return val
    def onCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onCheck,(self,) + _args, _kwargs)
        return val
    def onUncheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onUncheck,(self,) + _args, _kwargs)
        return val
    def onUnknown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onUnknown,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_setCheck,(self,) + _args, _kwargs)
        return val
    def getCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_getCheck,(self,) + _args, _kwargs)
        return val
    def setRadioButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_setRadioButtonStyle,(self,) + _args, _kwargs)
        return val
    def getRadioButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_getRadioButtonStyle,(self,) + _args, _kwargs)
        return val
    def getRadioColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_getRadioColor,(self,) + _args, _kwargs)
        return val
    def setRadioColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_RadioButton_setRadioColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_RadioButton instance at %s>" % (self.this,)
class FX_RadioButton(FX_RadioButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_RadioButton,_args,_kwargs)
        self.thisown = 1




class FXRadioButtonPtr(FX_RadioButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXRadioButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXRadioButton instance at %s>" % (self.this,)
class FXRadioButton(FXRadioButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXRadioButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CheckButtonPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onLeave,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onCheck,(self,) + _args, _kwargs)
        return val
    def onUncheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onUncheck,(self,) + _args, _kwargs)
        return val
    def onUnknown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onUnknown,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_setCheck,(self,) + _args, _kwargs)
        return val
    def getCheck(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_getCheck,(self,) + _args, _kwargs)
        return val
    def getBoxColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_getBoxColor,(self,) + _args, _kwargs)
        return val
    def setBoxColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_setBoxColor,(self,) + _args, _kwargs)
        return val
    def setCheckButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_setCheckButtonStyle,(self,) + _args, _kwargs)
        return val
    def getCheckButtonStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_CheckButton_getCheckButtonStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_CheckButton instance at %s>" % (self.this,)
class FX_CheckButton(FX_CheckButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_CheckButton,_args,_kwargs)
        self.thisown = 1




class FXCheckButtonPtr(FX_CheckButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXCheckButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXCheckButton instance at %s>" % (self.this,)
class FXCheckButton(FXCheckButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXCheckButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ArrowButtonPtr(FX_FramePtr):
    ID_REPEAT = controlsc.FX_ArrowButton_ID_REPEAT
    ID_LAST = controlsc.FX_ArrowButton_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onLeave,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onRepeat(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onRepeat,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_onQueryTip,(self,) + _args, _kwargs)
        return val
    def setState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setState,(self,) + _args, _kwargs)
        return val
    def getState(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getState,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getTipText,(self,) + _args, _kwargs)
        return val
    def setArrowStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setArrowStyle,(self,) + _args, _kwargs)
        return val
    def getArrowStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getArrowStyle,(self,) + _args, _kwargs)
        return val
    def setArrowSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setArrowSize,(self,) + _args, _kwargs)
        return val
    def getArrowSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getArrowSize,(self,) + _args, _kwargs)
        return val
    def setJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setJustify,(self,) + _args, _kwargs)
        return val
    def getJustify(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getJustify,(self,) + _args, _kwargs)
        return val
    def getArrowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_getArrowColor,(self,) + _args, _kwargs)
        return val
    def setArrowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ArrowButton_setArrowColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ArrowButton instance at %s>" % (self.this,)
class FX_ArrowButton(FX_ArrowButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ArrowButton,_args,_kwargs)
        self.thisown = 1




class FXArrowButtonPtr(FX_ArrowButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXArrowButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXArrowButton instance at %s>" % (self.this,)
class FXArrowButton(FXArrowButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXArrowButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PickerPtr(FX_ButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Picker_onMotion,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Picker_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Picker_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Picker_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Picker_onLeave,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Picker instance at %s>" % (self.this,)
class FX_Picker(FX_PickerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Picker,_args,_kwargs)
        self.thisown = 1




class FXPickerPtr(FX_PickerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXPicker_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPicker instance at %s>" % (self.this,)
class FXPicker(FXPickerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXPicker,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_SpinnerPtr(FX_PackerPtr):
    ID_INCREMENT = controlsc.FX_Spinner_ID_INCREMENT
    ID_DECREMENT = controlsc.FX_Spinner_ID_DECREMENT
    ID_ENTRY = controlsc.FX_Spinner_ID_ENTRY
    ID_LAST = controlsc.FX_Spinner_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onUpdIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onUpdIncrement,(self,) + _args, _kwargs)
        return val
    def onCmdIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdIncrement,(self,) + _args, _kwargs)
        return val
    def onUpdDecrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onUpdDecrement,(self,) + _args, _kwargs)
        return val
    def onCmdDecrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdDecrement,(self,) + _args, _kwargs)
        return val
    def onCmdEntry(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdEntry,(self,) + _args, _kwargs)
        return val
    def onChgEntry(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onChgEntry,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdSetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_onCmdGetIntRange,(self,) + _args, _kwargs)
        return val
    def increment(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_increment,(self,) + _args, _kwargs)
        return val
    def decrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_decrement,(self,) + _args, _kwargs)
        return val
    def isCyclic(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_isCyclic,(self,) + _args, _kwargs)
        return val
    def setCyclic(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setCyclic,(self,) + _args, _kwargs)
        return val
    def isTextVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_isTextVisible,(self,) + _args, _kwargs)
        return val
    def setTextVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setTextVisible,(self,) + _args, _kwargs)
        return val
    def setValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setValue,(self,) + _args, _kwargs)
        return val
    def getValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getValue,(self,) + _args, _kwargs)
        return val
    def setRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setRange,(self,) + _args, _kwargs)
        return val
    def getRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getRange,(self,) + _args, _kwargs)
        return val
    def setIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setIncrement,(self,) + _args, _kwargs)
        return val
    def getIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getIncrement,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getFont,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getTipText,(self,) + _args, _kwargs)
        return val
    def setSpinnerStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setSpinnerStyle,(self,) + _args, _kwargs)
        return val
    def getSpinnerStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_getSpinnerStyle,(self,) + _args, _kwargs)
        return val
    def setEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_setEditable,(self,) + _args, _kwargs)
        return val
    def isEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Spinner_isEditable,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Spinner instance at %s>" % (self.this,)
class FX_Spinner(FX_SpinnerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Spinner,_args,_kwargs)
        self.thisown = 1




class FXSpinnerPtr(FX_SpinnerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXSpinner_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXSpinner instance at %s>" % (self.this,)
class FXSpinner(FXSpinnerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXSpinner,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TooltipPtr(FX_ShellPtr):
    ID_TIP_SHOW = controlsc.FX_Tooltip_ID_TIP_SHOW
    ID_TIP_HIDE = controlsc.FX_Tooltip_ID_TIP_HIDE
    ID_LAST = controlsc.FX_Tooltip_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onUpdate,(self,) + _args, _kwargs)
        return val
    def onTipShow(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onTipShow,(self,) + _args, _kwargs)
        return val
    def onTipHide(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onTipHide,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_setText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_getText,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Tooltip_setTextColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Tooltip instance at %s>" % (self.this,)
class FX_Tooltip(FX_TooltipPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Tooltip,_args,_kwargs)
        self.thisown = 1




class FXTooltipPtr(FX_TooltipPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXTooltip_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTooltip instance at %s>" % (self.this,)
class FXTooltip(FXTooltipPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXTooltip,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_OptionPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onLeave,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Option_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Option instance at %s>" % (self.this,)
class FX_Option(FX_OptionPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Option,_args,_kwargs)
        self.thisown = 1




class FXOptionPtr(FX_OptionPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXOption_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXOption instance at %s>" % (self.this,)
class FXOption(FXOptionPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXOption,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_OptionMenuPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onMotion,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdPost(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onCmdPost,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_setCurrent,(self,) + _args, _kwargs)
        return val
    def getCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_getCurrent,(self,) + _args, _kwargs)
        return val
    def setCurrentNo(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_setCurrentNo,(self,) + _args, _kwargs)
        return val
    def getCurrentNo(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_getCurrentNo,(self,) + _args, _kwargs)
        return val
    def setPopup(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_setPopup,(self,) + _args, _kwargs)
        return val
    def getPopup(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_getPopup,(self,) + _args, _kwargs)
        return val
    def isPopped(self, *_args, **_kwargs):
        val = apply(controlsc.FX_OptionMenu_isPopped,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_OptionMenu instance at %s>" % (self.this,)
class FX_OptionMenu(FX_OptionMenuPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_OptionMenu,_args,_kwargs)
        self.thisown = 1




class FXOptionMenuPtr(FX_OptionMenuPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXOptionMenu_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXOptionMenu instance at %s>" % (self.this,)
class FXOptionMenu(FXOptionMenuPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXOptionMenu,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TabBarPtr(FX_PackerPtr):
    ID_OPEN_ITEM = controlsc.FX_TabBar_ID_OPEN_ITEM
    ID_OPEN_FIRST = controlsc.FX_TabBar_ID_OPEN_FIRST
    ID_OPEN_SECOND = controlsc.FX_TabBar_ID_OPEN_SECOND
    ID_OPEN_THIRD = controlsc.FX_TabBar_ID_OPEN_THIRD
    ID_OPEN_FOURTH = controlsc.FX_TabBar_ID_OPEN_FOURTH
    ID_OPEN_FIFTH = controlsc.FX_TabBar_ID_OPEN_FIFTH
    ID_OPEN_SIXTH = controlsc.FX_TabBar_ID_OPEN_SIXTH
    ID_OPEN_SEVENTH = controlsc.FX_TabBar_ID_OPEN_SEVENTH
    ID_OPEN_EIGHTH = controlsc.FX_TabBar_ID_OPEN_EIGHTH
    ID_OPEN_NINETH = controlsc.FX_TabBar_ID_OPEN_NINETH
    ID_OPEN_TENTH = controlsc.FX_TabBar_ID_OPEN_TENTH
    ID_OPEN_LAST = controlsc.FX_TabBar_ID_OPEN_LAST
    ID_LAST = controlsc.FX_TabBar_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onPaint,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onFocusRight,(self,) + _args, _kwargs)
        return val
    def onCmdOpenItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onCmdOpenItem,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdOpen(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onCmdOpen,(self,) + _args, _kwargs)
        return val
    def onUpdOpen(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_onUpdOpen,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_setCurrent,(self,) + _args, _kwargs)
        return val
    def getCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_getCurrent,(self,) + _args, _kwargs)
        return val
    def getTabStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_getTabStyle,(self,) + _args, _kwargs)
        return val
    def setTabStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBar_setTabStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TabBar instance at %s>" % (self.this,)
class FX_TabBar(FX_TabBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_TabBar,_args,_kwargs)
        self.thisown = 1




class FXTabBarPtr(FX_TabBarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_setBackColor,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBar_setCurrent,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTabBar instance at %s>" % (self.this,)
class FXTabBar(FXTabBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXTabBar,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TabItemPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onPaint,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def getTabOrientation(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_getTabOrientation,(self,) + _args, _kwargs)
        return val
    def setTabOrientation(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabItem_setTabOrientation,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TabItem instance at %s>" % (self.this,)
class FX_TabItem(FX_TabItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_TabItem,_args,_kwargs)
        self.thisown = 1




class FXTabItemPtr(FX_TabItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabItem_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTabItem instance at %s>" % (self.this,)
class FXTabItem(FXTabItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXTabItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TabBookPtr(FX_TabBarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onPaint,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onFocusRight,(self,) + _args, _kwargs)
        return val
    def onCmdOpenItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_TabBook_onCmdOpenItem,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_TabBook instance at %s>" % (self.this,)
class FX_TabBook(FX_TabBookPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_TabBook,_args,_kwargs)
        self.thisown = 1




class FXTabBookPtr(FX_TabBookPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_setBackColor,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FXTabBook_setCurrent,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTabBook instance at %s>" % (self.this,)
class FXTabBook(FXTabBookPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXTabBook,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ScrollbarPtr(FX_WindowPtr):
    ID_TIMEWHEEL = controlsc.FX_Scrollbar_ID_TIMEWHEEL
    ID_AUTOINC_LINE = controlsc.FX_Scrollbar_ID_AUTOINC_LINE
    ID_AUTODEC_LINE = controlsc.FX_Scrollbar_ID_AUTODEC_LINE
    ID_AUTOINC_PAGE = controlsc.FX_Scrollbar_ID_AUTOINC_PAGE
    ID_AUTODEC_PAGE = controlsc.FX_Scrollbar_ID_AUTODEC_PAGE
    ID_AUTOINC_PIX = controlsc.FX_Scrollbar_ID_AUTOINC_PIX
    ID_AUTODEC_PIX = controlsc.FX_Scrollbar_ID_AUTODEC_PIX
    ID_LAST = controlsc.FX_Scrollbar_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onPaint,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onMotion,(self,) + _args, _kwargs)
        return val
    def onMouseWheel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onMouseWheel,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onTimeIncPix(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeIncPix,(self,) + _args, _kwargs)
        return val
    def onTimeIncLine(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeIncLine,(self,) + _args, _kwargs)
        return val
    def onTimeIncPage(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeIncPage,(self,) + _args, _kwargs)
        return val
    def onTimeDecPix(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeDecPix,(self,) + _args, _kwargs)
        return val
    def onTimeDecLine(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeDecLine,(self,) + _args, _kwargs)
        return val
    def onTimeDecPage(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeDecPage,(self,) + _args, _kwargs)
        return val
    def onTimeWheel(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onTimeWheel,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onCmdSetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_onCmdGetIntRange,(self,) + _args, _kwargs)
        return val
    def setRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setRange,(self,) + _args, _kwargs)
        return val
    def getRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getRange,(self,) + _args, _kwargs)
        return val
    def setPage(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setPage,(self,) + _args, _kwargs)
        return val
    def getPage(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getPage,(self,) + _args, _kwargs)
        return val
    def setLine(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setLine,(self,) + _args, _kwargs)
        return val
    def getLine(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getLine,(self,) + _args, _kwargs)
        return val
    def setPosition(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setPosition,(self,) + _args, _kwargs)
        return val
    def getPosition(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getPosition,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getShadowColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getBorderColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setBorderColor,(self,) + _args, _kwargs)
        return val
    def getScrollbarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_getScrollbarStyle,(self,) + _args, _kwargs)
        return val
    def setScrollbarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Scrollbar_setScrollbarStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Scrollbar instance at %s>" % (self.this,)
class FX_Scrollbar(FX_ScrollbarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Scrollbar,_args,_kwargs)
        self.thisown = 1




class FXScrollbarPtr(FX_ScrollbarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollbar_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXScrollbar instance at %s>" % (self.this,)
class FXScrollbar(FXScrollbarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXScrollbar,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ScrollCornerPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ScrollCorner_onPaint,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ScrollCorner instance at %s>" % (self.this,)
class FX_ScrollCorner(FX_ScrollCornerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ScrollCorner,_args,_kwargs)
        self.thisown = 1




class FXScrollCornerPtr(FX_ScrollCornerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXScrollCorner_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXScrollCorner instance at %s>" % (self.this,)
class FXScrollCorner(FXScrollCornerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXScrollCorner,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ListItemPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setText,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_getIcon,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setIcon,(self,) + _args, _kwargs)
        return val
    def setData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setData,(self,) + _args, _kwargs)
        return val
    def getData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_getData,(self,) + _args, _kwargs)
        return val
    def hasFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_hasFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setFocus,(self,) + _args, _kwargs)
        return val
    def isSelected(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_isSelected,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setSelected,(self,) + _args, _kwargs)
        return val
    def isEnabled(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_isEnabled,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def isDraggable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_isDraggable,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def isIconOwned(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_isIconOwned,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ListItem instance at %s>" % (self.this,)
class FX_ListItem(FX_ListItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ListItem,_args,_kwargs)
        self.thisown = 1




class FXListItemPtr(FX_ListItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setText,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setIcon,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setFocus,(self,) + _args, _kwargs)
        return val
    def setSelected(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setSelected,(self,) + _args, _kwargs)
        return val
    def setEnabled(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setEnabled,(self,) + _args, _kwargs)
        return val
    def setDraggable(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setDraggable,(self,) + _args, _kwargs)
        return val
    def setIconOwned(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_setIconOwned,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXListItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXListItem instance at %s>" % (self.this,)
class FXListItem(FXListItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXListItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ListPtr(FX_ScrollAreaPtr):
    ID_TIPTIMER = controlsc.FX_List_ID_TIPTIMER
    ID_LOOKUPTIMER = controlsc.FX_List_ID_LOOKUPTIMER
    ID_LAST = controlsc.FX_List_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onLeave,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onMotion,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onCommand(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onCommand,(self,) + _args, _kwargs)
        return val
    def onTipTimer(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onTipTimer,(self,) + _args, _kwargs)
        return val
    def onLookupTimer(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onLookupTimer,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getNumVisible,(self,) + _args, _kwargs)
        return val
    def setNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setNumVisible,(self,) + _args, _kwargs)
        return val
    def retrieveItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_retrieveItem,(self,) + _args, _kwargs)
        if val: val = FX_ListItemPtr(val) 
        return val
    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_insertItemStr,(self,) + _args, _kwargs)
            return val
    def insertItemStr(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_insertItemStr,(self,) + _args, _kwargs)
        return val
    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_replaceItemStr,(self,) + _args, _kwargs)
            return val
    def replaceItemStr(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_replaceItemStr,(self,) + _args, _kwargs)
        return val
    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_appendItemStr,(self,) + _args, _kwargs)
            return val
    def appendItemStr(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_appendItemStr,(self,) + _args, _kwargs)
        return val
    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_prependItemStr,(self,) + _args, _kwargs)
            return val
    def prependItemStr(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_prependItemStr,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_removeItem,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_clearItems,(self,) + _args, _kwargs)
        return val
    def getItemWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemWidth,(self,) + _args, _kwargs)
        return val
    def getItemHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemHeight,(self,) + _args, _kwargs)
        return val
    def getItemAt(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemAt,(self,) + _args, _kwargs)
        return val
    def hitItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_hitItem,(self,) + _args, _kwargs)
        return val
    def findItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_findItem,(self,) + _args, _kwargs)
        return val
    def makeItemVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_makeItemVisible,(self,) + _args, _kwargs)
        return val
    def updateItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_updateItem,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setItemIcon,(self,) + _args, _kwargs)
        return val
    def getItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getItemData,(self,) + _args, _kwargs)
        return val
    def isItemSelected(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_isItemSelected,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def isItemVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_isItemVisible,(self,) + _args, _kwargs)
        return val
    def isItemEnabled(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_isItemEnabled,(self,) + _args, _kwargs)
        return val
    def enableItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_enableItem,(self,) + _args, _kwargs)
        return val
    def disableItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_disableItem,(self,) + _args, _kwargs)
        return val
    def selectItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_selectItem,(self,) + _args, _kwargs)
        return val
    def deselectItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_deselectItem,(self,) + _args, _kwargs)
        return val
    def toggleItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_toggleItem,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def setAnchorItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setAnchorItem,(self,) + _args, _kwargs)
        return val
    def getAnchorItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getAnchorItem,(self,) + _args, _kwargs)
        return val
    def getCursorItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getCursorItem,(self,) + _args, _kwargs)
        return val
    def extendSelection(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_extendSelection,(self,) + _args, _kwargs)
        return val
    def killSelection(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_killSelection,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setTextColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setSortFunc,(self,) + _args, _kwargs)
        return val
    def getListStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getListStyle,(self,) + _args, _kwargs)
        return val
    def setListStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setListStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_List_getHelpText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_List instance at %s>" % (self.this,)
class FX_List(FX_ListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_List,_args,_kwargs)
        self.thisown = 1




class FXListPtr(FX_ListPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(controlsc.FXList_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXList instance at %s>" % (self.this,)
class FXList(FXListPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXList,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ComboBoxPtr(FX_PackerPtr):
    ID_LIST = controlsc.FX_ComboBox_ID_LIST
    ID_TEXT = controlsc.FX_ComboBox_ID_TEXT
    ID_LAST = controlsc.FX_ComboBox_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onTextButton(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onTextButton,(self,) + _args, _kwargs)
        return val
    def onTextChanged(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onTextChanged,(self,) + _args, _kwargs)
        return val
    def onTextCommand(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onTextCommand,(self,) + _args, _kwargs)
        return val
    def onListClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onListClicked,(self,) + _args, _kwargs)
        return val
    def onFwdToText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onFwdToText,(self,) + _args, _kwargs)
        return val
    def onUpdFmText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_onUpdFmText,(self,) + _args, _kwargs)
        return val
    def isEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_isEditable,(self,) + _args, _kwargs)
        return val
    def setEditable(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setEditable,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getText,(self,) + _args, _kwargs)
        return val
    def setNumColumns(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setNumColumns,(self,) + _args, _kwargs)
        return val
    def getNumColumns(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getNumColumns,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getNumVisible,(self,) + _args, _kwargs)
        return val
    def setNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setNumVisible,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def retrieveItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_retrieveItem,(self,) + _args, _kwargs)
        return val
    def replaceItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_replaceItem,(self,) + _args, _kwargs)
        return val
    def insertItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_insertItem,(self,) + _args, _kwargs)
        return val
    def appendItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_appendItem,(self,) + _args, _kwargs)
        return val
    def prependItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_prependItem,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_removeItem,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_clearItems,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getItemData,(self,) + _args, _kwargs)
        return val
    def isPaneShown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_isPaneShown,(self,) + _args, _kwargs)
        return val
    def sortItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_sortItems,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getFont,(self,) + _args, _kwargs)
        return val
    def setComboStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setComboStyle,(self,) + _args, _kwargs)
        return val
    def getComboStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getComboStyle,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def getBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getBackColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getTextColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setSortFunc,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ComboBox_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ComboBox instance at %s>" % (self.this,)
class FX_ComboBox(FX_ComboBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ComboBox,_args,_kwargs)
        self.thisown = 1




class FXComboBoxPtr(FX_ComboBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXComboBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXComboBox instance at %s>" % (self.this,)
class FXComboBox(FXComboBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXComboBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DragCornerPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_onMotion,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DragCorner_setShadowColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DragCorner instance at %s>" % (self.this,)
class FX_DragCorner(FX_DragCornerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_DragCorner,_args,_kwargs)
        self.thisown = 1




class FXDragCornerPtr(FX_DragCornerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXDragCorner_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDragCorner instance at %s>" % (self.this,)
class FXDragCorner(FXDragCornerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXDragCorner,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_StatuslinePtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_onUpdate,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_setText,(self,) + _args, _kwargs)
        return val
    def setNormalText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_setNormalText,(self,) + _args, _kwargs)
        return val
    def getNormalText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_getNormalText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_getText,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextHighlightColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_getTextHighlightColor,(self,) + _args, _kwargs)
        return val
    def setTextHighlightColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusline_setTextHighlightColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Statusline instance at %s>" % (self.this,)
class FX_Statusline(FX_StatuslinePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Statusline,_args,_kwargs)
        self.thisown = 1




class FXStatuslinePtr(FX_StatuslinePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusline_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXStatusline instance at %s>" % (self.this,)
class FXStatusline(FXStatuslinePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXStatusline,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_StatusbarPtr(FX_HorizontalFramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setCornerStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusbar_setCornerStyle,(self,) + _args, _kwargs)
        return val
    def getCornerStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusbar_getCornerStyle,(self,) + _args, _kwargs)
        return val
    def getStatusline(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusbar_getStatusline,(self,) + _args, _kwargs)
        return val
    def getDragCorner(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Statusbar_getDragCorner,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Statusbar instance at %s>" % (self.this,)
class FX_Statusbar(FX_StatusbarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Statusbar,_args,_kwargs)
        self.thisown = 1




class FXStatusbarPtr(FX_StatusbarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXStatusbar_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXStatusbar instance at %s>" % (self.this,)
class FXStatusbar(FXStatusbarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXStatusbar,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_SliderPtr(FX_FramePtr):
    ID_AUTOINC = controlsc.FX_Slider_ID_AUTOINC
    ID_AUTODEC = controlsc.FX_Slider_ID_AUTODEC
    ID_LAST = controlsc.FX_Slider_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onMotion,(self,) + _args, _kwargs)
        return val
    def onTimeInc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onTimeInc,(self,) + _args, _kwargs)
        return val
    def onTimeDec(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onTimeDec,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdSetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetRealValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdGetRealValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdSetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdGetIntRange,(self,) + _args, _kwargs)
        return val
    def onCmdSetRealRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdSetRealRange,(self,) + _args, _kwargs)
        return val
    def onCmdGetRealRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onCmdGetRealRange,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_onQueryTip,(self,) + _args, _kwargs)
        return val
    def setRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setRange,(self,) + _args, _kwargs)
        return val
    def getRange(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getRange,(self,) + _args, _kwargs)
        return val
    def setValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setValue,(self,) + _args, _kwargs)
        return val
    def getValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getValue,(self,) + _args, _kwargs)
        return val
    def getSliderStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getSliderStyle,(self,) + _args, _kwargs)
        return val
    def setSliderStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setSliderStyle,(self,) + _args, _kwargs)
        return val
    def getHeadSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getHeadSize,(self,) + _args, _kwargs)
        return val
    def setHeadSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setHeadSize,(self,) + _args, _kwargs)
        return val
    def getSlotSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getSlotSize,(self,) + _args, _kwargs)
        return val
    def setSlotSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setSlotSize,(self,) + _args, _kwargs)
        return val
    def getIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getIncrement,(self,) + _args, _kwargs)
        return val
    def setIncrement(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setIncrement,(self,) + _args, _kwargs)
        return val
    def setTickDelta(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setTickDelta,(self,) + _args, _kwargs)
        return val
    def getTickDelta(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getTickDelta,(self,) + _args, _kwargs)
        return val
    def getSlotColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getSlotColor,(self,) + _args, _kwargs)
        return val
    def setSlotColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setSlotColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getBorderColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setBorderColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getBaseColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setBaseColor,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getHelpText,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setHelpText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_getTipText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Slider_setTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Slider instance at %s>" % (self.this,)
class FX_Slider(FX_SliderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Slider,_args,_kwargs)
        self.thisown = 1




class FXSliderPtr(FX_SliderPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXSlider_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXSlider instance at %s>" % (self.this,)
class FXSlider(FXSliderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXSlider,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_HeaderItemPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getText,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_setText,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getIcon,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_setIcon,(self,) + _args, _kwargs)
        return val
    def setData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_setData,(self,) + _args, _kwargs)
        return val
    def getData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getData,(self,) + _args, _kwargs)
        return val
    def setSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_setSize,(self,) + _args, _kwargs)
        return val
    def getSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getSize,(self,) + _args, _kwargs)
        return val
    def setArrowDir(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_setArrowDir,(self,) + _args, _kwargs)
        return val
    def getArrowDir(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getArrowDir,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FX_HeaderItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_HeaderItem instance at %s>" % (self.this,)
class FX_HeaderItem(FX_HeaderItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_HeaderItem,_args,_kwargs)
        self.thisown = 1




class FXHeaderItemPtr(FX_HeaderItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_onDefault,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_setText,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_setIcon,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeaderItem_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXHeaderItem instance at %s>" % (self.this,)
class FXHeaderItem(FXHeaderItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXHeaderItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_HeaderPtr(FX_FramePtr):
    ID_TIPTIMER = controlsc.FX_Header_ID_TIPTIMER
    ID_LAST = controlsc.FX_Header_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onMotion,(self,) + _args, _kwargs)
        return val
    def onTipTimer(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onTipTimer,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getNumItems,(self,) + _args, _kwargs)
        return val
    def retrieveItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_retrieveItem,(self,) + _args, _kwargs)
        return val
    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_replaceItem2,(self,) + _args, _kwargs)
            return val
    def replaceItem2(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_replaceItem2,(self,) + _args, _kwargs)
        return val
    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_insertItem2,(self,) + _args, _kwargs)
            return val
    def insertItem2(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_insertItem2,(self,) + _args, _kwargs)
        return val
    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_appendItem2,(self,) + _args, _kwargs)
            return val
    def appendItem2(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_appendItem2,(self,) + _args, _kwargs)
        return val
    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_prependItem2,(self,) + _args, _kwargs)
            return val
    def prependItem2(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_prependItem2,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_removeItem,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_clearItems,(self,) + _args, _kwargs)
        return val
    def getItemAt(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemAt,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setItemIcon,(self,) + _args, _kwargs)
        return val
    def getItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemIcon,(self,) + _args, _kwargs)
        return val
    def setItemSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setItemSize,(self,) + _args, _kwargs)
        return val
    def getItemSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemSize,(self,) + _args, _kwargs)
        return val
    def getItemOffset(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemOffset,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getItemData,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setTextColor,(self,) + _args, _kwargs)
        return val
    def setHeaderStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setHeaderStyle,(self,) + _args, _kwargs)
        return val
    def getHeaderStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getHeaderStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Header_getHelpText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Header instance at %s>" % (self.this,)
class FX_Header(FX_HeaderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_Header,_args,_kwargs)
        self.thisown = 1




class FXHeaderPtr(FX_HeaderPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXHeader_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXHeader instance at %s>" % (self.this,)
class FXHeader(FXHeaderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXHeader,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ProgressBarPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_onPaint,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def setProgress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setProgress,(self,) + _args, _kwargs)
        return val
    def getProgress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getProgress,(self,) + _args, _kwargs)
        return val
    def setTotal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setTotal,(self,) + _args, _kwargs)
        return val
    def getTotal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getTotal,(self,) + _args, _kwargs)
        return val
    def increment(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_increment,(self,) + _args, _kwargs)
        return val
    def hideNumber(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_hideNumber,(self,) + _args, _kwargs)
        return val
    def showNumber(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_showNumber,(self,) + _args, _kwargs)
        return val
    def setBarSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setBarSize,(self,) + _args, _kwargs)
        return val
    def getBarSize(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getBarSize,(self,) + _args, _kwargs)
        return val
    def setBarBGColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setBarBGColor,(self,) + _args, _kwargs)
        return val
    def getBarBGColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getBarBGColor,(self,) + _args, _kwargs)
        return val
    def setBarColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setBarColor,(self,) + _args, _kwargs)
        return val
    def getBarColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getBarColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextAltColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setTextAltColor,(self,) + _args, _kwargs)
        return val
    def getTextAltColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getTextAltColor,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getFont,(self,) + _args, _kwargs)
        return val
    def setBarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_setBarStyle,(self,) + _args, _kwargs)
        return val
    def getBarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ProgressBar_getBarStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ProgressBar instance at %s>" % (self.this,)
class FX_ProgressBar(FX_ProgressBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ProgressBar,_args,_kwargs)
        self.thisown = 1




class FXProgressBarPtr(FX_ProgressBarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXProgressBar_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXProgressBar instance at %s>" % (self.this,)
class FXProgressBar(FXProgressBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXProgressBar,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ToolbarTabPtr(FX_FramePtr):
    ID_COLLAPSE = controlsc.FX_ToolbarTab_ID_COLLAPSE
    ID_UNCOLLAPSE = controlsc.FX_ToolbarTab_ID_UNCOLLAPSE
    ID_LAST = controlsc.FX_ToolbarTab_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onLeave,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdCollapse(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onCmdCollapse,(self,) + _args, _kwargs)
        return val
    def onUpdCollapse(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onUpdCollapse,(self,) + _args, _kwargs)
        return val
    def onCmdUncollapse(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onCmdUncollapse,(self,) + _args, _kwargs)
        return val
    def onUpdUncollapse(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_onUpdUncollapse,(self,) + _args, _kwargs)
        return val
    def collapse(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_collapse,(self,) + _args, _kwargs)
        return val
    def isCollapsed(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_isCollapsed,(self,) + _args, _kwargs)
        return val
    def setTabStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_setTabStyle,(self,) + _args, _kwargs)
        return val
    def getTabStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_getTabStyle,(self,) + _args, _kwargs)
        return val
    def getActiveColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_getActiveColor,(self,) + _args, _kwargs)
        return val
    def setActiveColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarTab_setActiveColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ToolbarTab instance at %s>" % (self.this,)
class FX_ToolbarTab(FX_ToolbarTabPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ToolbarTab,_args,_kwargs)
        self.thisown = 1




class FXToolbarTabPtr(FX_ToolbarTabPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarTab_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXToolbarTab instance at %s>" % (self.this,)
class FXToolbarTab(FXToolbarTabPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXToolbarTab,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ToolbarPtr(FX_PackerPtr):
    ID_UNDOCK = controlsc.FX_Toolbar_ID_UNDOCK
    ID_DOCK_TOP = controlsc.FX_Toolbar_ID_DOCK_TOP
    ID_DOCK_BOTTOM = controlsc.FX_Toolbar_ID_DOCK_BOTTOM
    ID_DOCK_LEFT = controlsc.FX_Toolbar_ID_DOCK_LEFT
    ID_DOCK_RIGHT = controlsc.FX_Toolbar_ID_DOCK_RIGHT
    ID_TOOLBARGRIP = controlsc.FX_Toolbar_ID_TOOLBARGRIP
    ID_LAST = controlsc.FX_Toolbar_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdUndock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onCmdUndock,(self,) + _args, _kwargs)
        return val
    def onUpdUndock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onUpdUndock,(self,) + _args, _kwargs)
        return val
    def onCmdDockTop(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onCmdDockTop,(self,) + _args, _kwargs)
        return val
    def onUpdDockTop(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onUpdDockTop,(self,) + _args, _kwargs)
        return val
    def onCmdDockBottom(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onCmdDockBottom,(self,) + _args, _kwargs)
        return val
    def onUpdDockBottom(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onUpdDockBottom,(self,) + _args, _kwargs)
        return val
    def onCmdDockLeft(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onCmdDockLeft,(self,) + _args, _kwargs)
        return val
    def onUpdDockLeft(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onUpdDockLeft,(self,) + _args, _kwargs)
        return val
    def onCmdDockRight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onCmdDockRight,(self,) + _args, _kwargs)
        return val
    def onUpdDockRight(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onUpdDockRight,(self,) + _args, _kwargs)
        return val
    def onBeginDragGrip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onBeginDragGrip,(self,) + _args, _kwargs)
        return val
    def onEndDragGrip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onEndDragGrip,(self,) + _args, _kwargs)
        return val
    def onDraggedGrip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_onDraggedGrip,(self,) + _args, _kwargs)
        return val
    def setDryDock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_setDryDock,(self,) + _args, _kwargs)
        return val
    def setWetDock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_setWetDock,(self,) + _args, _kwargs)
        return val
    def getDryDock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_getDryDock,(self,) + _args, _kwargs)
        return val
    def getWetDock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_getWetDock,(self,) + _args, _kwargs)
        return val
    def isDocked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_isDocked,(self,) + _args, _kwargs)
        return val
    def dock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_dock,(self,) + _args, _kwargs)
        return val
    def undock(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_undock,(self,) + _args, _kwargs)
        return val
    def setDockingSide(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_setDockingSide,(self,) + _args, _kwargs)
        return val
    def getDockingSide(self, *_args, **_kwargs):
        val = apply(controlsc.FX_Toolbar_getDockingSide,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Toolbar instance at %s>" % (self.this,)
class FX_Toolbar(FX_ToolbarPtr):
    def __init__(self,this):
        self.this = this




class FXToolbarPtr(FX_ToolbarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_setBackColor,(self,) + _args, _kwargs)
        return val
    def dock(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_dock,(self,) + _args, _kwargs)
        return val
    def undock(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbar_undock,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXToolbar instance at %s>" % (self.this,)
class FXToolbar(FXToolbarPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(controlsc.CreateFloatingToolbar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(controlsc.CreateNonFloatingToolbar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_ToolbarShellPtr(FX_TopWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_onPaint,(self,) + _args, _kwargs)
        return val
    def setFrameStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_setFrameStyle,(self,) + _args, _kwargs)
        return val
    def getFrameStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getFrameStyle,(self,) + _args, _kwargs)
        return val
    def getBorderWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getBorderWidth,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_setBorderColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getBorderColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_setBaseColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarShell_getBaseColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ToolbarShell instance at %s>" % (self.this,)
class FX_ToolbarShell(FX_ToolbarShellPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ToolbarShell,_args,_kwargs)
        self.thisown = 1




class FXToolbarShellPtr(FX_ToolbarShellPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FXToolbarShell_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FXToolbarShell_show2,(self,) + _args, _kwargs)
            return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_setBackColor,(self,) + _args, _kwargs)
        return val
    def show2(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_show2,(self,) + _args, _kwargs)
        return val
    def iconify(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_iconify,(self,) + _args, _kwargs)
        return val
    def deiconify(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarShell_deiconify,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXToolbarShell instance at %s>" % (self.this,)
class FXToolbarShell(FXToolbarShellPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXToolbarShell,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ToolbarGripPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onMotion,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_onLeave,(self,) + _args, _kwargs)
        return val
    def setDoubleBar(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_setDoubleBar,(self,) + _args, _kwargs)
        return val
    def getDoubleBar(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_getDoubleBar,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_getShadowColor,(self,) + _args, _kwargs)
        return val
    def getActiveColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ToolbarGrip_getActiveColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ToolbarGrip instance at %s>" % (self.this,)
class FX_ToolbarGrip(FX_ToolbarGripPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ToolbarGrip,_args,_kwargs)
        self.thisown = 1




class FXToolbarGripPtr(FX_ToolbarGripPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXToolbarGrip_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXToolbarGrip instance at %s>" % (self.this,)
class FXToolbarGrip(FXToolbarGripPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXToolbarGrip,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ListBoxPtr(FX_PackerPtr):
    ID_LIST = controlsc.FX_ListBox_ID_LIST
    ID_FIELD = controlsc.FX_ListBox_ID_FIELD
    ID_LAST = controlsc.FX_ListBox_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFieldButton(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onFieldButton,(self,) + _args, _kwargs)
        return val
    def onListUpdate(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onListUpdate,(self,) + _args, _kwargs)
        return val
    def onListChanged(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onListChanged,(self,) + _args, _kwargs)
        return val
    def onListClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onListClicked,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def getNumItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getNumItems,(self,) + _args, _kwargs)
        return val
    def getNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getNumVisible,(self,) + _args, _kwargs)
        return val
    def setNumVisible(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setNumVisible,(self,) + _args, _kwargs)
        return val
    def isItemCurrent(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_isItemCurrent,(self,) + _args, _kwargs)
        return val
    def setCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setCurrentItem,(self,) + _args, _kwargs)
        return val
    def getCurrentItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getCurrentItem,(self,) + _args, _kwargs)
        return val
    def retrieveItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_retrieveItem,(self,) + _args, _kwargs)
        return val
    def replaceItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_replaceItem,(self,) + _args, _kwargs)
        return val
    def insertItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_insertItem,(self,) + _args, _kwargs)
        return val
    def appendItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_appendItem,(self,) + _args, _kwargs)
        return val
    def prependItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_prependItem,(self,) + _args, _kwargs)
        return val
    def removeItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_removeItem,(self,) + _args, _kwargs)
        return val
    def clearItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_clearItems,(self,) + _args, _kwargs)
        return val
    def findItem(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_findItem,(self,) + _args, _kwargs)
        return val
    def setItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setItemText,(self,) + _args, _kwargs)
        return val
    def getItemText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getItemText,(self,) + _args, _kwargs)
        return val
    def setItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setItemIcon,(self,) + _args, _kwargs)
        return val
    def getItemIcon(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getItemIcon,(self,) + _args, _kwargs)
        return val
    def setItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setItemData,(self,) + _args, _kwargs)
        return val
    def getItemData(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getItemData,(self,) + _args, _kwargs)
        return val
    def isPaneShown(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_isPaneShown,(self,) + _args, _kwargs)
        return val
    def sortItems(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_sortItems,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getFont,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def getBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getBackColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setTextColor,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getTextColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def getSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getSortFunc,(self,) + _args, _kwargs)
        return val
    def setSortFunc(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setSortFunc,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ListBox_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ListBox instance at %s>" % (self.this,)
class FX_ListBox(FX_ListBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ListBox,_args,_kwargs)
        self.thisown = 1




class FXListBoxPtr(FX_ListBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXListBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXListBox instance at %s>" % (self.this,)
class FXListBox(FXListBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXListBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DriveBoxPtr(FX_ListBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onListChanged(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_onListChanged,(self,) + _args, _kwargs)
        return val
    def onListClicked(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_onListClicked,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def setDrive(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_setDrive,(self,) + _args, _kwargs)
        return val
    def getDrive(self, *_args, **_kwargs):
        val = apply(controlsc.FX_DriveBox_getDrive,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DriveBox instance at %s>" % (self.this,)
class FX_DriveBox(FX_DriveBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_DriveBox,_args,_kwargs)
        self.thisown = 1




class FXDriveBoxPtr(FX_DriveBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXDriveBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDriveBox instance at %s>" % (self.this,)
class FXDriveBox(FXDriveBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXDriveBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ColorBarPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onMotion,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_onQueryTip,(self,) + _args, _kwargs)
        return val
    def setHue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setHue,(self,) + _args, _kwargs)
        return val
    def getHue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getHue,(self,) + _args, _kwargs)
        return val
    def setSat(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setSat,(self,) + _args, _kwargs)
        return val
    def getSat(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getSat,(self,) + _args, _kwargs)
        return val
    def setVal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setVal,(self,) + _args, _kwargs)
        return val
    def getVal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getVal,(self,) + _args, _kwargs)
        return val
    def getBarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getBarStyle,(self,) + _args, _kwargs)
        return val
    def setBarStyle(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setBarStyle,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorBar_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ColorBar instance at %s>" % (self.this,)
class FX_ColorBar(FX_ColorBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ColorBar,_args,_kwargs)
        self.thisown = 1




class FXColorBarPtr(FX_ColorBarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorBar_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXColorBar instance at %s>" % (self.this,)
class FXColorBar(FXColorBarPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXColorBar,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ColorWheelPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onPaint,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onMotion,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_onQueryTip,(self,) + _args, _kwargs)
        return val
    def setHue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_setHue,(self,) + _args, _kwargs)
        return val
    def getHue(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_getHue,(self,) + _args, _kwargs)
        return val
    def setSat(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_setSat,(self,) + _args, _kwargs)
        return val
    def getSat(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_getSat,(self,) + _args, _kwargs)
        return val
    def setVal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_setVal,(self,) + _args, _kwargs)
        return val
    def getVal(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_getVal,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(controlsc.FX_ColorWheel_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ColorWheel instance at %s>" % (self.this,)
class FX_ColorWheel(FX_ColorWheelPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FX_ColorWheel,_args,_kwargs)
        self.thisown = 1




class FXColorWheelPtr(FX_ColorWheelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(controlsc.FXColorWheel_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXColorWheel instance at %s>" % (self.this,)
class FXColorWheel(FXColorWheelPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(controlsc.new_FXColorWheel,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateFloatingToolbar(*_args, **_kwargs):
    val = apply(controlsc.CreateFloatingToolbar,_args,_kwargs)
    if val: val = FXToolbarPtr(val)
    return val

def CreateNonFloatingToolbar(*_args, **_kwargs):
    val = apply(controlsc.CreateNonFloatingToolbar,_args,_kwargs)
    if val: val = FXToolbarPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

JUSTIFY_NORMAL = controlsc.JUSTIFY_NORMAL
JUSTIFY_CENTER_X = controlsc.JUSTIFY_CENTER_X
JUSTIFY_LEFT = controlsc.JUSTIFY_LEFT
JUSTIFY_RIGHT = controlsc.JUSTIFY_RIGHT
JUSTIFY_HZ_APART = controlsc.JUSTIFY_HZ_APART
JUSTIFY_CENTER_Y = controlsc.JUSTIFY_CENTER_Y
JUSTIFY_TOP = controlsc.JUSTIFY_TOP
JUSTIFY_BOTTOM = controlsc.JUSTIFY_BOTTOM
JUSTIFY_VT_APART = controlsc.JUSTIFY_VT_APART
ICON_UNDER_TEXT = controlsc.ICON_UNDER_TEXT
ICON_AFTER_TEXT = controlsc.ICON_AFTER_TEXT
ICON_BEFORE_TEXT = controlsc.ICON_BEFORE_TEXT
ICON_ABOVE_TEXT = controlsc.ICON_ABOVE_TEXT
ICON_BELOW_TEXT = controlsc.ICON_BELOW_TEXT
TEXT_OVER_ICON = controlsc.TEXT_OVER_ICON
TEXT_AFTER_ICON = controlsc.TEXT_AFTER_ICON
TEXT_BEFORE_ICON = controlsc.TEXT_BEFORE_ICON
TEXT_ABOVE_ICON = controlsc.TEXT_ABOVE_ICON
TEXT_BELOW_ICON = controlsc.TEXT_BELOW_ICON
LABEL_NORMAL = controlsc.LABEL_NORMAL
DIAL_VERTICAL = controlsc.DIAL_VERTICAL
DIAL_HORIZONTAL = controlsc.DIAL_HORIZONTAL
DIAL_CYCLIC = controlsc.DIAL_CYCLIC
DIAL_HAS_NOTCH = controlsc.DIAL_HAS_NOTCH
DIAL_NORMAL = controlsc.DIAL_NORMAL
COLORWELL_OPAQUEONLY = controlsc.COLORWELL_OPAQUEONLY
COLORWELL_SOURCEONLY = controlsc.COLORWELL_SOURCEONLY
COLORWELL_NORMAL = controlsc.COLORWELL_NORMAL
TEXTFIELD_PASSWD = controlsc.TEXTFIELD_PASSWD
TEXTFIELD_INTEGER = controlsc.TEXTFIELD_INTEGER
TEXTFIELD_REAL = controlsc.TEXTFIELD_REAL
TEXTFIELD_READONLY = controlsc.TEXTFIELD_READONLY
TEXTFIELD_ENTER_ONLY = controlsc.TEXTFIELD_ENTER_ONLY
TEXTFIELD_LIMITED = controlsc.TEXTFIELD_LIMITED
TEXTFIELD_OVERSTRIKE = controlsc.TEXTFIELD_OVERSTRIKE
TEXTFIELD_NORMAL = controlsc.TEXTFIELD_NORMAL
STATE_UP = controlsc.STATE_UP
STATE_DOWN = controlsc.STATE_DOWN
STATE_ENGAGED = controlsc.STATE_ENGAGED
STATE_UNCHECKED = controlsc.STATE_UNCHECKED
STATE_CHECKED = controlsc.STATE_CHECKED
BUTTON_AUTOGRAY = controlsc.BUTTON_AUTOGRAY
BUTTON_AUTOHIDE = controlsc.BUTTON_AUTOHIDE
BUTTON_TOOLBAR = controlsc.BUTTON_TOOLBAR
BUTTON_DEFAULT = controlsc.BUTTON_DEFAULT
BUTTON_INITIAL = controlsc.BUTTON_INITIAL
BUTTON_NORMAL = controlsc.BUTTON_NORMAL
TOGGLEBUTTON_AUTOGRAY = controlsc.TOGGLEBUTTON_AUTOGRAY
TOGGLEBUTTON_AUTOHIDE = controlsc.TOGGLEBUTTON_AUTOHIDE
TOGGLEBUTTON_TOOLBAR = controlsc.TOGGLEBUTTON_TOOLBAR
TOGGLEBUTTON_NORMAL = controlsc.TOGGLEBUTTON_NORMAL
RADIOBUTTON_AUTOGRAY = controlsc.RADIOBUTTON_AUTOGRAY
RADIOBUTTON_AUTOHIDE = controlsc.RADIOBUTTON_AUTOHIDE
RADIOBUTTON_NORMAL = controlsc.RADIOBUTTON_NORMAL
CHECKBUTTON_AUTOGRAY = controlsc.CHECKBUTTON_AUTOGRAY
CHECKBUTTON_AUTOHIDE = controlsc.CHECKBUTTON_AUTOHIDE
CHECKBUTTON_NORMAL = controlsc.CHECKBUTTON_NORMAL
ARROW_NONE = controlsc.ARROW_NONE
ARROW_UP = controlsc.ARROW_UP
ARROW_DOWN = controlsc.ARROW_DOWN
ARROW_LEFT = controlsc.ARROW_LEFT
ARROW_RIGHT = controlsc.ARROW_RIGHT
ARROW_REPEAT = controlsc.ARROW_REPEAT
ARROW_AUTOGRAY = controlsc.ARROW_AUTOGRAY
ARROW_AUTOHIDE = controlsc.ARROW_AUTOHIDE
ARROW_TOOLBAR = controlsc.ARROW_TOOLBAR
ARROW_NORMAL = controlsc.ARROW_NORMAL
SPIN_NORMAL = controlsc.SPIN_NORMAL
SPIN_CYCLIC = controlsc.SPIN_CYCLIC
SPIN_NOTEXT = controlsc.SPIN_NOTEXT
SPIN_NOMAX = controlsc.SPIN_NOMAX
SPIN_NOMIN = controlsc.SPIN_NOMIN
TOOLTIP_NORMAL = controlsc.TOOLTIP_NORMAL
TOOLTIP_PERMANENT = controlsc.TOOLTIP_PERMANENT
TOOLTIP_VARIABLE = controlsc.TOOLTIP_VARIABLE
TAB_TOP = controlsc.TAB_TOP
TAB_LEFT = controlsc.TAB_LEFT
TAB_RIGHT = controlsc.TAB_RIGHT
TAB_BOTTOM = controlsc.TAB_BOTTOM
TAB_TOP_NORMAL = controlsc.TAB_TOP_NORMAL
TAB_BOTTOM_NORMAL = controlsc.TAB_BOTTOM_NORMAL
TAB_LEFT_NORMAL = controlsc.TAB_LEFT_NORMAL
TAB_RIGHT_NORMAL = controlsc.TAB_RIGHT_NORMAL
TABBOOK_TOPTABS = controlsc.TABBOOK_TOPTABS
TABBOOK_BOTTOMTABS = controlsc.TABBOOK_BOTTOMTABS
TABBOOK_SIDEWAYS = controlsc.TABBOOK_SIDEWAYS
TABBOOK_LEFTTABS = controlsc.TABBOOK_LEFTTABS
TABBOOK_RIGHTTABS = controlsc.TABBOOK_RIGHTTABS
TABBOOK_NORMAL = controlsc.TABBOOK_NORMAL
SCROLLBAR_HORIZONTAL = controlsc.SCROLLBAR_HORIZONTAL
SCROLLBAR_VERTICAL = controlsc.SCROLLBAR_VERTICAL
LIST_EXTENDEDSELECT = controlsc.LIST_EXTENDEDSELECT
LIST_SINGLESELECT = controlsc.LIST_SINGLESELECT
LIST_BROWSESELECT = controlsc.LIST_BROWSESELECT
LIST_MULTIPLESELECT = controlsc.LIST_MULTIPLESELECT
LIST_AUTOSELECT = controlsc.LIST_AUTOSELECT
LIST_NORMAL = controlsc.LIST_NORMAL
COMBOBOX_NO_REPLACE = controlsc.COMBOBOX_NO_REPLACE
COMBOBOX_REPLACE = controlsc.COMBOBOX_REPLACE
COMBOBOX_INSERT_BEFORE = controlsc.COMBOBOX_INSERT_BEFORE
COMBOBOX_INSERT_AFTER = controlsc.COMBOBOX_INSERT_AFTER
COMBOBOX_INSERT_FIRST = controlsc.COMBOBOX_INSERT_FIRST
COMBOBOX_INSERT_LAST = controlsc.COMBOBOX_INSERT_LAST
COMBOBOX_STATIC = controlsc.COMBOBOX_STATIC
COMBOBOX_NORMAL = controlsc.COMBOBOX_NORMAL
STATUSBAR_WITH_DRAGCORNER = controlsc.STATUSBAR_WITH_DRAGCORNER
SLIDERBAR_SIZE = controlsc.SLIDERBAR_SIZE
SLIDERHEAD_SIZE = controlsc.SLIDERHEAD_SIZE
SLIDER_HORIZONTAL = controlsc.SLIDER_HORIZONTAL
SLIDER_VERTICAL = controlsc.SLIDER_VERTICAL
SLIDER_ARROW_UP = controlsc.SLIDER_ARROW_UP
SLIDER_ARROW_DOWN = controlsc.SLIDER_ARROW_DOWN
SLIDER_ARROW_LEFT = controlsc.SLIDER_ARROW_LEFT
SLIDER_ARROW_RIGHT = controlsc.SLIDER_ARROW_RIGHT
SLIDER_INSIDE_BAR = controlsc.SLIDER_INSIDE_BAR
SLIDER_TICKS_TOP = controlsc.SLIDER_TICKS_TOP
SLIDER_TICKS_BOTTOM = controlsc.SLIDER_TICKS_BOTTOM
SLIDER_TICKS_LEFT = controlsc.SLIDER_TICKS_LEFT
SLIDER_TICKS_RIGHT = controlsc.SLIDER_TICKS_RIGHT
SLIDER_NORMAL = controlsc.SLIDER_NORMAL
HEADER_BUTTON = controlsc.HEADER_BUTTON
HEADER_HORIZONTAL = controlsc.HEADER_HORIZONTAL
HEADER_VERTICAL = controlsc.HEADER_VERTICAL
HEADER_TRACKING = controlsc.HEADER_TRACKING
HEADER_NORMAL = controlsc.HEADER_NORMAL
PROGRESSBAR_HORIZONTAL = controlsc.PROGRESSBAR_HORIZONTAL
PROGRESSBAR_VERTICAL = controlsc.PROGRESSBAR_VERTICAL
PROGRESSBAR_PERCENTAGE = controlsc.PROGRESSBAR_PERCENTAGE
PROGRESSBAR_DIAL = controlsc.PROGRESSBAR_DIAL
PROGRESSBAR_NORMAL = controlsc.PROGRESSBAR_NORMAL
TOOLBARTAB_HORIZONTAL = controlsc.TOOLBARTAB_HORIZONTAL
TOOLBARTAB_VERTICAL = controlsc.TOOLBARTAB_VERTICAL
TOOLBARGRIP_SINGLE = controlsc.TOOLBARGRIP_SINGLE
TOOLBARGRIP_DOUBLE = controlsc.TOOLBARGRIP_DOUBLE
TOOLBARGRIP_SEPARATOR = controlsc.TOOLBARGRIP_SEPARATOR
LISTBOX_NORMAL = controlsc.LISTBOX_NORMAL
COLORBAR_HORIZONTAL = controlsc.COLORBAR_HORIZONTAL
COLORBAR_VERTICAL = controlsc.COLORBAR_VERTICAL
cvar = controlsc.cvar
