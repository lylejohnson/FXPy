#! /usr/bin/env python

import os
import re
import string
import sys

def mangle_name(classname):
    return string.replace(classname, "FX", "FXPy")

def unmangle_name(classname):
    return string.replace(classname, "FXPy", "FX")

def gen_dock(classname, mc):
    print 'void %s::dock(FXuint side,FXWindow* after){ FXPyCallVoidFunction(this,"dock",side,after); }' % mc
    print 'void %s::_dock(FXuint side,FXWindow* after){ %s::dock(side,after); }\n' % (mc,classname)

def gen_undock(classname, mc):
    print 'void %s::undock(){ FXPyCallVoidFunction(this,"undock"); }' % mc
    print 'void %s::_undock(){ %s::undock(); }\n' % (mc,classname)

def gen_show(classname, mc):
    print 'void %s::show(){ FXPyCallVoidFunction(this,"show"); }' % mc
    print 'void %s::_show(){ %s::show(); }\n' % (mc,classname)

def gen_hide(classname, mc):
    print 'void %s::hide(){ FXPyCallVoidFunction(this,"hide"); }' % mc
    print 'void %s::_hide(){ %s::hide(); }\n' % (mc,classname)

def gen_enable(classname, mc):
    print 'void %s::enable(){ FXPyCallVoidFunction(this,"enable"); }' % mc
    print 'void %s::_enable(){ %s::enable(); }\n' % (mc,classname)

def gen_disable(classname, mc):
    print 'void %s::disable(){ FXPyCallVoidFunction(this,"disable"); }' % mc
    print 'void %s::_disable(){ %s::disable(); }\n' % (mc,classname)

def gen_canFocus(classname, mc):
    print 'FXbool %s::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }' % mc
    print 'FXbool %s::_canFocus() const { return %s::canFocus(); }\n' % (mc,classname)

def gen_setWindowFocus(classname, mc):
    print 'void %s::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }' % mc
    print 'void %s::_setFocus(){ %s::setFocus(); }\n' % (mc,classname)

def gen_killFocus(classname, mc):
    print 'void %s::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }' % mc
    print 'void %s::_killFocus(){ %s::killFocus(); }\n' % (mc,classname)

def gen_setDefault(classname, mc):
    print 'void %s::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }' % mc
    print 'void %s::_setDefault(FXbool enable){ %s::setDefault(enable); }\n' % (mc,classname)

def gen_create(classname, mc):
    print 'void %s::create(){ FXPyCallVoidFunction(this,"create"); }' % mc
    print 'void %s::_create(){ %s::create(); }\n' % (mc,classname)

# Generate wrappers for detach() function
def gen_detach(classname, mc):
    print 'void %s::detach(){ FXPyCallVoidFunction(this,"detach"); }' % mc
    print 'void %s::_detach(){ %s::detach(); }\n' % (mc,classname)

# Generate wrappers for destroy() function
def gen_destroy(classname, mc):
    print 'void %s::destroy(){ FXPyCallVoidFunction(this,"destroy"); }' % mc
    print 'void %s::_destroy(){ %s::destroy(); }\n' % (mc,classname)

def gen_lower(classname, mc):
    print 'void %s::lower(){ FXPyCallVoidFunction(this,"lower"); }' % mc
    print 'void %s::_lowerWindow(){ %s::lower(); }\n' % (mc,classname)

def gen_move(classname, mc):
    print 'void %s::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }' % mc
    print 'void %s::_move(FXint x,FXint y){ %s::move(x,y); }\n' % (mc,classname)

def gen_resize(classname, mc):
    print 'void %s::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }' % mc
    print 'void %s::_resize(FXint w,FXint h){ %s::resize(w,h); }\n' % (mc,classname)

def gen_contains(classname, mc):
    print 'FXbool %s::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }' % mc
    print 'FXbool %s::_contains(FXint x,FXint y) const { return %s::contains(x,y); }\n' % (mc,classname)

def gen_position(classname, mc):
    print 'void %s::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }' % mc
    print 'void %s::_position(FXint x,FXint y,FXint w,FXint h){ %s::position(x,y,w,h); }\n' % (mc,classname)

