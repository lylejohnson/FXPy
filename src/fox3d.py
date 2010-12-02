# This file was created automatically by SWIG.
import fox3dc

from misc import *

from windows import *

from containers import *
import fox
class FX_GLContextPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def isShared(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_isShared,(self,) + _args, _kwargs)
        return val
    def getVisual(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_getVisual,(self,) + _args, _kwargs)
        if val: val = FX_GLVisualPtr(val) 
        return val
    def create(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_destroy,(self,) + _args, _kwargs)
        return val
    def begin(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_begin,(self,) + _args, _kwargs)
        return val
    def end(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_end,(self,) + _args, _kwargs)
        return val
    def swapBuffers(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_swapBuffers,(self,) + _args, _kwargs)
        return val
    def swapSubBuffers(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLContext_swapSubBuffers,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLContext instance at %s>" % (self.this,)
class FX_GLContext(FX_GLContextPtr):
    def __init__(self,this):
        self.this = this




class FXGLContextPtr(FX_GLContextPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLContext_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLContext_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLContext_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLContext_detach,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLContext instance at %s>" % (self.this,)
class FXGLContext(FXGLContextPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLContext1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLContext2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_GLVisualPtr(FX_VisualPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getRedSize,(self,) + _args, _kwargs)
        return val
    def getGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getGreenSize,(self,) + _args, _kwargs)
        return val
    def getBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getBlueSize,(self,) + _args, _kwargs)
        return val
    def getAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getAlphaSize,(self,) + _args, _kwargs)
        return val
    def getDepthSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getDepthSize,(self,) + _args, _kwargs)
        return val
    def getStencilSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getStencilSize,(self,) + _args, _kwargs)
        return val
    def getAccumRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getAccumRedSize,(self,) + _args, _kwargs)
        return val
    def getAccumGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getAccumGreenSize,(self,) + _args, _kwargs)
        return val
    def getAccumBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getAccumBlueSize,(self,) + _args, _kwargs)
        return val
    def getAccumAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getAccumAlphaSize,(self,) + _args, _kwargs)
        return val
    def setRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setRedSize,(self,) + _args, _kwargs)
        return val
    def setGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setGreenSize,(self,) + _args, _kwargs)
        return val
    def setBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setBlueSize,(self,) + _args, _kwargs)
        return val
    def setAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setAlphaSize,(self,) + _args, _kwargs)
        return val
    def setDepthSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setDepthSize,(self,) + _args, _kwargs)
        return val
    def setStencilSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setStencilSize,(self,) + _args, _kwargs)
        return val
    def setAccumRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setAccumRedSize,(self,) + _args, _kwargs)
        return val
    def setAccumGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setAccumGreenSize,(self,) + _args, _kwargs)
        return val
    def setAccumBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setAccumBlueSize,(self,) + _args, _kwargs)
        return val
    def setAccumAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_setAccumAlphaSize,(self,) + _args, _kwargs)
        return val
    def getActualRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualRedSize,(self,) + _args, _kwargs)
        return val
    def getActualGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualGreenSize,(self,) + _args, _kwargs)
        return val
    def getActualBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualBlueSize,(self,) + _args, _kwargs)
        return val
    def getActualAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualAlphaSize,(self,) + _args, _kwargs)
        return val
    def getActualDepthSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualDepthSize,(self,) + _args, _kwargs)
        return val
    def getActualStencilSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualStencilSize,(self,) + _args, _kwargs)
        return val
    def getActualAccumRedSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualAccumRedSize,(self,) + _args, _kwargs)
        return val
    def getActualAccumGreenSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualAccumGreenSize,(self,) + _args, _kwargs)
        return val
    def getActualAccumBlueSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualAccumBlueSize,(self,) + _args, _kwargs)
        return val
    def getActualAccumAlphaSize(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_getActualAccumAlphaSize,(self,) + _args, _kwargs)
        return val
    def isDoubleBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_isDoubleBuffer,(self,) + _args, _kwargs)
        return val
    def isStereo(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_isStereo,(self,) + _args, _kwargs)
        return val
    def isAccelerated(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_isAccelerated,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLVisual_destroy,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLVisual instance at %s>" % (self.this,)
class FX_GLVisual(FX_GLVisualPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLVisual,_args,_kwargs)
        self.thisown = 1




class FXGLVisualPtr(FX_GLVisualPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLVisual_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLVisual instance at %s>" % (self.this,)
class FXGLVisual(FXGLVisualPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLVisual,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLCanvasPtr(FX_CanvasPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def isShared(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_isShared,(self,) + _args, _kwargs)
        return val
    def isCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_isCurrent,(self,) + _args, _kwargs)
        return val
    def makeCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_makeCurrent,(self,) + _args, _kwargs)
        return val
    def getContext(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_getContext,(self,) + _args, _kwargs)
        return val
    def makeNonCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_makeNonCurrent,(self,) + _args, _kwargs)
        return val
    def swapBuffers(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCanvas_swapBuffers,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLCanvas instance at %s>" % (self.this,)
class FX_GLCanvas(FX_GLCanvasPtr):
    def __init__(self,this):
        self.this = this




class FXGLCanvasPtr(FX_GLCanvasPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_setBackColor,(self,) + _args, _kwargs)
        return val
    def isCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_isCurrent,(self,) + _args, _kwargs)
        return val
    def makeCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_makeCurrent,(self,) + _args, _kwargs)
        return val
    def makeNonCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_makeNonCurrent,(self,) + _args, _kwargs)
        return val
    def swapBuffers(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCanvas_swapBuffers,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLCanvas instance at %s>" % (self.this,)
class FXGLCanvas(FXGLCanvasPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLCanvas1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLCanvas2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FXViewportPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "w" :
            fox3dc.FXViewport_w_set(self,value)
            return
        if name == "h" :
            fox3dc.FXViewport_h_set(self,value)
            return
        if name == "left" :
            fox3dc.FXViewport_left_set(self,value)
            return
        if name == "right" :
            fox3dc.FXViewport_right_set(self,value)
            return
        if name == "bottom" :
            fox3dc.FXViewport_bottom_set(self,value)
            return
        if name == "top" :
            fox3dc.FXViewport_top_set(self,value)
            return
        if name == "hither" :
            fox3dc.FXViewport_hither_set(self,value)
            return
        if name == "yon" :
            fox3dc.FXViewport_yon_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "w" : 
            return fox3dc.FXViewport_w_get(self)
        if name == "h" : 
            return fox3dc.FXViewport_h_get(self)
        if name == "left" : 
            return fox3dc.FXViewport_left_get(self)
        if name == "right" : 
            return fox3dc.FXViewport_right_get(self)
        if name == "bottom" : 
            return fox3dc.FXViewport_bottom_get(self)
        if name == "top" : 
            return fox3dc.FXViewport_top_get(self)
        if name == "hither" : 
            return fox3dc.FXViewport_hither_get(self)
        if name == "yon" : 
            return fox3dc.FXViewport_yon_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXViewport instance at %s>" % (self.this,)
class FXViewport(FXViewportPtr):
    def __init__(self,this):
        self.this = this




class FXLightPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "ambient" :
            fox3dc.FXLight_ambient_set(self,value)
            return
        if name == "diffuse" :
            fox3dc.FXLight_diffuse_set(self,value)
            return
        if name == "specular" :
            fox3dc.FXLight_specular_set(self,value)
            return
        if name == "position" :
            fox3dc.FXLight_position_set(self,value)
            return
        if name == "direction" :
            fox3dc.FXLight_direction_set(self,value)
            return
        if name == "exponent" :
            fox3dc.FXLight_exponent_set(self,value)
            return
        if name == "cutoff" :
            fox3dc.FXLight_cutoff_set(self,value)
            return
        if name == "c_attn" :
            fox3dc.FXLight_c_attn_set(self,value)
            return
        if name == "l_attn" :
            fox3dc.FXLight_l_attn_set(self,value)
            return
        if name == "q_attn" :
            fox3dc.FXLight_q_attn_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "ambient" : 
            return fox3dc.FXLight_ambient_get(self)
        if name == "diffuse" : 
            return fox3dc.FXLight_diffuse_get(self)
        if name == "specular" : 
            return fox3dc.FXLight_specular_get(self)
        if name == "position" : 
            return fox3dc.FXLight_position_get(self)
        if name == "direction" : 
            return fox3dc.FXLight_direction_get(self)
        if name == "exponent" : 
            return fox3dc.FXLight_exponent_get(self)
        if name == "cutoff" : 
            return fox3dc.FXLight_cutoff_get(self)
        if name == "c_attn" : 
            return fox3dc.FXLight_c_attn_get(self)
        if name == "l_attn" : 
            return fox3dc.FXLight_l_attn_get(self)
        if name == "q_attn" : 
            return fox3dc.FXLight_q_attn_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXLight instance at %s>" % (self.this,)
class FXLight(FXLightPtr):
    def __init__(self,this):
        self.this = this




class FXMaterialPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "ambient" :
            fox3dc.FXMaterial_ambient_set(self,value)
            return
        if name == "diffuse" :
            fox3dc.FXMaterial_diffuse_set(self,value)
            return
        if name == "specular" :
            fox3dc.FXMaterial_specular_set(self,value)
            return
        if name == "emission" :
            fox3dc.FXMaterial_emission_set(self,value)
            return
        if name == "shininess" :
            fox3dc.FXMaterial_shininess_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "ambient" : 
            return fox3dc.FXMaterial_ambient_get(self)
        if name == "diffuse" : 
            return fox3dc.FXMaterial_diffuse_get(self)
        if name == "specular" : 
            return fox3dc.FXMaterial_specular_get(self)
        if name == "emission" : 
            return fox3dc.FXMaterial_emission_get(self)
        if name == "shininess" : 
            return fox3dc.FXMaterial_shininess_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXMaterial instance at %s>" % (self.this,)
class FXMaterial(FXMaterialPtr):
    def __init__(self,this):
        self.this = this




class FX_GLViewerPtr(FX_GLCanvasPtr):
    PARALLEL = fox3dc.FX_GLViewer_PARALLEL
    PERSPECTIVE = fox3dc.FX_GLViewer_PERSPECTIVE
    OFFSETPROJECTION = fox3dc.FX_GLViewer_OFFSETPROJECTION
    SURFACEPROJECTION = fox3dc.FX_GLViewer_SURFACEPROJECTION
    ID_PERSPECTIVE = fox3dc.FX_GLViewer_ID_PERSPECTIVE
    ID_PARALLEL = fox3dc.FX_GLViewer_ID_PARALLEL
    ID_FRONT = fox3dc.FX_GLViewer_ID_FRONT
    ID_BACK = fox3dc.FX_GLViewer_ID_BACK
    ID_LEFT = fox3dc.FX_GLViewer_ID_LEFT
    ID_RIGHT = fox3dc.FX_GLViewer_ID_RIGHT
    ID_TOP = fox3dc.FX_GLViewer_ID_TOP
    ID_BOTTOM = fox3dc.FX_GLViewer_ID_BOTTOM
    ID_RESETVIEW = fox3dc.FX_GLViewer_ID_RESETVIEW
    ID_FITVIEW = fox3dc.FX_GLViewer_ID_FITVIEW
    ID_TIPTIMER = fox3dc.FX_GLViewer_ID_TIPTIMER
    ID_BACK_COLOR = fox3dc.FX_GLViewer_ID_BACK_COLOR
    ID_AMBIENT_COLOR = fox3dc.FX_GLViewer_ID_AMBIENT_COLOR
    ID_LIGHT_AMBIENT = fox3dc.FX_GLViewer_ID_LIGHT_AMBIENT
    ID_LIGHT_DIFFUSE = fox3dc.FX_GLViewer_ID_LIGHT_DIFFUSE
    ID_LIGHT_SPECULAR = fox3dc.FX_GLViewer_ID_LIGHT_SPECULAR
    ID_LIGHTING = fox3dc.FX_GLViewer_ID_LIGHTING
    ID_TURBO = fox3dc.FX_GLViewer_ID_TURBO
    ID_FOG = fox3dc.FX_GLViewer_ID_FOG
    ID_DITHER = fox3dc.FX_GLViewer_ID_DITHER
    ID_SCALE_X = fox3dc.FX_GLViewer_ID_SCALE_X
    ID_SCALE_Y = fox3dc.FX_GLViewer_ID_SCALE_Y
    ID_SCALE_Z = fox3dc.FX_GLViewer_ID_SCALE_Z
    ID_DIAL_X = fox3dc.FX_GLViewer_ID_DIAL_X
    ID_DIAL_Y = fox3dc.FX_GLViewer_ID_DIAL_Y
    ID_DIAL_Z = fox3dc.FX_GLViewer_ID_DIAL_Z
    ID_ROLL = fox3dc.FX_GLViewer_ID_ROLL
    ID_PITCH = fox3dc.FX_GLViewer_ID_PITCH
    ID_YAW = fox3dc.FX_GLViewer_ID_YAW
    ID_FOV = fox3dc.FX_GLViewer_ID_FOV
    ID_ZOOM = fox3dc.FX_GLViewer_ID_ZOOM
    ID_LOCK = fox3dc.FX_GLViewer_ID_LOCK
    ID_CUT_SEL = fox3dc.FX_GLViewer_ID_CUT_SEL
    ID_COPY_SEL = fox3dc.FX_GLViewer_ID_COPY_SEL
    ID_PASTE_SEL = fox3dc.FX_GLViewer_ID_PASTE_SEL
    ID_DELETE_SEL = fox3dc.FX_GLViewer_ID_DELETE_SEL
    ID_PRINT_IMAGE = fox3dc.FX_GLViewer_ID_PRINT_IMAGE
    ID_PRINT_VECTOR = fox3dc.FX_GLViewer_ID_PRINT_VECTOR
    ID_LASSO_ZOOM = fox3dc.FX_GLViewer_ID_LASSO_ZOOM
    ID_LASSO_SELECT = fox3dc.FX_GLViewer_ID_LASSO_SELECT
    ID_LAST = fox3dc.FX_GLViewer_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onPaint(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onPaint,(self,) + _args, _kwargs)
        return val
    def onEnter(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onEnter,(self,) + _args, _kwargs)
        return val
    def onLeave(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onLeave,(self,) + _args, _kwargs)
        return val
    def onMotion(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onMotion,(self,) + _args, _kwargs)
        return val
    def onMouseWheel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onMouseWheel,(self,) + _args, _kwargs)
        return val
    def onChanged(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onChanged,(self,) + _args, _kwargs)
        return val
    def onPick(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onPick,(self,) + _args, _kwargs)
        return val
    def onClicked(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onClicked,(self,) + _args, _kwargs)
        return val
    def onDoubleClicked(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDoubleClicked,(self,) + _args, _kwargs)
        return val
    def onTripleClicked(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onTripleClicked,(self,) + _args, _kwargs)
        return val
    def onLassoed(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onLassoed,(self,) + _args, _kwargs)
        return val
    def onSelected(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onSelected,(self,) + _args, _kwargs)
        return val
    def onDeselected(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDeselected,(self,) + _args, _kwargs)
        return val
    def onInserted(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onInserted,(self,) + _args, _kwargs)
        return val
    def onDeleted(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDeleted,(self,) + _args, _kwargs)
        return val
    def onLeftBtnPress(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onLeftBtnPress,(self,) + _args, _kwargs)
        return val
    def onLeftBtnRelease(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onLeftBtnRelease,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnPress(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onMiddleBtnPress,(self,) + _args, _kwargs)
        return val
    def onMiddleBtnRelease(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onMiddleBtnRelease,(self,) + _args, _kwargs)
        return val
    def onRightBtnPress(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onRightBtnPress,(self,) + _args, _kwargs)
        return val
    def onRightBtnRelease(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onRightBtnRelease,(self,) + _args, _kwargs)
        return val
    def onUngrabbed(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUngrabbed,(self,) + _args, _kwargs)
        return val
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def onFocusIn(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onFocusIn,(self,) + _args, _kwargs)
        return val
    def onFocusOut(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onFocusOut,(self,) + _args, _kwargs)
        return val
    def onClipboardLost(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onClipboardLost,(self,) + _args, _kwargs)
        return val
    def onClipboardGained(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onClipboardGained,(self,) + _args, _kwargs)
        return val
    def onClipboardRequest(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onClipboardRequest,(self,) + _args, _kwargs)
        return val
    def onCmdPerspective(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdPerspective,(self,) + _args, _kwargs)
        return val
    def onUpdPerspective(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdPerspective,(self,) + _args, _kwargs)
        return val
    def onCmdParallel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdParallel,(self,) + _args, _kwargs)
        return val
    def onUpdParallel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdParallel,(self,) + _args, _kwargs)
        return val
    def onCmdFront(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdFront,(self,) + _args, _kwargs)
        return val
    def onUpdFront(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdFront,(self,) + _args, _kwargs)
        return val
    def onCmdBack(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdBack,(self,) + _args, _kwargs)
        return val
    def onUpdBack(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdBack,(self,) + _args, _kwargs)
        return val
    def onCmdLeft(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLeft,(self,) + _args, _kwargs)
        return val
    def onUpdLeft(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLeft,(self,) + _args, _kwargs)
        return val
    def onCmdRight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdRight,(self,) + _args, _kwargs)
        return val
    def onUpdRight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdRight,(self,) + _args, _kwargs)
        return val
    def onCmdTop(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdTop,(self,) + _args, _kwargs)
        return val
    def onUpdTop(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdTop,(self,) + _args, _kwargs)
        return val
    def onCmdBottom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdBottom,(self,) + _args, _kwargs)
        return val
    def onUpdBottom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdBottom,(self,) + _args, _kwargs)
        return val
    def onCmdResetView(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdResetView,(self,) + _args, _kwargs)
        return val
    def onCmdFitView(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdFitView,(self,) + _args, _kwargs)
        return val
    def onDNDEnter(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDNDEnter,(self,) + _args, _kwargs)
        return val
    def onDNDLeave(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDNDLeave,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onTipTimer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onTipTimer,(self,) + _args, _kwargs)
        return val
    def onQueryHelp(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onQueryHelp,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdXYZDial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdXYZDial,(self,) + _args, _kwargs)
        return val
    def onUpdXYZDial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdXYZDial,(self,) + _args, _kwargs)
        return val
    def onCmdRollPitchYaw(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdRollPitchYaw,(self,) + _args, _kwargs)
        return val
    def onUpdRollPitchYaw(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdRollPitchYaw,(self,) + _args, _kwargs)
        return val
    def onCmdXYZScale(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdXYZScale,(self,) + _args, _kwargs)
        return val
    def onUpdXYZScale(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdXYZScale,(self,) + _args, _kwargs)
        return val
    def onUpdCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdCurrent,(self,) + _args, _kwargs)
        return val
    def onCmdCutSel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdCutSel,(self,) + _args, _kwargs)
        return val
    def onCmdCopySel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdCopySel,(self,) + _args, _kwargs)
        return val
    def onCmdPasteSel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdPasteSel,(self,) + _args, _kwargs)
        return val
    def onCmdDeleteSel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdDeleteSel,(self,) + _args, _kwargs)
        return val
    def onUpdDeleteSel(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdDeleteSel,(self,) + _args, _kwargs)
        return val
    def onCmdBackColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdBackColor,(self,) + _args, _kwargs)
        return val
    def onUpdBackColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdBackColor,(self,) + _args, _kwargs)
        return val
    def onCmdAmbientColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdAmbientColor,(self,) + _args, _kwargs)
        return val
    def onUpdAmbientColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdAmbientColor,(self,) + _args, _kwargs)
        return val
    def onCmdLock(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLock,(self,) + _args, _kwargs)
        return val
    def onUpdLock(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLock,(self,) + _args, _kwargs)
        return val
    def onCmdLighting(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLighting,(self,) + _args, _kwargs)
        return val
    def onUpdLighting(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLighting,(self,) + _args, _kwargs)
        return val
    def onCmdFog(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdFog,(self,) + _args, _kwargs)
        return val
    def onUpdFog(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdFog,(self,) + _args, _kwargs)
        return val
    def onCmdDither(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdDither,(self,) + _args, _kwargs)
        return val
    def onUpdDither(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdDither,(self,) + _args, _kwargs)
        return val
    def onCmdFov(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdFov,(self,) + _args, _kwargs)
        return val
    def onUpdFov(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdFov,(self,) + _args, _kwargs)
        return val
    def onCmdZoom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdZoom,(self,) + _args, _kwargs)
        return val
    def onUpdZoom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdZoom,(self,) + _args, _kwargs)
        return val
    def onCmdLightAmbient(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLightAmbient,(self,) + _args, _kwargs)
        return val
    def onUpdLightAmbient(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLightAmbient,(self,) + _args, _kwargs)
        return val
    def onCmdLightDiffuse(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLightDiffuse,(self,) + _args, _kwargs)
        return val
    def onUpdLightDiffuse(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLightDiffuse,(self,) + _args, _kwargs)
        return val
    def onCmdLightSpecular(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLightSpecular,(self,) + _args, _kwargs)
        return val
    def onUpdLightSpecular(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdLightSpecular,(self,) + _args, _kwargs)
        return val
    def onCmdTurbo(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdTurbo,(self,) + _args, _kwargs)
        return val
    def onUpdTurbo(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onUpdTurbo,(self,) + _args, _kwargs)
        return val
    def onCmdPrintImage(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdPrintImage,(self,) + _args, _kwargs)
        return val
    def onCmdPrintVector(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdPrintVector,(self,) + _args, _kwargs)
        return val
    def onCmdLassoZoom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLassoZoom,(self,) + _args, _kwargs)
        return val
    def onCmdLassoSelect(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_onCmdLassoSelect,(self,) + _args, _kwargs)
        return val
    def worldPix(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_worldPix,(self,) + _args, _kwargs)
        return val
    def modelPix(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_modelPix,(self,) + _args, _kwargs)
        return val
    def lasso(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_lasso,(self,) + _args, _kwargs)
        return val
    def select(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_select,(self,) + _args, _kwargs)
        return val
    def pick(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_pick,(self,) + _args, _kwargs)
        return val
    def setBounds(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setBounds,(self,) + _args, _kwargs)
        return val
    def fitToBounds(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_fitToBounds,(self,) + _args, _kwargs)
        return val
    def getViewport(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getViewport,(self,) + _args, _kwargs)
        if val: val = FXViewportPtr(val) ; val.thisown = 1
        return val
    def eyeToScreen(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_eyeToScreen,(self,) + _args, _kwargs)
        return val
    def screenToEye(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_screenToEye,(self,) + _args, _kwargs)
        return val
    def screenToTarget(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_screenToTarget,(self,) + _args, _kwargs)
        return val
    def worldToEye(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_worldToEye,(self,) + _args, _kwargs)
        return val
    def worldToEyeZ(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_worldToEyeZ,(self,) + _args, _kwargs)
        return val
    def eyeToWorld(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_eyeToWorld,(self,) + _args, _kwargs)
        return val
    def worldVector(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_worldVector,(self,) + _args, _kwargs)
        return val
    def setMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setMaterial,(self,) + _args, _kwargs)
        return val
    def getMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getMaterial,(self,) + _args, _kwargs)
        if val: val = FXMaterialPtr(val) ; val.thisown = 1
        return val
    def setFieldOfView(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setFieldOfView,(self,) + _args, _kwargs)
        return val
    def getFieldOfView(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getFieldOfView,(self,) + _args, _kwargs)
        return val
    def setZoom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setZoom,(self,) + _args, _kwargs)
        return val
    def getZoom(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getZoom,(self,) + _args, _kwargs)
        return val
    def setDistance(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setDistance,(self,) + _args, _kwargs)
        return val
    def getDistance(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getDistance,(self,) + _args, _kwargs)
        return val
    def setOrientation(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setOrientation,(self,) + _args, _kwargs)
        return val
    def getOrientation(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getOrientation,(self,) + _args, _kwargs)
        return val
    def setCenter(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setCenter,(self,) + _args, _kwargs)
        return val
    def getCenter(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getCenter,(self,) + _args, _kwargs)
        return val
    def translate(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_translate,(self,) + _args, _kwargs)
        return val
    def getBoreVector(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getBoreVector,(self,) + _args, _kwargs)
        return val
    def getEyeVector(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getEyeVector,(self,) + _args, _kwargs)
        return val
    def getEyePosition(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getEyePosition,(self,) + _args, _kwargs)
        return val
    def setHelpText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setHelpText,(self,) + _args, _kwargs)
        return val
    def getHelpText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getHelpText,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getTipText,(self,) + _args, _kwargs)
        return val
    def getTransform(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getTransform,(self,) + _args, _kwargs)
        return val
    def getInvTransform(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getInvTransform,(self,) + _args, _kwargs)
        return val
    def setScene(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setScene,(self,) + _args, _kwargs)
        return val
    def getScene(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getScene,(self,) + _args, _kwargs)
        return val
    def setSelection(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setSelection,(self,) + _args, _kwargs)
        return val
    def getSelection(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getSelection,(self,) + _args, _kwargs)
        return val
    def setProjection(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setProjection,(self,) + _args, _kwargs)
        return val
    def getProjection(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getProjection,(self,) + _args, _kwargs)
        return val
    def setViewLock(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setViewLock,(self,) + _args, _kwargs)
        return val
    def getViewLock(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getViewLock,(self,) + _args, _kwargs)
        return val
    def setBackgroundColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setBackgroundColor,(self,) + _args, _kwargs)
        return val
    def getBackgroundColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getBackgroundColor,(self,) + _args, _kwargs)
        return val
    def setAmbientColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setAmbientColor,(self,) + _args, _kwargs)
        return val
    def getAmbientColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getAmbientColor,(self,) + _args, _kwargs)
        return val
    def readPixels(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_readPixels,(self,) + _args, _kwargs)
        return val
    def readFeedback(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_readFeedback,(self,) + _args, _kwargs)
        return val
    def setMaxHits(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setMaxHits,(self,) + _args, _kwargs)
        return val
    def getMaxHits(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getMaxHits,(self,) + _args, _kwargs)
        return val
    def doesTurbo(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_doesTurbo,(self,) + _args, _kwargs)
        return val
    def getTurboMode(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getTurboMode,(self,) + _args, _kwargs)
        return val
    def setTurboMode(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setTurboMode,(self,) + _args, _kwargs)
        return val
    def setLight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setLight,(self,) + _args, _kwargs)
        return val
    def getLight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getLight,(self,) + _args, _kwargs)
        if val: val = FXLightPtr(val) ; val.thisown = 1
        return val
    def setOffset(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_setOffset,(self,) + _args, _kwargs)
        return val
    def getOffset(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLViewer_getOffset,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLViewer instance at %s>" % (self.this,)
class FX_GLViewer(FX_GLViewerPtr):
    def __init__(self,this):
        self.this = this




class FXGLViewerPtr(FX_GLViewerPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_resize,(self,) + _args, _kwargs)
        return val
    def getDefaultWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_getDefaultWidth,(self,) + _args, _kwargs)
        return val
    def getDefaultHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_getDefaultHeight,(self,) + _args, _kwargs)
        return val
    def show(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_show,(self,) + _args, _kwargs)
        return val
    def hide(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_hide,(self,) + _args, _kwargs)
        return val
    def enable(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_enable,(self,) + _args, _kwargs)
        return val
    def disable(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_disable,(self,) + _args, _kwargs)
        return val
    def canFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_canFocus,(self,) + _args, _kwargs)
        return val
    def setFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_setFocus,(self,) + _args, _kwargs)
        return val
    def killFocus(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_killFocus,(self,) + _args, _kwargs)
        return val
    def setDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_setDefault,(self,) + _args, _kwargs)
        return val
    def recalc(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_recalc,(self,) + _args, _kwargs)
        return val
    def layout(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_layout,(self,) + _args, _kwargs)
        return val
    def lower(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_lower,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_move,(self,) + _args, _kwargs)
        return val
    def position(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_position,(self,) + _args, _kwargs)
        return val
    def isComposite(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_isComposite,(self,) + _args, _kwargs)
        return val
    def contains(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_contains,(self,) + _args, _kwargs)
        return val
    def getWidthForHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_getWidthForHeight,(self,) + _args, _kwargs)
        return val
    def getHeightForWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_getHeightForWidth,(self,) + _args, _kwargs)
        return val
    def doesSaveUnder(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_doesSaveUnder,(self,) + _args, _kwargs)
        return val
    def reparent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_reparent,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_setBackColor,(self,) + _args, _kwargs)
        return val
    def isCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_isCurrent,(self,) + _args, _kwargs)
        return val
    def makeCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_makeCurrent,(self,) + _args, _kwargs)
        return val
    def makeNonCurrent(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_makeNonCurrent,(self,) + _args, _kwargs)
        return val
    def swapBuffers(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_swapBuffers,(self,) + _args, _kwargs)
        return val
    def select(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_select,(self,) + _args, _kwargs)
        return val
    def pick(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLViewer_pick,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLViewer instance at %s>" % (self.this,)
class FXGLViewer(FXGLViewerPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLViewer1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLViewer2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_GLObjectPtr(FX_ObjectPtr):
    ID_LAST = fox3dc.FX_GLObject_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def bounds(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_bounds,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLObject_drag,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLObject instance at %s>" % (self.this,)
class FX_GLObject(FX_GLObjectPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLObject,_args,_kwargs)
        self.thisown = 1




class FXGLObjectPtr(FX_GLObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLObject_drag,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLObject instance at %s>" % (self.this,)
class FXGLObject(FXGLObjectPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLObject,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLGroupPtr(FX_GLObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getList(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_getList,(self,) + _args, _kwargs)
        return val
    def no(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_no,(self,) + _args, _kwargs)
        return val
    def child(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_child,(self,) + _args, _kwargs)
        return val
    def insert(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_insert,(self,) + _args, _kwargs)
        return val
    def prepend(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_prepend,(self,) + _args, _kwargs)
        return val
    def append(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_append,(self,) + _args, _kwargs)
        return val
    def replace(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_replace,(self,) + _args, _kwargs)
        return val
    def removeObj(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_removeObj,(self,) + _args, _kwargs)
        return val
    def removePos(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_removePos,(self,) + _args, _kwargs)
        return val
    def clear(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLGroup_clear,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLGroup instance at %s>" % (self.this,)
class FX_GLGroup(FX_GLGroupPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLGroup,_args,_kwargs)
        self.thisown = 1




class FXGLGroupPtr(FX_GLGroupPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLGroup_drag,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLGroup instance at %s>" % (self.this,)
class FXGLGroup(FXGLGroupPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLGroup,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLShapePtr(FX_GLObjectPtr):
    ID_SHADEOFF = fox3dc.FX_GLShape_ID_SHADEOFF
    ID_SHADEON = fox3dc.FX_GLShape_ID_SHADEON
    ID_SHADESMOOTH = fox3dc.FX_GLShape_ID_SHADESMOOTH
    ID_TOGGLE_SIDED = fox3dc.FX_GLShape_ID_TOGGLE_SIDED
    ID_TOGGLE_CULLING = fox3dc.FX_GLShape_ID_TOGGLE_CULLING
    ID_STYLE_POINTS = fox3dc.FX_GLShape_ID_STYLE_POINTS
    ID_STYLE_WIREFRAME = fox3dc.FX_GLShape_ID_STYLE_WIREFRAME
    ID_STYLE_SURFACE = fox3dc.FX_GLShape_ID_STYLE_SURFACE
    ID_STYLE_BOUNDINGBOX = fox3dc.FX_GLShape_ID_STYLE_BOUNDINGBOX
    ID_FRONT_MATERIAL = fox3dc.FX_GLShape_ID_FRONT_MATERIAL
    ID_BACK_MATERIAL = fox3dc.FX_GLShape_ID_BACK_MATERIAL
    ID_LAST = fox3dc.FX_GLShape_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDNDDrop(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onDNDDrop,(self,) + _args, _kwargs)
        return val
    def onDNDMotion(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onDNDMotion,(self,) + _args, _kwargs)
        return val
    def onQueryTip(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onQueryTip,(self,) + _args, _kwargs)
        return val
    def onCmdShadeOff(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdShadeOff,(self,) + _args, _kwargs)
        return val
    def onUpdShadeOff(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdShadeOff,(self,) + _args, _kwargs)
        return val
    def onCmdShadeOn(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdShadeOn,(self,) + _args, _kwargs)
        return val
    def onUpdShadeOn(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdShadeOn,(self,) + _args, _kwargs)
        return val
    def onCmdShadeSmooth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdShadeSmooth,(self,) + _args, _kwargs)
        return val
    def onUpdShadeSmooth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdShadeSmooth,(self,) + _args, _kwargs)
        return val
    def onCmdFrontMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdFrontMaterial,(self,) + _args, _kwargs)
        return val
    def onUpdFrontMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdFrontMaterial,(self,) + _args, _kwargs)
        return val
    def onCmdBackMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdBackMaterial,(self,) + _args, _kwargs)
        return val
    def onUpdBackMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdBackMaterial,(self,) + _args, _kwargs)
        return val
    def onCmdDrawingStyle(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onCmdDrawingStyle,(self,) + _args, _kwargs)
        return val
    def onUpdDrawingStyle(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_onUpdDrawingStyle,(self,) + _args, _kwargs)
        return val
    def setTipText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_setTipText,(self,) + _args, _kwargs)
        return val
    def getTipText(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_getTipText,(self,) + _args, _kwargs)
        return val
    def setMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_setMaterial,(self,) + _args, _kwargs)
        return val
    def getMaterial(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLShape_getMaterial,(self,) + _args, _kwargs)
        if val: val = FXMaterialPtr(val) ; val.thisown = 1
        return val
    def __repr__(self):
        return "<C FX_GLShape instance at %s>" % (self.this,)
class FX_GLShape(FX_GLShapePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLShape,_args,_kwargs)
        self.thisown = 1




class FXGLShapePtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLShape_drag,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLShape instance at %s>" % (self.this,)
class FXGLShape(FXGLShapePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLShape,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLPointPtr(FX_GLObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "pos" :
            fox3dc.FX_GLPoint_pos_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "pos" : 
            return fox3dc.FX_GLPoint_pos_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLPoint instance at %s>" % (self.this,)
class FX_GLPoint(FX_GLPointPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLPoint,_args,_kwargs)
        self.thisown = 1




class FXGLPointPtr(FX_GLPointPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLPoint_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "pos" :
            fox3dc.FXGLPoint_pos_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "pos" : 
            return fox3dc.FXGLPoint_pos_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLPoint instance at %s>" % (self.this,)
class FXGLPoint(FXGLPointPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLPoint,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLLinePtr(FX_GLObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "fm" :
            fox3dc.FX_GLLine_fm_set(self,value.this)
            return
        if name == "to" :
            fox3dc.FX_GLLine_to_set(self,value.this)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "fm" : 
            return FX_GLPointPtr(fox3dc.FX_GLLine_fm_get(self))
        if name == "to" : 
            return FX_GLPointPtr(fox3dc.FX_GLLine_to_get(self))
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLLine instance at %s>" % (self.this,)
class FX_GLLine(FX_GLLinePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLLine,_args,_kwargs)
        self.thisown = 1




class FXGLLinePtr(FX_GLLinePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLLine_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "fm" :
            fox3dc.FXGLLine_fm_set(self,value.this)
            return
        if name == "to" :
            fox3dc.FXGLLine_to_set(self,value.this)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "fm" : 
            return FX_GLPointPtr(fox3dc.FXGLLine_fm_get(self))
        if name == "to" : 
            return FX_GLPointPtr(fox3dc.FXGLLine_to_get(self))
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLLine instance at %s>" % (self.this,)
class FXGLLine(FXGLLinePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLLine,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLCubePtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_setWidth,(self,) + _args, _kwargs)
        return val
    def getWidth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_getWidth,(self,) + _args, _kwargs)
        return val
    def setHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_setHeight,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_getHeight,(self,) + _args, _kwargs)
        return val
    def setDepth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_setDepth,(self,) + _args, _kwargs)
        return val
    def getDepth(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCube_getDepth,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "width" :
            fox3dc.FX_GLCube_width_set(self,value)
            return
        if name == "height" :
            fox3dc.FX_GLCube_height_set(self,value)
            return
        if name == "depth" :
            fox3dc.FX_GLCube_depth_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "width" : 
            return fox3dc.FX_GLCube_width_get(self)
        if name == "height" : 
            return fox3dc.FX_GLCube_height_get(self)
        if name == "depth" : 
            return fox3dc.FX_GLCube_depth_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLCube instance at %s>" % (self.this,)
class FX_GLCube(FX_GLCubePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLCube,_args,_kwargs)
        self.thisown = 1




class FXGLCubePtr(FX_GLCubePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCube_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "width" :
            fox3dc.FXGLCube_width_set(self,value)
            return
        if name == "height" :
            fox3dc.FXGLCube_height_set(self,value)
            return
        if name == "depth" :
            fox3dc.FXGLCube_depth_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "width" : 
            return fox3dc.FXGLCube_width_get(self)
        if name == "height" : 
            return fox3dc.FXGLCube_height_get(self)
        if name == "depth" : 
            return fox3dc.FXGLCube_depth_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLCube instance at %s>" % (self.this,)
class FXGLCube(FXGLCubePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLCube,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLSpherePtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_setRadius,(self,) + _args, _kwargs)
        return val
    def getRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_getRadius,(self,) + _args, _kwargs)
        return val
    def setSlices(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_setSlices,(self,) + _args, _kwargs)
        return val
    def getSlices(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_getSlices,(self,) + _args, _kwargs)
        return val
    def setStacks(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_setStacks,(self,) + _args, _kwargs)
        return val
    def getStacks(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLSphere_getStacks,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "radius" :
            fox3dc.FX_GLSphere_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "radius" : 
            return fox3dc.FX_GLSphere_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLSphere instance at %s>" % (self.this,)
class FX_GLSphere(FX_GLSpherePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLSphere,_args,_kwargs)
        self.thisown = 1




class FXGLSpherePtr(FX_GLSpherePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLSphere_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "radius" :
            fox3dc.FXGLSphere_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "radius" : 
            return fox3dc.FXGLSphere_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLSphere instance at %s>" % (self.this,)
class FXGLSphere(FXGLSpherePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLSphere,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLCylinderPtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCylinder_setRadius,(self,) + _args, _kwargs)
        return val
    def getRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCylinder_getRadius,(self,) + _args, _kwargs)
        return val
    def setHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCylinder_setHeight,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCylinder_getHeight,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "height" :
            fox3dc.FX_GLCylinder_height_set(self,value)
            return
        if name == "radius" :
            fox3dc.FX_GLCylinder_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "height" : 
            return fox3dc.FX_GLCylinder_height_get(self)
        if name == "radius" : 
            return fox3dc.FX_GLCylinder_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLCylinder instance at %s>" % (self.this,)
class FX_GLCylinder(FX_GLCylinderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLCylinder,_args,_kwargs)
        self.thisown = 1




class FXGLCylinderPtr(FX_GLCylinderPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCylinder_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "height" :
            fox3dc.FXGLCylinder_height_set(self,value)
            return
        if name == "radius" :
            fox3dc.FXGLCylinder_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "height" : 
            return fox3dc.FXGLCylinder_height_get(self)
        if name == "radius" : 
            return fox3dc.FXGLCylinder_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLCylinder instance at %s>" % (self.this,)
class FXGLCylinder(FXGLCylinderPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLCylinder,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLConePtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCone_setRadius,(self,) + _args, _kwargs)
        return val
    def getRadius(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCone_getRadius,(self,) + _args, _kwargs)
        return val
    def setHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCone_setHeight,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLCone_getHeight,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "height" :
            fox3dc.FX_GLCone_height_set(self,value)
            return
        if name == "radius" :
            fox3dc.FX_GLCone_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "height" : 
            return fox3dc.FX_GLCone_height_get(self)
        if name == "radius" : 
            return fox3dc.FX_GLCone_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_GLCone instance at %s>" % (self.this,)
class FX_GLCone(FX_GLConePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLCone,_args,_kwargs)
        self.thisown = 1




class FXGLConePtr(FX_GLConePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLCone_drag,(self,) + _args, _kwargs)
        return val
    def __setattr__(self,name,value):
        if name == "height" :
            fox3dc.FXGLCone_height_set(self,value)
            return
        if name == "radius" :
            fox3dc.FXGLCone_radius_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "height" : 
            return fox3dc.FXGLCone_height_get(self)
        if name == "radius" : 
            return fox3dc.FXGLCone_radius_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXGLCone instance at %s>" % (self.this,)
class FXGLCone(FXGLConePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLCone,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GLTriangleMeshPtr(FX_GLShapePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setVertexNumber(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_setVertexNumber,(self,) + _args, _kwargs)
        return val
    def getVertexNumber(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_getVertexNumber,(self,) + _args, _kwargs)
        return val
    def setVertexBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_setVertexBuffer,(self,) + _args, _kwargs)
        return val
    def setColorBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_setColorBuffer,(self,) + _args, _kwargs)
        return val
    def setNormalBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_setNormalBuffer,(self,) + _args, _kwargs)
        return val
    def setTextureCoordBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_setTextureCoordBuffer,(self,) + _args, _kwargs)
        return val
    def getVertexBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_getVertexBuffer,(self,) + _args, _kwargs)
        return val
    def getColorBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_getColorBuffer,(self,) + _args, _kwargs)
        return val
    def getNormalBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_getNormalBuffer,(self,) + _args, _kwargs)
        return val
    def getTextureCoordBuffer(self, *_args, **_kwargs):
        val = apply(fox3dc.FX_GLTriangleMesh_getTextureCoordBuffer,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_GLTriangleMesh instance at %s>" % (self.this,)
class FX_GLTriangleMesh(FX_GLTriangleMeshPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FX_GLTriangleMesh,_args,_kwargs)
        self.thisown = 1




class FXGLTriangleMeshPtr(FX_GLTriangleMeshPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_onDefault,(self,) + _args, _kwargs)
        return val
    def draw(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_draw,(self,) + _args, _kwargs)
        return val
    def hit(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_hit,(self,) + _args, _kwargs)
        return val
    def copy(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_copy,(self,) + _args, _kwargs)
        return val
    def identify(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_identify,(self,) + _args, _kwargs)
        return val
    def canDrag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_canDrag,(self,) + _args, _kwargs)
        return val
    def canDelete(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_canDelete,(self,) + _args, _kwargs)
        return val
    def drag(self, *_args, **_kwargs):
        val = apply(fox3dc.FXGLTriangleMesh_drag,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGLTriangleMesh instance at %s>" % (self.this,)
class FXGLTriangleMesh(FXGLTriangleMeshPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(fox3dc.new_FXGLTriangleMesh,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)






#-------------- FUNCTION WRAPPERS ------------------

def CreateGLContext1(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLContext1,_args,_kwargs)
    if val: val = FXGLContextPtr(val)
    return val

def CreateGLContext2(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLContext2,_args,_kwargs)
    if val: val = FXGLContextPtr(val)
    return val

def CreateGLCanvas1(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLCanvas1,_args,_kwargs)
    if val: val = FXGLCanvasPtr(val)
    return val

def CreateGLCanvas2(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLCanvas2,_args,_kwargs)
    if val: val = FXGLCanvasPtr(val)
    return val

def CreateGLViewer1(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLViewer1,_args,_kwargs)
    if val: val = FXGLViewerPtr(val)
    return val

def CreateGLViewer2(*_args, **_kwargs):
    val = apply(fox3dc.CreateGLViewer2,_args,_kwargs)
    if val: val = FXGLViewerPtr(val)
    return val



#-------------- VARIABLE WRAPPERS ------------------

PICK_TOL = fox3dc.PICK_TOL
VIEWER_LOCKED = fox3dc.VIEWER_LOCKED
VIEWER_LIGHTING = fox3dc.VIEWER_LIGHTING
VIEWER_FOG = fox3dc.VIEWER_FOG
VIEWER_DITHER = fox3dc.VIEWER_DITHER
SURFACE_SINGLESIDED = fox3dc.SURFACE_SINGLESIDED
SURFACE_DUALSIDED = fox3dc.SURFACE_DUALSIDED
SHADING_NONE = fox3dc.SHADING_NONE
SHADING_SMOOTH = fox3dc.SHADING_SMOOTH
SHADING_FLAT = fox3dc.SHADING_FLAT
FACECULLING_OFF = fox3dc.FACECULLING_OFF
FACECULLING_ON = fox3dc.FACECULLING_ON
STYLE_SURFACE = fox3dc.STYLE_SURFACE
STYLE_WIREFRAME = fox3dc.STYLE_WIREFRAME
STYLE_POINTS = fox3dc.STYLE_POINTS
STYLE_BOUNDBOX = fox3dc.STYLE_BOUNDBOX
cvar = fox3dc.cvar
