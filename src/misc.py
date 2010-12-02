# This file was created automatically by SWIG.
import miscc
import fox
class FX_RectanglePtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __eq__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle___eq__,(self,) + _args, _kwargs)
        return val
    def __ne__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle___ne__,(self,) + _args, _kwargs)
        return val
    def containsPoint(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_containsPoint,(self,) + _args, _kwargs)
        return val
    def containsXY(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_containsXY,(self,) + _args, _kwargs)
        return val
    def containsRectangle(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_containsRectangle,(self,) + _args, _kwargs)
        return val
    def overlaps(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_overlaps,(self,) + _args, _kwargs)
        return val
    def move(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_move,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def grow(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_grow,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def grow2(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_grow2,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def grow4(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_grow4,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def shrink(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_shrink,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def shrink2(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_shrink2,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def shrink4(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_shrink4,(self,) + _args, _kwargs)
        if val: val = FX_RectanglePtr(val) 
        return val
    def tl(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_tl,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def tr(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_tr,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def bl(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_bl,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def br(self, *_args, **_kwargs):
        val = apply(miscc.FX_Rectangle_br,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __setattr__(self,name,value):
        if name == "x" :
            miscc.FX_Rectangle_x_set(self,value)
            return
        if name == "y" :
            miscc.FX_Rectangle_y_set(self,value)
            return
        if name == "w" :
            miscc.FX_Rectangle_w_set(self,value)
            return
        if name == "h" :
            miscc.FX_Rectangle_h_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "x" : 
            return miscc.FX_Rectangle_x_get(self)
        if name == "y" : 
            return miscc.FX_Rectangle_y_get(self)
        if name == "w" : 
            return miscc.FX_Rectangle_w_get(self)
        if name == "h" : 
            return miscc.FX_Rectangle_h_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_Rectangle instance at %s>" % (self.this,)
class FX_Rectangle(FX_RectanglePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Rectangle,_args,_kwargs)
        self.thisown = 1




class FX_SizePtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __eq__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___eq__,(self,) + _args, _kwargs)
        return val
    def __ne__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___ne__,(self,) + _args, _kwargs)
        return val
    def __add__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___add__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) ; val.thisown = 1
        return val
    def __sub__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___sub__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) ; val.thisown = 1
        return val
    def __mul__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___mul__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) ; val.thisown = 1
        return val
    def __div__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___div__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) ; val.thisown = 1
        return val
    def __iadd__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___iadd__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) 
        return val
    def __isub__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___isub__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) 
        return val
    def __imul__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___imul__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) 
        return val
    def __idiv__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___idiv__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) 
        return val
    def __neg__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Size___neg__,(self,) + _args, _kwargs)
        if val: val = FX_SizePtr(val) ; val.thisown = 1
        return val
    def __setattr__(self,name,value):
        if name == "w" :
            miscc.FX_Size_w_set(self,value)
            return
        if name == "h" :
            miscc.FX_Size_h_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "w" : 
            return miscc.FX_Size_w_get(self)
        if name == "h" : 
            return miscc.FX_Size_h_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_Size instance at %s>" % (self.this,)
class FX_Size(FX_SizePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Size,_args,_kwargs)
        self.thisown = 1




class FX_PointPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __eq__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___eq__,(self,) + _args, _kwargs)
        return val
    def __ne__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___ne__,(self,) + _args, _kwargs)
        return val
    def __add__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___add__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __sub__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___sub__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __mul__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___mul__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __div__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___div__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __iadd__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___iadd__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) 
        return val
    def __isub__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___isub__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) 
        return val
    def __imul__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___imul__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) 
        return val
    def __idiv__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___idiv__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) 
        return val
    def __neg__(self, *_args, **_kwargs):
        val = apply(miscc.FX_Point___neg__,(self,) + _args, _kwargs)
        if val: val = FX_PointPtr(val) ; val.thisown = 1
        return val
    def __setattr__(self,name,value):
        if name == "x" :
            miscc.FX_Point_x_set(self,value)
            return
        if name == "y" :
            miscc.FX_Point_y_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "x" : 
            return miscc.FX_Point_x_get(self)
        if name == "y" : 
            return miscc.FX_Point_y_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FX_Point instance at %s>" % (self.this,)
class FX_Point(FX_PointPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Point,_args,_kwargs)
        self.thisown = 1




class FXFontDescPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "face" :
            miscc.FXFontDesc_face_set(self,value)
            return
        if name == "size" :
            miscc.FXFontDesc_size_set(self,value)
            return
        if name == "weight" :
            miscc.FXFontDesc_weight_set(self,value)
            return
        if name == "slant" :
            miscc.FXFontDesc_slant_set(self,value)
            return
        if name == "encoding" :
            miscc.FXFontDesc_encoding_set(self,value)
            return
        if name == "setwidth" :
            miscc.FXFontDesc_setwidth_set(self,value)
            return
        if name == "flags" :
            miscc.FXFontDesc_flags_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "face" : 
            return miscc.FXFontDesc_face_get(self)
        if name == "size" : 
            return miscc.FXFontDesc_size_get(self)
        if name == "weight" : 
            return miscc.FXFontDesc_weight_get(self)
        if name == "slant" : 
            return miscc.FXFontDesc_slant_get(self)
        if name == "encoding" : 
            return miscc.FXFontDesc_encoding_get(self)
        if name == "setwidth" : 
            return miscc.FXFontDesc_setwidth_get(self)
        if name == "flags" : 
            return miscc.FXFontDesc_flags_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXFontDesc instance at %s>" % (self.this,)
class FXFontDesc(FXFontDescPtr):
    def __init__(self,this):
        self.this = this




class FXPrinterPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "name" :
            miscc.FXPrinter_name_set(self,value)
            return
        if name == "firstpage" :
            miscc.FXPrinter_firstpage_set(self,value)
            return
        if name == "lastpage" :
            miscc.FXPrinter_lastpage_set(self,value)
            return
        if name == "currentpage" :
            miscc.FXPrinter_currentpage_set(self,value)
            return
        if name == "frompage" :
            miscc.FXPrinter_frompage_set(self,value)
            return
        if name == "topage" :
            miscc.FXPrinter_topage_set(self,value)
            return
        if name == "mediasize" :
            miscc.FXPrinter_mediasize_set(self,value)
            return
        if name == "mediawidth" :
            miscc.FXPrinter_mediawidth_set(self,value)
            return
        if name == "mediaheight" :
            miscc.FXPrinter_mediaheight_set(self,value)
            return
        if name == "leftmargin" :
            miscc.FXPrinter_leftmargin_set(self,value)
            return
        if name == "rightmargin" :
            miscc.FXPrinter_rightmargin_set(self,value)
            return
        if name == "topmargin" :
            miscc.FXPrinter_topmargin_set(self,value)
            return
        if name == "bottommargin" :
            miscc.FXPrinter_bottommargin_set(self,value)
            return
        if name == "numcopies" :
            miscc.FXPrinter_numcopies_set(self,value)
            return
        if name == "flags" :
            miscc.FXPrinter_flags_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "name" : 
            return miscc.FXPrinter_name_get(self)
        if name == "firstpage" : 
            return miscc.FXPrinter_firstpage_get(self)
        if name == "lastpage" : 
            return miscc.FXPrinter_lastpage_get(self)
        if name == "currentpage" : 
            return miscc.FXPrinter_currentpage_get(self)
        if name == "frompage" : 
            return miscc.FXPrinter_frompage_get(self)
        if name == "topage" : 
            return miscc.FXPrinter_topage_get(self)
        if name == "mediasize" : 
            return miscc.FXPrinter_mediasize_get(self)
        if name == "mediawidth" : 
            return miscc.FXPrinter_mediawidth_get(self)
        if name == "mediaheight" : 
            return miscc.FXPrinter_mediaheight_get(self)
        if name == "leftmargin" : 
            return miscc.FXPrinter_leftmargin_get(self)
        if name == "rightmargin" : 
            return miscc.FXPrinter_rightmargin_get(self)
        if name == "topmargin" : 
            return miscc.FXPrinter_topmargin_get(self)
        if name == "bottommargin" : 
            return miscc.FXPrinter_bottommargin_get(self)
        if name == "numcopies" : 
            return miscc.FXPrinter_numcopies_get(self)
        if name == "flags" : 
            return miscc.FXPrinter_flags_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXPrinter instance at %s>" % (self.this,)