def gen_isComposite(classname, mc):
    print 'FXbool %s::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }' % mc
    print 'FXbool %s::_isComposite() const { return %s::isComposite(); }\n' % (mc,classname)

def gen_doesSaveUnder(classname, mc):
    print 'FXbool %s::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }' % mc
    print 'FXbool %s::_doesSaveUnder() const { return %s::doesSaveUnder(); }\n' % (mc,classname)

def gen_reparent(classname, mc):
    print 'void %s::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }' % mc
    print 'void %s::_reparent(FXComposite* newparent) { %s::reparent(newparent); }\n' % (mc,classname)

# Generate wrappers for handle() function
#def gen_handle(classname, mc):
#    print "long %s::_handle(FXObject* sender,FXSelector sel,void* ptr){" % (mc)
#    print "  return %s::handle(sender,sel,ptr);" % (classname)
#    print "  }\n"


def gen_onDefault(classname, mc):
    print "long %s::onDefault(FXObject* sender,FXSelector sel,void* ptr){" % mc
    print "  return ::_onDefault(this,sender,sel,ptr);"
    print "  }\n"
    print "long %s::_onDefault(FXObject* sender,FXSelector sel,void* ptr){" % mc
    print "  return %s::onDefault(sender,sel,ptr);" % classname
    print "  }\n"


# Generate wrappers for getDefaultWidth()
def gen_getDefaultWidth(classname, mc):
    print 'FXint %s::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }' % mc
    print 'FXint %s::_getDefaultWidth() { return %s::getDefaultWidth(); }\n' % (mc, classname)

def gen_getWidthForHeight(classname, mc):
    print 'FXint %s::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }' % mc
    print 'FXint %s::_getWidthForHeight(FXint h) { return %s::getWidthForHeight(h); }\n' % (mc, classname)

# Generate wrappers for getDefaultHeight()
def gen_getDefaultHeight(classname, mc):
    print 'FXint %s::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }' % mc
    print 'FXint %s::_getDefaultHeight() { return %s::getDefaultHeight(); }\n' % (mc, classname)

def gen_getHeightForWidth(classname, mc):
    print 'FXint %s::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }' % mc
    print 'FXint %s::_getHeightForWidth(FXint w) { return %s::getHeightForWidth(w); }\n' % (mc, classname)

# Generate wrappers for getWidth(const FXTreeList* list)
def gen_FXTreeItem_getWidth(classname, mc):
    print 'FXint %s::getWidth(const FXTreeList* list) const { return ::_getWidth(this, list); }' % mc
    print 'FXint %s::_getWidth(const FXTreeList* list) const { return %s::getWidth(list); }\n' % (mc, classname)

# Generate wrappers for getHeight(const FXTreeList* list)
def gen_FXTreeItem_getHeight(classname, mc):
    print 'FXint %s::getHeight(const FXTreeList* list) const { return ::_getHeight(this, list); }' % mc
    print 'FXint %s::_getHeight(const FXTreeList* list) const { return %s::getHeight(list); }\n' % (mc, classname)

# Generate wrappers for getWidth(const FXHeader* header)
def gen_FXHeaderItem_getWidth(classname, mc):
    print 'FXint %s::getWidth(const FXHeader* header) const { return ::_getWidth(this, header); }' % mc
    print 'FXint %s::_getWidth(const FXHeader* header) const { return %s::getWidth(header); }\n' % (mc, classname)

# Generate wrappers for getHeight(const FXHeader* header)
def gen_FXHeaderItem_getHeight(classname, mc):
    print 'FXint %s::getHeight(const FXHeader* header) const { return ::_getHeight(this, header); }' % mc
    print 'FXint %s::_getHeight(const FXHeader* header) const { return %s::getHeight(header); }\n' % (mc, classname)

# Generate wrappers for getWidth(const FXIconList* list)
def gen_FXIconItem_getWidth(classname, mc):
    print 'FXint %s::getWidth(const FXIconList* list) const { return ::_getWidth(this, list); }' % mc
    print 'FXint %s::_getWidth(const FXIconList* list) const { return %s::getWidth(list); }\n' % (mc, classname)

