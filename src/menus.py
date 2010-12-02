# This file was created automatically by SWIG.
import menusc

from windows import *

from misc import *

from containers import *

from controls import *
import fox
class FX_MenuSeparatorPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuSeparator_onPaint,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuSeparator_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuSeparator_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuSeparator_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuSeparator_getShadowColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuSeparator instance at %s>" % (self.this,)
class FX_MenuSeparator(FX_MenuSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuSeparator,_args,_kwargs)
        self.thisown = 1




class FXMenuSeparatorPtr(FX_MenuSeparatorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuSeparator_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuSeparator instance at %s>" % (self.this,)
class FXMenuSeparator(FXMenuSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuSeparator,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenuCaptionPtr(FX_WindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_onPaint,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_onUpdate,(self,) + _args, _kwargs)
        return val
    def onCmdGetStringValue(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_onCmdGetStringValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetStringValue(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_onCmdSetStringValue,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getText,(self,) + _args, _kwargs)
        return val
    def setIcon(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setIcon,(self,) + _args, _kwargs)
        return val
    def getIcon(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getIcon,(self,) + _args, _kwargs)
        return val
    def setFont(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setFont,(self,) + _args, _kwargs)
        return val
    def getFont(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getFont,(self,) + _args, _kwargs)
        return val
    def getTextColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getTextColor,(self,) + _args, _kwargs)
        return val
    def setTextColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setTextColor,(self,) + _args, _kwargs)
        return val
    def getSelBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getSelBackColor,(self,) + _args, _kwargs)
        return val
    def setSelBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setSelBackColor,(self,) + _args, _kwargs)
        return val
    def getSelTextColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getSelTextColor,(self,) + _args, _kwargs)
        return val
    def setSelTextColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setSelTextColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setShadowColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getShadowColor,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCaption_getHelpText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuCaption instance at %s>" % (self.this,)
class FX_MenuCaption(FX_MenuCaptionPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuCaption,_args,_kwargs)
        self.thisown = 1