class FXPrinter(FXPrinterPtr):
    def __init__(self,this):
        self.this = this




class FXPSBoundsPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "xmin" :
            miscc.FXPSBounds_xmin_set(self,value)
            return
        if name == "xmax" :
            miscc.FXPSBounds_xmax_set(self,value)
            return
        if name == "ymin" :
            miscc.FXPSBounds_ymin_set(self,value)
            return
        if name == "ymax" :
            miscc.FXPSBounds_ymax_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "xmin" : 
            return miscc.FXPSBounds_xmin_get(self)
        if name == "xmax" : 
            return miscc.FXPSBounds_xmax_get(self)
        if name == "ymin" : 
            return miscc.FXPSBounds_ymin_get(self)
        if name == "ymax" : 
            return miscc.FXPSBounds_ymax_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXPSBounds instance at %s>" % (self.this,)
class FXPSBounds(FXPSBoundsPtr):
    def __init__(self,this):
        self.this = this




class FXEventPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __setattr__(self,name,value):
        if name == "type" :
            miscc.FXEvent_type_set(self,value)
            return
        if name == "time" :
            miscc.FXEvent_time_set(self,value)
            return
        if name == "win_x" :
            miscc.FXEvent_win_x_set(self,value)
            return
        if name == "win_y" :
            miscc.FXEvent_win_y_set(self,value)
            return
        if name == "root_x" :
            miscc.FXEvent_root_x_set(self,value)
            return
        if name == "root_y" :
            miscc.FXEvent_root_y_set(self,value)
            return
        if name == "state" :
            miscc.FXEvent_state_set(self,value)
            return
        if name == "code" :
            miscc.FXEvent_code_set(self,value)
            return
        if name == "text" :
            miscc.FXEvent_text_set(self,value)
            return
        if name == "last_x" :
            miscc.FXEvent_last_x_set(self,value)
            return
        if name == "last_y" :
            miscc.FXEvent_last_y_set(self,value)
            return
        if name == "click_x" :
            miscc.FXEvent_click_x_set(self,value)
            return
        if name == "click_y" :
            miscc.FXEvent_click_y_set(self,value)
            return
        if name == "click_time" :
            miscc.FXEvent_click_time_set(self,value)
            return
        if name == "click_button" :
            miscc.FXEvent_click_button_set(self,value)
            return
        if name == "click_count" :
            miscc.FXEvent_click_count_set(self,value)
            return
        if name == "moved" :
            miscc.FXEvent_moved_set(self,value)
            return
        if name == "rect" :
            miscc.FXEvent_rect_set(self,value.this)
            return
        if name == "synthetic" :
            miscc.FXEvent_synthetic_set(self,value)
            return
        if name == "target" :
            miscc.FXEvent_target_set(self,value)
            return
        self.__dict__[name] = value
    def __getattr__(self,name):
        if name == "type" : 
            return miscc.FXEvent_type_get(self)
        if name == "time" : 
            return miscc.FXEvent_time_get(self)
        if name == "win_x" : 
            return miscc.FXEvent_win_x_get(self)
        if name == "win_y" : 
            return miscc.FXEvent_win_y_get(self)
        if name == "root_x" : 
            return miscc.FXEvent_root_x_get(self)
        if name == "root_y" : 
            return miscc.FXEvent_root_y_get(self)
        if name == "state" : 
            return miscc.FXEvent_state_get(self)
        if name == "code" : 
            return miscc.FXEvent_code_get(self)
        if name == "text" : 
            return miscc.FXEvent_text_get(self)
        if name == "last_x" : 
            return miscc.FXEvent_last_x_get(self)
        if name == "last_y" : 
            return miscc.FXEvent_last_y_get(self)
        if name == "click_x" : 
            return miscc.FXEvent_click_x_get(self)
        if name == "click_y" : 
            return miscc.FXEvent_click_y_get(self)
        if name == "click_time" : 
            return miscc.FXEvent_click_time_get(self)
        if name == "click_button" : 
            return miscc.FXEvent_click_button_get(self)
        if name == "click_count" : 
            return miscc.FXEvent_click_count_get(self)
        if name == "moved" : 
            return miscc.FXEvent_moved_get(self)
        if name == "rect" : 
            return FX_RectanglePtr(miscc.FXEvent_rect_get(self))
        if name == "synthetic" : 
            return miscc.FXEvent_synthetic_get(self)
        if name == "target" : 
            return miscc.FXEvent_target_get(self)
        raise AttributeError,name
    def __repr__(self):
        return "<C FXEvent instance at %s>" % (self.this,)
class FXEvent(FXEventPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXEvent,_args,_kwargs)
        self.thisown = 1




class FX_ObjectPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getClassName(self, *_args, **_kwargs):
        val = apply(miscc.FX_Object_getClassName,(self,) + _args, _kwargs)
        return val
    def save(self, *_args, **_kwargs):
        val = apply(miscc.FX_Object_save,(self,) + _args, _kwargs)
        return val
    def load(self, *_args, **_kwargs):
        val = apply(miscc.FX_Object_load,(self,) + _args, _kwargs)
        return val
    def handle(self, *_args, **_kwargs):
        val = apply(miscc.FX_Object_handle,(self,) + _args, _kwargs)
        return val
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FX_Object_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Object instance at %s>" % (self.this,)
    
    def _search(self, key):
	try:
            for (keylo, keyhi, func) in self.FXMSGMAP:
                if keylo <= key and keyhi >= key:
                    return func
	except:
	    pass
        return None