# Generate wrappers for getHeight(const FXIconList* header)
def gen_FXIconItem_getHeight(classname, mc):
    print 'FXint %s::getHeight(const FXIconList* list) const { return ::_getHeight(this, list); }' % mc
    print 'FXint %s::_getHeight(const FXIconList* list) const { return %s::getHeight(list); }\n' % (mc, classname)

# Generate wrappers for getWidth(const FXList* list)
def gen_FXListItem_getWidth(classname, mc):
    print 'FXint %s::getWidth(const FXList* list) const { return ::_getWidth(this, list); }' % mc
    print 'FXint %s::_getWidth(const FXList* list) const { return %s::getWidth(list); }\n' % (mc, classname)

# Generate wrappers for getHeight(const FXList* header)
def gen_FXListItem_getHeight(classname, mc):
    print 'FXint %s::getHeight(const FXList* list) const { return ::_getHeight(this, list); }' % mc
    print 'FXint %s::_getHeight(const FXList* list) const { return %s::getHeight(list); }\n' % (mc, classname)

# Generate wrappers for getWidth(const FXTable* table)
def gen_FXTableItem_getWidth(classname, mc):
    print 'FXint %s::getWidth(const FXTable* table) const { return ::_getWidth(this, table); }' % mc
    print 'FXint %s::_getWidth(const FXTable* table) const { return %s::getWidth(table); }\n' % (mc, classname)

# Generate wrappers for getHeight(const FXTable* table)
def gen_FXTableItem_getHeight(classname, mc):
    print 'FXint %s::getHeight(const FXTable* table) const { return ::_getHeight(this, table); }' % mc
    print 'FXint %s::_getHeight(const FXTable* table) const { return %s::getHeight(table); }\n' % (mc, classname)

# Wrappers for FXGLObject virtuals
def gen_FXGLObject_draw(classname, mc):
    print 'void %s::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }' % mc
    print 'void %s::_draw(FXGLViewer* viewer) { %s::draw(viewer); }\n' % (mc, classname)

def gen_FXGLObject_hit(classname, mc):
    print 'void %s::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }' % mc
    print 'void %s::_hit(FXGLViewer* viewer) { %s::hit(viewer); }\n' % (mc, classname)

def gen_FXGLObject_canDrag(classname, mc):
    print 'FXbool %s::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }' % mc
    print 'FXbool %s::_canDrag() const { return %s::canDrag(); }\n' % (mc, classname)

def gen_FXGLObject_canDelete(classname, mc):
    print 'FXbool %s::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }' % mc
    print 'FXbool %s::_canDelete() const { return %s::canDelete(); }\n' % (mc, classname)

def gen_FXGLObject_drag(classname, mc):
    print 'FXbool %s::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }' % mc
    print 'FXbool %s::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return %s::drag(viewer,fx,fy,tx,ty); }\n' % (mc, classname)

def gen_FXGLObject_copy(classname, mc):
    print 'FXGLObject* %s::copy() { return FXPyCallGLObjectFunction(this,"copy"); }' % mc
    print 'FXGLObject* %s::_copy() { return %s::copy(); }\n' % (mc, classname)

def gen_FXGLObject_identify(classname, mc):
    print 'FXGLObject* %s::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }' % mc
    print 'FXGLObject* %s::_identify(FXuint* path) { return %s::identify(path); }\n' % (mc, classname)

# Generate wrappers for layout()
def gen_layout(classname, mc):
    print 'void %s::layout() { FXPyCallVoidFunction(this,"layout"); }' % mc
    print 'void %s::_layout() { %s::layout(); }\n' % (mc, classname)

def gen_recalc(classname, mc):
    print 'void %s::recalc() { FXPyCallVoidFunction(this,"recalc"); }' % mc
    print 'void %s::_recalc() { %s::recalc(); }\n' % (mc, classname)

def gen_setText(classname, mc):
    print 'void %s::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }' % mc
    print 'void %s::_setText(const FXString& text) { %s::setText(text); }\n' % (mc, classname)

