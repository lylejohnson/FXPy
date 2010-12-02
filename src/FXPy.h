/***********************************************************************
 * $Id: FXPy.h,v 1.38 2002/03/29 00:01:42 lyle Exp $
 ***********************************************************************/

#ifndef FXPY_H
#define FXPY_H

// Thread support
#if defined(FXPy_USE_THREADS) && defined(WITH_THREAD)
#define FXPy_WITH_THREADS
#define FXPy_BEGIN_ALLOW_THREADS	Py_BEGIN_ALLOW_THREADS
#define FXPy_END_ALLOW_THREADS		Py_END_ALLOW_THREADS
#else
#undef FXPy_WITH_THREADS
#define FXPy_BEGIN_ALLOW_THREADS
#define FXPy_END_ALLOW_THREADS
#endif

// Global functions
extern void		FXPyCallVoidFunction(FXObject* obj, char* func);
extern FXbool		FXPyCanHandle(FXObject* self,FXSelector sel);
extern long		FXPyHandle(FXObject* self, FXObject* sender,
				   FXSelector sel, void* ptr);
extern void		FXPyRegister(PyObject *pPyObject);
extern void		FXPyUnregister(FXObject *pFXObject);
extern FXObject*	FXPyGetFXObject(PyObject *pPyObject);
extern PyObject*	FXPyGetPyObject(const FXObject *pFXObject);
extern PyObject*	FXPySetDict(PyObject* self, PyObject* args);
extern PyObject*	FXPyMakeShadowObject(const FXObject* obj);
extern FXbool		FXPyRestoreThread();
extern void		FXPySaveThread(FXbool doSave);


// Store a reference to the user data
template <class T>
void FXPySetData(T* item, PyObject *p)
{
    FXbool doSave = FXPyRestoreThread();
    PyObject *oldptr = (PyObject*) item->getData();
    Py_XDECREF(oldptr);
    item->setData((void*) p);
    Py_XINCREF(p);
    FXPySaveThread(doSave);
}


// Returns a new reference to the item data
template <class T>
PyObject* FXPyGetData(const T* item)
{
    PyObject *p = (PyObject*) item->getData();
    FXbool doSave = FXPyRestoreThread();
    Py_XINCREF(p);
    FXPySaveThread(doSave);
    return p;
}


/**
 * Macro to set up class implementation.
 * This is a modified version of the standard FOX macro FXIMPLEMENT();
 * this version's implementation of the virtual handle() function
 * first checks the Python class instance's message map to see if it
 * can handle the incoming message. If not, the regular C++ message
 * mapping takes over as in standard FOX applications.
 */

