# This file was created automatically by SWIG.
import containersc

from misc import *

from windows import *
import fox
class FXSegmentPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "x1" :
            containersc.FXSegment_x1_set(self,value)
            return
        if name == "y1" :
            containersc.FXSegment_y1_set(self,value)
            return
        if name == "x2" :
            containersc.FXSegment_x2_set(self,value)
            return
        if name == "y2" :
            containersc.FXSegment_y2_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "x1" : 
            return containersc.FXSegment_x1_get(self)
        if name == "y1" : 
            return containersc.FXSegment_y1_get(self)
        if name == "x2" : 
            return containersc.FXSegment_x2_get(self)
        if name == "y2" : 
            return containersc.FXSegment_y2_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXSegment instance at %s>" % (self.this,)
class FXSegment(FXSegmentPtr):
    def __init__(self,this):
        self.this = this




class FXArcPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "x" :
            containersc.FXArc_x_set(self,value)
            return
        if name == "y" :
            containersc.FXArc_y_set(self,value)
            return
        if name == "w" :
            containersc.FXArc_w_set(self,value)
            return
        if name == "h" :
            containersc.FXArc_h_set(self,value)
            return
        if name == "a" :
            containersc.FXArc_a_set(self,value)
            return
        if name == "b" :
            containersc.FXArc_b_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "x" : 
            return containersc.FXArc_x_get(self)
        if name == "y" : 
            return containersc.FXArc_y_get(self)
        if name == "w" : 
            return containersc.FXArc_w_get(self)
        if name == "h" : 
            return containersc.FXArc_h_get(self)
        if name == "a" : 
            return containersc.FXArc_a_get(self)
        if name == "b" : 
            return containersc.FXArc_b_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXArc instance at %s>" % (self.this,)
class FXArc(FXArcPtr):
    def __init__(self,this):
        self.this = this