def gen_setIcon(classname, mc):
    print 'void %s::setIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setIcon",icn); }' % mc
    print 'void %s::_setIcon(FXIcon *icn) { %s::setIcon(icn); }\n' % (mc, classname)

def gen_setMiniIcon(classname, mc):
    print 'void %s::setMiniIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setMiniIcon",icn); }' % mc
    print 'void %s::_setMiniIcon(FXIcon *icn) { %s::setMiniIcon(icn); }\n' % (mc, classname)

def gen_setBigIcon(classname, mc):
    print 'void %s::setBigIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setBigIcon",icn); }' % mc
    print 'void %s::_setBigIcon(FXIcon *icn) { %s::setBigIcon(icn); }\n' % (mc, classname)

def gen_setOpenIcon(classname, mc):
    print 'void %s::setOpenIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setOpenIcon",icn); }' % mc
    print 'void %s::_setOpenIcon(FXIcon *icn) { %s::setOpenIcon(icn); }\n' % (mc, classname)

def gen_setClosedIcon(classname, mc):
    print 'void %s::setClosedIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setClosedIcon",icn); }' % mc
    print 'void %s::_setClosedIcon(FXIcon *icn) { %s::setClosedIcon(icn); }\n' % (mc, classname)

def gen_setItemFocus(classname, mc):
    print 'void %s::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }' % mc
    print 'void %s::_setFocus(FXbool focus) { %s::setFocus(focus); }\n' % (mc, classname)

def gen_setSelected(classname, mc):
    print 'void %s::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }' % mc
    print 'void %s::_setSelected(FXbool selected) { %s::setSelected(selected); }\n' % (mc, classname)

def gen_setOpened(classname, mc):
    print 'void %s::setOpened(FXbool opened) { FXPyCallVoidFunction(this,"setOpened",opened); }' % mc
    print 'void %s::_setOpened(FXbool opened) { %s::setOpened(opened); }\n' % (mc, classname)

def gen_setExpanded(classname, mc):
    print 'void %s::setExpanded(FXbool expanded) { FXPyCallVoidFunction(this,"setExpanded",expanded); }' % mc
    print 'void %s::_setExpanded(FXbool expanded) { %s::setExpanded(expanded); }\n' % (mc, classname)

def gen_setEnabled(classname, mc):
    print 'void %s::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }' % mc
    print 'void %s::_setEnabled(FXbool enabled) { %s::setEnabled(enabled); }\n' % (mc, classname)

def gen_setDraggable(classname, mc):
    print 'void %s::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }' % mc
    print 'void %s::_setDraggable(FXbool draggable) { %s::setDraggable(draggable); }\n' % (mc, classname)

def gen_setIconOwned(classname, mc):
    print 'void %s::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }' % mc
    print 'void %s::_setIconOwned(FXuint owned) { %s::setIconOwned(owned); }\n' % (mc, classname)

def gen_setMarked(classname, mc):
    print 'void %s::setMarked(FXbool marked) { FXPyCallVoidFunction(this,"setMarked",marked); }' % mc
    print 'void %s::_setMarked(FXbool marked) { %s::setMarked(marked); }\n' % (mc, classname)


def gen_setJustify(classname, mc):
    print 'void %s::setJustify(FXuint justify) { FXPyCallVoidFunction(this,"setJustify",justify); }' % mc
    print 'void %s::_setJustify(FXuint justify) { %s::setJustify(justify); }\n' % (mc, classname)

def gen_FXShutter_setCurrent(classname, mc):
    print 'void %s::setCurrent(FXint panel) { FXPyCallVoidFunction(this,"setCurrent",panel); }' % mc
    print 'void %s::_setCurrent(FXint panel) { %s::setCurrent(panel); }\n' % (mc, classname)

def gen_FXTabBar_setCurrent(classname, mc):
    print 'void %s::setCurrent(FXint panel,FXbool notify) { FXPyCallVoidFunction(this,"setCurrent",panel,notify); }' % mc
    print 'void %s::_setCurrent(FXint panel,FXbool notify) { %s::setCurrent(panel,notify); }\n' % (mc, classname)

