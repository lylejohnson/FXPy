# This file was created automatically by SWIG.
import graphicsc

from misc import *

from containers import *

from windows import *
import fox
class FX_BitmapPtr(FX_DrawablePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def create(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_destroy,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_render,(self,) + _args, _kwargs)
        return val
    def getPixel(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_getPixel,(self,) + _args, _kwargs)
        return val
    def setPixel(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_setPixel,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_resize,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Bitmap_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Bitmap instance at %s>" % (self.this,)
class FX_Bitmap(FX_BitmapPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FX_Bitmap,_args,_kwargs)
        self.thisown = 1




class FXBitmapPtr(FX_BitmapPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXBitmap_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(graphicsc.FXBitmap_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(graphicsc.FXBitmap_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(graphicsc.FXBitmap_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(graphicsc.FXBitmap_resize,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXBitmap instance at %s>" % (self.this,)
class FXBitmap(FXBitmapPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FXBitmap,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CursorPtr(FX_IdPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getHotX(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_getHotX,(self,) + _args, _kwargs)
        return val
    def getHotY(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_getHotY,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_getHeight,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_destroy,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_Cursor_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Cursor instance at %s>" % (self.this,)
class FX_Cursor(FX_CursorPtr):
    def __init__(self,this):
        self.this = this




class FXCursorPtr(FX_CursorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCursor_onDefault,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCursor_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCursor_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXCursor instance at %s>" % (self.this,)
class FXCursor(FXCursorPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(graphicsc.CreateStockCursor,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(graphicsc.CreateCursorFromMask,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_GIFCursorPtr(FX_CursorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_GIFCursor instance at %s>" % (self.this,)
class FX_GIFCursor(FX_GIFCursorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FX_GIFCursor,_args,_kwargs)
        self.thisown = 1




class FXGIFCursorPtr(FX_GIFCursorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXGIFCursor_onDefault,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXGIFCursor_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXGIFCursor_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGIFCursor instance at %s>" % (self.this,)
class FXGIFCursor(FXGIFCursorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FXGIFCursor,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CURCursorPtr(FX_CursorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_CURCursor instance at %s>" % (self.this,)
class FX_CURCursor(FX_CURCursorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FX_CURCursor,_args,_kwargs)
        self.thisown = 1




class FXCURCursorPtr(FX_CURCursorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCURCursor_onDefault,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCURCursor_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(graphicsc.FXCURCursor_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXCURCursor instance at %s>" % (self.this,)
class FXCURCursor(FXCURCursorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FXCURCursor,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ImageViewPtr(FX_ScrollAreaPtr):
    ID_XYZ = graphicsc.FX_ImageView_ID_XYZ
    ID_LAST = graphicsc.FX_ImageView_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_onPaint,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_onMotion,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def setImage(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_setImage,(self,) + _args, _kwargs)
        return val
    def getImage(self, *_args, **_kwargs):
        val = apply(graphicsc.FX_ImageView_getImage,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ImageView instance at %s>" % (self.this,)
class FX_ImageView(FX_ImageViewPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FX_ImageView,_args,_kwargs)
        self.thisown = 1




class FXImageViewPtr(FX_ImageViewPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(graphicsc.FXImageView_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXImageView instance at %s>" % (self.this,)
class FXImageView(FXImageViewPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(graphicsc.new_FXImageView,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateStockCursor(*_args, **_kwargs):
    val = apply(graphicsc.CreateStockCursor,_args,_kwargs)
    if val: val = FXCursorPtr(val)
    return val

def CreateCursorFromMask(*_args, **_kwargs):
    val = apply(graphicsc.CreateCursorFromMask,_args,_kwargs)
    if val: val = FXCursorPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

BITMAP_KEEP = graphicsc.BITMAP_KEEP
BITMAP_OWNED = graphicsc.BITMAP_OWNED
BITMAP_SHMI = graphicsc.BITMAP_SHMI
BITMAP_SHMP = graphicsc.BITMAP_SHMP
CURSOR_ARROW = graphicsc.CURSOR_ARROW
CURSOR_RARROW = graphicsc.CURSOR_RARROW
CURSOR_IBEAM = graphicsc.CURSOR_IBEAM
CURSOR_WATCH = graphicsc.CURSOR_WATCH
CURSOR_CROSS = graphicsc.CURSOR_CROSS
CURSOR_UPDOWN = graphicsc.CURSOR_UPDOWN
CURSOR_LEFTRIGHT = graphicsc.CURSOR_LEFTRIGHT
CURSOR_MOVE = graphicsc.CURSOR_MOVE