class FX_Object(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this




class FXObjectPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXObject_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXObject instance at %s>" % (self.this,)
class FXObject(FXObjectPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXObject,_args,_kwargs)
        self.thisown = 1




class FX_IdPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getApp(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_getApp,(self,) + _args, _kwargs)
        return val
    def id(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_id,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_create,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_detach,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_destroy,(self,) + _args, _kwargs)
        return val
    def setUserData(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_setUserData,(self,) + _args, _kwargs)
        return val
    def getUserData(self, *_args, **_kwargs):
        val = apply(miscc.FX_Id_getUserData,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Id instance at %s>" % (self.this,)
class FX_Id(FX_IdPtr):
    def __init__(self,this):
        self.this = this




class FXIdPtr(FX_IdPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXId_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXId_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXId_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXId_detach,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXId instance at %s>" % (self.this,)
class FXId(FXIdPtr):
    def __init__(self,this):
        self.this = this




class FX_DrawablePtr(FX_IdPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getWidth(self, *_args, **_kwargs):
        val = apply(miscc.FX_Drawable_getWidth,(self,) + _args, _kwargs)
        return val
    def getHeight(self, *_args, **_kwargs):
        val = apply(miscc.FX_Drawable_getHeight,(self,) + _args, _kwargs)
        return val
    def getVisual(self, *_args, **_kwargs):
        val = apply(miscc.FX_Drawable_getVisual,(self,) + _args, _kwargs)
        if val: val = FX_VisualPtr(val) 
        return val
    def setVisual(self, *_args, **_kwargs):
        val = apply(miscc.FX_Drawable_setVisual,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FX_Drawable_resize,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Drawable instance at %s>" % (self.this,)
class FX_Drawable(FX_DrawablePtr):
    def __init__(self,this):
        self.this = this




class FXDrawablePtr(FX_DrawablePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXDrawable_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXDrawable_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXDrawable_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXDrawable_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXDrawable_resize,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDrawable instance at %s>" % (self.this,)
class FXDrawable(FXDrawablePtr):
    def __init__(self,this):
        self.this = this




class FX_AppPtr(FX_ObjectPtr):
    ID_QUIT = miscc.FX_App_ID_QUIT
    ID_DUMP = miscc.FX_App_ID_DUMP
    ID_LAST = miscc.FX_App_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdQuit(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_onCmdQuit,(self,) + _args, _kwargs)
        return val
    def onCmdDump(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_onCmdDump,(self,) + _args, _kwargs)
        return val
    def copyright(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_copyright,(self,) + _args, _kwargs)
        return val
    def getAppName(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getAppName,(self,) + _args, _kwargs)
        return val
    def getVendorName(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getVendorName,(self,) + _args, _kwargs)
        return val
    def openDisplay(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_openDisplay,(self,) + _args, _kwargs)
        return val
    def closeDisplay(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_closeDisplay,(self,) + _args, _kwargs)
        return val
    def getDefaultVisual(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getDefaultVisual,(self,) + _args, _kwargs)
        if val: val = FX_VisualPtr(val) 
        return val
    def setDefaultVisual(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setDefaultVisual,(self,) + _args, _kwargs)
        return val
    def getMonoVisual(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getMonoVisual,(self,) + _args, _kwargs)
        if val: val = FX_VisualPtr(val) 
        return val
    def getRoot(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getRoot,(self,) + _args, _kwargs)
        return val
    def getCursorWindow(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getCursorWindow,(self,) + _args, _kwargs)
        return val
    def getFocusWindow(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getFocusWindow,(self,) + _args, _kwargs)
        return val
    def getMainWindow(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getMainWindow,(self,) + _args, _kwargs)
        return val
    def findWindowWithId(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_findWindowWithId,(self,) + _args, _kwargs)
        return val
    def findWindowAt(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_findWindowAt,(self,) + _args, _kwargs)
        return val
    def addTimeout(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_addTimeout,(self,) + _args, _kwargs)
        return val
    def removeTimeout(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_removeTimeout,(self,) + _args, _kwargs)
        return val
    def addChore(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_addChore,(self,) + _args, _kwargs)
        return val
    def removeChore(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_removeChore,(self,) + _args, _kwargs)
        return val
    def addSignal(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_addSignal,(self,) + _args, _kwargs)
        return val
    def removeSignal(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_removeSignal,(self,) + _args, _kwargs)
        return val
    def addInput(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_addInput,(self,) + _args, _kwargs)
        return val
    def removeInput(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_removeInput,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_detach,(self,) + _args, _kwargs)
        return val
    def peekEvent(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_peekEvent,(self,) + _args, _kwargs)
        return val
    def runOneEvent(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runOneEvent,(self,) + _args, _kwargs)
        return val
    def runUntil(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runUntil,(self,) + _args, _kwargs)
        return val
    def runWhileEvents(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runWhileEvents,(self,) + _args, _kwargs)
        return val
    def runModal(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runModal,(self,) + _args, _kwargs)
        return val
    def runModalFor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runModalFor,(self,) + _args, _kwargs)
        return val
    def runModalWhileShown(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runModalWhileShown,(self,) + _args, _kwargs)
        return val
    def runPopup(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_runPopup,(self,) + _args, _kwargs)
        return val
    def isModal(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_isModal,(self,) + _args, _kwargs)
        return val
    def modalWindow(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_modalWindow,(self,) + _args, _kwargs)
        return val
    def modalModality(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_modalModality,(self,) + _args, _kwargs)
        return val
    def stop(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_stop,(self,) + _args, _kwargs)
        return val
    def stopModal(self, *_args, **_kwargs):
        try:
            val = apply(miscc.FX_App_stopModal,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(miscc.FX_App_stopModal2,(self,) + _args, _kwargs)
            return val
    def stopModal2(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_stopModal2,(self,) + _args, _kwargs)
        return val
    def forceRefresh(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_forceRefresh,(self,) + _args, _kwargs)
        return val
    def refresh(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_refresh,(self,) + _args, _kwargs)
        return val
    def flush(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_flush,(self,) + _args, _kwargs)
        return val
    def repaint(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_repaint,(self,) + _args, _kwargs)
        return val
    def exit(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_exit,(self,) + _args, _kwargs)
        return val
    def reg(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_reg,(self,) + _args, _kwargs)
        if val: val = FX_RegistryPtr(val) 
        return val
    def registerDragType(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_registerDragType,(self,) + _args, _kwargs)
        return val
    def getDragTypeName(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getDragTypeName,(self,) + _args, _kwargs)
        return val
    def beep(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_beep,(self,) + _args, _kwargs)
        return val
    def setNormalFont(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setNormalFont,(self,) + _args, _kwargs)
        return val
    def getNormalFont(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getNormalFont,(self,) + _args, _kwargs)
        return val
    def beginWaitCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_beginWaitCursor,(self,) + _args, _kwargs)
        return val
    def endWaitCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_endWaitCursor,(self,) + _args, _kwargs)
        return val
    def setWaitCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setWaitCursor,(self,) + _args, _kwargs)
        return val
    def getWaitCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getWaitCursor,(self,) + _args, _kwargs)
        return val
    def getDefaultCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getDefaultCursor,(self,) + _args, _kwargs)
        return val
    def setDefaultCursor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setDefaultCursor,(self,) + _args, _kwargs)
        return val
    def getTypingSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getTypingSpeed,(self,) + _args, _kwargs)
        return val
    def getClickSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getClickSpeed,(self,) + _args, _kwargs)
        return val
    def getScrollSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getScrollSpeed,(self,) + _args, _kwargs)
        return val
    def getScrollDelay(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getScrollDelay,(self,) + _args, _kwargs)
        return val
    def getBlinkSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getBlinkSpeed,(self,) + _args, _kwargs)
        return val
    def getAnimSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getAnimSpeed,(self,) + _args, _kwargs)
        return val
    def getMenuPause(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getMenuPause,(self,) + _args, _kwargs)
        return val
    def getTooltipPause(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getTooltipPause,(self,) + _args, _kwargs)
        return val
    def getTooltipTime(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getTooltipTime,(self,) + _args, _kwargs)
        return val
    def getDragDelta(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getDragDelta,(self,) + _args, _kwargs)
        return val
    def getWheelLines(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getWheelLines,(self,) + _args, _kwargs)
        return val
    def setTypingSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setTypingSpeed,(self,) + _args, _kwargs)
        return val
    def setClickSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setClickSpeed,(self,) + _args, _kwargs)
        return val
    def setScrollSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setScrollSpeed,(self,) + _args, _kwargs)
        return val
    def setScrollDelay(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setScrollDelay,(self,) + _args, _kwargs)
        return val
    def setBlinkSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setBlinkSpeed,(self,) + _args, _kwargs)
        return val
    def setAnimSpeed(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setAnimSpeed,(self,) + _args, _kwargs)
        return val
    def setMenuPause(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setMenuPause,(self,) + _args, _kwargs)
        return val
    def setTooltipPause(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setTooltipPause,(self,) + _args, _kwargs)
        return val
    def setTooltipTime(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setTooltipTime,(self,) + _args, _kwargs)
        return val
    def setDragDelta(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setDragDelta,(self,) + _args, _kwargs)
        return val
    def setWheelLines(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setWheelLines,(self,) + _args, _kwargs)
        return val
    def getBorderColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getBorderColor,(self,) + _args, _kwargs)
        return val
    def getBaseColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getBaseColor,(self,) + _args, _kwargs)
        return val
    def getHiliteColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getHiliteColor,(self,) + _args, _kwargs)
        return val
    def getShadowColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getShadowColor,(self,) + _args, _kwargs)
        return val
    def getBackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getBackColor,(self,) + _args, _kwargs)
        return val
    def getForeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getForeColor,(self,) + _args, _kwargs)
        return val
    def getSelforeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getSelforeColor,(self,) + _args, _kwargs)
        return val
    def getSelbackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getSelbackColor,(self,) + _args, _kwargs)
        return val
    def getTipforeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getTipforeColor,(self,) + _args, _kwargs)
        return val
    def getTipbackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_getTipbackColor,(self,) + _args, _kwargs)
        return val
    def setBorderColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setBorderColor,(self,) + _args, _kwargs)
        return val
    def setBaseColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setBaseColor,(self,) + _args, _kwargs)
        return val
    def setHiliteColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setHiliteColor,(self,) + _args, _kwargs)
        return val
    def setShadowColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setShadowColor,(self,) + _args, _kwargs)
        return val
    def setBackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setBackColor,(self,) + _args, _kwargs)
        return val
    def setForeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setForeColor,(self,) + _args, _kwargs)
        return val
    def setSelforeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setSelforeColor,(self,) + _args, _kwargs)
        return val
    def setSelbackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setSelbackColor,(self,) + _args, _kwargs)
        return val
    def setTipforeColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setTipforeColor,(self,) + _args, _kwargs)
        return val
    def setTipbackColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_setTipbackColor,(self,) + _args, _kwargs)
        return val
    def dumpWidgets(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_dumpWidgets,(self,) + _args, _kwargs)
        return val
    def init(self, *_args, **_kwargs):
        val = apply(miscc.FX_App_init,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_App instance at %s>" % (self.this,)
class FX_App(FX_AppPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_App,_args,_kwargs)
        self.thisown = 1




class FXAppPtr(FX_AppPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def enableEventHook(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_enableEventHook,(self,) + _args, _kwargs)
        return val
    def disableEventHook(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_disableEventHook,(self,) + _args, _kwargs)
        return val
    def run(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_run,(self,) + _args, _kwargs)
        return val
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXApp_detach,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXApp instance at %s>" % (self.this,)
class FXApp(FXAppPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXApp,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_VisualPtr(FX_IdPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getFlags(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getFlags,(self,) + _args, _kwargs)
        return val
    def getDepth(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getDepth,(self,) + _args, _kwargs)
        return val
    def getNumColors(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getNumColors,(self,) + _args, _kwargs)
        return val
    def getNumRed(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getNumRed,(self,) + _args, _kwargs)
        return val
    def getNumGreen(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getNumGreen,(self,) + _args, _kwargs)
        return val
    def getNumBlue(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getNumBlue,(self,) + _args, _kwargs)
        return val
    def getPixel(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getPixel,(self,) + _args, _kwargs)
        return val
    def getColor(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getColor,(self,) + _args, _kwargs)
        return val
    def setMaxColors(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_setMaxColors,(self,) + _args, _kwargs)
        return val
    def getMaxColors(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getMaxColors,(self,) + _args, _kwargs)
        return val
    def getType(self, *_args, **_kwargs):
        val = apply(miscc.FX_Visual_getType,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Visual instance at %s>" % (self.this,)
class FX_Visual(FX_VisualPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Visual,_args,_kwargs)
        self.thisown = 1




class FXVisualPtr(FX_VisualPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXVisual_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXVisual_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXVisual_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXVisual_detach,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXVisual instance at %s>" % (self.this,)
class FXVisual(FXVisualPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXVisual,_args,_kwargs)
        self.thisown = 1




class FX_FontPtr(FX_IdPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getName(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getName,(self,) + _args, _kwargs)
        return val
    def getSize(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getSize,(self,) + _args, _kwargs)
        return val
    def getWeight(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getWeight,(self,) + _args, _kwargs)
        return val
    def getSlant(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getSlant,(self,) + _args, _kwargs)
        return val
    def getEncoding(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getEncoding,(self,) + _args, _kwargs)
        return val
    def getSetWidth(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getSetWidth,(self,) + _args, _kwargs)
        return val
    def getHints(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getHints,(self,) + _args, _kwargs)
        return val
    def getFontDesc(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontDesc,(self,) + _args, _kwargs)
        if val: val = FXFontDescPtr(val) ; val.thisown = 1
        return val
    def setFontDesc(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_setFontDesc,(self,) + _args, _kwargs)
        return val
    def isFontMono(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_isFontMono,(self,) + _args, _kwargs)
        return val
    def hasChar(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_hasChar,(self,) + _args, _kwargs)
        return val
    def getMinChar(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getMinChar,(self,) + _args, _kwargs)
        return val
    def getMaxChar(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getMaxChar,(self,) + _args, _kwargs)
        return val
    def leftBearing(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_leftBearing,(self,) + _args, _kwargs)
        return val
    def rightBearing(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_rightBearing,(self,) + _args, _kwargs)
        return val
    def getFontWidth(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontWidth,(self,) + _args, _kwargs)
        return val
    def getFontHeight(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontHeight,(self,) + _args, _kwargs)
        return val
    def getFontAscent(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontAscent,(self,) + _args, _kwargs)
        return val
    def getFontDescent(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontDescent,(self,) + _args, _kwargs)
        return val
    def getFontLeading(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontLeading,(self,) + _args, _kwargs)
        return val
    def getFontSpacing(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getFontSpacing,(self,) + _args, _kwargs)
        return val
    def getTextWidth(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getTextWidth,(self,) + _args, _kwargs)
        return val
    def getTextHeight(self, *_args, **_kwargs):
        val = apply(miscc.FX_Font_getTextHeight,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Font instance at %s>" % (self.this,)
class FX_Font(FX_FontPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Font,_args,_kwargs)
        self.thisown = 1




class FXFontPtr(FX_FontPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXFont_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXFont_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXFont_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXFont_detach,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXFont instance at %s>" % (self.this,)
class FXFont(FXFontPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(miscc.CreateFont1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(miscc.CreateFont2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass

        try:
            self.this = apply(miscc.CreateFont3,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_ImagePtr(FX_DrawablePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getData(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_getData,(self,) + _args, _kwargs)
        return val
    def getOptions(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_getOptions,(self,) + _args, _kwargs)
        return val
    def setOptions(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_setOptions,(self,) + _args, _kwargs)
        return val
    def getChannels(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_getChannels,(self,) + _args, _kwargs)
        return val
    def getPixel(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_getPixel,(self,) + _args, _kwargs)
        return val
    def setPixel(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_setPixel,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FX_Image_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Image instance at %s>" % (self.this,)
class FX_Image(FX_ImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Image,_args,_kwargs)
        self.thisown = 1




class FXImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXImage instance at %s>" % (self.this,)
class FXImage(FXImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GIFImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_GIFImage instance at %s>" % (self.this,)
class FX_GIFImage(FX_GIFImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_GIFImage,_args,_kwargs)
        self.thisown = 1




class FXGIFImagePtr(FX_GIFImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGIFImage instance at %s>" % (self.this,)
class FXGIFImage(FXGIFImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXGIFImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_BMPImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_BMPImage instance at %s>" % (self.this,)
class FX_BMPImage(FX_BMPImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_BMPImage,_args,_kwargs)
        self.thisown = 1




class FXBMPImagePtr(FX_BMPImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXBMPImage instance at %s>" % (self.this,)
class FXBMPImage(FXBMPImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXBMPImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PNGImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_PNGImage instance at %s>" % (self.this,)
class FX_PNGImage(FX_PNGImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_PNGImage,_args,_kwargs)
        self.thisown = 1




class FXPNGImagePtr(FX_PNGImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPNGImage instance at %s>" % (self.this,)
class FXPNGImage(FXPNGImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXPNGImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_JPGImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setQuality(self, *_args, **_kwargs):
        val = apply(miscc.FX_JPGImage_setQuality,(self,) + _args, _kwargs)
        return val
    def getQuality(self, *_args, **_kwargs):
        val = apply(miscc.FX_JPGImage_getQuality,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_JPGImage instance at %s>" % (self.this,)
class FX_JPGImage(FX_JPGImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_JPGImage,_args,_kwargs)
        self.thisown = 1




class FXJPGImagePtr(FX_JPGImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXJPGImage instance at %s>" % (self.this,)
class FXJPGImage(FXJPGImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXJPGImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_XPMImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_XPMImage instance at %s>" % (self.this,)
class FX_XPMImage(FX_XPMImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_XPMImage,_args,_kwargs)
        self.thisown = 1




class FXXPMImagePtr(FX_XPMImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXXPMImage instance at %s>" % (self.this,)
class FXXPMImage(FXXPMImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXXPMImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PCXImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_PCXImage(self)
    def __repr__(self):
        return "<C FX_PCXImage instance at %s>" % (self.this,)
class FX_PCXImage(FX_PCXImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_PCXImage,_args,_kwargs)
        self.thisown = 1




class FXPCXImagePtr(FX_PCXImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPCXImage instance at %s>" % (self.this,)
class FXPCXImage(FXPCXImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXPCXImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TIFImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setCodec(self, *_args, **_kwargs):
        val = apply(miscc.FX_TIFImage_setCodec,(self,) + _args, _kwargs)
        return val
    def getCodec(self, *_args, **_kwargs):
        val = apply(miscc.FX_TIFImage_getCodec,(self,) + _args, _kwargs)
        return val
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_TIFImage(self)
    def __repr__(self):
        return "<C FX_TIFImage instance at %s>" % (self.this,)
class FX_TIFImage(FX_TIFImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_TIFImage,_args,_kwargs)
        self.thisown = 1




class FXTIFImagePtr(FX_TIFImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTIFImage instance at %s>" % (self.this,)
class FXTIFImage(FXTIFImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXTIFImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TGAImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_TGAImage(self)
    def __repr__(self):
        return "<C FX_TGAImage instance at %s>" % (self.this,)
class FX_TGAImage(FX_TGAImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_TGAImage,_args,_kwargs)
        self.thisown = 1




class FXTGAImagePtr(FX_TGAImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTGAImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTGAImage instance at %s>" % (self.this,)
class FXTGAImage(FXTGAImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXTGAImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RGBImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_RGBImage(self)
    def __repr__(self):
        return "<C FX_RGBImage instance at %s>" % (self.this,)
class FX_RGBImage(FX_RGBImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_RGBImage,_args,_kwargs)
        self.thisown = 1




class FXRGBImagePtr(FX_RGBImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXRGBImage instance at %s>" % (self.this,)
class FXRGBImage(FXRGBImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXRGBImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ICOImagePtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_ICOImage(self)
    def __repr__(self):
        return "<C FX_ICOImage instance at %s>" % (self.this,)
class FX_ICOImage(FX_ICOImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_ICOImage,_args,_kwargs)
        self.thisown = 1




class FXICOImagePtr(FX_ICOImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXICOImage_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXICOImage instance at %s>" % (self.this,)
class FXICOImage(FXICOImagePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXICOImage,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_IconPtr(FX_ImagePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_Icon instance at %s>" % (self.this,)
class FX_Icon(FX_IconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Icon,_args,_kwargs)
        self.thisown = 1




class FXIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXIcon instance at %s>" % (self.this,)
class FXIcon(FXIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_GIFIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_GIFIcon instance at %s>" % (self.this,)
class FX_GIFIcon(FX_GIFIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_GIFIcon,_args,_kwargs)
        self.thisown = 1




class FXGIFIconPtr(FX_GIFIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXGIFIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXGIFIcon instance at %s>" % (self.this,)
class FXGIFIcon(FXGIFIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXGIFIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_BMPIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_BMPIcon instance at %s>" % (self.this,)
class FX_BMPIcon(FX_BMPIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_BMPIcon,_args,_kwargs)
        self.thisown = 1




class FXBMPIconPtr(FX_BMPIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXBMPIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXBMPIcon instance at %s>" % (self.this,)
class FXBMPIcon(FXBMPIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXBMPIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PNGIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_PNGIcon instance at %s>" % (self.this,)
class FX_PNGIcon(FX_PNGIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_PNGIcon,_args,_kwargs)
        self.thisown = 1




class FXPNGIconPtr(FX_PNGIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPNGIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPNGIcon instance at %s>" % (self.this,)
class FXPNGIcon(FXPNGIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXPNGIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_JPGIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setQuality(self, *_args, **_kwargs):
        val = apply(miscc.FX_JPGIcon_setQuality,(self,) + _args, _kwargs)
        return val
    def getQuality(self, *_args, **_kwargs):
        val = apply(miscc.FX_JPGIcon_getQuality,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_JPGIcon instance at %s>" % (self.this,)
class FX_JPGIcon(FX_JPGIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_JPGIcon,_args,_kwargs)
        self.thisown = 1




class FXJPGIconPtr(FX_JPGIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXJPGIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXJPGIcon instance at %s>" % (self.this,)
class FXJPGIcon(FXJPGIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXJPGIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_XPMIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FX_XPMIcon instance at %s>" % (self.this,)
class FX_XPMIcon(FX_XPMIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_XPMIcon,_args,_kwargs)
        self.thisown = 1




class FXXPMIconPtr(FX_XPMIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXXPMIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXXPMIcon instance at %s>" % (self.this,)
class FXXPMIcon(FXXPMIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXXPMIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_PCXIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_PCXIcon(self)
    def __repr__(self):
        return "<C FX_PCXIcon instance at %s>" % (self.this,)
class FX_PCXIcon(FX_PCXIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_PCXIcon,_args,_kwargs)
        self.thisown = 1




class FXPCXIconPtr(FX_PCXIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FXPCXIcon(self)
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXPCXIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXPCXIcon instance at %s>" % (self.this,)
class FXPCXIcon(FXPCXIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXPCXIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TIFIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setCodec(self, *_args, **_kwargs):
        val = apply(miscc.FX_TIFIcon_setCodec,(self,) + _args, _kwargs)
        return val
    def getCodec(self, *_args, **_kwargs):
        val = apply(miscc.FX_TIFIcon_getCodec,(self,) + _args, _kwargs)
        return val
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_TIFIcon(self)
    def __repr__(self):
        return "<C FX_TIFIcon instance at %s>" % (self.this,)
class FX_TIFIcon(FX_TIFIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_TIFIcon,_args,_kwargs)
        self.thisown = 1




class FXTIFIconPtr(FX_TIFIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FXTIFIcon(self)
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXTIFIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXTIFIcon instance at %s>" % (self.this,)
class FXTIFIcon(FXTIFIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXTIFIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_TGAIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_TGAIcon(self)
    def __repr__(self):
        return "<C FX_TGAIcon instance at %s>" % (self.this,)
class FX_TGAIcon(FX_TGAIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_TGAIcon,_args,_kwargs)
        self.thisown = 1




class FXTGAIconPtr(FX_TGAIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FXTGAIcon(self)
    def __repr__(self):
        return "<C FXTGAIcon instance at %s>" % (self.this,)
class FXTGAIcon(FXTGAIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXTGAIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RGBIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_RGBIcon(self)
    def __repr__(self):
        return "<C FX_RGBIcon instance at %s>" % (self.this,)
class FX_RGBIcon(FX_RGBIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_RGBIcon,_args,_kwargs)
        self.thisown = 1




class FXRGBIconPtr(FX_RGBIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FXRGBIcon(self)
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXRGBIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXRGBIcon instance at %s>" % (self.this,)
class FXRGBIcon(FXRGBIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXRGBIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_ICOIconPtr(FX_IconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_ICOIcon(self)
    def __repr__(self):
        return "<C FX_ICOIcon instance at %s>" % (self.this,)
class FX_ICOIcon(FX_ICOIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_ICOIcon,_args,_kwargs)
        self.thisown = 1




class FXICOIconPtr(FX_ICOIconPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FXICOIcon(self)
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_onDefault,(self,) + _args, _kwargs)
        return val
    def create(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_create,(self,) + _args, _kwargs)
        return val
    def destroy(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_destroy,(self,) + _args, _kwargs)
        return val
    def detach(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_detach,(self,) + _args, _kwargs)
        return val
    def resize(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_resize,(self,) + _args, _kwargs)
        return val
    def restore(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_restore,(self,) + _args, _kwargs)
        return val
    def render(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_render,(self,) + _args, _kwargs)
        return val
    def scale(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_scale,(self,) + _args, _kwargs)
        return val
    def mirror(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_mirror,(self,) + _args, _kwargs)
        return val
    def rotate(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_rotate,(self,) + _args, _kwargs)
        return val
    def crop(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_crop,(self,) + _args, _kwargs)
        return val
    def savePixels(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_savePixels,(self,) + _args, _kwargs)
        return val
    def loadPixels(self, *_args, **_kwargs):
        val = apply(miscc.FXICOIcon_loadPixels,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXICOIcon instance at %s>" % (self.this,)
class FXICOIcon(FXICOIconPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXICOIcon,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_AccelTablePtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onKeyPress(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_onKeyPress,(self,) + _args, _kwargs)
        return val
    def onKeyRelease(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_onKeyRelease,(self,) + _args, _kwargs)
        return val
    def addAccel(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_addAccel,(self,) + _args, _kwargs)
        return val
    def hasAccel(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_hasAccel,(self,) + _args, _kwargs)
        return val
    def targetOfAccel(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_targetOfAccel,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def removeAccel(self, *_args, **_kwargs):
        val = apply(miscc.FX_AccelTable_removeAccel,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_AccelTable instance at %s>" % (self.this,)
class FX_AccelTable(FX_AccelTablePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_AccelTable,_args,_kwargs)
        self.thisown = 1




class FXAccelTablePtr(FX_AccelTablePtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXAccelTable_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXAccelTable instance at %s>" % (self.this,)
class FXAccelTable(FXAccelTablePtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXAccelTable,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RecentFilesPtr(FX_ObjectPtr):
    ID_CLEAR = miscc.FX_RecentFiles_ID_CLEAR
    ID_ANYFILES = miscc.FX_RecentFiles_ID_ANYFILES
    ID_FILE_1 = miscc.FX_RecentFiles_ID_FILE_1
    ID_FILE_2 = miscc.FX_RecentFiles_ID_FILE_2
    ID_FILE_3 = miscc.FX_RecentFiles_ID_FILE_3
    ID_FILE_4 = miscc.FX_RecentFiles_ID_FILE_4
    ID_FILE_5 = miscc.FX_RecentFiles_ID_FILE_5
    ID_FILE_6 = miscc.FX_RecentFiles_ID_FILE_6
    ID_FILE_7 = miscc.FX_RecentFiles_ID_FILE_7
    ID_FILE_8 = miscc.FX_RecentFiles_ID_FILE_8
    ID_FILE_9 = miscc.FX_RecentFiles_ID_FILE_9
    ID_FILE_10 = miscc.FX_RecentFiles_ID_FILE_10
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdClear(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_onCmdClear,(self,) + _args, _kwargs)
        return val
    def onCmdFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_onCmdFile,(self,) + _args, _kwargs)
        return val
    def onUpdFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_onUpdFile,(self,) + _args, _kwargs)
        return val
    def onUpdAnyFiles(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_onUpdAnyFiles,(self,) + _args, _kwargs)
        return val
    def setMaxFiles(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_setMaxFiles,(self,) + _args, _kwargs)
        return val
    def getMaxFiles(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_getMaxFiles,(self,) + _args, _kwargs)
        return val
    def setGroupName(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_setGroupName,(self,) + _args, _kwargs)
        return val
    def getGroupName(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_getGroupName,(self,) + _args, _kwargs)
        return val
    def setTarget(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_setTarget,(self,) + _args, _kwargs)
        return val
    def getTarget(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_getTarget,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def setSelector(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_setSelector,(self,) + _args, _kwargs)
        return val
    def getSelector(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_getSelector,(self,) + _args, _kwargs)
        return val
    def appendFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_appendFile,(self,) + _args, _kwargs)
        return val
    def removeFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_removeFile,(self,) + _args, _kwargs)
        return val
    def clear(self, *_args, **_kwargs):
        val = apply(miscc.FX_RecentFiles_clear,(self,) + _args, _kwargs)
        return val
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_RecentFiles(self)
    def __repr__(self):
        return "<C FX_RecentFiles instance at %s>" % (self.this,)
class FX_RecentFiles(FX_RecentFilesPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_RecentFiles,_args,_kwargs)
        self.thisown = 1




class FXRecentFilesPtr(FX_RecentFilesPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXRecentFiles_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXRecentFiles instance at %s>" % (self.this,)
class FXRecentFiles(FXRecentFilesPtr):
    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(miscc.CreateRecentFiles1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(miscc.CreateRecentFiles2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass




class FX_SettingsPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def parseFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_parseFile,(self,) + _args, _kwargs)
        return val
    def unparseFile(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_unparseFile,(self,) + _args, _kwargs)
        return val
    def data(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_data,(self,) + _args, _kwargs)
        if val: val = FX_StringDictPtr(val) 
        return val
    def find(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_find,(self,) + _args, _kwargs)
        if val: val = FX_StringDictPtr(val) 
        return val
    def readStringEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_readStringEntry,(self,) + _args, _kwargs)
        return val
    def readIntEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_readIntEntry,(self,) + _args, _kwargs)
        return val
    def readUnsignedEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_readUnsignedEntry,(self,) + _args, _kwargs)
        return val
    def readRealEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_readRealEntry,(self,) + _args, _kwargs)
        return val
    def readColorEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_readColorEntry,(self,) + _args, _kwargs)
        return val
    def writeStringEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_writeStringEntry,(self,) + _args, _kwargs)
        return val
    def writeIntEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_writeIntEntry,(self,) + _args, _kwargs)
        return val
    def writeUnsignedEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_writeUnsignedEntry,(self,) + _args, _kwargs)
        return val
    def writeRealEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_writeRealEntry,(self,) + _args, _kwargs)
        return val
    def writeColorEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_writeColorEntry,(self,) + _args, _kwargs)
        return val
    def deleteEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_deleteEntry,(self,) + _args, _kwargs)
        return val
    def deleteSection(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_deleteSection,(self,) + _args, _kwargs)
        return val
    def existingSection(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_existingSection,(self,) + _args, _kwargs)
        return val
    def existingEntry(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_existingEntry,(self,) + _args, _kwargs)
        return val
    def clear(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_clear,(self,) + _args, _kwargs)
        return val
    def setModified(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_setModified,(self,) + _args, _kwargs)
        return val
    def isModified(self, *_args, **_kwargs):
        val = apply(miscc.FX_Settings_isModified,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Settings instance at %s>" % (self.this,)
class FX_Settings(FX_SettingsPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Settings,_args,_kwargs)
        self.thisown = 1




class FX_RegistryPtr(FX_SettingsPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def read(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_read,(self,) + _args, _kwargs)
        return val
    def write(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_write,(self,) + _args, _kwargs)
        return val
    def getAppKey(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_getAppKey,(self,) + _args, _kwargs)
        return val
    def getVendorKey(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_getVendorKey,(self,) + _args, _kwargs)
        return val
    def setAsciiMode(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_setAsciiMode,(self,) + _args, _kwargs)
        return val
    def getAsciiMode(self, *_args, **_kwargs):
        val = apply(miscc.FX_Registry_getAsciiMode,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Registry instance at %s>" % (self.this,)
class FX_Registry(FX_RegistryPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Registry,_args,_kwargs)
        self.thisown = 1




class FX_StreamPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def open(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_open,(self,) + _args, _kwargs)
        return val
    def close(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_close,(self,) + _args, _kwargs)
        return val
    def status(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_status,(self,) + _args, _kwargs)
        return val
    def setError(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_setError,(self,) + _args, _kwargs)
        return val
    def direction(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_direction,(self,) + _args, _kwargs)
        return val
    def container(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_container,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def getPosition(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_getPosition,(self,) + _args, _kwargs)
        return val
    def setPosition(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_setPosition,(self,) + _args, _kwargs)
        return val
    def swapBytes(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_swapBytes,(self,) + _args, _kwargs)
        return val
    def bytesSwapped(self, *_args, **_kwargs):
        val = apply(miscc.FX_Stream_bytesSwapped,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Stream instance at %s>" % (self.this,)
class FX_Stream(FX_StreamPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Stream,_args,_kwargs)
        self.thisown = 1




class FXStreamPtr(FX_StreamPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXStream instance at %s>" % (self.this,)
class FXStream(FXStreamPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXStream,_args,_kwargs)
        self.thisown = 1




class FX_FileStreamPtr(FX_StreamPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def open(self, *_args, **_kwargs):
        val = apply(miscc.FX_FileStream_open,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_FileStream instance at %s>" % (self.this,)
class FX_FileStream(FX_FileStreamPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_FileStream,_args,_kwargs)
        self.thisown = 1




class FXFileStreamPtr(FX_FileStreamPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXFileStream instance at %s>" % (self.this,)
class FXFileStream(FXFileStreamPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXFileStream,_args,_kwargs)
        self.thisown = 1




class FX_DictPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getSize(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_getSize,(self,) + _args, _kwargs)
        return val
    def setSize(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_setSize,(self,) + _args, _kwargs)
        return val
    def no(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_no,(self,) + _args, _kwargs)
        return val
    def insert(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_insert,(self,) + _args, _kwargs)
        return val
    def replace(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_replace,(self,) + _args, _kwargs)
        return val
    def remove(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_remove,(self,) + _args, _kwargs)
        return val
    def find(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_find,(self,) + _args, _kwargs)
        return val
    def key(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_key,(self,) + _args, _kwargs)
        return val
    def data(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_data,(self,) + _args, _kwargs)
        return val
    def mark(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_mark,(self,) + _args, _kwargs)
        return val
    def first(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_first,(self,) + _args, _kwargs)
        return val
    def last(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_last,(self,) + _args, _kwargs)
        return val
    def next(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_next,(self,) + _args, _kwargs)
        return val
    def prev(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_prev,(self,) + _args, _kwargs)
        return val
    def clear(self, *_args, **_kwargs):
        val = apply(miscc.FX_Dict_clear,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Dict instance at %s>" % (self.this,)
class FX_Dict(FX_DictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Dict,_args,_kwargs)
        self.thisown = 1




class FXDictPtr(FX_DictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXDict_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDict instance at %s>" % (self.this,)
class FXDict(FXDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXDict,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_StringDictPtr(FX_DictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def insert(self, *_args, **_kwargs):
        val = apply(miscc.FX_StringDict_insert,(self,) + _args, _kwargs)
        return val
    def replace(self, *_args, **_kwargs):
        val = apply(miscc.FX_StringDict_replace,(self,) + _args, _kwargs)
        return val
    def remove(self, *_args, **_kwargs):
        val = apply(miscc.FX_StringDict_remove,(self,) + _args, _kwargs)
        return val
    def find(self, *_args, **_kwargs):
        val = apply(miscc.FX_StringDict_find,(self,) + _args, _kwargs)
        return val
    def data(self, *_args, **_kwargs):
        val = apply(miscc.FX_StringDict_data,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_StringDict instance at %s>" % (self.this,)
class FX_StringDict(FX_StringDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_StringDict,_args,_kwargs)
        self.thisown = 1




class FXStringDictPtr(FX_StringDictPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXStringDict_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXStringDict instance at %s>" % (self.this,)
class FXStringDict(FXStringDictPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXStringDict,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_RegionPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def empty(self, *_args, **_kwargs):
        val = apply(miscc.FX_Region_empty,(self,) + _args, _kwargs)
        return val
    def containsPoint(self, *_args, **_kwargs):
        val = apply(miscc.FX_Region_containsPoint,(self,) + _args, _kwargs)
        return val
    def containsRectangle(self, *_args, **_kwargs):
        val = apply(miscc.FX_Region_containsRectangle,(self,) + _args, _kwargs)
        return val
    def bounds(self, *_args, **_kwargs):
        val = apply(miscc.FX_Region_bounds,(self,) + _args, _kwargs)
        return val
    def offset(self, *_args, **_kwargs):
        val = apply(miscc.FX_Region_offset,(self,) + _args, _kwargs)
        if val: val = FX_RegionPtr(val) 
        return val
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_Region(self)
    def __repr__(self):
        return "<C FX_Region instance at %s>" % (self.this,)
class FX_Region(FX_RegionPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Region,_args,_kwargs)
        self.thisown = 1




class FX_DelegatorPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def getDelegate(self, *_args, **_kwargs):
        val = apply(miscc.FX_Delegator_getDelegate,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def setDelegate(self, *_args, **_kwargs):
        val = apply(miscc.FX_Delegator_setDelegate,(self,) + _args, _kwargs)
        return val
    def handle(self, *_args, **_kwargs):
        val = apply(miscc.FX_Delegator_handle,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_Delegator instance at %s>" % (self.this,)
class FX_Delegator(FX_DelegatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_Delegator,_args,_kwargs)
        self.thisown = 1




class FXDelegatorPtr(FX_DelegatorPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXDelegator_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDelegator instance at %s>" % (self.this,)
class FXDelegator(FXDelegatorPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXDelegator,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DataTargetPtr(FX_ObjectPtr):
    DT_VOID = miscc.FX_DataTarget_DT_VOID
    DT_CHAR = miscc.FX_DataTarget_DT_CHAR
    DT_UCHAR = miscc.FX_DataTarget_DT_UCHAR
    DT_SHORT = miscc.FX_DataTarget_DT_SHORT
    DT_USHORT = miscc.FX_DataTarget_DT_USHORT
    DT_INT = miscc.FX_DataTarget_DT_INT
    DT_UINT = miscc.FX_DataTarget_DT_UINT
    DT_FLOAT = miscc.FX_DataTarget_DT_FLOAT
    DT_DOUBLE = miscc.FX_DataTarget_DT_DOUBLE
    DT_STRING = miscc.FX_DataTarget_DT_STRING
    DT_LAST = miscc.FX_DataTarget_DT_LAST
    ID_VALUE = miscc.FX_DataTarget_ID_VALUE
    ID_OPTION = miscc.FX_DataTarget_ID_OPTION
    ID_LAST = miscc.FX_DataTarget_ID_LAST
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onCmdValue(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_onCmdValue,(self,) + _args, _kwargs)
        return val
    def onUpdValue(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_onUpdValue,(self,) + _args, _kwargs)
        return val
    def onCmdOption(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_onCmdOption,(self,) + _args, _kwargs)
        return val
    def onUpdOption(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_onUpdOption,(self,) + _args, _kwargs)
        return val
    def setTarget(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_setTarget,(self,) + _args, _kwargs)
        return val
    def getTarget(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_getTarget,(self,) + _args, _kwargs)
        if val: val = FX_ObjectPtr(val) 
        return val
    def setSelector(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_setSelector,(self,) + _args, _kwargs)
        return val
    def getSelector(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_getSelector,(self,) + _args, _kwargs)
        return val
    def getType(self, *_args, **_kwargs):
        val = apply(miscc.FX_DataTarget_getType,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DataTarget instance at %s>" % (self.this,)
class FX_DataTarget(FX_DataTargetPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_DataTarget,_args,_kwargs)
        self.thisown = 1




class FXDataTargetPtr(FX_DataTargetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def setValue(self, *_args, **_kwargs):
        val = apply(miscc.FXDataTarget_setValue,(self,) + _args, _kwargs)
        return val
    def getValue(self, *_args, **_kwargs):
        val = apply(miscc.FXDataTarget_getValue,(self,) + _args, _kwargs)
        return val
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXDataTarget_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDataTarget instance at %s>" % (self.this,)
class FXDataTarget(FXDataTargetPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXDataTarget,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_DebugTargetPtr(FX_ObjectPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onMessage(self, *_args, **_kwargs):
        val = apply(miscc.FX_DebugTarget_onMessage,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FX_DebugTarget instance at %s>" % (self.this,)
class FX_DebugTarget(FX_DebugTargetPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FX_DebugTarget,_args,_kwargs)
        self.thisown = 1




class FXDebugTargetPtr(FX_DataTargetPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def onDefault(self, *_args, **_kwargs):
        val = apply(miscc.FXDebugTarget_onDefault,(self,) + _args, _kwargs)
        return val
    def __repr__(self):
        return "<C FXDebugTarget instance at %s>" % (self.this,)
class FXDebugTarget(FXDebugTargetPtr):
    def __init__(self,*_args,**_kwargs):
        self.this = apply(miscc.new_FXDebugTarget,_args,_kwargs)
        self.thisown = 1
        FXPyRegister(self)




class FX_CommandPtr :
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def undo(self, *_args, **_kwargs):
        val = apply(miscc.FX_Command_undo,(self,) + _args, _kwargs)
        return val
    def redo(self, *_args, **_kwargs):
        val = apply(miscc.FX_Command_redo,(self,) + _args, _kwargs)
        return val
    def size(self, *_args, **_kwargs):
        val = apply(miscc.FX_Command_size,(self,) + _args, _kwargs)
        return val
    def undoName(self, *_args, **_kwargs):
        val = apply(miscc.FX_Command_undoName,(self,) + _args, _kwargs)
        return val
    def redoName(self, *_args, **_kwargs):
        val = apply(miscc.FX_Command_redoName,(self,) + _args, _kwargs)
        return val
    def __del__(self,miscc=miscc):
        if self.thisown == 1 :
            miscc.delete_FX_Command(self)
    def __repr__(self):
        return "<C FX_Command instance at %s>" % (self.this,)
class FX_Command(FX_CommandPtr):
    def __init__(self,this):
        self.this = this




class FXCommandPtr(FX_CommandPtr):
    def __init__(self,this):
        self.this = this
        self.thisown = 0
    def __repr__(self):
        return "<C FXCommand instance at %s>" % (self.this,)
class FXCommand(FXCommandPtr):
    def __init__(self,this):
        self.this = this






#-------------- FUNCTION WRAPPERS ------------------

FXPyRegister = miscc.FXPyRegister

def CreateFont1(*_args, **_kwargs):
    val = apply(miscc.CreateFont1,_args,_kwargs)
    if val: val = FXFontPtr(val)
    return val

def CreateFont2(*_args, **_kwargs):
    val = apply(miscc.CreateFont2,_args,_kwargs)
    if val: val = FXFontPtr(val)
    return val

def CreateFont3(*_args, **_kwargs):
    val = apply(miscc.CreateFont3,_args,_kwargs)
    if val: val = FXFontPtr(val)
    return val

def CreateRecentFiles1(*_args, **_kwargs):
    val = apply(miscc.CreateRecentFiles1,_args,_kwargs)
    if val: val = FXRecentFilesPtr(val)
    return val

def CreateRecentFiles2(*_args, **_kwargs):
    val = apply(miscc.CreateRecentFiles2,_args,_kwargs)
    if val: val = FXRecentFilesPtr(val)
    return val

def FX_App_instance(*_args, **_kwargs):
    val = apply(miscc.FX_App_instance,_args,_kwargs)
    return val

FX_Stream_isLittleEndian = miscc.FX_Stream_isLittleEndian



#-------------- VARIABLE WRAPPERS ------------------

INPUT_NONE = miscc.INPUT_NONE
INPUT_READ = miscc.INPUT_READ
INPUT_WRITE = miscc.INPUT_WRITE
INPUT_EXCEPT = miscc.INPUT_EXCEPT
MODAL_FOR_NONE = miscc.MODAL_FOR_NONE
MODAL_FOR_WINDOW = miscc.MODAL_FOR_WINDOW
MODAL_FOR_POPUP = miscc.MODAL_FOR_POPUP
DEF_ARROW_CURSOR = miscc.DEF_ARROW_CURSOR
DEF_RARROW_CURSOR = miscc.DEF_RARROW_CURSOR
DEF_TEXT_CURSOR = miscc.DEF_TEXT_CURSOR
DEF_HSPLIT_CURSOR = miscc.DEF_HSPLIT_CURSOR
DEF_VSPLIT_CURSOR = miscc.DEF_VSPLIT_CURSOR
DEF_XSPLIT_CURSOR = miscc.DEF_XSPLIT_CURSOR
DEF_SWATCH_CURSOR = miscc.DEF_SWATCH_CURSOR
DEF_MOVE_CURSOR = miscc.DEF_MOVE_CURSOR
DEF_DRAGH_CURSOR = miscc.DEF_DRAGH_CURSOR
DEF_DRAGV_CURSOR = miscc.DEF_DRAGV_CURSOR
DEF_DRAGTL_CURSOR = miscc.DEF_DRAGTL_CURSOR
DEF_DRAGBR_CURSOR = miscc.DEF_DRAGBR_CURSOR
DEF_DRAGTR_CURSOR = miscc.DEF_DRAGTR_CURSOR
DEF_DRAGBL_CURSOR = miscc.DEF_DRAGBL_CURSOR
DEF_DNDSTOP_CURSOR = miscc.DEF_DNDSTOP_CURSOR
DEF_DNDCOPY_CURSOR = miscc.DEF_DNDCOPY_CURSOR
DEF_DNDMOVE_CURSOR = miscc.DEF_DNDMOVE_CURSOR
DEF_DNDLINK_CURSOR = miscc.DEF_DNDLINK_CURSOR
DEF_CROSSHAIR_CURSOR = miscc.DEF_CROSSHAIR_CURSOR
DEF_CORNERNE_CURSOR = miscc.DEF_CORNERNE_CURSOR
DEF_CORNERNW_CURSOR = miscc.DEF_CORNERNW_CURSOR
DEF_CORNERSE_CURSOR = miscc.DEF_CORNERSE_CURSOR
DEF_CORNERSW_CURSOR = miscc.DEF_CORNERSW_CURSOR
DEF_ROTATE_CURSOR = miscc.DEF_ROTATE_CURSOR
VISUAL_DEFAULT = miscc.VISUAL_DEFAULT
VISUAL_MONOCHROME = miscc.VISUAL_MONOCHROME
VISUAL_BEST = miscc.VISUAL_BEST
VISUAL_INDEXCOLOR = miscc.VISUAL_INDEXCOLOR
VISUAL_GRAYSCALE = miscc.VISUAL_GRAYSCALE
VISUAL_TRUECOLOR = miscc.VISUAL_TRUECOLOR
VISUAL_OWNCOLORMAP = miscc.VISUAL_OWNCOLORMAP
VISUAL_DOUBLEBUFFER = miscc.VISUAL_DOUBLEBUFFER
VISUAL_STEREO = miscc.VISUAL_STEREO
VISUAL_NOACCEL = miscc.VISUAL_NOACCEL
VISUALTYPE_UNKNOWN = miscc.VISUALTYPE_UNKNOWN
VISUALTYPE_MONO = miscc.VISUALTYPE_MONO
VISUALTYPE_TRUE = miscc.VISUALTYPE_TRUE
VISUALTYPE_INDEX = miscc.VISUALTYPE_INDEX
VISUALTYPE_GRAY = miscc.VISUALTYPE_GRAY
IMAGE_KEEP = miscc.IMAGE_KEEP
IMAGE_OWNED = miscc.IMAGE_OWNED
IMAGE_DITHER = miscc.IMAGE_DITHER
IMAGE_NEAREST = miscc.IMAGE_NEAREST
IMAGE_ALPHA = miscc.IMAGE_ALPHA
IMAGE_OPAQUE = miscc.IMAGE_OPAQUE
IMAGE_ALPHACOLOR = miscc.IMAGE_ALPHACOLOR
IMAGE_SHMI = miscc.IMAGE_SHMI
IMAGE_SHMP = miscc.IMAGE_SHMP
IMAGE_ALPHAGUESS = miscc.IMAGE_ALPHAGUESS
FXStreamDead = miscc.FXStreamDead
FXStreamSave = miscc.FXStreamSave
FXStreamLoad = miscc.FXStreamLoad
FXStreamOK = miscc.FXStreamOK
FXStreamEnd = miscc.FXStreamEnd
FXStreamFull = miscc.FXStreamFull
FXStreamNoWrite = miscc.FXStreamNoWrite
FXStreamNoRead = miscc.FXStreamNoRead
FXStreamFormat = miscc.FXStreamFormat
FXStreamUnknown = miscc.FXStreamUnknown
FXStreamAlloc = miscc.FXStreamAlloc