def gen_restore(classname, mc):
    print 'void %s::restore()  { FXPyCallVoidFunction(this,"restore"); }' % mc
    print 'void %s::_restore() { %s::restore(); }\n' % (mc, classname)

def gen_render(classname, mc):
    print 'void %s::render()  { FXPyCallVoidFunction(this,"render"); }' % mc
    print 'void %s::_render() { %s::render(); }\n' % (mc, classname)

def gen_scale(classname, mc):
    print 'void %s::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }' % mc
    print 'void %s::_scale(FXint w,FXint h) { %s::scale(w,h); }\n' % (mc, classname)

def gen_mirror(classname, mc):
    print 'void %s::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }' % mc
    print 'void %s::_mirror(FXbool horizontal,FXbool vertical) { %s::mirror(horizontal,vertical); }\n' % (mc, classname)

def gen_rotate(classname, mc):
    print 'void %s::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }' % mc
    print 'void %s::_rotate(FXint degrees) { %s::rotate(degrees); }\n' % (mc, classname)

def gen_crop(classname, mc):
    print 'void %s::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }' % mc
    print 'void %s::_crop(FXint x,FXint y,FXint w,FXint h) { %s::crop(x,y,w,h); }\n' % (mc, classname)

def gen_savePixels(classname, mc):
    print 'void %s::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }' % mc
    print 'void %s::_savePixels(FXStream& store) const { %s::savePixels(store); }\n' % (mc, classname)

def gen_loadPixels(classname, mc):
    print 'void %s::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }' % mc
    print 'void %s::_loadPixels(FXStream& store) { %s::loadPixels(store); }\n' % (mc, classname)

def gen_getContentWidth(classname, mc):
    print 'FXint %s::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }' % mc
    print 'FXint %s::_getContentWidth() { return %s::getContentWidth(); }\n' % (mc, classname)

def gen_getContentHeight(classname, mc):
    print 'FXint %s::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }' % mc
    print 'FXint %s::_getContentHeight() { return %s::getContentHeight(); }\n' % (mc, classname)

def gen_getViewportWidth(classname, mc):
    print 'FXint %s::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }' % mc
    print 'FXint %s::_getViewportWidth() { return %s::getViewportWidth(); }\n' % (mc, classname)

def gen_getViewportHeight(classname, mc):
    print 'FXint %s::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }' % mc
    print 'FXint %s::_getViewportHeight() { return %s::getViewportHeight(); }\n' % (mc, classname)

def gen_moveContents(classname, mc):
    print 'void %s::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }' % mc
    print 'void %s::_moveContents(FXint x,FXint y) { %s::moveContents(x,y); }\n' % (mc, classname)

def gen_FXMDIChild_restore(classname, mc):
    print 'void %s::restore(FXbool notify) { FXPyCallVoidFunction(this,"restore",notify); }' % mc
    print 'void %s::_restore(FXbool notify) { %s::restore(notify); }\n' % (mc, classname)

def gen_minimize(classname, mc):
    print 'void %s::minimize(FXbool notify) { FXPyCallVoidFunction(this,"minimize",notify); }' % mc
    print 'void %s::_minimize(FXbool notify) { %s::minimize(notify); }\n' % (mc, classname)

def gen_maximize(classname, mc):
    print 'void %s::maximize(FXbool notify) { FXPyCallVoidFunction(this,"maximize",notify); }' % mc
    print 'void %s::_maximize(FXbool notify) { %s::maximize(notify); }\n' % (mc, classname)

def gen_FXText_setCursorPos(classname, mc):
    print 'void %s::setCursorPos(FXint pos,FXbool notify) { FXPyCallVoidFunction(this,"setCursorPos",pos,notify); }' % mc
    print 'void %s::_setCursorPos(FXint pos,FXbool notify) { %s::setCursorPos(pos,notify); }\n' % (mc, classname)

def gen_FXText_extendSelection(classname, mc):
    print 'FXbool %s::extendSelection(FXint pos,FXTextSelectionMode mode,FXbool notify) { return FXPyCallBoolFunction(this,"extendSelection",pos,mode,notify); }' % mc
    print 'FXbool %s::_extendSelection(FXint pos,FXTextSelectionMode mode,FXbool notify) { return %s::extendSelection(pos,mode,notify); }\n' % (mc, classname)