class FXMenuCaptionPtr(FX_MenuCaptionPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCaption_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuCaption instance at %s>" % (self.this,)
class FXMenuCaption(FXMenuCaptionPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuCaption,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenuPanePtr(FX_PopupPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_MenuPane instance at %s>" % (self.this,)
class FX_MenuPane(FX_MenuPanePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuPane,_args,_kwargs)
        self.thisown = 1




class FXMenuPanePtr(FX_MenuPanePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_setBackColor,(self,) + _args, _kwargs)
        return val
    def popup(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_popup,(self,) + _args, _kwargs)
        return val
    def popdown(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuPane_popdown,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuPane instance at %s>" % (self.this,)
class FXMenuPane(FXMenuPanePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuPane,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenubarPtr(FX_ToolbarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onFocusRight,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onLeave,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onMotion,(self,) + _args, _kwargs)
        return val
    def onButtonPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onButtonPress,(self,) + _args, _kwargs)
        return val
    def onButtonRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onButtonRelease,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(menusc.FX_Menubar_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Menubar instance at %s>" % (self.this,)
class FX_Menubar(FX_MenubarPtr):
    def __init__(self,this):
        self.this = this




class FXMenubarPtr(FX_MenubarPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_setBackColor,(self,) + _args, _kwargs)
        return val
    def dock(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_dock,(self,) + _args, _kwargs)
        return val
    def undock(self, *_args, **_kwargs):
        val = apply(menusc.FXMenubar_undock,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenubar instance at %s>" % (self.this,)
class FXMenubar(FXMenubarPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(menusc.CreateFloatingMenubar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(menusc.CreateNonFloatingMenubar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_MenuButtonPtr(FX_LabelPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onPaint,(self,) + _args, _kwargs)
        return val
    def onUpdate(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onUpdate,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onLeave,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onMotion,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdPost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onCmdPost,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def setMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setMenu,(self,) + _args, _kwargs)
        return val
    def getMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getMenu,(self,) + _args, _kwargs)
        return val
    def setXOffset(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setXOffset,(self,) + _args, _kwargs)
        return val
    def getXOffset(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getXOffset,(self,) + _args, _kwargs)
        return val
    def setYOffset(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setYOffset,(self,) + _args, _kwargs)
        return val
    def getYOffset(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getYOffset,(self,) + _args, _kwargs)
        return val
    def setButtonStyle(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setButtonStyle,(self,) + _args, _kwargs)
        return val
    def getButtonStyle(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getButtonStyle,(self,) + _args, _kwargs)
        return val
    def setPopupStyle(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setPopupStyle,(self,) + _args, _kwargs)
        return val
    def getPopupStyle(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getPopupStyle,(self,) + _args, _kwargs)
        return val
    def setAttachment(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_setAttachment,(self,) + _args, _kwargs)
        return val
    def getAttachment(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuButton_getAttachment,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuButton instance at %s>" % (self.this,)
class FX_MenuButton(FX_MenuButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuButton,_args,_kwargs)
        self.thisown = 1




class FXMenuButtonPtr(FX_MenuButtonPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuButton_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuButton instance at %s>" % (self.this,)
class FXMenuButton(FXMenuButtonPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuButton,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenuCascadePtr(FX_MenuCaptionPtr):
    ID_MENUTIMER = menusc.FX_MenuCascade_ID_MENUTIMER
    ID_LAST = menusc.FX_MenuCascade_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onLeave,(self,) + _args, _kwargs)
        return val
    def onTimeout(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onTimeout,(self,) + _args, _kwargs)
        return val
    def onButtonPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onButtonPress,(self,) + _args, _kwargs)
        return val
    def onButtonRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onButtonRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCmdPost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onCmdPost,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def setMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_setMenu,(self,) + _args, _kwargs)
        return val
    def getMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCascade_getMenu,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuCascade instance at %s>" % (self.this,)
class FX_MenuCascade(FX_MenuCascadePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuCascade,_args,_kwargs)
        self.thisown = 1




class FXMenuCascadePtr(FX_MenuCascadePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCascade_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuCascade instance at %s>" % (self.this,)
class FXMenuCascade(FXMenuCascadePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuCascade,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenuCommandPtr(FX_MenuCaptionPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onLeave,(self,) + _args, _kwargs)
        return val
    def onButtonPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onButtonPress,(self,) + _args, _kwargs)
        return val
    def onButtonRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onButtonRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onCheck(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onCheck,(self,) + _args, _kwargs)
        return val
    def onUncheck(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onUncheck,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdAccel(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_onCmdAccel,(self,) + _args, _kwargs)
        return val
    def check(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_check,(self,) + _args, _kwargs)
        return val
    def uncheck(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_uncheck,(self,) + _args, _kwargs)
        return val
    def isChecked(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_isChecked,(self,) + _args, _kwargs)
        return val
    def checkRadio(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_checkRadio,(self,) + _args, _kwargs)
        return val
    def uncheckRadio(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_uncheckRadio,(self,) + _args, _kwargs)
        return val
    def isRadioChecked(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_isRadioChecked,(self,) + _args, _kwargs)
        return val
    def setAccelText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_setAccelText,(self,) + _args, _kwargs)
        return val
    def getAccelText(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuCommand_getAccelText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuCommand instance at %s>" % (self.this,)
class FX_MenuCommand(FX_MenuCommandPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuCommand,_args,_kwargs)
        self.thisown = 1




class FXMenuCommandPtr(FX_MenuCommandPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuCommand_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuCommand instance at %s>" % (self.this,)
class FXMenuCommand(FXMenuCommandPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuCommand,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MenuTitlePtr(FX_MenuCaptionPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onLeave,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onHotKeyPress(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onHotKeyPress,(self,) + _args, _kwargs)
        return val
    def onHotKeyRelease(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onHotKeyRelease,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onCmdPost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onCmdPost,(self,) + _args, _kwargs)
        return val
    def onCmdUnpost(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_onCmdUnpost,(self,) + _args, _kwargs)
        return val
    def setMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_setMenu,(self,) + _args, _kwargs)
        return val
    def getMenu(self, *_args, **_kwargs):
        val = apply(menusc.FX_MenuTitle_getMenu,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_MenuTitle instance at %s>" % (self.this,)
class FX_MenuTitle(FX_MenuTitlePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FX_MenuTitle,_args,_kwargs)
        self.thisown = 1




class FXMenuTitlePtr(FX_MenuTitlePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(menusc.FXMenuTitle_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMenuTitle instance at %s>" % (self.this,)
class FXMenuTitle(FXMenuTitlePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(menusc.new_FXMenuTitle,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateFloatingMenubar(*_args, **_kwargs):
    val = apply(menusc.CreateFloatingMenubar,_args,_kwargs)
    if val: val = FXMenubarPtr(val)
    return val

def CreateNonFloatingMenubar(*_args, **_kwargs):
    val = apply(menusc.CreateNonFloatingMenubar,_args,_kwargs)
    if val: val = FXMenubarPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

MENU_AUTOGRAY = menusc.MENU_AUTOGRAY
MENU_AUTOHIDE = menusc.MENU_AUTOHIDE
MENUBUTTON_AUTOGRAY = menusc.MENUBUTTON_AUTOGRAY
MENUBUTTON_AUTOHIDE = menusc.MENUBUTTON_AUTOHIDE
MENUBUTTON_TOOLBAR = menusc.MENUBUTTON_TOOLBAR
MENUBUTTON_DOWN = menusc.MENUBUTTON_DOWN
MENUBUTTON_UP = menusc.MENUBUTTON_UP
MENUBUTTON_LEFT = menusc.MENUBUTTON_LEFT
MENUBUTTON_RIGHT = menusc.MENUBUTTON_RIGHT
MENUBUTTON_NOARROWS = menusc.MENUBUTTON_NOARROWS
MENUBUTTON_ATTACH_LEFT = menusc.MENUBUTTON_ATTACH_LEFT
MENUBUTTON_ATTACH_TOP = menusc.MENUBUTTON_ATTACH_TOP
MENUBUTTON_ATTACH_RIGHT = menusc.MENUBUTTON_ATTACH_RIGHT
MENUBUTTON_ATTACH_BOTTOM = menusc.MENUBUTTON_ATTACH_BOTTOM
MENUBUTTON_ATTACH_CENTER = menusc.MENUBUTTON_ATTACH_CENTER
MENUBUTTON_ATTACH_BOTH = menusc.MENUBUTTON_ATTACH_BOTH
MENUSTATE_NORMAL = menusc.MENUSTATE_NORMAL
MENUSTATE_CHECKED = menusc.MENUSTATE_CHECKED
MENUSTATE_RCHECKED = menusc.MENUSTATE_RCHECKED
cvar = menusc.cvar