class FX_DCPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getApp(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getApp,(self,) + _args, _kwargs)
        return val
    def readPixel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_readPixel,(self,) + _args, _kwargs)
        return val
    def drawPoint(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawPoint,(self,) + _args, _kwargs)
        return val
    def drawPoints(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawPoints,(self,) + _args, _kwargs)
        return val
    def drawPointsRel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawPointsRel,(self,) + _args, _kwargs)
        return val
    def drawLine(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawLine,(self,) + _args, _kwargs)
        return val
    def drawLines(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawLines,(self,) + _args, _kwargs)
        return val
    def drawLinesRel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawLinesRel,(self,) + _args, _kwargs)
        return val
    def drawLineSegments(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawLineSegments,(self,) + _args, _kwargs)
        return val
    def drawRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawRectangle,(self,) + _args, _kwargs)
        return val
    def drawRectangles(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawRectangles,(self,) + _args, _kwargs)
        return val
    def drawArc(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawArc,(self,) + _args, _kwargs)
        return val
    def drawArcs(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawArcs,(self,) + _args, _kwargs)
        return val
    def fillRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillRectangle,(self,) + _args, _kwargs)
        return val
    def fillRectangles(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillRectangles,(self,) + _args, _kwargs)
        return val
    def fillArc(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillArc,(self,) + _args, _kwargs)
        return val
    def fillArcs(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillArcs,(self,) + _args, _kwargs)
        return val
    def fillPolygon(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillPolygon,(self,) + _args, _kwargs)
        return val
    def fillConcavePolygon(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillConcavePolygon,(self,) + _args, _kwargs)
        return val
    def fillComplexPolygon(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillComplexPolygon,(self,) + _args, _kwargs)
        return val
    def fillPolygonRel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillPolygonRel,(self,) + _args, _kwargs)
        return val
    def fillConcavePolygonRel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillConcavePolygonRel,(self,) + _args, _kwargs)
        return val
    def fillComplexPolygonRel(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_fillComplexPolygonRel,(self,) + _args, _kwargs)
        return val
    def drawHashBox(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawHashBox,(self,) + _args, _kwargs)
        return val
    def drawFocusRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawFocusRectangle,(self,) + _args, _kwargs)
        return val
    def drawArea(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawArea,(self,) + _args, _kwargs)
        return val
    def drawImage(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawImage,(self,) + _args, _kwargs)
        return val
    def drawBitmap(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawBitmap,(self,) + _args, _kwargs)
        return val
    def drawIcon(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawIcon,(self,) + _args, _kwargs)
        return val
    def drawIconShaded(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawIconShaded,(self,) + _args, _kwargs)
        return val
    def drawIconSunken(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawIconSunken,(self,) + _args, _kwargs)
        return val
    def drawText(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawText,(self,) + _args, _kwargs)
        return val
    def drawImageText(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_drawImageText,(self,) + _args, _kwargs)
        return val
    def setForeground(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setForeground,(self,) + _args, _kwargs)
        return val
    def setBackground(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setBackground,(self,) + _args, _kwargs)
        return val
    def setDashes(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setDashes,(self,) + _args, _kwargs)
        return val
    def getDashPattern(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getDashPattern,(self,) + _args, _kwargs)
        return val
    def getDashOffset(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getDashOffset,(self,) + _args, _kwargs)
        return val
    def getDashLength(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getDashLength,(self,) + _args, _kwargs)
        return val
    def setLineWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setLineWidth,(self,) + _args, _kwargs)
        return val
    def getLineWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getLineWidth,(self,) + _args, _kwargs)
        return val
    def setLineCap(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setLineCap,(self,) + _args, _kwargs)
        return val
    def getLineCap(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getLineCap,(self,) + _args, _kwargs)
        return val
    def setLineJoin(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setLineJoin,(self,) + _args, _kwargs)
        return val
    def getLineJoin(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getLineJoin,(self,) + _args, _kwargs)
        return val
    def setLineStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setLineStyle,(self,) + _args, _kwargs)
        return val
    def getLineStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getLineStyle,(self,) + _args, _kwargs)
        return val
    def setFillStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setFillStyle,(self,) + _args, _kwargs)
        return val
    def getFillStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getFillStyle,(self,) + _args, _kwargs)
        return val
    def setFillRule(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setFillRule,(self,) + _args, _kwargs)
        return val
    def getFillRule(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getFillRule,(self,) + _args, _kwargs)
        return val
    def setFunction(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setFunction,(self,) + _args, _kwargs)
        return val
    def getFunction(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getFunction,(self,) + _args, _kwargs)
        return val
    def setTile(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setTile,(self,) + _args, _kwargs)
        return val
    def getTile(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getTile,(self,) + _args, _kwargs)
        return val
    def setStipple(self, *_args, **_kwargs):
        try:
            val = apply(containersc.FX_DC_setStipple,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(containersc.FX_DC_setStipple2,(self,) + _args, _kwargs)
            return val
    def getStippleBitmap(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getStippleBitmap,(self,) + _args, _kwargs)
        return val
    def setStipple2(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setStipple2,(self,) + _args, _kwargs)
        return val
    def getStipplePattern(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getStipplePattern,(self,) + _args, _kwargs)
        return val
    def setClipRegion(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setClipRegion,(self,) + _args, _kwargs)
        return val
    def setClipRectangle2(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setClipRectangle2,(self,) + _args, _kwargs)
        return val
    def getClipRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getClipRectangle,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def setClipRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setClipRectangle,(self,) + _args, _kwargs)
        return val
    def getClipX(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getClipX,(self,) + _args, _kwargs)
        return val
    def getClipY(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getClipY,(self,) + _args, _kwargs)
        return val
    def getClipWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getClipWidth,(self,) + _args, _kwargs)
        return val
    def getClipHeight(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getClipHeight,(self,) + _args, _kwargs)
        return val
    def clearClipRectangle(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_clearClipRectangle,(self,) + _args, _kwargs)
        return val
    def setClipMask(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setClipMask,(self,) + _args, _kwargs)
        return val
    def clearClipMask(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_clearClipMask,(self,) + _args, _kwargs)
        return val
    def setTextFont(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_setTextFont,(self,) + _args, _kwargs)
        return val
    def getTextFont(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_getTextFont,(self,) + _args, _kwargs)
        return val
    def clipChildren(self, *_args, **_kwargs):
        val = apply(containersc.FX_DC_clipChildren,(self,) + _args, _kwargs)
        return val
    def __del__(self,containersc=containersc):
        if self.thisown == 1 :
            containersc.delete_FX_DC(self)
    def __repr__(self):
        return "<C FX_DC instance at %s>" % (self.this,)
class FX_DC(FX_DCPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_DC,_args,_kwargs)
        self.thisown = 1