def gen_FXText_killSelection(classname, mc):
    print 'FXbool %s::killSelection(FXbool notify) { return FXPyCallBoolFunction(this,"killSelection",notify); }' % mc
    print 'FXbool %s::_killSelection(FXbool notify) { return %s::killSelection(notify); }\n' % (mc, classname)

def gen_FXTopWindow_iconify(classname, mc):
    print 'void %s::iconify() { FXPyCallVoidFunction(this, "iconify"); }' % mc
    print 'void %s::_iconify() { %s::iconify(); }\n' % (mc, classname)

def gen_FXTopWindow_deiconify(classname, mc):
    print 'void %s::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }' % mc
    print 'void %s::_deiconify() { %s::deiconify(); }\n' % (mc, classname)

def gen_FXTopWindow_show2(classname, mc):
    print 'void %s::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }' % mc
    print 'void %s::_show(FXuint placement) { %s::show(placement); }\n' % (mc, classname)

def gen_isCurrent(classname, mc):
    print 'FXbool %s::isCurrent() const { return FXPyCallBoolFunction(this,"isCurrent"); }' % mc
    print 'FXbool %s::_isCurrent() const { return %s::isCurrent(); }\n' % (mc, classname)

def gen_makeCurrent(classname, mc):
    print 'FXbool %s::makeCurrent() { return FXPyCallBoolFunction(this,"makeCurrent"); }' % mc
    print 'FXbool %s::_makeCurrent() { return %s::makeCurrent(); }\n' % (mc, classname)

def gen_makeNonCurrent(classname, mc):
    print 'FXbool %s::makeNonCurrent() { return FXPyCallBoolFunction(this,"makeNonCurrent"); }' % mc
    print 'FXbool %s::_makeNonCurrent() { return %s::makeNonCurrent(); }\n' % (mc, classname)

def gen_swapBuffers(classname, mc):
    print 'void %s::swapBuffers() { FXPyCallVoidFunction(this,"swapBuffers"); }' % mc
    print 'void %s::_swapBuffers() { %s::swapBuffers(); }\n' % (mc, classname)

def gen_popup(classname, mc):
    print 'void %s::popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { FXPyCallVoidFunction(this,"popup",grabto,x,y,w,h); }' % mc
    print 'void %s::_popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { %s::popup(grabto,x,y,w,h); }\n' % (mc, classname)

def gen_popdown(classname, mc):
    print 'void %s::popdown() { FXPyCallVoidFunction(this,"popdown"); }' % mc
    print 'void %s::_popdown() { %s::popdown(); }\n' % (mc, classname)

def gen_setBackColor(classname, mc):
    print 'void %s::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }' % mc
    print 'void %s::_setBackColor(FXColor clr) { %s::setBackColor(clr); }\n' % (mc, classname)

def gen_select(classname, mc):
    print 'FXGLObject** %s::select(FXint x,FXint y,FXint w,FXint h) { return FXPyCallGLObjectListFunction(this,"select",x,y,w,h); }' % mc
    print 'FXGLObject** %s::_select(FXint x,FXint y,FXint w,FXint h) { return %s::select(x,y,w,h); }\n' % (mc, classname)

def gen_pick(classname, mc):
    print 'FXGLObject* %s::pick(FXint x,FXint y) { return FXPyCallGLObjectFunction(this,"pick",x,y); }' % mc
    print 'FXGLObject* %s::_pick(FXint x,FXint y) { return %s::pick(x,y); }\n' % (mc, classname)

def locate_include_file(incdirs, filename):
    """Search include files path for the specified filename"""
    for incdir in incdirs:
        fullpath = os.path.join(incdir, filename)
        if os.path.exists(fullpath):
            return fullpath

def preprocess(incdirs, lines):
    """Simple preprocessor, replaces #include directives with actual text."""
    newlines = []
    incline = re.compile('^ *#include')
    for line in lines:
	if incline.match(line):
	    words = string.split(line, '"')
	    filename = locate_include_file(incdirs, words[1])
	    for s in open(filename, 'r').readlines():
		newlines.append(s)
	else:
	    newlines.append(line)
    return newlines

