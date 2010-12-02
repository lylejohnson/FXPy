import re, sys

def print_app_virtuals():
    print 'public:'
    print '  %name(create) void _create();'
    print '  %name(destroy) void _destroy();'
    print '  %name(detach) void _detach();'

def print_object_virtuals():
    print 'public:'
#   print '  %name(handle) long _handle(FXObject*,FXSelector,void* ptr);'
    print '  %name(onDefault) long _onDefault(FXObject*,FXSelector,void* ptr);'

def print_id_virtuals():
    print 'public:'
    print '  %name(create) void _create();'
    print '  %name(destroy) void _destroy();'
    print '  %name(detach) void _detach();'

def print_image_virtuals():
    print 'public:'
    print '  %name(restore) void _restore();'
    print '  %name(render) void _render();'
    print '  %name(scale) void _scale(FXint w,FXint h);'
    print '  %name(mirror) void _mirror(FXbool horizontal,FXbool vertical);'
    print '  %name(rotate) void _rotate(FXint degrees);'
    print '  %name(crop) void _crop(FXint x,FXint y,FXint w,FXint h);'
    print '  %name(savePixels) void _savePixels(FXStream& store) const;'
    print '  %name(loadPixels) void _loadPixels(FXStream& store);'

def print_drawable_virtuals():
    print 'public:'
    print '  %name(resize) void _resize(FXint w,FXint h);'

def print_window_virtuals():
    print 'public:'
    print '  %name(getDefaultWidth) FXint _getDefaultWidth();'
    print '  %name(getDefaultHeight) FXint _getDefaultHeight();'
    print '  %name(show) void _show();'
    print '  %name(hide) void _hide();'
    print '  %name(enable) void _enable();'
    print '  %name(disable) void _disable();'
    print '  %name(canFocus) FXbool _canFocus() const;'
    print '  %name(setFocus) void _setFocus();'
    print '  %name(killFocus) void _killFocus();'
    print '  %name(setDefault) void _setDefault(FXbool enable=TRUE);'
    print '  %name(recalc) void _recalc();'
    print '  %name(layout) void _layout();'
    print '  %name(lower) void _lowerWindow();'
    print '  %name(move) void _move(FXint x,FXint y);'
    print '  %name(position) void _position(FXint x,FXint y,FXint w,FXint h);'
    print '  %name(isComposite) FXbool _isComposite() const;'
    print '  %name(contains) FXbool _contains(FXint x,FXint y) const;'
    print '  %name(getWidthForHeight) FXint _getWidthForHeight(FXint h);'
    print '  %name(getHeightForWidth) FXint _getHeightForWidth(FXint w);'
    print '  %name(doesSaveUnder) FXbool _doesSaveUnder() const;'
    print '  %name(reparent) void _reparent(FXComposite* newparent);'
    print '  %name(setBackColor) void _setBackColor(FXColor clr);'

def print_scrollarea_virtuals():
    print 'public:'
    print '  %name(getContentWidth) FXint _getContentWidth();'
    print '  %name(getContentHeight) FXint _getContentHeight();'
    print '  %name(getViewportWidth) FXint _getViewportWidth();'
    print '  %name(getViewportHeight) FXint _getViewportHeight();'
    print '  %name(moveContents) void _moveContents(FXint x,FXint y);'

def print_treeitem_virtuals():
    print 'public:'
    print '  %name(setText) void _setText(const FXString& text);'
    print '  %name(setOpenIcon) void _setOpenIcon(FXIcon* ic);'
    print '  %name(setClosedIcon) void _setClosedIcon(FXIcon* ic);'
    print '  %name(setFocus) void _setFocus(FXbool focus);'
    print '  %name(setSelected) void _setSelected(FXbool selected);'
    print '  %name(setOpened) void _setOpened(FXbool opened);'
    print '  %name(setExpanded) void _setExpanded(FXbool expanded);'
    print '  %name(setEnabled) void _setEnabled(FXbool enabled);'
    print '  %name(setDraggable) void _setDraggable(FXbool draggable);'
    print '  %name(setIconOwned) void _setIconOwned(FXuint owned);'
    print '  %name(getWidth) FXint _getWidth(const FXTreeList* list) const;'
    print '  %name(getHeight) FXint _getHeight(const FXTreeList* list) const;'
    print '  %name(create) void _create() const;'
    print '  %name(detach) void _detach();'
    print '  %name(destroy) void _destroy();'