class FXDCPtr(FX_DCPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXDC instance at %s>" % (self.this,)
class FXDC(FXDCPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXDC,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DCWindowPtr(FX_DCPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def begin(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCWindow_begin,(self,) + _args, _kwargs)
        return val
    def end(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCWindow_end,(self,) + _args, _kwargs)
        return val
    def __del__(self,containersc=containersc):
        if self.thisown == 1 :
            containersc.delete_FX_DCWindow(self)
    def __repr__(self):
        return "<C FX_DCWindow instance at %s>" % (self.this,)
class FX_DCWindow(FX_DCWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_DCWindow,_args,_kwargs)
        self.thisown = 1




class FXDCWindowPtr(FX_DCWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXDCWindow instance at %s>" % (self.this,)
class FXDCWindow(FXDCWindowPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.CreateDCWindow,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.CreateClippedDCWindow,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_DCPrintPtr(FX_DCPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def beginPrint(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCPrint_beginPrint,(self,) + _args, _kwargs)
        return val
    def endPrint(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCPrint_endPrint,(self,) + _args, _kwargs)
        return val
    def beginPage(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCPrint_beginPage,(self,) + _args, _kwargs)
        return val
    def endPage(self, *_args, **_kwargs):
        val = apply(containersc.FX_DCPrint_endPage,(self,) + _args, _kwargs)
        return val
    def __del__(self,containersc=containersc):
        if self.thisown == 1 :
            containersc.delete_FX_DCPrint(self)
    def __repr__(self):
        return "<C FX_DCPrint instance at %s>" % (self.this,)
class FX_DCPrint(FX_DCPrintPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_DCPrint,_args,_kwargs)
        self.thisown = 1




class FXDCPrintPtr(FX_DCPrintPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXDCPrint instance at %s>" % (self.this,)
class FXDCPrint(FXDCPrintPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXDCPrint,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_HorizontalSeparatorPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_HorizontalSeparator instance at %s>" % (self.this,)
class FX_HorizontalSeparator(FX_HorizontalSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_HorizontalSeparator,_args,_kwargs)
        self.thisown = 1




class FXHorizontalSeparatorPtr(FX_HorizontalSeparatorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalSeparator_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXHorizontalSeparator instance at %s>" % (self.this,)
class FXHorizontalSeparator(FXHorizontalSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXHorizontalSeparator,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_VerticalSeparatorPtr(FX_FramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_VerticalSeparator instance at %s>" % (self.this,)
class FX_VerticalSeparator(FX_VerticalSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_VerticalSeparator,_args,_kwargs)
        self.thisown = 1




class FXVerticalSeparatorPtr(FX_VerticalSeparatorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalSeparator_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXVerticalSeparator instance at %s>" % (self.this,)
class FXVerticalSeparator(FXVerticalSeparatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXVerticalSeparator,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PackerPtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_onPaint,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_onFocusRight,(self,) + _args, _kwargs)
        return val
    def setFrameStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setFrameStyle,(self,) + _args, _kwargs)
        return val
    def getFrameStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getFrameStyle,(self,) + _args, _kwargs)
        return val
    def setPackingHints(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setPackingHints,(self,) + _args, _kwargs)
        return val
    def getPackingHints(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getPackingHints,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getShadowColor,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getBorderColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getBaseColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setShadowColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setBorderColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setBaseColor,(self,) + _args, _kwargs)
        return val
    def getPadTop(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getPadTop,(self,) + _args, _kwargs)
        return val
    def getPadBottom(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getPadBottom,(self,) + _args, _kwargs)
        return val
    def getPadLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getPadLeft,(self,) + _args, _kwargs)
        return val
    def getPadRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getPadRight,(self,) + _args, _kwargs)
        return val
    def setPadTop(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setPadTop,(self,) + _args, _kwargs)
        return val
    def setPadBottom(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setPadBottom,(self,) + _args, _kwargs)
        return val
    def setPadLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setPadLeft,(self,) + _args, _kwargs)
        return val
    def setPadRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setPadRight,(self,) + _args, _kwargs)
        return val
    def getHSpacing(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getHSpacing,(self,) + _args, _kwargs)
        return val
    def getVSpacing(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getVSpacing,(self,) + _args, _kwargs)
        return val
    def setHSpacing(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setHSpacing,(self,) + _args, _kwargs)
        return val
    def setVSpacing(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_setVSpacing,(self,) + _args, _kwargs)
        return val
    def getBorderWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_Packer_getBorderWidth,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Packer instance at %s>" % (self.this,)
class FX_Packer(FX_PackerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_Packer,_args,_kwargs)
        self.thisown = 1




class FXPackerPtr(FX_PackerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXPacker_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPacker instance at %s>" % (self.this,)
class FXPacker(FXPackerPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXPacker,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_HorizontalFramePtr(FX_PackerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_HorizontalFrame instance at %s>" % (self.this,)
class FX_HorizontalFrame(FX_HorizontalFramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_HorizontalFrame,_args,_kwargs)
        self.thisown = 1




class FXHorizontalFramePtr(FX_HorizontalFramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXHorizontalFrame_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXHorizontalFrame instance at %s>" % (self.this,)
class FXHorizontalFrame(FXHorizontalFramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXHorizontalFrame,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_VerticalFramePtr(FX_PackerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_VerticalFrame instance at %s>" % (self.this,)
class FX_VerticalFrame(FX_VerticalFramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_VerticalFrame,_args,_kwargs)
        self.thisown = 1




class FXVerticalFramePtr(FX_VerticalFramePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXVerticalFrame_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXVerticalFrame instance at %s>" % (self.this,)
class FXVerticalFrame(FXVerticalFramePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXVerticalFrame,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_MatrixPtr(FX_PackerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_onFocusRight,(self,) + _args, _kwargs)
        return val
    def childAtRowCol(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_childAtRowCol,(self,) + _args, _kwargs)
        return val
    def rowOfChild(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_rowOfChild,(self,) + _args, _kwargs)
        return val
    def colOfChild(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_colOfChild,(self,) + _args, _kwargs)
        return val
    def setMatrixStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_setMatrixStyle,(self,) + _args, _kwargs)
        return val
    def getMatrixStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_getMatrixStyle,(self,) + _args, _kwargs)
        return val
    def setNumRows(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_setNumRows,(self,) + _args, _kwargs)
        return val
    def getNumRows(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_getNumRows,(self,) + _args, _kwargs)
        return val
    def setNumColumns(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_setNumColumns,(self,) + _args, _kwargs)
        return val
    def getNumColumns(self, *_args, **_kwargs):
        val = apply(containersc.FX_Matrix_getNumColumns,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Matrix instance at %s>" % (self.this,)
class FX_Matrix(FX_MatrixPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_Matrix,_args,_kwargs)
        self.thisown = 1




class FXMatrixPtr(FX_MatrixPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXMatrix_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXMatrix instance at %s>" % (self.this,)
class FXMatrix(FXMatrixPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXMatrix,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GroupBoxPtr(FX_PackerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(containersc.FX_GroupBox_onPaint,(self,) + _args, _kwargs)
        return val
    def onUncheckOther(self, *_args, **_kwargs):
        val = apply(containersc.FX_GroupBox_onUncheckOther,(self,) + _args, _kwargs)
        return val
    def setText(self, *_args, **_kwargs):
        val = apply(containersc.FX_GroupBox_setText,(self,) + _args, _kwargs)
        return val
    def getText(self, *_args, **_kwargs):
        val = apply(containersc.FX_GroupBox_getText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GroupBox instance at %s>" % (self.this,)
class FX_GroupBox(FX_GroupBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_GroupBox,_args,_kwargs)
        self.thisown = 1




class FXGroupBoxPtr(FX_GroupBoxPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXGroupBox_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGroupBox instance at %s>" % (self.this,)
class FXGroupBox(FXGroupBoxPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXGroupBox,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_SwitcherPtr(FX_PackerPtr):
    ID_OPEN_FIRST = containersc.FX_Switcher_ID_OPEN_FIRST
    ID_OPEN_LAST = containersc.FX_Switcher_ID_OPEN_LAST
    ID_LAST = containersc.FX_Switcher_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onPaint,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdOpen(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onCmdOpen,(self,) + _args, _kwargs)
        return val
    def onUpdOpen(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_onUpdOpen,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_setCurrent,(self,) + _args, _kwargs)
        return val
    def getCurrent(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_getCurrent,(self,) + _args, _kwargs)
        return val
    def setSwitcherStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_setSwitcherStyle,(self,) + _args, _kwargs)
        return val
    def getSwitcherStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Switcher_getSwitcherStyle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Switcher instance at %s>" % (self.this,)
class FX_Switcher(FX_SwitcherPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_Switcher,_args,_kwargs)
        self.thisown = 1




class FXSwitcherPtr(FX_SwitcherPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXSwitcher_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXSwitcher instance at %s>" % (self.this,)
class FXSwitcher(FXSwitcherPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXSwitcher,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ScrollAreaPtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onHMouseWheel(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onHMouseWheel,(self,) + _args, _kwargs)
        return val
    def onVMouseWheel(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onVMouseWheel,(self,) + _args, _kwargs)
        return val
    def onHScrollerChanged(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onHScrollerChanged,(self,) + _args, _kwargs)
        return val
    def onVScrollerChanged(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onVScrollerChanged,(self,) + _args, _kwargs)
        return val
    def onHScrollerDragged(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onHScrollerDragged,(self,) + _args, _kwargs)
        return val
    def onVScrollerDragged(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onVScrollerDragged,(self,) + _args, _kwargs)
        return val
    def onAutoScroll(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_onAutoScroll,(self,) + _args, _kwargs)
        return val
    def setScrollStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_setScrollStyle,(self,) + _args, _kwargs)
        return val
    def getScrollStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getScrollStyle,(self,) + _args, _kwargs)
        return val
    def isHorizontalScrollable(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_isHorizontalScrollable,(self,) + _args, _kwargs)
        return val
    def isVerticalScrollable(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_isVerticalScrollable,(self,) + _args, _kwargs)
        return val
    def horizontalScrollbar(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_horizontalScrollbar,(self,) + _args, _kwargs)
        return val
    def verticalScrollbar(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_verticalScrollbar,(self,) + _args, _kwargs)
        return val
    def getXPosition(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getXPosition,(self,) + _args, _kwargs)
        return val
    def getYPosition(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getYPosition,(self,) + _args, _kwargs)
        return val
    def setPosition(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_setPosition,(self,) + _args, _kwargs)
        return val
    def getPosition(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getPosition,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollArea_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ScrollArea instance at %s>" % (self.this,)
class FX_ScrollArea(FX_ScrollAreaPtr):
    def __init__(self,this):
        self.this = this




class FXScrollAreaPtr(FX_ScrollAreaPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollArea_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXScrollArea instance at %s>" % (self.this,)
class FXScrollArea(FXScrollAreaPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXScrollArea,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ScrollWindowPtr(FX_ScrollAreaPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollWindow_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollWindow_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onFocusSelf(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollWindow_onFocusSelf,(self,) + _args, _kwargs)
        return val
    def contentWindow(self, *_args, **_kwargs):
        val = apply(containersc.FX_ScrollWindow_contentWindow,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ScrollWindow instance at %s>" % (self.this,)
class FX_ScrollWindow(FX_ScrollWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_ScrollWindow,_args,_kwargs)
        self.thisown = 1




class FXScrollWindowPtr(FX_ScrollWindowPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_setBackColor,(self,) + _args, _kwargs)
        return val
    def getContentWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getContentWidth,(self,) + _args, _kwargs)
        return val
    def getContentHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getContentHeight,(self,) + _args, _kwargs)
        return val
    def getViewportWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getViewportWidth,(self,) + _args, _kwargs)
        return val
    def getViewportHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_getViewportHeight,(self,) + _args, _kwargs)
        return val
    def moveContents(self, *_args, **_kwargs):
        val = apply(containersc.FXScrollWindow_moveContents,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXScrollWindow instance at %s>" % (self.this,)
class FXScrollWindow(FXScrollWindowPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXScrollWindow,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_SplitterPtr(FX_CompositePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onMotion,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_onFocusRight,(self,) + _args, _kwargs)
        return val
    def getSplitterStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_getSplitterStyle,(self,) + _args, _kwargs)
        return val
    def setSplitterStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_setSplitterStyle,(self,) + _args, _kwargs)
        return val
    def setBarSize(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_setBarSize,(self,) + _args, _kwargs)
        return val
    def getBarSize(self, *_args, **_kwargs):
        val = apply(containersc.FX_Splitter_getBarSize,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Splitter instance at %s>" % (self.this,)
class FX_Splitter(FX_SplitterPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_Splitter,_args,_kwargs)
        self.thisown = 1




class FXSplitterPtr(FX_SplitterPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXSplitter_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXSplitter instance at %s>" % (self.this,)
class FXSplitter(FXSplitterPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.CreateSplitter1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.CreateSplitter2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_4SplitterPtr(FX_CompositePtr):
    ID_EXPAND_ALL = containersc.FX_4Splitter_ID_EXPAND_ALL
    ID_EXPAND_TOPLEFT = containersc.FX_4Splitter_ID_EXPAND_TOPLEFT
    ID_EXPAND_TOPRIGHT = containersc.FX_4Splitter_ID_EXPAND_TOPRIGHT
    ID_EXPAND_BOTTOMLEFT = containersc.FX_4Splitter_ID_EXPAND_BOTTOMLEFT
    ID_EXPAND_BOTTOMRIGHT = containersc.FX_4Splitter_ID_EXPAND_BOTTOMRIGHT
    ID_LAST = containersc.FX_4Splitter_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onMotion,(self,) + _args, _kwargs)
        return val
    def onFocusNext(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusNext,(self,) + _args, _kwargs)
        return val
    def onFocusPrev(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusPrev,(self,) + _args, _kwargs)
        return val
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onFocusLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusLeft,(self,) + _args, _kwargs)
        return val
    def onFocusRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onFocusRight,(self,) + _args, _kwargs)
        return val
    def onCmdExpand(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onCmdExpand,(self,) + _args, _kwargs)
        return val
    def onUpdExpand(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_onUpdExpand,(self,) + _args, _kwargs)
        return val
    def getTopLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getTopLeft,(self,) + _args, _kwargs)
        return val
    def getTopRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getTopRight,(self,) + _args, _kwargs)
        return val
    def getBottomLeft(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getBottomLeft,(self,) + _args, _kwargs)
        return val
    def getBottomRight(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getBottomRight,(self,) + _args, _kwargs)
        return val
    def getHSplit(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getHSplit,(self,) + _args, _kwargs)
        return val
    def getVSplit(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getVSplit,(self,) + _args, _kwargs)
        return val
    def setHSplit(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_setHSplit,(self,) + _args, _kwargs)
        return val
    def setVSplit(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_setVSplit,(self,) + _args, _kwargs)
        return val
    def getSplitterStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getSplitterStyle,(self,) + _args, _kwargs)
        return val
    def setSplitterStyle(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_setSplitterStyle,(self,) + _args, _kwargs)
        return val
    def setBarSize(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_setBarSize,(self,) + _args, _kwargs)
        return val
    def getBarSize(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getBarSize,(self,) + _args, _kwargs)
        return val
    def setExpanded(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_setExpanded,(self,) + _args, _kwargs)
        return val
    def getExpanded(self, *_args, **_kwargs):
        val = apply(containersc.FX_4Splitter_getExpanded,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_4Splitter instance at %s>" % (self.this,)
class FX_4Splitter(FX_4SplitterPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_4Splitter,_args,_kwargs)
        self.thisown = 1




class FX4SplitterPtr(FX_4SplitterPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FX4Splitter_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX4Splitter instance at %s>" % (self.this,)
class FX4Splitter(FX4SplitterPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.Create4Splitter1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.Create4Splitter2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_ShutterItemPtr(FX_VerticalFramePtr):
    ID_SHUTTERITEM_BUTTON = containersc.FX_ShutterItem_ID_SHUTTERITEM_BUTTON
    ID_LAST = containersc.FX_ShutterItem_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onCmdButton(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_onCmdButton,(self,) + _args, _kwargs)
        return val
    def getButton(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_getButton,(self,) + _args, _kwargs)
        return val
    def getContent(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_getContent,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(containersc.FX_ShutterItem_getTipText,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_ShutterItem instance at %s>" % (self.this,)
class FX_ShutterItem(FX_ShutterItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_ShutterItem,_args,_kwargs)
        self.thisown = 1




class FXShutterItemPtr(FX_ShutterItemPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXShutterItem_setBackColor,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXShutterItem instance at %s>" % (self.this,)
class FXShutterItem(FXShutterItemPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXShutterItem,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ShutterPtr(FX_VerticalFramePtr):
    ID_SHUTTER_TIMEOUT = containersc.FX_Shutter_ID_SHUTTER_TIMEOUT
    ID_OPEN_SHUTTERITEM = containersc.FX_Shutter_ID_OPEN_SHUTTERITEM
    ID_OPEN_FIRST = containersc.FX_Shutter_ID_OPEN_FIRST
    ID_OPEN_LAST = containersc.FX_Shutter_ID_OPEN_LAST
    ID_LAST = containersc.FX_Shutter_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onFocusUp(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onFocusUp,(self,) + _args, _kwargs)
        return val
    def onFocusDown(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onFocusDown,(self,) + _args, _kwargs)
        return val
    def onTimeout(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onTimeout,(self,) + _args, _kwargs)
        return val
    def onOpenItem(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onOpenItem,(self,) + _args, _kwargs)
        return val
    def onCmdSetValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onCmdSetValue,(self,) + _args, _kwargs)
        return val
    def onCmdSetIntValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onCmdSetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdGetIntValue(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onCmdGetIntValue,(self,) + _args, _kwargs)
        return val
    def onCmdOpen(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onCmdOpen,(self,) + _args, _kwargs)
        return val
    def onUpdOpen(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_onUpdOpen,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_setCurrent,(self,) + _args, _kwargs)
        return val
    def getCurrent(self, *_args, **_kwargs):
        val = apply(containersc.FX_Shutter_getCurrent,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Shutter instance at %s>" % (self.this,)
class FX_Shutter(FX_ShutterPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FX_Shutter,_args,_kwargs)
        self.thisown = 1




class FXShutterPtr(FX_ShutterPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_setBackColor,(self,) + _args, _kwargs)
        return val
    def setCurrent(self, *_args, **_kwargs):
        val = apply(containersc.FXShutter_setCurrent,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXShutter instance at %s>" % (self.this,)
class FXShutter(FXShutterPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(containersc.new_FXShutter,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateDCWindow(*_args, **_kwargs):
    val = apply(containersc.CreateDCWindow,_args,_kwargs)
    if val: val = FXDCWindowPtr(val)
    return val

def CreateClippedDCWindow(*_args, **_kwargs):
    val = apply(containersc.CreateClippedDCWindow,_args,_kwargs)
    if val: val = FXDCWindowPtr(val)
    return val

def CreateSplitter1(*_args, **_kwargs):
    val = apply(containersc.CreateSplitter1,_args,_kwargs)
    if val: val = FXSplitterPtr(val)
    return val

def CreateSplitter2(*_args, **_kwargs):
    val = apply(containersc.CreateSplitter2,_args,_kwargs)
    if val: val = FXSplitterPtr(val)
    return val

def Create4Splitter1(*_args, **_kwargs):
    val = apply(containersc.Create4Splitter1,_args,_kwargs)
    if val: val = FX4SplitterPtr(val)
    return val

def Create4Splitter2(*_args, **_kwargs):
    val = apply(containersc.Create4Splitter2,_args,_kwargs)
    if val: val = FX4SplitterPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

BLT_CLR = containersc.BLT_CLR
BLT_SRC_AND_DST = containersc.BLT_SRC_AND_DST
BLT_SRC_AND_NOT_DST = containersc.BLT_SRC_AND_NOT_DST
BLT_SRC = containersc.BLT_SRC
BLT_NOT_SRC_AND_DST = containersc.BLT_NOT_SRC_AND_DST
BLT_DST = containersc.BLT_DST
BLT_SRC_XOR_DST = containersc.BLT_SRC_XOR_DST
BLT_SRC_OR_DST = containersc.BLT_SRC_OR_DST
BLT_NOT_SRC_AND_NOT_DST = containersc.BLT_NOT_SRC_AND_NOT_DST
BLT_NOT_SRC_XOR_DST = containersc.BLT_NOT_SRC_XOR_DST
BLT_NOT_DST = containersc.BLT_NOT_DST
BLT_SRC_OR_NOT_DST = containersc.BLT_SRC_OR_NOT_DST
BLT_NOT_SRC = containersc.BLT_NOT_SRC
BLT_NOT_SRC_OR_DST = containersc.BLT_NOT_SRC_OR_DST
BLT_NOT_SRC_OR_NOT_DST = containersc.BLT_NOT_SRC_OR_NOT_DST
BLT_SET = containersc.BLT_SET
LINE_SOLID = containersc.LINE_SOLID
LINE_ONOFF_DASH = containersc.LINE_ONOFF_DASH
LINE_DOUBLE_DASH = containersc.LINE_DOUBLE_DASH
CAP_NOT_LAST = containersc.CAP_NOT_LAST
CAP_BUTT = containersc.CAP_BUTT
CAP_ROUND = containersc.CAP_ROUND
CAP_PROJECTING = containersc.CAP_PROJECTING
JOIN_MITER = containersc.JOIN_MITER
JOIN_ROUND = containersc.JOIN_ROUND
JOIN_BEVEL = containersc.JOIN_BEVEL
FILL_SOLID = containersc.FILL_SOLID
FILL_TILED = containersc.FILL_TILED
FILL_STIPPLED = containersc.FILL_STIPPLED
FILL_OPAQUESTIPPLED = containersc.FILL_OPAQUESTIPPLED
RULE_EVEN_ODD = containersc.RULE_EVEN_ODD
RULE_WINDING = containersc.RULE_WINDING
STIPPLE_0 = containersc.STIPPLE_0
STIPPLE_NONE = containersc.STIPPLE_NONE
STIPPLE_BLACK = containersc.STIPPLE_BLACK
STIPPLE_1 = containersc.STIPPLE_1
STIPPLE_2 = containersc.STIPPLE_2
STIPPLE_3 = containersc.STIPPLE_3
STIPPLE_4 = containersc.STIPPLE_4
STIPPLE_5 = containersc.STIPPLE_5
STIPPLE_6 = containersc.STIPPLE_6
STIPPLE_7 = containersc.STIPPLE_7
STIPPLE_8 = containersc.STIPPLE_8
STIPPLE_GRAY = containersc.STIPPLE_GRAY
STIPPLE_9 = containersc.STIPPLE_9
STIPPLE_10 = containersc.STIPPLE_10
STIPPLE_11 = containersc.STIPPLE_11
STIPPLE_12 = containersc.STIPPLE_12
STIPPLE_13 = containersc.STIPPLE_13
STIPPLE_14 = containersc.STIPPLE_14
STIPPLE_15 = containersc.STIPPLE_15
STIPPLE_16 = containersc.STIPPLE_16
STIPPLE_WHITE = containersc.STIPPLE_WHITE
STIPPLE_HORZ = containersc.STIPPLE_HORZ
STIPPLE_VERT = containersc.STIPPLE_VERT
STIPPLE_CROSS = containersc.STIPPLE_CROSS
STIPPLE_DIAG = containersc.STIPPLE_DIAG
STIPPLE_REVDIAG = containersc.STIPPLE_REVDIAG
STIPPLE_CROSSDIAG = containersc.STIPPLE_CROSSDIAG
SEPARATOR_NONE = containersc.SEPARATOR_NONE
SEPARATOR_GROOVE = containersc.SEPARATOR_GROOVE
SEPARATOR_RIDGE = containersc.SEPARATOR_RIDGE
SEPARATOR_LINE = containersc.SEPARATOR_LINE
DEFAULT_SPACING = containersc.DEFAULT_SPACING
MATRIX_BY_ROWS = containersc.MATRIX_BY_ROWS
MATRIX_BY_COLUMNS = containersc.MATRIX_BY_COLUMNS
GROUPBOX_TITLE_LEFT = containersc.GROUPBOX_TITLE_LEFT
GROUPBOX_TITLE_CENTER = containersc.GROUPBOX_TITLE_CENTER
GROUPBOX_TITLE_RIGHT = containersc.GROUPBOX_TITLE_RIGHT
GROUPBOX_NORMAL = containersc.GROUPBOX_NORMAL
SWITCHER_HCOLLAPSE = containersc.SWITCHER_HCOLLAPSE
SWITCHER_VCOLLAPSE = containersc.SWITCHER_VCOLLAPSE
SCROLLERS_NORMAL = containersc.SCROLLERS_NORMAL
HSCROLLER_ALWAYS = containersc.HSCROLLER_ALWAYS
HSCROLLER_NEVER = containersc.HSCROLLER_NEVER
VSCROLLER_ALWAYS = containersc.VSCROLLER_ALWAYS
VSCROLLER_NEVER = containersc.VSCROLLER_NEVER
HSCROLLING_ON = containersc.HSCROLLING_ON
HSCROLLING_OFF = containersc.HSCROLLING_OFF
VSCROLLING_ON = containersc.VSCROLLING_ON
VSCROLLING_OFF = containersc.VSCROLLING_OFF
SCROLLERS_TRACK = containersc.SCROLLERS_TRACK
SCROLLERS_DONT_TRACK = containersc.SCROLLERS_DONT_TRACK
SPLITTER_HORIZONTAL = containersc.SPLITTER_HORIZONTAL
SPLITTER_VERTICAL = containersc.SPLITTER_VERTICAL
SPLITTER_REVERSED = containersc.SPLITTER_REVERSED
SPLITTER_TRACKING = containersc.SPLITTER_TRACKING
SPLITTER_NORMAL = containersc.SPLITTER_NORMAL
FOURSPLITTER_TRACKING = containersc.FOURSPLITTER_TRACKING
FOURSPLITTER_NORMAL = containersc.FOURSPLITTER_NORMAL