# Map regular expressions to functions
funclist = [
    (re.compile('void iconify\(') , gen_FXTopWindow_iconify),
    (re.compile('void deiconify\(') , gen_FXTopWindow_deiconify),
    (re.compile('void show\(FXuint') , gen_FXTopWindow_show2),

#   (re.compile('long _handle\(') , gen_handle),
    (re.compile('long onDefault\(') , gen_onDefault),

    (re.compile('void create\(') , gen_create),
    (re.compile('void detach\(') , gen_detach),
    (re.compile('void destroy\(') , gen_destroy),
    (re.compile('void enable\(') , gen_enable),
    (re.compile('void disable\(') , gen_disable),

    (re.compile('FXbool canFocus\(') , gen_canFocus),
    (re.compile('void setFocus\(\)') , gen_setWindowFocus),
    (re.compile('void killFocus\(') , gen_killFocus),
    (re.compile('void setDefault\(FXbool') , gen_setDefault),

    (re.compile('FXint getDefaultHeight\(') , gen_getDefaultHeight),
    (re.compile('FXint getWidthForHeight\(') , gen_getWidthForHeight),
    (re.compile('FXint getDefaultWidth\(') , gen_getDefaultWidth),
    (re.compile('FXint getHeightForWidth\(') , gen_getHeightForWidth),
    (re.compile('void layout\(') , gen_layout),
    (re.compile('void recalc\(') , gen_recalc),

    (re.compile('void show\(') , gen_show),
    (re.compile('void hide\(') , gen_hide),
    (re.compile('void lower\(') , gen_lower),
    (re.compile('void move\(') , gen_move),
    (re.compile('void resize\(') , gen_resize),
    (re.compile('void position\(') , gen_position),
    (re.compile('FXbool contains\(') , gen_contains),
    (re.compile('FXbool isComposite\(') , gen_isComposite),
    (re.compile('FXbool doesSaveUnder\(') , gen_doesSaveUnder),
    (re.compile('void reparent\(') , gen_reparent),

    (re.compile('void restore\(\)') , gen_restore),
    (re.compile('void render\(') , gen_render),
    (re.compile('void scale\(') , gen_scale),
    (re.compile('void mirror\(') , gen_mirror),
    (re.compile('void rotate\(') , gen_rotate),
    (re.compile('void crop\(') , gen_crop),
    (re.compile('void savePixels\(') , gen_savePixels),
    (re.compile('void loadPixels\(') , gen_loadPixels),

    (re.compile('void dock\(') , gen_dock),
    (re.compile('void undock\(') , gen_undock),

    (re.compile('void minimize\(') , gen_minimize),
    (re.compile('void maximize\(') , gen_maximize),
    (re.compile('void restore\(FXbool notify') , gen_FXMDIChild_restore),

    (re.compile('FXint getContentWidth\(') , gen_getContentWidth),
    (re.compile('FXint getContentHeight\(') , gen_getContentHeight),
    (re.compile('FXint getViewportWidth\(') , gen_getViewportWidth),
    (re.compile('FXint getViewportHeight\(') , gen_getViewportHeight),
    (re.compile('void moveContents\(') , gen_moveContents),

    (re.compile('FXint getWidth\(const FXTreeList') , gen_FXTreeItem_getWidth),
    (re.compile('FXint getHeight\(const FXTreeList') , gen_FXTreeItem_getHeight),

    (re.compile('FXint getWidth\(const FXHeader') , gen_FXHeaderItem_getWidth),
    (re.compile('FXint getHeight\(const FXHeader') , gen_FXHeaderItem_getHeight),

    (re.compile('FXint getWidth\(const FXIconList') , gen_FXIconItem_getWidth),
    (re.compile('FXint getHeight\(const FXIconList') , gen_FXIconItem_getHeight),

    (re.compile('FXint getWidth\(const FXList') , gen_FXListItem_getWidth),
    (re.compile('FXint getHeight\(const FXList') , gen_FXListItem_getHeight),

    (re.compile('FXint getWidth\(const FXTable') , gen_FXTableItem_getWidth),
    (re.compile('FXint getHeight\(const FXTable') , gen_FXTableItem_getHeight),

    (re.compile('void setText\(const FXString') , gen_setText),
    (re.compile('void setIcon\(FXIcon') , gen_setIcon),
    (re.compile('void setBigIcon\(FXIcon') , gen_setBigIcon),
    (re.compile('void setMiniIcon\(FXIcon') , gen_setMiniIcon),
    (re.compile('void setOpenIcon\(FXIcon') , gen_setOpenIcon),
    (re.compile('void setClosedIcon\(FXIcon') , gen_setClosedIcon),
    (re.compile('void setFocus\(FXbool focus') , gen_setItemFocus),
    (re.compile('void setSelected\(FXbool selected') , gen_setSelected),
    (re.compile('void setOpened\(FXbool opened') , gen_setOpened),
    (re.compile('void setExpanded\(FXbool expanded') , gen_setExpanded),
    (re.compile('void setEnabled\(FXbool enabled') , gen_setEnabled),
    (re.compile('void setDraggable\(FXbool draggable') , gen_setDraggable),
    (re.compile('void setIconOwned\(FXuint owned') , gen_setIconOwned),
    (re.compile('void setMarked\(FXbool marked') , gen_setMarked),
    (re.compile('void setJustify\(FXuint justify') , gen_setJustify),
    (re.compile('void setCurrent\(FXint panel\)') , gen_FXShutter_setCurrent),
    (re.compile('void setCurrent\(FXint panel,FXbool notify\)') , gen_FXTabBar_setCurrent),

    (re.compile('void draw\(FXGLViewer') , gen_FXGLObject_draw),
    (re.compile('void hit\(FXGLViewer') , gen_FXGLObject_hit),
    (re.compile('FXbool canDrag\(') , gen_FXGLObject_canDrag),
    (re.compile('FXbool canDelete\(') , gen_FXGLObject_canDelete),
    (re.compile('FXbool drag\(FXGLViewer') , gen_FXGLObject_drag),
    (re.compile('FXGLObject\* copy\(') , gen_FXGLObject_copy),
    (re.compile('FXGLObject\* identify\(') , gen_FXGLObject_identify),

    (re.compile('void setCursorPos\(') , gen_FXText_setCursorPos),
    (re.compile('FXbool extendSelection\(') , gen_FXText_extendSelection),
    (re.compile('FXbool killSelection\(') , gen_FXText_killSelection),

    (re.compile('FXbool isCurrent\(') , gen_isCurrent),
    (re.compile('FXbool makeCurrent\(') , gen_makeCurrent),
    (re.compile('FXbool makeNonCurrent\(') , gen_makeNonCurrent),
    (re.compile('void swapBuffers\(') , gen_swapBuffers),

    (re.compile('void popup\(') , gen_popup),
    (re.compile('void popdown\(') , gen_popdown),

    (re.compile('void setBackColor\(') , gen_setBackColor),

    (re.compile('FXGLObject\*\* select\(') , gen_select),
    (re.compile('FXGLObject\* pick\(') , gen_pick),
]

def make_virtuals(incfile, outp, include_dirs):
    # Send output to this file name
    sys.stdout = open(outp, 'w')

    # Read the header file as-is
    lines = open(incfile, "r").readlines()

    # Expand all of the #include directives in the file so that
    # we get the full text
    lines = preprocess(include_dirs, lines)

    class_header = re.compile("^class")
    for i in xrange(len(lines)):
        curr = lines[i]
        if class_header.match(curr):
            words = string.split(curr)
            classname = words[1]
        else:
            for pat, func in funclist:
                if pat.search(curr):
                    func(unmangle_name(classname), classname)
                    break

if __name__ == '__main__':
    file_pairs = {'FXPy.h' : 'virtuals.cpp'}
    include_dirs = ['.']
    for incfile, srcfile in file_pairs.items():
        make_virtuals(incfile, srcfile, include_dirs)