def print_headeritem_virtuals():
    print 'public:'
    print '  %name(setText) void _setText(const FXString& text);'
    print '  %name(setIcon) void _setIcon(FXIcon *ic);'
    print '  %name(getWidth) FXint _getWidth(const FXHeader* header) const;'
    print '  %name(getHeight) FXint _getHeight(const FXHeader* header) const;'
    print '  %name(create) void _create() const;'
    print '  %name(detach) void _detach();'
    print '  %name(destroy) void _destroy();'

def print_iconitem_virtuals():
    print 'public:'
    print '  %name(setText) void _setText(const FXString& text);'
    print '  %name(setBigIcon) void _setBigIcon(FXIcon* ic);'
    print '  %name(setMiniIcon) void _setMiniIcon(FXIcon* ic);'
    print '  %name(setFocus) void _setFocus(FXbool focus);'
    print '  %name(setSelected) void _setSelected(FXbool selected);'
    print '  %name(setEnabled) void _setEnabled(FXbool enabled);'
    print '  %name(setDraggable) void _setDraggable(FXbool draggable);'
    print '  %name(setIconOwned) void _setIconOwned(FXuint owned);'
    print '  %name(getWidth) FXint _getWidth(const FXIconList* list) const;'
    print '  %name(getHeight) FXint _getHeight(const FXIconList* list) const;'
    print '  %name(create) void _create() const;'
    print '  %name(detach) void _detach();'
    print '  %name(destroy) void _destroy();'

def print_listitem_virtuals():
    print 'public:'
    print '  %name(setText) void _setText(const FXString& text);'
    print '  %name(setIcon) void _setIcon(FXIcon* ic);'
    print '  %name(setFocus) void _setFocus(FXbool focus);'
    print '  %name(setSelected) void _setSelected(FXbool selected);'
    print '  %name(setEnabled) void _setEnabled(FXbool enabled);'
    print '  %name(setDraggable) void _setDraggable(FXbool draggable);'
    print '  %name(setIconOwned) void _setIconOwned(FXuint owned);'
    print '  %name(getWidth) FXint _getWidth(const FXList* list) const;'
    print '  %name(getHeight) FXint _getHeight(const FXList* list) const;'
    print '  %name(create) void _create() const;'
    print '  %name(detach) void _detach();'
    print '  %name(destroy) void _destroy();'

def print_tableitem_virtuals():
    print 'public:'
    print '  %name(setText) void _setText(const FXString& text);'
    print '  %name(setIcon) void _setIcon(FXIcon* ic);'
    print '  %name(setFocus) void _setFocus(FXbool focus);'
    print '  %name(setSelected) void _setSelected(FXbool selected);'
    print '  %name(setEnabled) void _setEnabled(FXbool enabled);'
    print '  %name(setDraggable) void _setDraggable(FXbool draggable);'
    print '  %name(setJustify) void _setJustify(FXuint justify);'
    print '  %name(getWidth) FXint _getWidth(const FXTable* table) const;'
    print '  %name(getHeight) FXint _getHeight(const FXTable* table) const;'
    print '  %name(create) void _create() const;'
    print '  %name(detach) void _detach();'
    print '  %name(destroy) void _destroy();'

def print_globject_virtuals():
    print 'public:'
    print '  %name(draw) void _draw(FXGLViewer* viewer);'
    print '  %name(hit) void _hit(FXGLViewer* viewer);'
    print '  %name(copy) FXGLObject* _copy();'
    print '  %name(identify) FXGLObject* _identify(FXuint* path);'
    print '  %name(canDrag) FXbool _canDrag();'
    print '  %name(canDelete) FXbool _canDelete();'
    print '  %name(drag) FXbool _drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty);'

def print_mdichild_virtuals():
    print 'public:'
    print '  %name(minimize) void _minimize(FXbool notify=FALSE);'
    print '  %name(maximize) void _maximize(FXbool notify=FALSE);'
    print '  %name(restore) void _restore(FXbool notify=FALSE);'

def print_toolbar_virtuals():
    print 'public:'
    print '  %name(dock) void _dock(FXuint side=LAYOUT_SIDE_TOP,FXWindow* after=-1);'
    print '  %name(undock) void _undock();'

def print_text_virtuals():
    print 'public:'
    print '  %name(setCursorPos) void _setCursorPos(FXint pos,FXbool notify=FALSE);'
    print '  %name(extendSelection) FXbool _extendSelection(FXint pos,FXTextSelectionMode mode=SELECT_CHARS,FXbool notify=FALSE);'
    print '  %name(killSelection) FXbool _killSelection(FXbool notify=FALSE);'