#define FXPy_IMPLEMENT(classname,baseclassname,mapping,nmappings) \
  FXObject* classname::manufacture(){return new classname;} \
  const FXMetaClass classname::metaClass={#classname,classname::manufacture,&baseclassname::metaClass,mapping,nmappings,sizeof(classname::FXMapEntry),sizeof(#classname)}; \
  __FXMETACLASSINITIALIZER__ classname##Initializer(&classname::metaClass); \
  long classname::handle(FXObject* sender,FXSelector key,void* ptr){ \
    if(FXPyCanHandle(this,key)){ \
      return FXPyHandle(this,sender,key,ptr); \
      } \
    else { \
      const FXMapEntry* me=(const FXMapEntry*)metaClass.search(key); \
      return me ? (this->* me->func)(sender,key,ptr) : baseclassname::handle(sender,key,ptr); \
      } \
    } 


// Forward declarations as needed
class FXPyApp;
class FXPyGLViewer;


// Base class for FOX objects
class FXPyObject : public FXObject {
  FXDECLARE(FXPyObject)
#include "object_virtuals.h"
  };


// Accelerator table
class FXPyAccelTable : public FXAccelTable {
  FXDECLARE(FXPyAccelTable)
public:
  FXPyAccelTable(){}
#include "object_virtuals.h"
  };


// Handle to something in the server
class FXPyId : public FXId {
  FXDECLARE(FXPyId)
protected:
  FXPyId(){}
  FXPyId(FXApp* app) : FXId(app){}
public:
#include "object_virtuals.h"
#include "id_virtuals.h"
  };


// Cursor
class FXPyCursor : public FXCursor {
  FXDECLARE(FXPyCursor)
protected:
  FXPyCursor(){}
  FXPyCursor(const FXPyCursor&);
public:
  // Construct a stock cursor
  FXPyCursor(FXApp* app,FXStockCursor curid) : FXCursor(app,curid){}

  // Construct from shape and mask bitmaps
  FXPyCursor(FXApp* app,const void* src,const void* msk,FXint w,FXint h,FXint hx,FXint hy) : FXCursor(app,src,msk,w,h,hx,hy){}

public:
#include "object_virtuals.h"
#include "cursor_virtuals.h"
  };


// GIF cursor
class FXPyGIFCursor : public FXGIFCursor {
  FXDECLARE(FXPyGIFCursor)
private:
  FXPyGIFCursor(const FXPyGIFCursor&);
  FXPyGIFCursor& operator=(const FXPyGIFCursor&);
protected:
  FXPyGIFCursor(){}
public:
  // Constructor
  FXPyGIFCursor(FXApp* app,const void* pix,FXint hx,FXint hy) : FXGIFCursor(app,pix,hx,hy) {}

public:
#include "object_virtuals.h"
#include "cursor_virtuals.h"
  };


// CUR cursor
class FXPyCURCursor : public FXCURCursor {
  FXDECLARE(FXPyCURCursor)
private:
  FXPyCURCursor(const FXPyCURCursor&);
  FXPyCURCursor& operator=(const FXPyCURCursor&);
protected:
  FXPyCURCursor(){}
public:
  // Constructor
  FXPyCURCursor(FXApp* app,const void* pix) : FXCURCursor(app,pix) {}

public:
#include "object_virtuals.h"
#include "cursor_virtuals.h"
  };


// Icon
class FXPyIcon : public FXIcon {
  FXDECLARE(FXPyIcon)
protected:
  FXPyIcon(){}
public:
  FXPyIcon(FXApp* a,const void *pix,FXColor clr,FXuint opts,FXint w,FXint h) : FXIcon(a,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


// GIF icon
class FXPyGIFIcon : public FXGIFIcon {
  FXDECLARE(FXPyGIFIcon)
protected:
  FXPyGIFIcon(){}
public:
  FXPyGIFIcon(FXApp* app,const void* pix,FXColor clr,FXuint opts,FXint w,FXint h) : FXGIFIcon(app,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


// BMP icon
class FXPyBMPIcon : public FXBMPIcon {
  FXDECLARE(FXPyBMPIcon)
protected:
  FXPyBMPIcon(){}
  FXPyBMPIcon(const FXPyBMPIcon&);
public:
  FXPyBMPIcon(FXApp* app,const void* pix,FXColor clr,FXuint opts,FXint w,FXint h) : FXBMPIcon(app,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


// PNG icon
class FXPyPNGIcon : public FXPNGIcon {
  FXDECLARE(FXPyPNGIcon)
protected:
  FXPyPNGIcon(){}
  FXPyPNGIcon(const FXPyPNGIcon&);
public:
  FXPyPNGIcon(FXApp* app,const void* pix,FXColor clr,FXuint opts,FXint w,FXint h) : FXPNGIcon(app,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


// Font
class FXPyFont : public FXFont {
  FXDECLARE(FXPyFont)
protected:
  FXPyFont(){}
public:
  FXPyFont(FXApp* a,const FXString& text) : FXFont(a,text) {}
  FXPyFont(FXApp* a,const FXString& face,FXuint sz,FXuint wt,FXuint sl,FXuint enc,FXuint setw,FXuint h) : FXFont(a,face,sz,wt,sl,enc,setw,h) {}
  FXPyFont(FXApp* a,const FXFontDesc& fontdesc) : FXFont(a,fontdesc) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
  };


// Composite
class FXPyComposite : public FXComposite {
  FXDECLARE(FXPyComposite)
protected:
  FXPyComposite(){}
public:
  FXPyComposite(FXComposite* p,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXComposite(p,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Button
class FXPyButton : public FXButton {
  FXDECLARE(FXPyButton)
protected:
  FXPyButton(){}
public:
  FXPyButton(FXComposite* p,const FXString& text,FXIcon *ic=0,FXObject* tgt=NULL,FXSelector sel=0,FXuint opts=BUTTON_NORMAL,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pb=DEFAULT_PAD,FXint pt=DEFAULT_PAD) : FXButton(p,text,ic,tgt,sel,opts,x,y,w,h,pl,pr,pb,pt){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Device Context
class FXPyDC : public FXDC {
public:
  FXPyDC(FXApp* app) : FXDC(app){}
  };


// Window Device Context
class FXPyDCWindow : public FXDCWindow {
public:
  // Construct for drawable surface
  FXPyDCWindow(FXDrawable* drawable) : FXDCWindow(drawable){}

  // Construct for drawable surface, with specified clip rectangle
  FXPyDCWindow(FXDrawable* drawable,FXEvent* ev) : FXDCWindow(drawable,ev){}
  };


// Printer Device Context
class FXPyDCPrint : public FXDCPrint {
public:
  // Constructor
  FXPyDCPrint(FXApp* app) : FXDCPrint(app){}
  };


// Drawable
class FXPyDrawable : public FXDrawable {
  FXDECLARE(FXPyDrawable)
protected:
  FXPyDrawable(){}
  FXPyDrawable(FXApp* app,FXint w,FXint h) : FXDrawable(app,w,w) {}
public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
  };


// Image
class FXPyImage : public FXImage {
  FXDECLARE(FXPyImage)
protected:
  FXPyImage(){}
public:
  FXPyImage(FXApp* a,const void *pix,FXuint opts,FXint w,FXint h) : FXImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


// Frame
class FXPyFrame : public FXFrame {
  FXDECLARE(FXPyFrame)
protected:
  FXPyFrame(){}
public:
  FXPyFrame(FXComposite* p,FXuint opts=FRAME_NORMAL,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pt=DEFAULT_PAD,FXint pb=DEFAULT_PAD) : FXFrame(p,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Horizontal Frame
class FXPyHorizontalFrame : public FXHorizontalFrame {
  FXDECLARE(FXPyHorizontalFrame)
protected:
  FXPyHorizontalFrame(){}
public:
  FXPyHorizontalFrame(FXComposite* p,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pb=DEFAULT_PAD,FXint pt=DEFAULT_PAD,FXint hs=DEFAULT_SPACING,FXint vs=DEFAULT_SPACING) : FXHorizontalFrame(p,opts,x,y,w,h,pl,pr,pb,pt,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Horizontal Separator
class FXPyHorizontalSeparator : public FXHorizontalSeparator {
  FXDECLARE(FXPyHorizontalSeparator)
protected:
  FXPyHorizontalSeparator(){}
public:
  FXPyHorizontalSeparator(FXComposite* p,FXuint opts=SEPARATOR_GROOVE|LAYOUT_FILL_X,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=1,FXint pr=1,FXint pt=0,FXint pb=0) : FXHorizontalSeparator(p,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Label
class FXPyLabel : public FXLabel {
  FXDECLARE(FXPyLabel)
protected:
  FXPyLabel(){}
public:
  FXPyLabel(FXComposite* p,const FXString& text,FXIcon *ic=0,FXuint opts=JUSTIFY_NORMAL|ICON_BEFORE_TEXT,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pt=DEFAULT_PAD,FXint pb=DEFAULT_PAD) : FXLabel(p,text,ic,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Vertical Frame
class FXPyVerticalFrame : public FXVerticalFrame {
  FXDECLARE(FXPyVerticalFrame)
protected:
  FXPyVerticalFrame(){}
public:
  FXPyVerticalFrame(FXComposite* p,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pb=DEFAULT_PAD,FXint pt=DEFAULT_PAD,FXint hs=DEFAULT_SPACING,FXint vs=DEFAULT_SPACING) : FXVerticalFrame(p,opts,x,y,w,h,pl,pr,pb,pt,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Vertical Separator
class FXPyVerticalSeparator : public FXVerticalSeparator {
  FXDECLARE(FXPyVerticalSeparator)
protected:
  FXPyVerticalSeparator(){}
public:
  FXPyVerticalSeparator(FXComposite* p,FXuint opts=SEPARATOR_GROOVE|LAYOUT_FILL_X,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=1,FXint pr=1,FXint pt=0,FXint pb=0) : FXVerticalSeparator(p,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Window
class FXPyWindow : public FXWindow {
  FXDECLARE(FXPyWindow)
protected:
  FXPyWindow(){}
  FXPyWindow(const FXPyWindow&);
public:
  FXPyWindow(FXComposite* p,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXWindow(p,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Canvas
class FXPyCanvas : public FXCanvas {
  FXDECLARE(FXPyCanvas)
protected:
  FXPyCanvas(){}
public:
  FXPyCanvas(FXComposite* p,FXObject* tgt=NULL,FXSelector sel=0,FXuint opts=FRAME_NORMAL,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXCanvas(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Main window
class FXPyMainWindow : public FXMainWindow {
  FXDECLARE(FXPyMainWindow)
protected:
  FXPyMainWindow(){}
public:
  // Constructor
  FXPyMainWindow(FXApp* a,const FXString& name,FXIcon *ic=NULL,FXIcon *mi=NULL,FXuint opts=DECOR_ALL,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=0,FXint pr=0,FXint pt=0,FXint pb=0,FXint hs=4,FXint vs=4) : FXMainWindow(a,name,ic,mi,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Packer
class FXPyPacker : public FXPacker {
  FXDECLARE(FXPyPacker)
protected:
  FXPyPacker(){}
public:
  FXPyPacker(FXComposite* p,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint pl=DEFAULT_PAD,FXint pr=DEFAULT_PAD,FXint pt=DEFAULT_PAD,FXint pb=DEFAULT_PAD,FXint hs=DEFAULT_SPACING,FXint vs=DEFAULT_SPACING) : FXPacker(p,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Popup
class FXPyPopup : public FXPopup {
  FXDECLARE(FXPyPopup)
protected:
  FXPyPopup(){}
public:
  // Constructor
  FXPyPopup(FXWindow* owner,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXPopup(owner,opts,x,y,w,h) {}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "popup_virtuals.h"
  };


// Shell
class FXPyShell : public FXShell {
  FXDECLARE(FXPyShell)
private:
  FXPyShell(const FXPyShell&);
  FXPyShell &operator=(const FXPyShell&);
protected:
  FXPyShell(){}
  FXPyShell(FXApp* a,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXShell(a,opts,x,y,w,h){}
  FXPyShell(FXWindow* own,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXShell(own,opts,x,y,w,h){}
public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Tooltip
class FXPyTooltip : public FXTooltip {
  FXDECLARE(FXPyTooltip)
protected:
  FXPyTooltip(){}
  FXPyTooltip(const FXPyTooltip&);
public:
  FXPyTooltip(FXApp* app,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXTooltip(app,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };

// Top-level window
class FXPyTopWindow : public FXTopWindow {
  FXDECLARE(FXPyTopWindow)
protected:
  FXPyTopWindow(){}
  FXPyTopWindow(FXWindow* owner,const FXString& name,FXIcon *ic,FXIcon *mi,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXTopWindow(owner,name,ic,mi,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
  FXPyTopWindow(FXApp* app,const FXString& name,FXIcon *ic,FXIcon *mi,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXTopWindow(app,name,ic,mi,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Dialog Box
class FXPyDialogBox : public FXDialogBox {
  FXDECLARE(FXPyDialogBox)
protected:
  FXPyDialogBox(){}
public:
  // Construct owned dialog box
  FXPyDialogBox(FXWindow* owner,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXDialogBox(owner,name,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}

  // Constructing free-floating dialog box
  FXPyDialogBox(FXApp* app,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXDialogBox(app,name,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Status bar
class FXPyStatusbar : public FXStatusbar {
  FXDECLARE(FXPyStatusbar)
protected:
  FXPyStatusbar(){}
public:
  FXPyStatusbar(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXStatusbar(p,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Group box
class FXPyGroupBox : public FXGroupBox {
  FXDECLARE(FXPyGroupBox)
protected:
  FXPyGroupBox(){}
public:
  FXPyGroupBox(FXComposite* p,const FXString& text,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXGroupBox(p,text,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Check button
class FXPyCheckButton : public FXCheckButton {
  FXDECLARE(FXPyCheckButton)
protected:
  FXPyCheckButton(){}
public:
  FXPyCheckButton(FXComposite* p,const FXString& text,FXObject *tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXCheckButton(p,text,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Picker
class FXPyPicker : public FXPicker {
  FXDECLARE(FXPyPicker)
protected:
  FXPyPicker(){}
public:
  FXPyPicker(FXComposite* p,const FXString& text,FXIcon* icon,FXObject *tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXPicker(p,text,icon,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Radio button
class FXPyRadioButton : public FXRadioButton {
  FXDECLARE(FXPyRadioButton)
protected:
  FXPyRadioButton(){}
public:
  FXPyRadioButton(FXComposite* p,const FXString& text,FXObject *tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXRadioButton(p,text,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Menu item separator
class FXPyMenuSeparator : public FXMenuSeparator {
  FXDECLARE(FXPyMenuSeparator)
protected:
  FXPyMenuSeparator(){}
public:
  FXPyMenuSeparator(FXComposite* p,FXuint opts) : FXMenuSeparator(p,opts){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Text menu item
class FXPyMenuCaption : public FXMenuCaption {
  FXDECLARE(FXPyMenuCaption)
protected:
  FXPyMenuCaption(){}
public:
  FXPyMenuCaption(FXComposite* p,const FXString& text,FXIcon* ic,FXuint opts) : FXMenuCaption(p,text,ic,opts){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Popup menu pane
class FXPyMenuPane : public FXMenuPane {
  FXDECLARE(FXPyMenuPane)
protected:
  FXPyMenuPane(){}
public:
  // Constructor
  FXPyMenuPane(FXWindow* owner,FXuint opts) : FXMenuPane(owner,opts){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "popup_virtuals.h"
  };


// Menu title button
class FXPyMenuTitle : public FXMenuTitle {
  FXDECLARE(FXPyMenuTitle)
protected:
  FXPyMenuTitle(){}
public:
  FXPyMenuTitle(FXComposite* p,const FXString& text,FXIcon* ic,FXPopup* pup,FXuint opts) : FXMenuTitle(p,text,ic,pup,opts){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Menu cascade button
class FXPyMenuCascade : public FXMenuCascade {
  FXDECLARE(FXPyMenuCascade)
protected:
  FXPyMenuCascade(){}
public:
  FXPyMenuCascade(FXComposite* p,const FXString& text,FXIcon* ic,FXMenuPane* pup,FXuint opts) : FXMenuCascade(p,text,ic,pup,opts){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Command menu item
class FXPyMenuCommand : public FXMenuCommand {
  FXDECLARE(FXPyMenuCommand)
protected:
  FXPyMenuCommand(){}
public:
  FXPyMenuCommand(FXComposite* p,const FXString& text,FXIcon* ic,FXObject* tgt,FXSelector sel,FXuint opts) : FXMenuCommand(p,text,ic,tgt,sel,opts){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };
  

// Menu bar
class FXPyMenubar : public FXMenubar {
  FXDECLARE(FXPyMenubar)
protected:
  FXPyMenubar(){}
public:
  // Constructor
  FXPyMenubar(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXMenubar(p,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}

  // Constructor
  FXPyMenubar(FXComposite* p,FXComposite* q,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXMenubar(p,q,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}

#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "toolbar_virtuals.h"
  };


// Four-way split
class FXPy4Splitter : public FX4Splitter {
  FXDECLARE(FXPy4Splitter)
protected:
  FXPy4Splitter(){}
public:
  // Constructor
  FXPy4Splitter(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FX4Splitter(p,opts,x,y,w,h) {}

  // Alternate constructor takes a target
  FXPy4Splitter(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FX4Splitter(p,tgt,sel,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Matrix packer
class FXPyMatrix : public FXMatrix {
  FXDECLARE(FXPyMatrix)
protected:
  FXPyMatrix(){}
public:
  FXPyMatrix(FXComposite* p,FXint n,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXMatrix(p,n,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Dial
class FXPyDial : public FXDial {
  FXDECLARE(FXPyDial)
protected:
  FXPyDial(){}
public:
  FXPyDial(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXDial(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Text field
class FXPyTextField : public FXTextField {
  FXDECLARE(FXPyTextField)
protected:
  FXPyTextField(){}
public:
  FXPyTextField(FXComposite* p,FXint cols,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTextField(p,cols,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Slider
class FXPySlider : public FXSlider {
  FXDECLARE(FXPySlider)
protected:
  FXPySlider(){}
public:
  FXPySlider(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXSlider(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Option button
class FXPyOption : public FXOption {
  FXDECLARE(FXPyOption)
protected:
  FXPyOption(){}
public:
  FXPyOption(FXComposite* p,const FXString& text,FXIcon* ic,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXOption(p,text,ic,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Option menu
class FXPyOptionMenu : public FXOptionMenu {
  FXDECLARE(FXPyOptionMenu)
protected:
  FXPyOptionMenu(){}
public:
  FXPyOptionMenu(FXComposite* p,FXPopup* pup,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXOptionMenu(p,pup,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Menu button
class FXPyMenuButton : public FXMenuButton {
  FXDECLARE(FXPyMenuButton)
protected:
  FXPyMenuButton(){}
public:
  FXPyMenuButton(FXComposite* p,const FXString& text,FXIcon* ic,FXPopup* pup,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXMenuButton(p,text,ic,pup,opts,x,y,w,h,pl,pr,pt,pb) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Splitter
class FXPySplitter : public FXSplitter {
  FXDECLARE(FXPySplitter)
protected:
  FXPySplitter(){}
public:
  // Constructor
  FXPySplitter(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXSplitter(p,opts,x,y,w,h){}

  // Constructor with targets
  FXPySplitter(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXSplitter(p,opts,x,y,w,h){}

#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Base class for scrolled stuff
class FXPyScrollArea : public FXScrollArea {
  FXDECLARE(FXPyScrollArea)
protected:
  FXPyScrollArea(){}
public:
  FXPyScrollArea(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXScrollArea(p,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


// Automatic scroll area
class FXPyScrollWindow : public FXScrollWindow {
  FXDECLARE(FXPyScrollWindow)
protected:
  FXPyScrollWindow(){}
public:
  FXPyScrollWindow(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXScrollWindow(p,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyTreeList;


// Tree list item
class FXPyTreeItem : public FXTreeItem {
  FXDECLARE(FXPyTreeItem)
protected:
  FXPyTreeItem(){}
  FXPyTreeItem(const FXPyTreeItem&);
  FXPyTreeItem& operator=(const FXPyTreeItem&);
public:
  FXPyTreeItem(const FXString& text,FXIcon* oi,FXIcon *ci,void *ptr) : FXTreeItem(text,oi,ci,ptr){}
#include "object_virtuals.h"
#include "treeitem_virtuals.h"
};


// Tree list
class FXPyTreeList : public FXTreeList {
  FXDECLARE(FXPyTreeList)
protected:
  FXPyTreeList(){}
  FXPyTreeList(const FXPyTreeList&);
public:
  FXPyTreeList(FXComposite* p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXTreeList(p,nvis,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
 };


// Tree list box
class FXPyTreeListBox : public FXTreeListBox {
  FXDECLARE(FXPyTreeListBox)
protected:
  FXPyTreeListBox(){}
  FXPyTreeListBox(const FXPyTreeListBox&);
public:
  FXPyTreeListBox(FXComposite* p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTreeListBox(p,nvis,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Toolbar Tab
class FXPyToolbarTab : public FXToolbarTab {
  FXDECLARE(FXPyToolbarTab)
protected:
  FXPyToolbarTab(){}
  FXPyToolbarTab(const FXPyToolbarTab&);
public:
  FXPyToolbarTab(FXComposite* p,FXObject* tgt=NULL,FXSelector sel=0,FXuint opts=FRAME_RAISED,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXToolbarTab(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Tab Bar
class FXPyTabBar : public FXTabBar {
  FXDECLARE(FXPyTabBar)
protected:
  FXPyTabBar(){}
  FXPyTabBar(const FXPyTabBar&);
public:
  FXPyTabBar(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTabBar(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "tabbar_virtuals.h"
  };


// Tab item
class FXPyTabItem : public FXTabItem {
  FXDECLARE(FXPyTabItem)
protected:
  FXPyTabItem(){}
  FXPyTabItem(const FXPyTabItem&);
public:
  FXPyTabItem(FXTabBar* p,const FXString& text,FXIcon* ic,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTabItem(p,text,ic,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Tab Book
class FXPyTabBook : public FXTabBook {
  FXDECLARE(FXPyTabBook)
protected:
  FXPyTabBook(){}
  FXPyTabBook(const FXPyTabBook&);
public:
  FXPyTabBook(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTabBook(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "tabbar_virtuals.h"
  };


// Scroll bar
class FXPyScrollbar : public FXScrollbar {
  FXDECLARE(FXPyScrollbar)
protected:
  FXPyScrollbar(){}
  FXPyScrollbar(const FXPyScrollbar&);
public:
  FXPyScrollbar(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXScrollbar(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Corner between scrollbars
class FXPyScrollCorner : public FXScrollCorner {
  FXDECLARE(FXPyScrollCorner)
protected:
  FXPyScrollCorner(){}
  FXPyScrollCorner(const FXPyScrollCorner&);
public:
  FXPyScrollCorner(FXComposite* p) : FXScrollCorner(p){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Progress bar widget
class FXPyProgressBar : public FXProgressBar {
  FXDECLARE(FXPyProgressBar)
protected:
  FXPyProgressBar(){}
  FXPyProgressBar(const FXPyProgressBar&);
public:
  FXPyProgressBar(FXComposite* p,FXObject* target,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXProgressBar(p,target,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Printer selection
class FXPyPrintDialog : public FXPrintDialog {
  FXDECLARE(FXPyPrintDialog)
protected:
  FXPyPrintDialog(){}
  FXPyPrintDialog(const FXPyPrintDialog&);
public:
  FXPyPrintDialog(FXWindow* owner,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXPrintDialog(owner,name,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


class FXPyVisual : public FXVisual {
  FXDECLARE(FXPyVisual)
protected:
  FXPyVisual(){}
  FXPyVisual(const FXPyVisual&);
public:
  FXPyVisual(FXApp* a,FXuint flgs,FXuint d=32) : FXVisual(a,flgs,d){}
#include "object_virtuals.h"
#include "id_virtuals.h"
  };


class FXPyBMPImage : public FXBMPImage {
  FXDECLARE(FXPyBMPImage)
protected:
  FXPyBMPImage(){}
  FXPyBMPImage(FXPyBMPImage&);
public:
  FXPyBMPImage(FXApp* a,const void *pix,FXuint opts,FXint w,FXint h) : FXBMPImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


class FXPyGIFImage : public FXGIFImage {
  FXDECLARE(FXPyGIFImage)
protected:
  FXPyGIFImage(){}
  FXPyGIFImage(FXPyGIFImage&);
public:
  FXPyGIFImage(FXApp* a,const void *pix,FXuint opts,FXint w,FXint h) : FXGIFImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


class FXPyPNGImage : public FXPNGImage {
  FXDECLARE(FXPyPNGImage)
protected:
  FXPyPNGImage(){}
  FXPyPNGImage(FXPyPNGImage&);
public:
  FXPyPNGImage(FXApp* a,const void *pix,FXuint opts,FXint w,FXint h) : FXPNGImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


class FXPyJPGImage : public FXJPGImage {
  FXDECLARE(FXPyJPGImage)
protected:
  FXPyJPGImage(){}
  FXPyJPGImage(FXPyJPGImage&);
public:
  FXPyJPGImage(FXApp* a,const void *pix,FXuint opts,FXint w,FXint h) : FXJPGImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


class FXPyColorWell : public FXColorWell {
  FXDECLARE(FXPyColorWell)
protected:
  FXPyColorWell(){}
  FXPyColorWell(FXPyColorWell&);
public:
  FXPyColorWell(FXComposite* p,FXColor clr,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXColorWell(p,clr,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyColorWheel : public FXColorWheel {
  FXDECLARE(FXPyColorWheel)
protected:
  FXPyColorWheel(){}
  FXPyColorWheel(FXPyColorWheel&);
public:
  FXPyColorWheel(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXColorWheel(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyColorBar : public FXColorBar {
  FXDECLARE(FXPyColorBar)
protected:
  FXPyColorBar(){}
  FXPyColorBar(FXPyColorBar&);
public:
  FXPyColorBar(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXColorBar(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyArrowButton : public FXArrowButton {
  FXDECLARE(FXPyArrowButton)
protected:
  FXPyArrowButton(){}
  FXPyArrowButton(FXPyArrowButton&);
public:
  FXPyArrowButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXArrowButton(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyToggleButton : public FXToggleButton {
  FXDECLARE(FXPyToggleButton)
protected:
  FXPyToggleButton(){}
  FXPyToggleButton(FXPyToggleButton&);
public:
  FXPyToggleButton(FXComposite* p,const FXString& text1,const FXString& text2,FXIcon* ic1,FXIcon* ic2,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXToggleButton(p,text1,text2,ic1,ic2,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyRootWindow : public FXRootWindow {
  FXDECLARE(FXPyRootWindow)
protected:
  FXPyRootWindow(){}
  FXPyRootWindow(FXPyRootWindow&);
public:
  FXPyRootWindow(FXApp* a,FXVisual* vis) : FXRootWindow(a,vis){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPySpinner : public FXSpinner {
  FXDECLARE(FXPySpinner)
protected:
  FXPySpinner(){}
  FXPySpinner(FXPySpinner&);
public:
  FXPySpinner(FXComposite *p,FXint cols,FXObject *tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXSpinner(p,cols,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPySwitcher : public FXSwitcher {
  FXDECLARE(FXPySwitcher)
protected:
  FXPySwitcher(){}
  FXPySwitcher(FXPySwitcher&);
public:
  FXPySwitcher(FXComposite *p,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXSwitcher(p,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyList : public FXList {
  FXDECLARE(FXPyList)
protected:
  FXPyList(){}
  FXPyList(FXPyList&);
public:
  FXPyList(FXComposite *p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXList(p,nvis,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyListItem : public FXListItem {
  FXDECLARE(FXPyListItem)
protected:
  FXPyListItem(){}
  FXPyListItem(const FXPyListItem&);
public:
  FXPyListItem(const FXString& text,FXIcon* ic,void* ptr) : FXListItem(text,ic,ptr){}
#include "object_virtuals.h"
#include "listitem_virtuals.h"
  };


class FXPyComboBox : public FXComboBox {
  FXDECLARE(FXPyComboBox)
protected:
  FXPyComboBox(){}
  FXPyComboBox(FXPyComboBox&);
public:
  FXPyComboBox(FXComposite *p,FXint cols,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXComboBox(p,cols,nvis,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMessageBox : public FXMessageBox {
  FXDECLARE(FXPyMessageBox)
protected:
  FXPyMessageBox(){}
  FXPyMessageBox(FXPyMessageBox&);
public:
  FXPyMessageBox(FXWindow* owner,const FXString& name,const FXString& text,FXIcon* ic,FXuint opts,FXint x,FXint y) : FXMessageBox(owner,name,text,ic,opts,x,y){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Directory list items
class FXPyDirItem : public FXDirItem {
  FXDECLARE(FXPyDirItem)
protected:
  FXPyDirItem(){}
  FXPyDirItem(const FXPyDirItem&);
  FXPyDirItem& operator=(const FXPyDirItem&);
public:
  FXPyDirItem(const FXString& text,FXIcon* oi,FXIcon* ci,void* ptr) : FXDirItem(text,oi,ci,ptr) {}
#include "object_virtuals.h"
#include "treeitem_virtuals.h"
};


class FXPyDirList : public FXDirList {
  FXDECLARE(FXPyDirList)
protected:
  FXPyDirList(){}
  FXPyDirList(FXPyDirList&);
public:
  FXPyDirList(FXComposite *p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXDirList(p,nvis,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyHeader;


class FXPyHeaderItem : public FXHeaderItem {
  FXDECLARE(FXPyHeaderItem)
protected:
  FXPyHeaderItem(){}
  FXPyHeaderItem(const FXPyHeaderItem&);
public:
  FXPyHeaderItem(const FXString& text,FXIcon *ic,FXint size,void *ptr) : FXHeaderItem(text,ic,size,ptr){}
#include "object_virtuals.h"
#include "headeritem_virtuals.h"
  };


class FXPyHeader : public FXHeader {
  FXDECLARE(FXPyHeader)
protected:
  FXPyHeader(){}
  FXPyHeader(FXPyHeader&);
public:
  FXPyHeader(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXHeader(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyShutter : public FXShutter {
  FXDECLARE(FXPyShutter)
protected:
  FXPyShutter(){}
  FXPyShutter(FXPyShutter&);
public:
  FXPyShutter(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXShutter(p,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "shutter_virtuals.h"
  };


class FXPyShutterItem : public FXShutterItem {
  FXDECLARE(FXPyShutterItem)
protected:
  FXPyShutterItem(){}
  FXPyShutterItem(const FXPyShutterItem&);
public:
  FXPyShutterItem(FXShutter *p,const FXString& text,FXIcon* ic,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXShutterItem(p,text,ic,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyIconList;


class FXPyIconItem : public FXIconItem {
  FXDECLARE(FXPyIconItem)
protected:
  FXPyIconItem(){}
  FXPyIconItem(const FXPyIconItem&);
public:
  FXPyIconItem(const FXString& text,FXIcon* bi,FXIcon* mi,void* ptr) : FXIconItem(text,bi,mi,ptr){}
#include "object_virtuals.h"
#include "iconitem_virtuals.h"
  };


class FXPyIconList : public FXIconList {
  FXDECLARE(FXPyIconList)
protected:
  FXPyIconList(){}
  FXPyIconList(FXPyIconList&);
public:
  FXPyIconList(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXIconList(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyFileItem : public FXFileItem {
  FXDECLARE(FXPyFileItem)
protected:
  FXPyFileItem(){}
  FXPyFileItem(const FXPyFileItem&);
  FXPyFileItem& operator=(const FXPyFileItem&);
public:
  FXPyFileItem(const FXString& text,FXIcon* bi,FXIcon* mi,void* ptr) : FXFileItem(text,bi,mi,ptr) {}
#include "object_virtuals.h"
#include "iconitem_virtuals.h"
};


class FXPyFileList : public FXFileList {
  FXDECLARE(FXPyFileList)
protected:
  FXPyFileList(){}
  FXPyFileList(const FXPyFileList&);
public:
  FXPyFileList(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXFileList(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyDirBox : public FXDirBox {
  FXDECLARE(FXPyDirBox)
protected:
  FXPyDirBox(){}
  FXPyDirBox(FXPyDirBox&);
public:
  FXPyDirBox(FXComposite *p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXDirBox(p,nvis,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyFileSelector : public FXFileSelector {
  FXDECLARE(FXPyFileSelector)
protected:
  FXPyFileSelector(){}
  FXPyFileSelector(FXPyFileSelector&);
public:
  FXPyFileSelector(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXFileSelector(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyFileDialog : public FXFileDialog {
  FXDECLARE(FXPyFileDialog)
protected:
  FXPyFileDialog(){}
  FXPyFileDialog(FXPyFileDialog&);
public:
  FXPyFileDialog(FXWindow* owner,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXFileDialog(owner,name,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


class FXPyColorSelector : public FXColorSelector {
  FXDECLARE(FXPyColorSelector)
protected:
  FXPyColorSelector(){}
  FXPyColorSelector(FXPyColorSelector&);
public:
  FXPyColorSelector(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXColorSelector(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyColorDialog : public FXColorDialog {
  FXDECLARE(FXPyColorDialog)
protected:
  FXPyColorDialog(){}
  FXPyColorDialog(FXPyColorDialog&);
public:
  FXPyColorDialog(FXWindow* owner,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXColorDialog(owner,name,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


class FXPyFontSelector : public FXFontSelector {
  FXDECLARE(FXPyFontSelector)
protected:
  FXPyFontSelector(){}
  FXPyFontSelector(FXPyFontSelector&);
public:
  FXPyFontSelector(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXFontSelector(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyFontDialog : public FXFontDialog {
  FXDECLARE(FXPyFontDialog)
protected:
  FXPyFontDialog(){}
  FXPyFontDialog(FXPyFontDialog&);
public:
  FXPyFontDialog(FXWindow* owner,const FXString& name,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXFontDialog(owner,name,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


class FXPyText : public FXText {
  FXDECLARE(FXPyText)
protected:
  FXPyText(){}
  FXPyText(FXPyText&);
public:
  FXPyText(FXComposite *p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXText(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
#include "text_virtuals.h"
  };


class FXPyDocument : public FXDocument {
  FXDECLARE(FXPyDocument)
protected:
  FXPyDocument(FXPyDocument&);
public:
  FXPyDocument() : FXDocument(){}
#include "object_virtuals.h"
  };


class FXPyMDIDeleteButton : public FXMDIDeleteButton {
  FXDECLARE(FXPyMDIDeleteButton)
protected:
  FXPyMDIDeleteButton(){}
  FXPyMDIDeleteButton(FXPyMDIDeleteButton&);
public:
  FXPyMDIDeleteButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIDeleteButton(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIMaximizeButton : public FXMDIMaximizeButton {
  FXDECLARE(FXPyMDIMaximizeButton)
protected:
  FXPyMDIMaximizeButton(){}
  FXPyMDIMaximizeButton(FXPyMDIMaximizeButton&);
public:
  FXPyMDIMaximizeButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIMaximizeButton(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIMenu : public FXMDIMenu {
  FXDECLARE(FXPyMDIMenu)
protected:
  FXPyMDIMenu(){}
  FXPyMDIMenu(FXPyMDIMenu&);
public:
  FXPyMDIMenu(FXWindow* owner,FXObject* tgt) : FXMDIMenu(owner,tgt){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIMinimizeButton : public FXMDIMinimizeButton {
  FXDECLARE(FXPyMDIMinimizeButton)
protected:
  FXPyMDIMinimizeButton(){}
  FXPyMDIMinimizeButton(FXPyMDIMinimizeButton&);
public:
  FXPyMDIMinimizeButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIMinimizeButton(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIRestoreButton : public FXMDIRestoreButton {
  FXDECLARE(FXPyMDIRestoreButton)
protected:
  FXPyMDIRestoreButton(){}
  FXPyMDIRestoreButton(FXPyMDIRestoreButton&);
public:
  FXPyMDIRestoreButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIRestoreButton(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIWindowButton : public FXMDIWindowButton {
  FXDECLARE(FXPyMDIWindowButton)
protected:
  FXPyMDIWindowButton(){}
  FXPyMDIWindowButton(FXPyMDIWindowButton&);
public:
  FXPyMDIWindowButton(FXComposite* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIWindowButton(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyMDIClient : public FXMDIClient {
  FXDECLARE(FXPyMDIClient)
protected:
  FXPyMDIClient(){}
  FXPyMDIClient(FXPyMDIClient&);
public:
  FXPyMDIClient(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIClient(p,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


class FXPyMDIChild : public FXMDIChild {
  FXDECLARE(FXPyMDIChild)
protected:
  FXPyMDIChild(){}
  FXPyMDIChild(FXPyMDIChild&);
public:
  FXPyMDIChild(FXMDIClient* p,const FXString& name,FXIcon* ic,FXMenuPane* mn,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXMDIChild(p,name,ic,mn,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "mdichild_virtuals.h"
  };

// GL object
class FXPyGLObject : public FXGLObject {
  FXDECLARE(FXPyGLObject)
public:
  FXPyGLObject() : FXGLObject() {}
#include "object_virtuals.h"
#include "globject_virtuals.h"
  };


// Shape
class FXPyGLShape : public FXGLShape {
  FXDECLARE(FXPyGLShape)
protected:
  FXPyGLShape(){}
  FXPyGLShape(const FXPyGLShape&);
  FXPyGLShape& operator=(const FXPyGLShape&);
public:
  FXPyGLShape(FXfloat x,FXfloat y,FXfloat z,FXuint opts) : FXGLShape(x,y,z,opts) {}
#include "object_virtuals.h"
#include "globject_virtuals.h"
};


// Cone
class FXPyGLCone : public FXGLCone {
  FXDECLARE(FXPyGLCone)
protected:
  FXPyGLCone(){}
  FXPyGLCone(const FXPyGLCone&);
  FXPyGLCone& operator=(const FXPyGLCone&);
public:
  FXPyGLCone(FXfloat x,FXfloat y,FXfloat z,FXfloat h,FXfloat r) : FXGLCone(x,y,z,h,r){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
};


// Cylinder
class FXPyGLCylinder : public FXGLCylinder {
  FXDECLARE(FXPyGLCylinder)
protected:
  FXPyGLCylinder(){}
  FXPyGLCylinder(const FXPyGLCylinder&);
  FXPyGLCylinder& operator=(const FXPyGLCylinder&);
public:
  FXPyGLCylinder(FXfloat x,FXfloat y,FXfloat z,FXfloat h,FXfloat r) : FXGLCylinder(x,y,z,h,r){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
};


// Triangle Mesh
class FXPyGLTriangleMesh : public FXGLTriangleMesh {
  FXDECLARE(FXPyGLTriangleMesh)
protected:
  FXPyGLTriangleMesh(){}
  FXPyGLTriangleMesh(const FXPyGLTriangleMesh&);
  FXPyGLTriangleMesh& operator=(const FXPyGLTriangleMesh&);
public:
  FXPyGLTriangleMesh(FXfloat x,FXfloat y,FXfloat z,FXint nv,FXfloat* v,FXfloat *c,FXfloat* p,FXfloat* t) : FXGLTriangleMesh(x,y,z,nv,v,c,p,t) {}
#include "object_virtuals.h"
#include "globject_virtuals.h"
};


// OpenGL Visual
class FXPyGLVisual : public FXGLVisual {
  FXDECLARE(FXPyGLVisual)
protected:
  FXPyGLVisual(){}
  FXPyGLVisual(FXPyGLVisual&);
public:
  FXPyGLVisual(FXApp* app,FXuint flags) : FXGLVisual(app,flags){}
#include "object_virtuals.h"
  };


class FXPyGLCanvas : public FXGLCanvas {
  FXDECLARE(FXPyGLCanvas)
protected:
  FXPyGLCanvas(){}
  FXPyGLCanvas(FXPyGLCanvas&);
public:
  // Constructor
  FXPyGLCanvas(FXComposite* p,FXGLVisual *vis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXGLCanvas(p,vis,tgt,sel,opts,x,y,w,h){}

  // Constructor
  FXPyGLCanvas(FXComposite* p,FXGLVisual *vis,FXGLCanvas* sharegroup,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXGLCanvas(p,vis,sharegroup,tgt,sel,opts,x,y,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "glcanvas_virtuals.h"
  };


class FXPyGLCube : public FXGLCube {
  FXDECLARE(FXPyGLCube)
protected:
  FXPyGLCube(){}
  FXPyGLCube(FXPyGLCube&);
public:
  FXPyGLCube(FXfloat x,FXfloat y,FXfloat z,FXfloat w,FXfloat h,FXfloat d) : FXGLCube(x,y,z,w,h,d){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
 };


class FXPyGLGroup : public FXGLGroup {
  FXDECLARE(FXPyGLGroup)
protected:
  FXPyGLGroup(FXPyGLGroup&);
public:
  FXPyGLGroup() : FXGLGroup(){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
  };


class FXPyGLLine : public FXGLLine {
  FXDECLARE(FXPyGLLine)
protected:
  FXPyGLLine(){}
  FXPyGLLine(FXPyGLLine&);
public:
  FXPyGLLine(FXfloat fx,FXfloat fy,FXfloat fz,FXfloat tx,FXfloat ty,FXfloat tz) : FXGLLine(fx,fy,fz,tx,ty,tz){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
  };


class FXPyGLPoint : public FXGLPoint {
  FXDECLARE(FXPyGLPoint)
protected:
  FXPyGLPoint(){}
  FXPyGLPoint(FXPyGLPoint&);
public:
  FXPyGLPoint(FXfloat x,FXfloat y,FXfloat z) : FXGLPoint(x,y,z){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
  };


class FXPyGLSphere : public FXGLSphere {
  FXDECLARE(FXPyGLSphere)
protected:
  FXPyGLSphere(){}
  FXPyGLSphere(FXPyGLSphere&);
public:
  FXPyGLSphere(FXfloat x,FXfloat y,FXfloat z,FXfloat r) : FXGLSphere(x,y,z,r){}
#include "object_virtuals.h"
#include "globject_virtuals.h"
  };


class FXPyGLViewer : public FXGLViewer {
  FXDECLARE(FXPyGLViewer)
protected:
  FXPyGLViewer(){}
  FXPyGLViewer(FXPyGLViewer&);
public:
  // Constructor
  FXPyGLViewer(FXComposite* p,FXGLVisual *vis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXGLViewer(p,vis,tgt,sel,opts,x,y,w,h){}

  // Constructor
  FXPyGLViewer(FXComposite* p,FXGLVisual *vis,FXGLViewer* sharegroup,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXGLViewer(p,vis,sharegroup,tgt,sel,opts,x,y,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "glcanvas_virtuals.h"
#include "glviewer_virtuals.h"
  };


// Table
class FXPyTable : public FXTable {
  FXDECLARE(FXPyTable)
protected:
  FXPyTable(){}
  FXPyTable(const FXPyTable&);
  FXPyTable& operator=(const FXPyTable& rhs);
public:
  FXPyTable(FXComposite *p,FXint nr,FXint nc,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXTable(p,nr,nc,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


// Table items
class FXPyTableItem : public FXTableItem {
  FXDECLARE(FXPyTableItem)
protected:
  FXPyTableItem(){}
  FXPyTableItem(const FXPyTableItem&);
  FXPyTableItem& operator=(const FXPyTableItem& rhs);
public:
  FXPyTableItem(const FXString& text,FXIcon *ic,void *ptr) : FXTableItem(text,ic,ptr) {}
#include "object_virtuals.h"
#include "tableitem_virtuals.h"
};


// Monochrome bitmap
class FXPyBitmap : public FXBitmap {
  FXDECLARE(FXPyBitmap)
protected:
  FXPyBitmap(){}
  FXPyBitmap(const FXPyBitmap&);
public:
  FXPyBitmap(FXApp* app,const void* pix,FXuint opts,FXint w,FXint h) : FXBitmap(app,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
  };


// Dictionary
class FXPyDict : public FXDict {
  FXDECLARE(FXPyDict)
public:
  FXPyDict(){}
#include "object_virtuals.h"
  };


// Icon dictionary
class FXPyIconDict : public FXIconDict {
  FXDECLARE(FXPyIconDict)
protected:
  FXPyIconDict(){}
  FXPyIconDict(const FXPyIconDict&);
public:
  FXPyIconDict(FXApp* app) : FXIconDict(app) {}
#include "object_virtuals.h"
  };


// File dictionary
class FXPyFileDict : public FXFileDict {
  FXDECLARE(FXPyFileDict)
protected:
  FXPyFileDict(){}
  FXPyFileDict(const FXPyFileDict&);
public:
  FXPyFileDict(FXApp* app) : FXFileDict(app) {}
#include "object_virtuals.h"
  };


// String dictionary
class FXPyStringDict : public FXStringDict {
  FXDECLARE(FXPyStringDict)
protected:
  FXPyStringDict(const FXPyStringDict&);
public:
  FXPyStringDict(){}
#include "object_virtuals.h"
  };


// Status line
class FXPyStatusline : public FXStatusline {
  FXDECLARE(FXPyStatusline)
protected:
  FXPyStatusline(){}
  FXPyStatusline(const FXPyStatusline&);
public:
  FXPyStatusline(FXComposite* p,FXObject* tgt,FXSelector sel) : FXStatusline(p,tgt,sel) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
};


// Drag corner for same
class FXPyDragCorner : public FXDragCorner {
  FXDECLARE(FXPyDragCorner)
protected:
  FXPyDragCorner(){}
  FXPyDragCorner(const FXPyDragCorner&);
public:
  FXPyDragCorner(FXComposite* p) : FXDragCorner(p) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
};


// Recently used files
class FXPyRecentFiles : public FXRecentFiles {
  FXDECLARE(FXPyRecentFiles)
private:
  FXPyRecentFiles(const FXPyRecentFiles&);
  FXPyRecentFiles& operator=(const FXPyRecentFiles&);
public:
    FXPyRecentFiles() : FXRecentFiles() {}
    FXPyRecentFiles(const FXString& gp,FXObject* tgt,FXSelector sel) : FXRecentFiles(gp,tgt,sel) {}
#include "object_virtuals.h"
  };


/// X Pixmap icon
class FXPyXPMIcon : public FXXPMIcon {
  FXDECLARE(FXPyXPMIcon)
private:
  FXPyXPMIcon(const FXPyXPMIcon&);
  FXPyXPMIcon &operator=(const FXPyXPMIcon&);
protected:
  FXPyXPMIcon(){}
public:
  /// Construct icon from compiled-in X Pixmap format
  FXPyXPMIcon(FXApp* a,const FXchar **pix=NULL,FXColor clr=0,FXuint opts=0,FXint w=1,FXint h=1) : FXXPMIcon(a,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// X Pixmap image
class FXPyXPMImage : public FXXPMImage {
  FXDECLARE(FXPyXPMImage)
protected:
  FXPyXPMImage(){}
private:
  FXPyXPMImage(const FXPyXPMImage&);
  FXPyXPMImage &operator=(const FXPyXPMImage&);
public:
  /// Construct image from compiled-in X Pixmap format
  FXPyXPMImage(FXApp* a,const FXchar **pix=NULL,FXuint opts=0,FXint w=1,FXint h=1) : FXXPMImage(a,pix,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// PCX icon
class FXPyPCXIcon : public FXPCXIcon {
  FXDECLARE(FXPyPCXIcon)
private:
  FXPyPCXIcon(const FXPyPCXIcon&);
  FXPyPCXIcon &operator=(const FXPyPCXIcon&);
protected:
  FXPyPCXIcon(){}
public:
  /// Constructor
  FXPyPCXIcon(FXApp* a,const void *pix=NULL,FXColor clr=FXRGB(192,192,192),FXuint opts=0,FXint w=1,FXint h=1) : FXPCXIcon(a,pix,clr,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// PCX image
class FXPyPCXImage : public FXPCXImage {
  FXDECLARE(FXPyPCXImage)
protected:
  FXPyPCXImage(){}
private:
  FXPyPCXImage(const FXPyPCXImage&);
  FXPyPCXImage &operator=(const FXPyPCXImage&);
public:
  /// Constructor
  FXPyPCXImage(FXApp* a,const void *pix=NULL,FXuint opts=0,FXint w=1,FXint h=1):FXPCXImage(a,pix,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// TIFF icon
class FXPyTIFIcon : public FXTIFIcon {
  FXDECLARE(FXPyTIFIcon)
private:
  FXPyTIFIcon(const FXPyTIFIcon&);
  FXPyTIFIcon &operator=(const FXPyTIFIcon&);
protected:
  FXPyTIFIcon(){}
public:
  /// Constructor
  FXPyTIFIcon(FXApp* a,const void *pix=NULL,FXColor clr=FXRGB(192,192,192),FXuint opts=0,FXint w=1,FXint h=1) : FXTIFIcon(a,pix,clr,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// TIFF image
class FXPyTIFImage : public FXTIFImage {
  FXDECLARE(FXPyTIFImage)
protected:
  FXPyTIFImage(){}
private:
  FXPyTIFImage(const FXPyTIFImage&);
  FXPyTIFImage &operator=(const FXPyTIFImage&);
public:
  /// Constructor
  FXPyTIFImage(FXApp* a,const void *pix=NULL,FXuint opts=0,FXint w=1,FXint h=1):FXTIFImage(a,pix,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// TGA icon
class FXPyTGAIcon : public FXTGAIcon {
  FXDECLARE(FXPyTGAIcon)
private:
  FXPyTGAIcon(const FXPyTGAIcon&);
  FXPyTGAIcon &operator=(const FXPyTGAIcon&);
protected:
  FXPyTGAIcon(){}
public:
  /// Constructor
  FXPyTGAIcon(FXApp* a,const void *pix=NULL,FXColor clr=FXRGB(192,192,192),FXuint opts=0,FXint w=1,FXint h=1) : FXTGAIcon(a,pix,clr,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// TGA image
class FXPyTGAImage : public FXTGAImage {
  FXDECLARE(FXPyTGAImage)
protected:
  FXPyTGAImage(){}
private:
  FXPyTGAImage(const FXPyTGAImage&);
  FXPyTGAImage &operator=(const FXPyTGAImage&);
public:
  /// Constructor
  FXPyTGAImage(FXApp* a,const void *pix=NULL,FXuint opts=0,FXint w=1,FXint h=1):FXTGAImage(a,pix,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// RGB icon
class FXPyRGBIcon : public FXRGBIcon {
  FXDECLARE(FXPyRGBIcon)
private:
  FXPyRGBIcon(const FXPyRGBIcon&);
  FXPyRGBIcon &operator=(const FXPyRGBIcon&);
protected:
  FXPyRGBIcon(){}
public:
  /// Constructor
  FXPyRGBIcon(FXApp* a,const void *pix=NULL,FXColor clr=FXRGB(192,192,192),FXuint opts=0,FXint w=1,FXint h=1) : FXRGBIcon(a,pix,clr,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// RGB image
class FXPyRGBImage : public FXRGBImage {
  FXDECLARE(FXPyRGBImage)
protected:
  FXPyRGBImage(){}
private:
  FXPyRGBImage(const FXPyRGBImage&);
  FXPyRGBImage &operator=(const FXPyRGBImage&);
public:
  /// Constructor
  FXPyRGBImage(FXApp* a,const void *pix=NULL,FXuint opts=0,FXint w=1,FXint h=1):FXRGBImage(a,pix,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// ICO icon
class FXPyICOIcon : public FXICOIcon {
  FXDECLARE(FXPyICOIcon)
private:
  FXPyICOIcon(const FXPyICOIcon&);
  FXPyICOIcon &operator=(const FXPyICOIcon&);
protected:
  FXPyICOIcon(){}
public:
  /// Constructor
  FXPyICOIcon(FXApp* a,const void *pix=NULL,FXColor clr=FXRGB(192,192,192),FXuint opts=0,FXint w=1,FXint h=1) : FXICOIcon(a,pix,clr,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// ICO image
class FXPyICOImage : public FXICOImage {
  FXDECLARE(FXPyICOImage)
protected:
  FXPyICOImage(){}
private:
  FXPyICOImage(const FXPyICOImage&);
  FXPyICOImage &operator=(const FXPyICOImage&);
public:
  /// Constructor
  FXPyICOImage(FXApp* a,const void *pix=NULL,FXuint opts=0,FXint w=1,FXint h=1):FXICOImage(a,pix,opts,w,h){}

public:
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


/// Delegator
class FXPyDelegator : public FXDelegator {
  FXDECLARE(FXPyDelegator)
private:
  FXPyDelegator(const FXPyDelegator&);
  FXPyDelegator& operator=(const FXPyDelegator&);
public:
  FXPyDelegator(FXObject* target=NULL) : FXDelegator(target){}
#include "object_virtuals.h"
  };


/// Image view
class FXPyImageView : public FXImageView {
  FXDECLARE(FXPyImageView)
private:
  FXPyImageView(const FXPyImageView&);
  FXPyImageView& operator=(const FXPyImageView&);
protected:
  FXPyImageView(){}
public:
  FXPyImageView(FXComposite* p,FXImage* img=NULL,FXObject* tgt=NULL,FXSelector sel=0,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXImageView(p,img,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "scrollarea_virtuals.h"
  };


// Toolbar
class FXPyToolbar : public FXToolbar {
  FXDECLARE(FXPyToolbar)
private:
  FXPyToolbar(const FXPyToolbar&);
  FXPyToolbar& operator=(const FXPyToolbar&);
protected:
  FXPyToolbar(){}
public:
  FXPyToolbar(FXComposite* p,FXComposite* q,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXToolbar(p,q,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
  FXPyToolbar(FXComposite* p,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb,FXint hs,FXint vs) : FXToolbar(p,opts,x,y,w,h,pl,pr,pt,pb,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "toolbar_virtuals.h"
  };


// Toolbar Shell
class FXPyToolbarShell : public FXToolbarShell {
  FXDECLARE(FXPyToolbarShell)
private:
  FXPyToolbarShell(const FXPyToolbarShell&);
  FXPyToolbarShell& operator=(const FXPyToolbarShell&);
protected:
  FXPyToolbarShell(){}
public:
  FXPyToolbarShell(FXWindow* owner,FXuint opts=FRAME_RAISED|FRAME_THICK,FXint x=0,FXint y=0,FXint w=0,FXint h=0,FXint hs=4,FXint vs=4) : FXToolbarShell(owner,opts,x,y,w,h,hs,vs){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };

// Directory selection dialog
class FXPyDirDialog : public FXDirDialog {
  FXDECLARE(FXPyDirDialog)
private:
  FXPyDirDialog(const FXPyDirDialog&);
  FXPyDirDialog& operator=(const FXPyDirDialog&);
protected:
  FXPyDirDialog(){}
public:
  FXPyDirDialog(FXWindow* owner,const FXString& name,FXuint opts=0,FXint x=0,FXint y=0,FXint w=500,FXint h=300) : FXDirDialog(owner,name,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };

// Directory selection widget
class FXPyDirSelector : public FXDirSelector {
  FXDECLARE(FXPyDirSelector)
private:
  FXPyDirSelector(const FXPyDirSelector&);
  FXPyDirSelector& operator=(const FXPyDirSelector&);
protected:
  FXPyDirSelector(){}
public:
  FXPyDirSelector(FXComposite *p,FXObject* tgt=NULL,FXSelector sel=0,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXDirSelector(p,tgt,sel,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


// Replace text
class FXPyReplaceDialog : public FXReplaceDialog {
  FXDECLARE(FXPyReplaceDialog)
private:
  FXPyReplaceDialog(const FXPyReplaceDialog&);
  FXPyReplaceDialog& operator=(const FXPyReplaceDialog&);
protected:
  FXPyReplaceDialog(){}
public:
  FXPyReplaceDialog(FXWindow* owner,const FXString& caption,FXIcon* ic=NULL,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXReplaceDialog(owner,caption,ic,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Search text
class FXPySearchDialog : public FXSearchDialog {
  FXDECLARE(FXPySearchDialog)
private:
  FXPySearchDialog(const FXPySearchDialog&);
  FXPySearchDialog& operator=(const FXPySearchDialog&);
protected:
  FXPySearchDialog(){}
public:
  FXPySearchDialog(FXWindow* owner,const FXString& caption,FXIcon* ic=NULL,FXuint opts=0,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXSearchDialog(owner,caption,ic,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// OpenGL Context
class FXPyGLContext : public FXGLContext {
  FXDECLARE(FXPyGLContext)
private:
  FXPyGLContext(const FXPyGLContext&);
  FXPyGLContext& operator=(const FXPyGLContext&);
protected:
  FXPyGLContext(){}
public:
  // Constructor
  FXPyGLContext(FXApp* app,FXGLVisual* vis) : FXGLContext(app,vis) {}

  // Construct with shared context
  FXPyGLContext(FXApp* app,FXGLVisual* vis,FXGLContext* shared) : FXGLContext(app,vis,shared) {}

public:
#include "object_virtuals.h"
#include "glcontext_virtuals.h"
  };


class FXPyToolbarGrip : public FXToolbarGrip {
  FXDECLARE(FXPyToolbarGrip)
private:
  FXPyToolbarGrip(const FXPyToolbarGrip&);
  FXPyToolbarGrip& operator=(const FXPyToolbarGrip&);
protected:
  FXPyToolbarGrip(){}
public:
  FXPyToolbarGrip(FXToolbar* p,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h) : FXToolbarGrip(p,tgt,sel,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyJPGIcon : public FXJPGIcon {
  FXDECLARE(FXPyJPGIcon)
protected:
  FXPyJPGIcon(){}
  FXPyJPGIcon(FXPyJPGIcon&);
public:
  FXPyJPGIcon(FXApp* a,const void *pix,FXColor clr,FXuint opts,FXint w,FXint h) : FXJPGIcon(a,pix,clr,opts,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "image_virtuals.h"
  };


class FXPyStream : public FXStream {
public:
  FXPyStream(const FXObject* container) : FXStream(container) {}
  };


class FXPyFileStream : public FXFileStream {
public:
  FXPyFileStream(const FXObject* container) : FXFileStream(container) {}
  };


class FXPyListBox : public FXListBox {
  FXDECLARE(FXPyListBox)
private:
  FXPyListBox(const FXPyListBox&);
  FXPyListBox& operator=(const FXPyListBox&);
protected:
  FXPyListBox(){}
public:
  FXPyListBox(FXComposite* p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXListBox(p,nvis,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyDriveBox : public FXDriveBox {
  FXDECLARE(FXPyDriveBox)
private:
  FXPyDriveBox(const FXPyDriveBox&);
  FXPyDriveBox& operator=(const FXPyDriveBox&);
protected:
  FXPyDriveBox(){}
public:
  FXPyDriveBox(FXComposite* p,FXint nvis,FXObject* tgt,FXSelector sel,FXuint opts,FXint x,FXint y,FXint w,FXint h,FXint pl,FXint pr,FXint pt,FXint pb) : FXDriveBox(p,nvis,tgt,sel,opts,x,y,w,h,pl,pr,pt,pb) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
  };


class FXPyInputDialog : public FXInputDialog {
  FXDECLARE(FXPyInputDialog)
private:
  FXPyInputDialog(const FXPyInputDialog&);
  FXPyInputDialog& operator=(const FXPyInputDialog&);
protected:
  FXPyInputDialog(){}
public:
  FXPyInputDialog(FXWindow* owner,const FXString& caption,const FXString& label,FXIcon* ic=NULL,FXuint opts=INPUTDIALOG_STRING,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXInputDialog(owner,caption,label,ic,opts,x,y,w,h) {}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


class FXPyProgressDialog : public FXProgressDialog {
  FXDECLARE(FXPyProgressDialog)
private:
  FXPyProgressDialog(const FXPyProgressDialog&);
  FXPyProgressDialog& operator=(const FXPyProgressDialog&);
protected:
  FXPyProgressDialog(){}
public:
  FXPyProgressDialog(FXWindow* owner,const FXString& caption,const FXString& label,FXuint opts=PROGRESSDIALOG_NORMAL,FXint x=0,FXint y=0,FXint w=0,FXint h=0) : FXProgressDialog(owner,caption,label,opts,x,y,w,h){}
#include "object_virtuals.h"
#include "id_virtuals.h"
#include "drawable_virtuals.h"
#include "window_virtuals.h"
#include "topwindow_virtuals.h"
  };


// Data targets
class FXPyDataTarget : public FXDataTarget {
  FXDECLARE(FXPyDataTarget)
private:
  FXPyDataTarget(const FXPyDataTarget&);
  FXPyDataTarget& operator=(const FXPyDataTarget&);

private:
  // Associated integer value (if it's an integer)
  FXint intValue;

  // Associated double value (if it's a float)
  FXdouble doubleValue;

  // Associated string value (if it's a string)
  FXString stringValue;

public:
  // Construct and initialize with the current value of this Python object
  FXPyDataTarget(PyObject* value=NULL,FXObject* tgt=NULL,FXSelector sel=0);

  // Set the new value for this object
  void setValue(PyObject* value);

  // Return its current value
  PyObject* getValue() const;

#include "object_virtuals.h"
  };

// Debug target
class FXPyDebugTarget : public FXDebugTarget {
  FXDECLARE(FXPyDebugTarget)
private:
  FXPyDebugTarget(const FXPyDebugTarget&);
  FXPyDebugTarget& operator=(const FXPyDebugTarget&);

public:
  // Constructor
  FXPyDebugTarget(){}

#include "object_virtuals.h"
  };

class FXPyCommand : public FXCommand {
    FXDECLARE(FXPyCommand)
protected:
    FXPyCommand();
};


#endif