def print_topwindow_virtuals():
    print 'public:'
    print '  %name(show2) void _show(FXuint placement);'
    print '  %name(iconify) void _iconify();'
    print '  %name(deiconify) void _deiconify();'

def print_FXShutter_virtuals():
    print 'public:'
    print '  %name(setCurrent) void _setCurrent(FXint panel);'

def print_FXCursor_virtuals():
    print 'public:'
    print '  %name(savePixels) void _savePixels(FXStream& store) const;'
    print '  %name(loadPixels) void _loadPixels(FXStream& store);'

def print_FXGLContext_virtuals():
    print 'public:'
    print '  %name(create) void _create();'
    print '  %name(destroy) void _destroy();'
    print '  %name(detach) void _detach();'

def print_FXGLCanvas_virtuals():
    print 'public:'
    print '  %name(isCurrent) FXbool _isCurrent() const;'
    print '  %name(makeCurrent) FXbool _makeCurrent();'
    print '  %name(makeNonCurrent) FXbool _makeNonCurrent();'
    print '  %name(swapBuffers) void _swapBuffers();'

def print_FXGLViewer_virtuals():
    print 'public:'
    print '  %name(select) FXGLObject** _select(FXint x,FXint y,FXint w,FXint h);'
    print '  %name(pick) FXGLObject* _pick(FXint x,FXint y);'

def print_FXPopup_virtuals():
    print 'public:'
    print '  %name(popup) void _popup(FXWindow* grabto,FXint x,FXint y,FXint w=0,FXint h=0);'
    print '  %name(popdown) void _popdown();'

def print_FXTabBar_virtuals():
    print 'public:'
    print '  %name(setCurrent) void _setCurrent(FXint panel,FXbool notify=FALSE);'

exprmap = {
    re.compile('^ *APP_VIRTUALS') : print_app_virtuals,
    re.compile('^ *OBJECT_VIRTUALS') : print_object_virtuals,
    re.compile('^ *ID_VIRTUALS') : print_id_virtuals,
    re.compile('^ *DRAWABLE_VIRTUALS') : print_drawable_virtuals,
    re.compile('^ *IMAGE_VIRTUALS') : print_image_virtuals,
    re.compile('^ *WINDOW_VIRTUALS') : print_window_virtuals,
    re.compile('^ *MDICHILD_VIRTUALS') : print_mdichild_virtuals,
    re.compile('^ *SCROLLAREA_VIRTUALS') : print_scrollarea_virtuals,
    re.compile('^ *TREEITEM_VIRTUALS') : print_treeitem_virtuals,
    re.compile('^ *HEADERITEM_VIRTUALS') : print_headeritem_virtuals,
    re.compile('^ *ICONITEM_VIRTUALS') : print_iconitem_virtuals,
    re.compile('^ *LISTITEM_VIRTUALS') : print_listitem_virtuals,
    re.compile('^ *TABLEITEM_VIRTUALS') : print_tableitem_virtuals,
    re.compile('^ *GLOBJECT_VIRTUALS') : print_globject_virtuals,
    re.compile('^ *TOOLBAR_VIRTUALS') : print_toolbar_virtuals,
    re.compile('^ *TEXT_VIRTUALS') : print_text_virtuals,
    re.compile('^ *TOPWINDOW_VIRTUALS') : print_topwindow_virtuals,
    re.compile('^ *FXSHUTTER_VIRTUALS') : print_FXShutter_virtuals,
    re.compile('^ *FXCURSOR_VIRTUALS') : print_FXCursor_virtuals,
    re.compile('^ *FXGLCONTEXT_VIRTUALS') : print_FXGLContext_virtuals,
    re.compile('^ *FXGLCANVAS_VIRTUALS') : print_FXGLCanvas_virtuals,
    re.compile('^ *FXGLVIEWER_VIRTUALS') : print_FXGLViewer_virtuals,
    re.compile('^ *FXPOPUP_VIRTUALS') : print_FXPopup_virtuals,
    re.compile('^ *FXTABBAR_VIRTUALS') : print_FXTabBar_virtuals,
}

filename = sys.argv[1]
expressions = exprmap.keys()
for line in open(filename, 'r').readlines():
    for expression in expressions:
	if expression.match(line):
	    exprmap[expression]()
	    break
    else:
	print line,
