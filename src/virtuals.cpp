long FXPyObject::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyObject::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXObject::onDefault(sender,sel,ptr);
  }

long FXPyAccelTable::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyAccelTable::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXAccelTable::onDefault(sender,sel,ptr);
  }

long FXPyId::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyId::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXId::onDefault(sender,sel,ptr);
  }

void FXPyId::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyId::_create(){ FXId::create(); }

void FXPyId::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyId::_destroy(){ FXId::destroy(); }

void FXPyId::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyId::_detach(){ FXId::detach(); }

long FXPyCursor::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyCursor::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXCursor::onDefault(sender,sel,ptr);
  }

void FXPyCursor::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyCursor::_savePixels(FXStream& store) const { FXCursor::savePixels(store); }

void FXPyCursor::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyCursor::_loadPixels(FXStream& store) { FXCursor::loadPixels(store); }

long FXPyGIFCursor::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGIFCursor::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGIFCursor::onDefault(sender,sel,ptr);
  }

void FXPyGIFCursor::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyGIFCursor::_savePixels(FXStream& store) const { FXGIFCursor::savePixels(store); }

void FXPyGIFCursor::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyGIFCursor::_loadPixels(FXStream& store) { FXGIFCursor::loadPixels(store); }

long FXPyCURCursor::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyCURCursor::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXCURCursor::onDefault(sender,sel,ptr);
  }

void FXPyCURCursor::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyCURCursor::_savePixels(FXStream& store) const { FXCURCursor::savePixels(store); }

void FXPyCURCursor::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyCURCursor::_loadPixels(FXStream& store) { FXCURCursor::loadPixels(store); }

long FXPyIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXIcon::onDefault(sender,sel,ptr);
  }

void FXPyIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyIcon::_create(){ FXIcon::create(); }

void FXPyIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyIcon::_destroy(){ FXIcon::destroy(); }

void FXPyIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyIcon::_detach(){ FXIcon::detach(); }

void FXPyIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyIcon::_resize(FXint w,FXint h){ FXIcon::resize(w,h); }

void FXPyIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyIcon::_restore() { FXIcon::restore(); }

void FXPyIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyIcon::_render() { FXIcon::render(); }

void FXPyIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyIcon::_scale(FXint w,FXint h) { FXIcon::scale(w,h); }

void FXPyIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyIcon::_mirror(FXbool horizontal,FXbool vertical) { FXIcon::mirror(horizontal,vertical); }

void FXPyIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyIcon::_rotate(FXint degrees) { FXIcon::rotate(degrees); }

void FXPyIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXIcon::crop(x,y,w,h); }

void FXPyIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyIcon::_savePixels(FXStream& store) const { FXIcon::savePixels(store); }

void FXPyIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyIcon::_loadPixels(FXStream& store) { FXIcon::loadPixels(store); }

long FXPyGIFIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGIFIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGIFIcon::onDefault(sender,sel,ptr);
  }

void FXPyGIFIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGIFIcon::_create(){ FXGIFIcon::create(); }

void FXPyGIFIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGIFIcon::_destroy(){ FXGIFIcon::destroy(); }

void FXPyGIFIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGIFIcon::_detach(){ FXGIFIcon::detach(); }

void FXPyGIFIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyGIFIcon::_resize(FXint w,FXint h){ FXGIFIcon::resize(w,h); }

void FXPyGIFIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyGIFIcon::_restore() { FXGIFIcon::restore(); }

void FXPyGIFIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyGIFIcon::_render() { FXGIFIcon::render(); }

void FXPyGIFIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyGIFIcon::_scale(FXint w,FXint h) { FXGIFIcon::scale(w,h); }

void FXPyGIFIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyGIFIcon::_mirror(FXbool horizontal,FXbool vertical) { FXGIFIcon::mirror(horizontal,vertical); }

void FXPyGIFIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyGIFIcon::_rotate(FXint degrees) { FXGIFIcon::rotate(degrees); }

void FXPyGIFIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyGIFIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXGIFIcon::crop(x,y,w,h); }

void FXPyGIFIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyGIFIcon::_savePixels(FXStream& store) const { FXGIFIcon::savePixels(store); }

void FXPyGIFIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyGIFIcon::_loadPixels(FXStream& store) { FXGIFIcon::loadPixels(store); }

long FXPyBMPIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyBMPIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXBMPIcon::onDefault(sender,sel,ptr);
  }

void FXPyBMPIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyBMPIcon::_create(){ FXBMPIcon::create(); }

void FXPyBMPIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyBMPIcon::_destroy(){ FXBMPIcon::destroy(); }

void FXPyBMPIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyBMPIcon::_detach(){ FXBMPIcon::detach(); }

void FXPyBMPIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyBMPIcon::_resize(FXint w,FXint h){ FXBMPIcon::resize(w,h); }

void FXPyBMPIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyBMPIcon::_restore() { FXBMPIcon::restore(); }

void FXPyBMPIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyBMPIcon::_render() { FXBMPIcon::render(); }

void FXPyBMPIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyBMPIcon::_scale(FXint w,FXint h) { FXBMPIcon::scale(w,h); }

void FXPyBMPIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyBMPIcon::_mirror(FXbool horizontal,FXbool vertical) { FXBMPIcon::mirror(horizontal,vertical); }

void FXPyBMPIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyBMPIcon::_rotate(FXint degrees) { FXBMPIcon::rotate(degrees); }

void FXPyBMPIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyBMPIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXBMPIcon::crop(x,y,w,h); }

void FXPyBMPIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyBMPIcon::_savePixels(FXStream& store) const { FXBMPIcon::savePixels(store); }

void FXPyBMPIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyBMPIcon::_loadPixels(FXStream& store) { FXBMPIcon::loadPixels(store); }

long FXPyPNGIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPNGIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPNGIcon::onDefault(sender,sel,ptr);
  }

void FXPyPNGIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPNGIcon::_create(){ FXPNGIcon::create(); }

void FXPyPNGIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPNGIcon::_destroy(){ FXPNGIcon::destroy(); }

void FXPyPNGIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPNGIcon::_detach(){ FXPNGIcon::detach(); }

void FXPyPNGIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPNGIcon::_resize(FXint w,FXint h){ FXPNGIcon::resize(w,h); }

void FXPyPNGIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyPNGIcon::_restore() { FXPNGIcon::restore(); }

void FXPyPNGIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyPNGIcon::_render() { FXPNGIcon::render(); }

void FXPyPNGIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyPNGIcon::_scale(FXint w,FXint h) { FXPNGIcon::scale(w,h); }

void FXPyPNGIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyPNGIcon::_mirror(FXbool horizontal,FXbool vertical) { FXPNGIcon::mirror(horizontal,vertical); }

void FXPyPNGIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyPNGIcon::_rotate(FXint degrees) { FXPNGIcon::rotate(degrees); }

void FXPyPNGIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyPNGIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXPNGIcon::crop(x,y,w,h); }

void FXPyPNGIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyPNGIcon::_savePixels(FXStream& store) const { FXPNGIcon::savePixels(store); }

void FXPyPNGIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyPNGIcon::_loadPixels(FXStream& store) { FXPNGIcon::loadPixels(store); }

long FXPyFont::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFont::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFont::onDefault(sender,sel,ptr);
  }

void FXPyFont::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFont::_create(){ FXFont::create(); }

void FXPyFont::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFont::_destroy(){ FXFont::destroy(); }

void FXPyFont::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFont::_detach(){ FXFont::detach(); }

long FXPyComposite::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyComposite::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXComposite::onDefault(sender,sel,ptr);
  }

void FXPyComposite::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyComposite::_create(){ FXComposite::create(); }

void FXPyComposite::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyComposite::_destroy(){ FXComposite::destroy(); }

void FXPyComposite::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyComposite::_detach(){ FXComposite::detach(); }

void FXPyComposite::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyComposite::_resize(FXint w,FXint h){ FXComposite::resize(w,h); }

void FXPyComposite::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyComposite::_enable(){ FXComposite::enable(); }

void FXPyComposite::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyComposite::_disable(){ FXComposite::disable(); }

void FXPyComposite::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyComposite::_show(){ FXComposite::show(); }

void FXPyComposite::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyComposite::_hide(){ FXComposite::hide(); }

void FXPyComposite::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyComposite::_lowerWindow(){ FXComposite::lower(); }

FXint FXPyComposite::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyComposite::_getDefaultHeight() { return FXComposite::getDefaultHeight(); }

FXint FXPyComposite::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyComposite::_getDefaultWidth() { return FXComposite::getDefaultWidth(); }

FXint FXPyComposite::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyComposite::_getWidthForHeight(FXint h) { return FXComposite::getWidthForHeight(h); }

FXint FXPyComposite::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyComposite::_getHeightForWidth(FXint w) { return FXComposite::getHeightForWidth(w); }

void FXPyComposite::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyComposite::_layout() { FXComposite::layout(); }

void FXPyComposite::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyComposite::_recalc() { FXComposite::recalc(); }

FXbool FXPyComposite::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyComposite::_isComposite() const { return FXComposite::isComposite(); }

void FXPyComposite::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyComposite::_move(FXint x,FXint y){ FXComposite::move(x,y); }

void FXPyComposite::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyComposite::_position(FXint x,FXint y,FXint w,FXint h){ FXComposite::position(x,y,w,h); }

FXbool FXPyComposite::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyComposite::_canFocus() const { return FXComposite::canFocus(); }

void FXPyComposite::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyComposite::_setFocus(){ FXComposite::setFocus(); }

void FXPyComposite::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyComposite::_killFocus(){ FXComposite::killFocus(); }

void FXPyComposite::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyComposite::_setDefault(FXbool enable){ FXComposite::setDefault(enable); }

FXbool FXPyComposite::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyComposite::_contains(FXint x,FXint y) const { return FXComposite::contains(x,y); }

FXbool FXPyComposite::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyComposite::_doesSaveUnder() const { return FXComposite::doesSaveUnder(); }

void FXPyComposite::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyComposite::_reparent(FXComposite* newparent) { FXComposite::reparent(newparent); }

void FXPyComposite::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyComposite::_setBackColor(FXColor clr) { FXComposite::setBackColor(clr); }

long FXPyButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXButton::onDefault(sender,sel,ptr);
  }

void FXPyButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyButton::_create(){ FXButton::create(); }

void FXPyButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyButton::_destroy(){ FXButton::destroy(); }

void FXPyButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyButton::_detach(){ FXButton::detach(); }

void FXPyButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyButton::_resize(FXint w,FXint h){ FXButton::resize(w,h); }

void FXPyButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyButton::_enable(){ FXButton::enable(); }

void FXPyButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyButton::_disable(){ FXButton::disable(); }

void FXPyButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyButton::_show(){ FXButton::show(); }

void FXPyButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyButton::_hide(){ FXButton::hide(); }

void FXPyButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyButton::_lowerWindow(){ FXButton::lower(); }

FXint FXPyButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyButton::_getDefaultHeight() { return FXButton::getDefaultHeight(); }

FXint FXPyButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyButton::_getDefaultWidth() { return FXButton::getDefaultWidth(); }

FXint FXPyButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyButton::_getWidthForHeight(FXint h) { return FXButton::getWidthForHeight(h); }

FXint FXPyButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyButton::_getHeightForWidth(FXint w) { return FXButton::getHeightForWidth(w); }

void FXPyButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyButton::_layout() { FXButton::layout(); }

void FXPyButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyButton::_recalc() { FXButton::recalc(); }

FXbool FXPyButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyButton::_isComposite() const { return FXButton::isComposite(); }

void FXPyButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyButton::_move(FXint x,FXint y){ FXButton::move(x,y); }

void FXPyButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyButton::_position(FXint x,FXint y,FXint w,FXint h){ FXButton::position(x,y,w,h); }

FXbool FXPyButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyButton::_canFocus() const { return FXButton::canFocus(); }

void FXPyButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyButton::_setFocus(){ FXButton::setFocus(); }

void FXPyButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyButton::_killFocus(){ FXButton::killFocus(); }

void FXPyButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyButton::_setDefault(FXbool enable){ FXButton::setDefault(enable); }

FXbool FXPyButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyButton::_contains(FXint x,FXint y) const { return FXButton::contains(x,y); }

FXbool FXPyButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyButton::_doesSaveUnder() const { return FXButton::doesSaveUnder(); }

void FXPyButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyButton::_reparent(FXComposite* newparent) { FXButton::reparent(newparent); }

void FXPyButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyButton::_setBackColor(FXColor clr) { FXButton::setBackColor(clr); }

long FXPyDrawable::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDrawable::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDrawable::onDefault(sender,sel,ptr);
  }

void FXPyDrawable::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDrawable::_create(){ FXDrawable::create(); }

void FXPyDrawable::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDrawable::_destroy(){ FXDrawable::destroy(); }

void FXPyDrawable::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDrawable::_detach(){ FXDrawable::detach(); }

void FXPyDrawable::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDrawable::_resize(FXint w,FXint h){ FXDrawable::resize(w,h); }

long FXPyImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXImage::onDefault(sender,sel,ptr);
  }

void FXPyImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyImage::_create(){ FXImage::create(); }

void FXPyImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyImage::_destroy(){ FXImage::destroy(); }

void FXPyImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyImage::_detach(){ FXImage::detach(); }

void FXPyImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyImage::_resize(FXint w,FXint h){ FXImage::resize(w,h); }

void FXPyImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyImage::_restore() { FXImage::restore(); }

void FXPyImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyImage::_render() { FXImage::render(); }

void FXPyImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyImage::_scale(FXint w,FXint h) { FXImage::scale(w,h); }

void FXPyImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyImage::_mirror(FXbool horizontal,FXbool vertical) { FXImage::mirror(horizontal,vertical); }

void FXPyImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyImage::_rotate(FXint degrees) { FXImage::rotate(degrees); }

void FXPyImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXImage::crop(x,y,w,h); }

void FXPyImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyImage::_savePixels(FXStream& store) const { FXImage::savePixels(store); }

void FXPyImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyImage::_loadPixels(FXStream& store) { FXImage::loadPixels(store); }

long FXPyFrame::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFrame::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFrame::onDefault(sender,sel,ptr);
  }

void FXPyFrame::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFrame::_create(){ FXFrame::create(); }

void FXPyFrame::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFrame::_destroy(){ FXFrame::destroy(); }

void FXPyFrame::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFrame::_detach(){ FXFrame::detach(); }

void FXPyFrame::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFrame::_resize(FXint w,FXint h){ FXFrame::resize(w,h); }

void FXPyFrame::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFrame::_enable(){ FXFrame::enable(); }

void FXPyFrame::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFrame::_disable(){ FXFrame::disable(); }

void FXPyFrame::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFrame::_show(){ FXFrame::show(); }

void FXPyFrame::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFrame::_hide(){ FXFrame::hide(); }

void FXPyFrame::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFrame::_lowerWindow(){ FXFrame::lower(); }

FXint FXPyFrame::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFrame::_getDefaultHeight() { return FXFrame::getDefaultHeight(); }

FXint FXPyFrame::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFrame::_getDefaultWidth() { return FXFrame::getDefaultWidth(); }

FXint FXPyFrame::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFrame::_getWidthForHeight(FXint h) { return FXFrame::getWidthForHeight(h); }

FXint FXPyFrame::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFrame::_getHeightForWidth(FXint w) { return FXFrame::getHeightForWidth(w); }

void FXPyFrame::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFrame::_layout() { FXFrame::layout(); }

void FXPyFrame::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFrame::_recalc() { FXFrame::recalc(); }

FXbool FXPyFrame::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFrame::_isComposite() const { return FXFrame::isComposite(); }

void FXPyFrame::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFrame::_move(FXint x,FXint y){ FXFrame::move(x,y); }

void FXPyFrame::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFrame::_position(FXint x,FXint y,FXint w,FXint h){ FXFrame::position(x,y,w,h); }

FXbool FXPyFrame::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFrame::_canFocus() const { return FXFrame::canFocus(); }

void FXPyFrame::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFrame::_setFocus(){ FXFrame::setFocus(); }

void FXPyFrame::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFrame::_killFocus(){ FXFrame::killFocus(); }

void FXPyFrame::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFrame::_setDefault(FXbool enable){ FXFrame::setDefault(enable); }

FXbool FXPyFrame::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFrame::_contains(FXint x,FXint y) const { return FXFrame::contains(x,y); }

FXbool FXPyFrame::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFrame::_doesSaveUnder() const { return FXFrame::doesSaveUnder(); }

void FXPyFrame::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFrame::_reparent(FXComposite* newparent) { FXFrame::reparent(newparent); }

void FXPyFrame::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFrame::_setBackColor(FXColor clr) { FXFrame::setBackColor(clr); }

long FXPyHorizontalFrame::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyHorizontalFrame::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXHorizontalFrame::onDefault(sender,sel,ptr);
  }

void FXPyHorizontalFrame::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyHorizontalFrame::_create(){ FXHorizontalFrame::create(); }

void FXPyHorizontalFrame::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyHorizontalFrame::_destroy(){ FXHorizontalFrame::destroy(); }

void FXPyHorizontalFrame::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyHorizontalFrame::_detach(){ FXHorizontalFrame::detach(); }

void FXPyHorizontalFrame::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyHorizontalFrame::_resize(FXint w,FXint h){ FXHorizontalFrame::resize(w,h); }

void FXPyHorizontalFrame::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyHorizontalFrame::_enable(){ FXHorizontalFrame::enable(); }

void FXPyHorizontalFrame::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyHorizontalFrame::_disable(){ FXHorizontalFrame::disable(); }

void FXPyHorizontalFrame::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyHorizontalFrame::_show(){ FXHorizontalFrame::show(); }

void FXPyHorizontalFrame::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyHorizontalFrame::_hide(){ FXHorizontalFrame::hide(); }

void FXPyHorizontalFrame::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyHorizontalFrame::_lowerWindow(){ FXHorizontalFrame::lower(); }

FXint FXPyHorizontalFrame::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyHorizontalFrame::_getDefaultHeight() { return FXHorizontalFrame::getDefaultHeight(); }

FXint FXPyHorizontalFrame::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyHorizontalFrame::_getDefaultWidth() { return FXHorizontalFrame::getDefaultWidth(); }

FXint FXPyHorizontalFrame::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyHorizontalFrame::_getWidthForHeight(FXint h) { return FXHorizontalFrame::getWidthForHeight(h); }

FXint FXPyHorizontalFrame::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyHorizontalFrame::_getHeightForWidth(FXint w) { return FXHorizontalFrame::getHeightForWidth(w); }

void FXPyHorizontalFrame::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyHorizontalFrame::_layout() { FXHorizontalFrame::layout(); }

void FXPyHorizontalFrame::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyHorizontalFrame::_recalc() { FXHorizontalFrame::recalc(); }

FXbool FXPyHorizontalFrame::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyHorizontalFrame::_isComposite() const { return FXHorizontalFrame::isComposite(); }

void FXPyHorizontalFrame::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyHorizontalFrame::_move(FXint x,FXint y){ FXHorizontalFrame::move(x,y); }

void FXPyHorizontalFrame::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyHorizontalFrame::_position(FXint x,FXint y,FXint w,FXint h){ FXHorizontalFrame::position(x,y,w,h); }

FXbool FXPyHorizontalFrame::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyHorizontalFrame::_canFocus() const { return FXHorizontalFrame::canFocus(); }

void FXPyHorizontalFrame::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyHorizontalFrame::_setFocus(){ FXHorizontalFrame::setFocus(); }

void FXPyHorizontalFrame::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyHorizontalFrame::_killFocus(){ FXHorizontalFrame::killFocus(); }

void FXPyHorizontalFrame::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyHorizontalFrame::_setDefault(FXbool enable){ FXHorizontalFrame::setDefault(enable); }

FXbool FXPyHorizontalFrame::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyHorizontalFrame::_contains(FXint x,FXint y) const { return FXHorizontalFrame::contains(x,y); }

FXbool FXPyHorizontalFrame::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyHorizontalFrame::_doesSaveUnder() const { return FXHorizontalFrame::doesSaveUnder(); }

void FXPyHorizontalFrame::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyHorizontalFrame::_reparent(FXComposite* newparent) { FXHorizontalFrame::reparent(newparent); }

void FXPyHorizontalFrame::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyHorizontalFrame::_setBackColor(FXColor clr) { FXHorizontalFrame::setBackColor(clr); }

long FXPyHorizontalSeparator::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyHorizontalSeparator::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXHorizontalSeparator::onDefault(sender,sel,ptr);
  }

void FXPyHorizontalSeparator::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyHorizontalSeparator::_create(){ FXHorizontalSeparator::create(); }

void FXPyHorizontalSeparator::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyHorizontalSeparator::_destroy(){ FXHorizontalSeparator::destroy(); }

void FXPyHorizontalSeparator::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyHorizontalSeparator::_detach(){ FXHorizontalSeparator::detach(); }

void FXPyHorizontalSeparator::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyHorizontalSeparator::_resize(FXint w,FXint h){ FXHorizontalSeparator::resize(w,h); }

void FXPyHorizontalSeparator::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyHorizontalSeparator::_enable(){ FXHorizontalSeparator::enable(); }

void FXPyHorizontalSeparator::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyHorizontalSeparator::_disable(){ FXHorizontalSeparator::disable(); }

void FXPyHorizontalSeparator::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyHorizontalSeparator::_show(){ FXHorizontalSeparator::show(); }

void FXPyHorizontalSeparator::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyHorizontalSeparator::_hide(){ FXHorizontalSeparator::hide(); }

void FXPyHorizontalSeparator::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyHorizontalSeparator::_lowerWindow(){ FXHorizontalSeparator::lower(); }

FXint FXPyHorizontalSeparator::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyHorizontalSeparator::_getDefaultHeight() { return FXHorizontalSeparator::getDefaultHeight(); }

FXint FXPyHorizontalSeparator::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyHorizontalSeparator::_getDefaultWidth() { return FXHorizontalSeparator::getDefaultWidth(); }

FXint FXPyHorizontalSeparator::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyHorizontalSeparator::_getWidthForHeight(FXint h) { return FXHorizontalSeparator::getWidthForHeight(h); }

FXint FXPyHorizontalSeparator::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyHorizontalSeparator::_getHeightForWidth(FXint w) { return FXHorizontalSeparator::getHeightForWidth(w); }

void FXPyHorizontalSeparator::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyHorizontalSeparator::_layout() { FXHorizontalSeparator::layout(); }

void FXPyHorizontalSeparator::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyHorizontalSeparator::_recalc() { FXHorizontalSeparator::recalc(); }

FXbool FXPyHorizontalSeparator::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyHorizontalSeparator::_isComposite() const { return FXHorizontalSeparator::isComposite(); }

void FXPyHorizontalSeparator::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyHorizontalSeparator::_move(FXint x,FXint y){ FXHorizontalSeparator::move(x,y); }

void FXPyHorizontalSeparator::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyHorizontalSeparator::_position(FXint x,FXint y,FXint w,FXint h){ FXHorizontalSeparator::position(x,y,w,h); }

FXbool FXPyHorizontalSeparator::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyHorizontalSeparator::_canFocus() const { return FXHorizontalSeparator::canFocus(); }

void FXPyHorizontalSeparator::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyHorizontalSeparator::_setFocus(){ FXHorizontalSeparator::setFocus(); }

void FXPyHorizontalSeparator::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyHorizontalSeparator::_killFocus(){ FXHorizontalSeparator::killFocus(); }

void FXPyHorizontalSeparator::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyHorizontalSeparator::_setDefault(FXbool enable){ FXHorizontalSeparator::setDefault(enable); }

FXbool FXPyHorizontalSeparator::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyHorizontalSeparator::_contains(FXint x,FXint y) const { return FXHorizontalSeparator::contains(x,y); }

FXbool FXPyHorizontalSeparator::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyHorizontalSeparator::_doesSaveUnder() const { return FXHorizontalSeparator::doesSaveUnder(); }

void FXPyHorizontalSeparator::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyHorizontalSeparator::_reparent(FXComposite* newparent) { FXHorizontalSeparator::reparent(newparent); }

void FXPyHorizontalSeparator::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyHorizontalSeparator::_setBackColor(FXColor clr) { FXHorizontalSeparator::setBackColor(clr); }

long FXPyLabel::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyLabel::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXLabel::onDefault(sender,sel,ptr);
  }

void FXPyLabel::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyLabel::_create(){ FXLabel::create(); }

void FXPyLabel::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyLabel::_destroy(){ FXLabel::destroy(); }

void FXPyLabel::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyLabel::_detach(){ FXLabel::detach(); }

void FXPyLabel::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyLabel::_resize(FXint w,FXint h){ FXLabel::resize(w,h); }

void FXPyLabel::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyLabel::_enable(){ FXLabel::enable(); }

void FXPyLabel::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyLabel::_disable(){ FXLabel::disable(); }

void FXPyLabel::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyLabel::_show(){ FXLabel::show(); }

void FXPyLabel::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyLabel::_hide(){ FXLabel::hide(); }

void FXPyLabel::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyLabel::_lowerWindow(){ FXLabel::lower(); }

FXint FXPyLabel::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyLabel::_getDefaultHeight() { return FXLabel::getDefaultHeight(); }

FXint FXPyLabel::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyLabel::_getDefaultWidth() { return FXLabel::getDefaultWidth(); }

FXint FXPyLabel::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyLabel::_getWidthForHeight(FXint h) { return FXLabel::getWidthForHeight(h); }

FXint FXPyLabel::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyLabel::_getHeightForWidth(FXint w) { return FXLabel::getHeightForWidth(w); }

void FXPyLabel::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyLabel::_layout() { FXLabel::layout(); }

void FXPyLabel::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyLabel::_recalc() { FXLabel::recalc(); }

FXbool FXPyLabel::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyLabel::_isComposite() const { return FXLabel::isComposite(); }

void FXPyLabel::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyLabel::_move(FXint x,FXint y){ FXLabel::move(x,y); }

void FXPyLabel::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyLabel::_position(FXint x,FXint y,FXint w,FXint h){ FXLabel::position(x,y,w,h); }

FXbool FXPyLabel::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyLabel::_canFocus() const { return FXLabel::canFocus(); }

void FXPyLabel::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyLabel::_setFocus(){ FXLabel::setFocus(); }

void FXPyLabel::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyLabel::_killFocus(){ FXLabel::killFocus(); }

void FXPyLabel::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyLabel::_setDefault(FXbool enable){ FXLabel::setDefault(enable); }

FXbool FXPyLabel::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyLabel::_contains(FXint x,FXint y) const { return FXLabel::contains(x,y); }

FXbool FXPyLabel::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyLabel::_doesSaveUnder() const { return FXLabel::doesSaveUnder(); }

void FXPyLabel::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyLabel::_reparent(FXComposite* newparent) { FXLabel::reparent(newparent); }

void FXPyLabel::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyLabel::_setBackColor(FXColor clr) { FXLabel::setBackColor(clr); }

long FXPyVerticalFrame::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyVerticalFrame::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXVerticalFrame::onDefault(sender,sel,ptr);
  }

void FXPyVerticalFrame::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyVerticalFrame::_create(){ FXVerticalFrame::create(); }

void FXPyVerticalFrame::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyVerticalFrame::_destroy(){ FXVerticalFrame::destroy(); }

void FXPyVerticalFrame::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyVerticalFrame::_detach(){ FXVerticalFrame::detach(); }

void FXPyVerticalFrame::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyVerticalFrame::_resize(FXint w,FXint h){ FXVerticalFrame::resize(w,h); }

void FXPyVerticalFrame::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyVerticalFrame::_enable(){ FXVerticalFrame::enable(); }

void FXPyVerticalFrame::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyVerticalFrame::_disable(){ FXVerticalFrame::disable(); }

void FXPyVerticalFrame::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyVerticalFrame::_show(){ FXVerticalFrame::show(); }

void FXPyVerticalFrame::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyVerticalFrame::_hide(){ FXVerticalFrame::hide(); }

void FXPyVerticalFrame::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyVerticalFrame::_lowerWindow(){ FXVerticalFrame::lower(); }

FXint FXPyVerticalFrame::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyVerticalFrame::_getDefaultHeight() { return FXVerticalFrame::getDefaultHeight(); }

FXint FXPyVerticalFrame::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyVerticalFrame::_getDefaultWidth() { return FXVerticalFrame::getDefaultWidth(); }

FXint FXPyVerticalFrame::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyVerticalFrame::_getWidthForHeight(FXint h) { return FXVerticalFrame::getWidthForHeight(h); }

FXint FXPyVerticalFrame::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyVerticalFrame::_getHeightForWidth(FXint w) { return FXVerticalFrame::getHeightForWidth(w); }

void FXPyVerticalFrame::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyVerticalFrame::_layout() { FXVerticalFrame::layout(); }

void FXPyVerticalFrame::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyVerticalFrame::_recalc() { FXVerticalFrame::recalc(); }

FXbool FXPyVerticalFrame::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyVerticalFrame::_isComposite() const { return FXVerticalFrame::isComposite(); }

void FXPyVerticalFrame::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyVerticalFrame::_move(FXint x,FXint y){ FXVerticalFrame::move(x,y); }

void FXPyVerticalFrame::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyVerticalFrame::_position(FXint x,FXint y,FXint w,FXint h){ FXVerticalFrame::position(x,y,w,h); }

FXbool FXPyVerticalFrame::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyVerticalFrame::_canFocus() const { return FXVerticalFrame::canFocus(); }

void FXPyVerticalFrame::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyVerticalFrame::_setFocus(){ FXVerticalFrame::setFocus(); }

void FXPyVerticalFrame::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyVerticalFrame::_killFocus(){ FXVerticalFrame::killFocus(); }

void FXPyVerticalFrame::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyVerticalFrame::_setDefault(FXbool enable){ FXVerticalFrame::setDefault(enable); }

FXbool FXPyVerticalFrame::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyVerticalFrame::_contains(FXint x,FXint y) const { return FXVerticalFrame::contains(x,y); }

FXbool FXPyVerticalFrame::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyVerticalFrame::_doesSaveUnder() const { return FXVerticalFrame::doesSaveUnder(); }

void FXPyVerticalFrame::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyVerticalFrame::_reparent(FXComposite* newparent) { FXVerticalFrame::reparent(newparent); }

void FXPyVerticalFrame::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyVerticalFrame::_setBackColor(FXColor clr) { FXVerticalFrame::setBackColor(clr); }

long FXPyVerticalSeparator::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyVerticalSeparator::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXVerticalSeparator::onDefault(sender,sel,ptr);
  }

void FXPyVerticalSeparator::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyVerticalSeparator::_create(){ FXVerticalSeparator::create(); }

void FXPyVerticalSeparator::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyVerticalSeparator::_destroy(){ FXVerticalSeparator::destroy(); }

void FXPyVerticalSeparator::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyVerticalSeparator::_detach(){ FXVerticalSeparator::detach(); }

void FXPyVerticalSeparator::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyVerticalSeparator::_resize(FXint w,FXint h){ FXVerticalSeparator::resize(w,h); }

void FXPyVerticalSeparator::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyVerticalSeparator::_enable(){ FXVerticalSeparator::enable(); }

void FXPyVerticalSeparator::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyVerticalSeparator::_disable(){ FXVerticalSeparator::disable(); }

void FXPyVerticalSeparator::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyVerticalSeparator::_show(){ FXVerticalSeparator::show(); }

void FXPyVerticalSeparator::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyVerticalSeparator::_hide(){ FXVerticalSeparator::hide(); }

void FXPyVerticalSeparator::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyVerticalSeparator::_lowerWindow(){ FXVerticalSeparator::lower(); }

FXint FXPyVerticalSeparator::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyVerticalSeparator::_getDefaultHeight() { return FXVerticalSeparator::getDefaultHeight(); }

FXint FXPyVerticalSeparator::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyVerticalSeparator::_getDefaultWidth() { return FXVerticalSeparator::getDefaultWidth(); }

FXint FXPyVerticalSeparator::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyVerticalSeparator::_getWidthForHeight(FXint h) { return FXVerticalSeparator::getWidthForHeight(h); }

FXint FXPyVerticalSeparator::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyVerticalSeparator::_getHeightForWidth(FXint w) { return FXVerticalSeparator::getHeightForWidth(w); }

void FXPyVerticalSeparator::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyVerticalSeparator::_layout() { FXVerticalSeparator::layout(); }

void FXPyVerticalSeparator::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyVerticalSeparator::_recalc() { FXVerticalSeparator::recalc(); }

FXbool FXPyVerticalSeparator::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyVerticalSeparator::_isComposite() const { return FXVerticalSeparator::isComposite(); }

void FXPyVerticalSeparator::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyVerticalSeparator::_move(FXint x,FXint y){ FXVerticalSeparator::move(x,y); }

void FXPyVerticalSeparator::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyVerticalSeparator::_position(FXint x,FXint y,FXint w,FXint h){ FXVerticalSeparator::position(x,y,w,h); }

FXbool FXPyVerticalSeparator::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyVerticalSeparator::_canFocus() const { return FXVerticalSeparator::canFocus(); }

void FXPyVerticalSeparator::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyVerticalSeparator::_setFocus(){ FXVerticalSeparator::setFocus(); }

void FXPyVerticalSeparator::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyVerticalSeparator::_killFocus(){ FXVerticalSeparator::killFocus(); }

void FXPyVerticalSeparator::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyVerticalSeparator::_setDefault(FXbool enable){ FXVerticalSeparator::setDefault(enable); }

FXbool FXPyVerticalSeparator::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyVerticalSeparator::_contains(FXint x,FXint y) const { return FXVerticalSeparator::contains(x,y); }

FXbool FXPyVerticalSeparator::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyVerticalSeparator::_doesSaveUnder() const { return FXVerticalSeparator::doesSaveUnder(); }

void FXPyVerticalSeparator::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyVerticalSeparator::_reparent(FXComposite* newparent) { FXVerticalSeparator::reparent(newparent); }

void FXPyVerticalSeparator::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyVerticalSeparator::_setBackColor(FXColor clr) { FXVerticalSeparator::setBackColor(clr); }

long FXPyWindow::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyWindow::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXWindow::onDefault(sender,sel,ptr);
  }

void FXPyWindow::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyWindow::_create(){ FXWindow::create(); }

void FXPyWindow::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyWindow::_destroy(){ FXWindow::destroy(); }

void FXPyWindow::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyWindow::_detach(){ FXWindow::detach(); }

void FXPyWindow::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyWindow::_resize(FXint w,FXint h){ FXWindow::resize(w,h); }

void FXPyWindow::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyWindow::_enable(){ FXWindow::enable(); }

void FXPyWindow::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyWindow::_disable(){ FXWindow::disable(); }

void FXPyWindow::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyWindow::_show(){ FXWindow::show(); }

void FXPyWindow::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyWindow::_hide(){ FXWindow::hide(); }

void FXPyWindow::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyWindow::_lowerWindow(){ FXWindow::lower(); }

FXint FXPyWindow::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyWindow::_getDefaultHeight() { return FXWindow::getDefaultHeight(); }

FXint FXPyWindow::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyWindow::_getDefaultWidth() { return FXWindow::getDefaultWidth(); }

FXint FXPyWindow::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyWindow::_getWidthForHeight(FXint h) { return FXWindow::getWidthForHeight(h); }

FXint FXPyWindow::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyWindow::_getHeightForWidth(FXint w) { return FXWindow::getHeightForWidth(w); }

void FXPyWindow::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyWindow::_layout() { FXWindow::layout(); }

void FXPyWindow::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyWindow::_recalc() { FXWindow::recalc(); }

FXbool FXPyWindow::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyWindow::_isComposite() const { return FXWindow::isComposite(); }

void FXPyWindow::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyWindow::_move(FXint x,FXint y){ FXWindow::move(x,y); }

void FXPyWindow::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyWindow::_position(FXint x,FXint y,FXint w,FXint h){ FXWindow::position(x,y,w,h); }

FXbool FXPyWindow::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyWindow::_canFocus() const { return FXWindow::canFocus(); }

void FXPyWindow::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyWindow::_setFocus(){ FXWindow::setFocus(); }

void FXPyWindow::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyWindow::_killFocus(){ FXWindow::killFocus(); }

void FXPyWindow::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyWindow::_setDefault(FXbool enable){ FXWindow::setDefault(enable); }

FXbool FXPyWindow::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyWindow::_contains(FXint x,FXint y) const { return FXWindow::contains(x,y); }

FXbool FXPyWindow::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyWindow::_doesSaveUnder() const { return FXWindow::doesSaveUnder(); }

void FXPyWindow::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyWindow::_reparent(FXComposite* newparent) { FXWindow::reparent(newparent); }

void FXPyWindow::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyWindow::_setBackColor(FXColor clr) { FXWindow::setBackColor(clr); }

long FXPyCanvas::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyCanvas::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXCanvas::onDefault(sender,sel,ptr);
  }

void FXPyCanvas::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyCanvas::_create(){ FXCanvas::create(); }

void FXPyCanvas::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyCanvas::_destroy(){ FXCanvas::destroy(); }

void FXPyCanvas::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyCanvas::_detach(){ FXCanvas::detach(); }

void FXPyCanvas::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyCanvas::_resize(FXint w,FXint h){ FXCanvas::resize(w,h); }

void FXPyCanvas::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyCanvas::_enable(){ FXCanvas::enable(); }

void FXPyCanvas::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyCanvas::_disable(){ FXCanvas::disable(); }

void FXPyCanvas::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyCanvas::_show(){ FXCanvas::show(); }

void FXPyCanvas::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyCanvas::_hide(){ FXCanvas::hide(); }

void FXPyCanvas::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyCanvas::_lowerWindow(){ FXCanvas::lower(); }

FXint FXPyCanvas::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyCanvas::_getDefaultHeight() { return FXCanvas::getDefaultHeight(); }

FXint FXPyCanvas::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyCanvas::_getDefaultWidth() { return FXCanvas::getDefaultWidth(); }

FXint FXPyCanvas::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyCanvas::_getWidthForHeight(FXint h) { return FXCanvas::getWidthForHeight(h); }

FXint FXPyCanvas::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyCanvas::_getHeightForWidth(FXint w) { return FXCanvas::getHeightForWidth(w); }

void FXPyCanvas::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyCanvas::_layout() { FXCanvas::layout(); }

void FXPyCanvas::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyCanvas::_recalc() { FXCanvas::recalc(); }

FXbool FXPyCanvas::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyCanvas::_isComposite() const { return FXCanvas::isComposite(); }

void FXPyCanvas::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyCanvas::_move(FXint x,FXint y){ FXCanvas::move(x,y); }

void FXPyCanvas::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyCanvas::_position(FXint x,FXint y,FXint w,FXint h){ FXCanvas::position(x,y,w,h); }

FXbool FXPyCanvas::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyCanvas::_canFocus() const { return FXCanvas::canFocus(); }

void FXPyCanvas::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyCanvas::_setFocus(){ FXCanvas::setFocus(); }

void FXPyCanvas::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyCanvas::_killFocus(){ FXCanvas::killFocus(); }

void FXPyCanvas::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyCanvas::_setDefault(FXbool enable){ FXCanvas::setDefault(enable); }

FXbool FXPyCanvas::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyCanvas::_contains(FXint x,FXint y) const { return FXCanvas::contains(x,y); }

FXbool FXPyCanvas::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyCanvas::_doesSaveUnder() const { return FXCanvas::doesSaveUnder(); }

void FXPyCanvas::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyCanvas::_reparent(FXComposite* newparent) { FXCanvas::reparent(newparent); }

void FXPyCanvas::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyCanvas::_setBackColor(FXColor clr) { FXCanvas::setBackColor(clr); }

long FXPyMainWindow::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMainWindow::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMainWindow::onDefault(sender,sel,ptr);
  }

void FXPyMainWindow::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMainWindow::_create(){ FXMainWindow::create(); }

void FXPyMainWindow::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMainWindow::_destroy(){ FXMainWindow::destroy(); }

void FXPyMainWindow::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMainWindow::_detach(){ FXMainWindow::detach(); }

void FXPyMainWindow::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMainWindow::_resize(FXint w,FXint h){ FXMainWindow::resize(w,h); }

void FXPyMainWindow::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMainWindow::_enable(){ FXMainWindow::enable(); }

void FXPyMainWindow::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMainWindow::_disable(){ FXMainWindow::disable(); }

void FXPyMainWindow::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMainWindow::_show(){ FXMainWindow::show(); }

void FXPyMainWindow::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMainWindow::_hide(){ FXMainWindow::hide(); }

void FXPyMainWindow::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMainWindow::_lowerWindow(){ FXMainWindow::lower(); }

FXint FXPyMainWindow::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMainWindow::_getDefaultHeight() { return FXMainWindow::getDefaultHeight(); }

FXint FXPyMainWindow::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMainWindow::_getDefaultWidth() { return FXMainWindow::getDefaultWidth(); }

FXint FXPyMainWindow::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMainWindow::_getWidthForHeight(FXint h) { return FXMainWindow::getWidthForHeight(h); }

FXint FXPyMainWindow::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMainWindow::_getHeightForWidth(FXint w) { return FXMainWindow::getHeightForWidth(w); }

void FXPyMainWindow::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMainWindow::_layout() { FXMainWindow::layout(); }

void FXPyMainWindow::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMainWindow::_recalc() { FXMainWindow::recalc(); }

FXbool FXPyMainWindow::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMainWindow::_isComposite() const { return FXMainWindow::isComposite(); }

void FXPyMainWindow::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMainWindow::_move(FXint x,FXint y){ FXMainWindow::move(x,y); }

void FXPyMainWindow::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMainWindow::_position(FXint x,FXint y,FXint w,FXint h){ FXMainWindow::position(x,y,w,h); }

FXbool FXPyMainWindow::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMainWindow::_canFocus() const { return FXMainWindow::canFocus(); }

void FXPyMainWindow::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMainWindow::_setFocus(){ FXMainWindow::setFocus(); }

void FXPyMainWindow::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMainWindow::_killFocus(){ FXMainWindow::killFocus(); }

void FXPyMainWindow::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMainWindow::_setDefault(FXbool enable){ FXMainWindow::setDefault(enable); }

FXbool FXPyMainWindow::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMainWindow::_contains(FXint x,FXint y) const { return FXMainWindow::contains(x,y); }

FXbool FXPyMainWindow::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMainWindow::_doesSaveUnder() const { return FXMainWindow::doesSaveUnder(); }

void FXPyMainWindow::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMainWindow::_reparent(FXComposite* newparent) { FXMainWindow::reparent(newparent); }

void FXPyMainWindow::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMainWindow::_setBackColor(FXColor clr) { FXMainWindow::setBackColor(clr); }

void FXPyMainWindow::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyMainWindow::_iconify() { FXMainWindow::iconify(); }

void FXPyMainWindow::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyMainWindow::_deiconify() { FXMainWindow::deiconify(); }

void FXPyMainWindow::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyMainWindow::_show(FXuint placement) { FXMainWindow::show(placement); }

long FXPyPacker::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPacker::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPacker::onDefault(sender,sel,ptr);
  }

void FXPyPacker::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPacker::_create(){ FXPacker::create(); }

void FXPyPacker::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPacker::_destroy(){ FXPacker::destroy(); }

void FXPyPacker::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPacker::_detach(){ FXPacker::detach(); }

void FXPyPacker::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPacker::_resize(FXint w,FXint h){ FXPacker::resize(w,h); }

void FXPyPacker::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyPacker::_enable(){ FXPacker::enable(); }

void FXPyPacker::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyPacker::_disable(){ FXPacker::disable(); }

void FXPyPacker::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyPacker::_show(){ FXPacker::show(); }

void FXPyPacker::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyPacker::_hide(){ FXPacker::hide(); }

void FXPyPacker::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyPacker::_lowerWindow(){ FXPacker::lower(); }

FXint FXPyPacker::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyPacker::_getDefaultHeight() { return FXPacker::getDefaultHeight(); }

FXint FXPyPacker::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyPacker::_getDefaultWidth() { return FXPacker::getDefaultWidth(); }

FXint FXPyPacker::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyPacker::_getWidthForHeight(FXint h) { return FXPacker::getWidthForHeight(h); }

FXint FXPyPacker::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyPacker::_getHeightForWidth(FXint w) { return FXPacker::getHeightForWidth(w); }

void FXPyPacker::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyPacker::_layout() { FXPacker::layout(); }

void FXPyPacker::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyPacker::_recalc() { FXPacker::recalc(); }

FXbool FXPyPacker::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyPacker::_isComposite() const { return FXPacker::isComposite(); }

void FXPyPacker::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyPacker::_move(FXint x,FXint y){ FXPacker::move(x,y); }

void FXPyPacker::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyPacker::_position(FXint x,FXint y,FXint w,FXint h){ FXPacker::position(x,y,w,h); }

FXbool FXPyPacker::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyPacker::_canFocus() const { return FXPacker::canFocus(); }

void FXPyPacker::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyPacker::_setFocus(){ FXPacker::setFocus(); }

void FXPyPacker::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyPacker::_killFocus(){ FXPacker::killFocus(); }

void FXPyPacker::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyPacker::_setDefault(FXbool enable){ FXPacker::setDefault(enable); }

FXbool FXPyPacker::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyPacker::_contains(FXint x,FXint y) const { return FXPacker::contains(x,y); }

FXbool FXPyPacker::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyPacker::_doesSaveUnder() const { return FXPacker::doesSaveUnder(); }

void FXPyPacker::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyPacker::_reparent(FXComposite* newparent) { FXPacker::reparent(newparent); }

void FXPyPacker::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyPacker::_setBackColor(FXColor clr) { FXPacker::setBackColor(clr); }

long FXPyPopup::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPopup::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPopup::onDefault(sender,sel,ptr);
  }

void FXPyPopup::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPopup::_create(){ FXPopup::create(); }

void FXPyPopup::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPopup::_destroy(){ FXPopup::destroy(); }

void FXPyPopup::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPopup::_detach(){ FXPopup::detach(); }

void FXPyPopup::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPopup::_resize(FXint w,FXint h){ FXPopup::resize(w,h); }

void FXPyPopup::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyPopup::_enable(){ FXPopup::enable(); }

void FXPyPopup::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyPopup::_disable(){ FXPopup::disable(); }

void FXPyPopup::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyPopup::_show(){ FXPopup::show(); }

void FXPyPopup::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyPopup::_hide(){ FXPopup::hide(); }

void FXPyPopup::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyPopup::_lowerWindow(){ FXPopup::lower(); }

FXint FXPyPopup::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyPopup::_getDefaultHeight() { return FXPopup::getDefaultHeight(); }

FXint FXPyPopup::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyPopup::_getDefaultWidth() { return FXPopup::getDefaultWidth(); }

FXint FXPyPopup::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyPopup::_getWidthForHeight(FXint h) { return FXPopup::getWidthForHeight(h); }

FXint FXPyPopup::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyPopup::_getHeightForWidth(FXint w) { return FXPopup::getHeightForWidth(w); }

void FXPyPopup::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyPopup::_layout() { FXPopup::layout(); }

void FXPyPopup::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyPopup::_recalc() { FXPopup::recalc(); }

FXbool FXPyPopup::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyPopup::_isComposite() const { return FXPopup::isComposite(); }

void FXPyPopup::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyPopup::_move(FXint x,FXint y){ FXPopup::move(x,y); }

void FXPyPopup::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyPopup::_position(FXint x,FXint y,FXint w,FXint h){ FXPopup::position(x,y,w,h); }

FXbool FXPyPopup::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyPopup::_canFocus() const { return FXPopup::canFocus(); }

void FXPyPopup::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyPopup::_setFocus(){ FXPopup::setFocus(); }

void FXPyPopup::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyPopup::_killFocus(){ FXPopup::killFocus(); }

void FXPyPopup::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyPopup::_setDefault(FXbool enable){ FXPopup::setDefault(enable); }

FXbool FXPyPopup::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyPopup::_contains(FXint x,FXint y) const { return FXPopup::contains(x,y); }

FXbool FXPyPopup::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyPopup::_doesSaveUnder() const { return FXPopup::doesSaveUnder(); }

void FXPyPopup::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyPopup::_reparent(FXComposite* newparent) { FXPopup::reparent(newparent); }

void FXPyPopup::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyPopup::_setBackColor(FXColor clr) { FXPopup::setBackColor(clr); }

void FXPyPopup::popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { FXPyCallVoidFunction(this,"popup",grabto,x,y,w,h); }
void FXPyPopup::_popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { FXPopup::popup(grabto,x,y,w,h); }

void FXPyPopup::popdown() { FXPyCallVoidFunction(this,"popdown"); }
void FXPyPopup::_popdown() { FXPopup::popdown(); }

long FXPyShell::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyShell::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXShell::onDefault(sender,sel,ptr);
  }

void FXPyShell::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyShell::_create(){ FXShell::create(); }

void FXPyShell::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyShell::_destroy(){ FXShell::destroy(); }

void FXPyShell::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyShell::_detach(){ FXShell::detach(); }

void FXPyShell::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyShell::_resize(FXint w,FXint h){ FXShell::resize(w,h); }

void FXPyShell::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyShell::_enable(){ FXShell::enable(); }

void FXPyShell::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyShell::_disable(){ FXShell::disable(); }

void FXPyShell::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyShell::_show(){ FXShell::show(); }

void FXPyShell::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyShell::_hide(){ FXShell::hide(); }

void FXPyShell::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyShell::_lowerWindow(){ FXShell::lower(); }

FXint FXPyShell::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyShell::_getDefaultHeight() { return FXShell::getDefaultHeight(); }

FXint FXPyShell::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyShell::_getDefaultWidth() { return FXShell::getDefaultWidth(); }

FXint FXPyShell::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyShell::_getWidthForHeight(FXint h) { return FXShell::getWidthForHeight(h); }

FXint FXPyShell::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyShell::_getHeightForWidth(FXint w) { return FXShell::getHeightForWidth(w); }

void FXPyShell::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyShell::_layout() { FXShell::layout(); }

void FXPyShell::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyShell::_recalc() { FXShell::recalc(); }

FXbool FXPyShell::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyShell::_isComposite() const { return FXShell::isComposite(); }

void FXPyShell::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyShell::_move(FXint x,FXint y){ FXShell::move(x,y); }

void FXPyShell::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyShell::_position(FXint x,FXint y,FXint w,FXint h){ FXShell::position(x,y,w,h); }

FXbool FXPyShell::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyShell::_canFocus() const { return FXShell::canFocus(); }

void FXPyShell::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyShell::_setFocus(){ FXShell::setFocus(); }

void FXPyShell::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyShell::_killFocus(){ FXShell::killFocus(); }

void FXPyShell::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyShell::_setDefault(FXbool enable){ FXShell::setDefault(enable); }

FXbool FXPyShell::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyShell::_contains(FXint x,FXint y) const { return FXShell::contains(x,y); }

FXbool FXPyShell::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyShell::_doesSaveUnder() const { return FXShell::doesSaveUnder(); }

void FXPyShell::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyShell::_reparent(FXComposite* newparent) { FXShell::reparent(newparent); }

void FXPyShell::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyShell::_setBackColor(FXColor clr) { FXShell::setBackColor(clr); }

long FXPyTooltip::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTooltip::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTooltip::onDefault(sender,sel,ptr);
  }

void FXPyTooltip::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTooltip::_create(){ FXTooltip::create(); }

void FXPyTooltip::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTooltip::_destroy(){ FXTooltip::destroy(); }

void FXPyTooltip::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTooltip::_detach(){ FXTooltip::detach(); }

void FXPyTooltip::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTooltip::_resize(FXint w,FXint h){ FXTooltip::resize(w,h); }

void FXPyTooltip::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTooltip::_enable(){ FXTooltip::enable(); }

void FXPyTooltip::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTooltip::_disable(){ FXTooltip::disable(); }

void FXPyTooltip::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTooltip::_show(){ FXTooltip::show(); }

void FXPyTooltip::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTooltip::_hide(){ FXTooltip::hide(); }

void FXPyTooltip::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTooltip::_lowerWindow(){ FXTooltip::lower(); }

FXint FXPyTooltip::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTooltip::_getDefaultHeight() { return FXTooltip::getDefaultHeight(); }

FXint FXPyTooltip::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTooltip::_getDefaultWidth() { return FXTooltip::getDefaultWidth(); }

FXint FXPyTooltip::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTooltip::_getWidthForHeight(FXint h) { return FXTooltip::getWidthForHeight(h); }

FXint FXPyTooltip::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTooltip::_getHeightForWidth(FXint w) { return FXTooltip::getHeightForWidth(w); }

void FXPyTooltip::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTooltip::_layout() { FXTooltip::layout(); }

void FXPyTooltip::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTooltip::_recalc() { FXTooltip::recalc(); }

FXbool FXPyTooltip::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTooltip::_isComposite() const { return FXTooltip::isComposite(); }

void FXPyTooltip::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTooltip::_move(FXint x,FXint y){ FXTooltip::move(x,y); }

void FXPyTooltip::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTooltip::_position(FXint x,FXint y,FXint w,FXint h){ FXTooltip::position(x,y,w,h); }

FXbool FXPyTooltip::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTooltip::_canFocus() const { return FXTooltip::canFocus(); }

void FXPyTooltip::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTooltip::_setFocus(){ FXTooltip::setFocus(); }

void FXPyTooltip::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTooltip::_killFocus(){ FXTooltip::killFocus(); }

void FXPyTooltip::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTooltip::_setDefault(FXbool enable){ FXTooltip::setDefault(enable); }

FXbool FXPyTooltip::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTooltip::_contains(FXint x,FXint y) const { return FXTooltip::contains(x,y); }

FXbool FXPyTooltip::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTooltip::_doesSaveUnder() const { return FXTooltip::doesSaveUnder(); }

void FXPyTooltip::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTooltip::_reparent(FXComposite* newparent) { FXTooltip::reparent(newparent); }

void FXPyTooltip::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTooltip::_setBackColor(FXColor clr) { FXTooltip::setBackColor(clr); }

long FXPyTopWindow::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTopWindow::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTopWindow::onDefault(sender,sel,ptr);
  }

void FXPyTopWindow::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTopWindow::_create(){ FXTopWindow::create(); }

void FXPyTopWindow::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTopWindow::_destroy(){ FXTopWindow::destroy(); }

void FXPyTopWindow::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTopWindow::_detach(){ FXTopWindow::detach(); }

void FXPyTopWindow::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTopWindow::_resize(FXint w,FXint h){ FXTopWindow::resize(w,h); }

void FXPyTopWindow::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTopWindow::_enable(){ FXTopWindow::enable(); }

void FXPyTopWindow::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTopWindow::_disable(){ FXTopWindow::disable(); }

void FXPyTopWindow::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTopWindow::_show(){ FXTopWindow::show(); }

void FXPyTopWindow::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTopWindow::_hide(){ FXTopWindow::hide(); }

void FXPyTopWindow::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTopWindow::_lowerWindow(){ FXTopWindow::lower(); }

FXint FXPyTopWindow::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTopWindow::_getDefaultHeight() { return FXTopWindow::getDefaultHeight(); }

FXint FXPyTopWindow::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTopWindow::_getDefaultWidth() { return FXTopWindow::getDefaultWidth(); }

FXint FXPyTopWindow::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTopWindow::_getWidthForHeight(FXint h) { return FXTopWindow::getWidthForHeight(h); }

FXint FXPyTopWindow::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTopWindow::_getHeightForWidth(FXint w) { return FXTopWindow::getHeightForWidth(w); }

void FXPyTopWindow::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTopWindow::_layout() { FXTopWindow::layout(); }

void FXPyTopWindow::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTopWindow::_recalc() { FXTopWindow::recalc(); }

FXbool FXPyTopWindow::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTopWindow::_isComposite() const { return FXTopWindow::isComposite(); }

void FXPyTopWindow::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTopWindow::_move(FXint x,FXint y){ FXTopWindow::move(x,y); }

void FXPyTopWindow::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTopWindow::_position(FXint x,FXint y,FXint w,FXint h){ FXTopWindow::position(x,y,w,h); }

FXbool FXPyTopWindow::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTopWindow::_canFocus() const { return FXTopWindow::canFocus(); }

void FXPyTopWindow::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTopWindow::_setFocus(){ FXTopWindow::setFocus(); }

void FXPyTopWindow::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTopWindow::_killFocus(){ FXTopWindow::killFocus(); }

void FXPyTopWindow::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTopWindow::_setDefault(FXbool enable){ FXTopWindow::setDefault(enable); }

FXbool FXPyTopWindow::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTopWindow::_contains(FXint x,FXint y) const { return FXTopWindow::contains(x,y); }

FXbool FXPyTopWindow::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTopWindow::_doesSaveUnder() const { return FXTopWindow::doesSaveUnder(); }

void FXPyTopWindow::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTopWindow::_reparent(FXComposite* newparent) { FXTopWindow::reparent(newparent); }

void FXPyTopWindow::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTopWindow::_setBackColor(FXColor clr) { FXTopWindow::setBackColor(clr); }

void FXPyTopWindow::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyTopWindow::_iconify() { FXTopWindow::iconify(); }

void FXPyTopWindow::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyTopWindow::_deiconify() { FXTopWindow::deiconify(); }

void FXPyTopWindow::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyTopWindow::_show(FXuint placement) { FXTopWindow::show(placement); }

long FXPyDialogBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDialogBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDialogBox::onDefault(sender,sel,ptr);
  }

void FXPyDialogBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDialogBox::_create(){ FXDialogBox::create(); }

void FXPyDialogBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDialogBox::_destroy(){ FXDialogBox::destroy(); }

void FXPyDialogBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDialogBox::_detach(){ FXDialogBox::detach(); }

void FXPyDialogBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDialogBox::_resize(FXint w,FXint h){ FXDialogBox::resize(w,h); }

void FXPyDialogBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDialogBox::_enable(){ FXDialogBox::enable(); }

void FXPyDialogBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDialogBox::_disable(){ FXDialogBox::disable(); }

void FXPyDialogBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDialogBox::_show(){ FXDialogBox::show(); }

void FXPyDialogBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDialogBox::_hide(){ FXDialogBox::hide(); }

void FXPyDialogBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDialogBox::_lowerWindow(){ FXDialogBox::lower(); }

FXint FXPyDialogBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDialogBox::_getDefaultHeight() { return FXDialogBox::getDefaultHeight(); }

FXint FXPyDialogBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDialogBox::_getDefaultWidth() { return FXDialogBox::getDefaultWidth(); }

FXint FXPyDialogBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDialogBox::_getWidthForHeight(FXint h) { return FXDialogBox::getWidthForHeight(h); }

FXint FXPyDialogBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDialogBox::_getHeightForWidth(FXint w) { return FXDialogBox::getHeightForWidth(w); }

void FXPyDialogBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDialogBox::_layout() { FXDialogBox::layout(); }

void FXPyDialogBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDialogBox::_recalc() { FXDialogBox::recalc(); }

FXbool FXPyDialogBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDialogBox::_isComposite() const { return FXDialogBox::isComposite(); }

void FXPyDialogBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDialogBox::_move(FXint x,FXint y){ FXDialogBox::move(x,y); }

void FXPyDialogBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDialogBox::_position(FXint x,FXint y,FXint w,FXint h){ FXDialogBox::position(x,y,w,h); }

FXbool FXPyDialogBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDialogBox::_canFocus() const { return FXDialogBox::canFocus(); }

void FXPyDialogBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDialogBox::_setFocus(){ FXDialogBox::setFocus(); }

void FXPyDialogBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDialogBox::_killFocus(){ FXDialogBox::killFocus(); }

void FXPyDialogBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDialogBox::_setDefault(FXbool enable){ FXDialogBox::setDefault(enable); }

FXbool FXPyDialogBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDialogBox::_contains(FXint x,FXint y) const { return FXDialogBox::contains(x,y); }

FXbool FXPyDialogBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDialogBox::_doesSaveUnder() const { return FXDialogBox::doesSaveUnder(); }

void FXPyDialogBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDialogBox::_reparent(FXComposite* newparent) { FXDialogBox::reparent(newparent); }

void FXPyDialogBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDialogBox::_setBackColor(FXColor clr) { FXDialogBox::setBackColor(clr); }

void FXPyDialogBox::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyDialogBox::_iconify() { FXDialogBox::iconify(); }

void FXPyDialogBox::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyDialogBox::_deiconify() { FXDialogBox::deiconify(); }

void FXPyDialogBox::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyDialogBox::_show(FXuint placement) { FXDialogBox::show(placement); }

long FXPyStatusbar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyStatusbar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXStatusbar::onDefault(sender,sel,ptr);
  }

void FXPyStatusbar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyStatusbar::_create(){ FXStatusbar::create(); }

void FXPyStatusbar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyStatusbar::_destroy(){ FXStatusbar::destroy(); }

void FXPyStatusbar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyStatusbar::_detach(){ FXStatusbar::detach(); }

void FXPyStatusbar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyStatusbar::_resize(FXint w,FXint h){ FXStatusbar::resize(w,h); }

void FXPyStatusbar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyStatusbar::_enable(){ FXStatusbar::enable(); }

void FXPyStatusbar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyStatusbar::_disable(){ FXStatusbar::disable(); }

void FXPyStatusbar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyStatusbar::_show(){ FXStatusbar::show(); }

void FXPyStatusbar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyStatusbar::_hide(){ FXStatusbar::hide(); }

void FXPyStatusbar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyStatusbar::_lowerWindow(){ FXStatusbar::lower(); }

FXint FXPyStatusbar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyStatusbar::_getDefaultHeight() { return FXStatusbar::getDefaultHeight(); }

FXint FXPyStatusbar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyStatusbar::_getDefaultWidth() { return FXStatusbar::getDefaultWidth(); }

FXint FXPyStatusbar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyStatusbar::_getWidthForHeight(FXint h) { return FXStatusbar::getWidthForHeight(h); }

FXint FXPyStatusbar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyStatusbar::_getHeightForWidth(FXint w) { return FXStatusbar::getHeightForWidth(w); }

void FXPyStatusbar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyStatusbar::_layout() { FXStatusbar::layout(); }

void FXPyStatusbar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyStatusbar::_recalc() { FXStatusbar::recalc(); }

FXbool FXPyStatusbar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyStatusbar::_isComposite() const { return FXStatusbar::isComposite(); }

void FXPyStatusbar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyStatusbar::_move(FXint x,FXint y){ FXStatusbar::move(x,y); }

void FXPyStatusbar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyStatusbar::_position(FXint x,FXint y,FXint w,FXint h){ FXStatusbar::position(x,y,w,h); }

FXbool FXPyStatusbar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyStatusbar::_canFocus() const { return FXStatusbar::canFocus(); }

void FXPyStatusbar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyStatusbar::_setFocus(){ FXStatusbar::setFocus(); }

void FXPyStatusbar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyStatusbar::_killFocus(){ FXStatusbar::killFocus(); }

void FXPyStatusbar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyStatusbar::_setDefault(FXbool enable){ FXStatusbar::setDefault(enable); }

FXbool FXPyStatusbar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyStatusbar::_contains(FXint x,FXint y) const { return FXStatusbar::contains(x,y); }

FXbool FXPyStatusbar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyStatusbar::_doesSaveUnder() const { return FXStatusbar::doesSaveUnder(); }

void FXPyStatusbar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyStatusbar::_reparent(FXComposite* newparent) { FXStatusbar::reparent(newparent); }

void FXPyStatusbar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyStatusbar::_setBackColor(FXColor clr) { FXStatusbar::setBackColor(clr); }

long FXPyGroupBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGroupBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGroupBox::onDefault(sender,sel,ptr);
  }

void FXPyGroupBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGroupBox::_create(){ FXGroupBox::create(); }

void FXPyGroupBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGroupBox::_destroy(){ FXGroupBox::destroy(); }

void FXPyGroupBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGroupBox::_detach(){ FXGroupBox::detach(); }

void FXPyGroupBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyGroupBox::_resize(FXint w,FXint h){ FXGroupBox::resize(w,h); }

void FXPyGroupBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyGroupBox::_enable(){ FXGroupBox::enable(); }

void FXPyGroupBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyGroupBox::_disable(){ FXGroupBox::disable(); }

void FXPyGroupBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyGroupBox::_show(){ FXGroupBox::show(); }

void FXPyGroupBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyGroupBox::_hide(){ FXGroupBox::hide(); }

void FXPyGroupBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyGroupBox::_lowerWindow(){ FXGroupBox::lower(); }

FXint FXPyGroupBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyGroupBox::_getDefaultHeight() { return FXGroupBox::getDefaultHeight(); }

FXint FXPyGroupBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyGroupBox::_getDefaultWidth() { return FXGroupBox::getDefaultWidth(); }

FXint FXPyGroupBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyGroupBox::_getWidthForHeight(FXint h) { return FXGroupBox::getWidthForHeight(h); }

FXint FXPyGroupBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyGroupBox::_getHeightForWidth(FXint w) { return FXGroupBox::getHeightForWidth(w); }

void FXPyGroupBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyGroupBox::_layout() { FXGroupBox::layout(); }

void FXPyGroupBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyGroupBox::_recalc() { FXGroupBox::recalc(); }

FXbool FXPyGroupBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyGroupBox::_isComposite() const { return FXGroupBox::isComposite(); }

void FXPyGroupBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyGroupBox::_move(FXint x,FXint y){ FXGroupBox::move(x,y); }

void FXPyGroupBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyGroupBox::_position(FXint x,FXint y,FXint w,FXint h){ FXGroupBox::position(x,y,w,h); }

FXbool FXPyGroupBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyGroupBox::_canFocus() const { return FXGroupBox::canFocus(); }

void FXPyGroupBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyGroupBox::_setFocus(){ FXGroupBox::setFocus(); }

void FXPyGroupBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyGroupBox::_killFocus(){ FXGroupBox::killFocus(); }

void FXPyGroupBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyGroupBox::_setDefault(FXbool enable){ FXGroupBox::setDefault(enable); }

FXbool FXPyGroupBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyGroupBox::_contains(FXint x,FXint y) const { return FXGroupBox::contains(x,y); }

FXbool FXPyGroupBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyGroupBox::_doesSaveUnder() const { return FXGroupBox::doesSaveUnder(); }

void FXPyGroupBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyGroupBox::_reparent(FXComposite* newparent) { FXGroupBox::reparent(newparent); }

void FXPyGroupBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyGroupBox::_setBackColor(FXColor clr) { FXGroupBox::setBackColor(clr); }

long FXPyCheckButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyCheckButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXCheckButton::onDefault(sender,sel,ptr);
  }

void FXPyCheckButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyCheckButton::_create(){ FXCheckButton::create(); }

void FXPyCheckButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyCheckButton::_destroy(){ FXCheckButton::destroy(); }

void FXPyCheckButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyCheckButton::_detach(){ FXCheckButton::detach(); }

void FXPyCheckButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyCheckButton::_resize(FXint w,FXint h){ FXCheckButton::resize(w,h); }

void FXPyCheckButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyCheckButton::_enable(){ FXCheckButton::enable(); }

void FXPyCheckButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyCheckButton::_disable(){ FXCheckButton::disable(); }

void FXPyCheckButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyCheckButton::_show(){ FXCheckButton::show(); }

void FXPyCheckButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyCheckButton::_hide(){ FXCheckButton::hide(); }

void FXPyCheckButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyCheckButton::_lowerWindow(){ FXCheckButton::lower(); }

FXint FXPyCheckButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyCheckButton::_getDefaultHeight() { return FXCheckButton::getDefaultHeight(); }

FXint FXPyCheckButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyCheckButton::_getDefaultWidth() { return FXCheckButton::getDefaultWidth(); }

FXint FXPyCheckButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyCheckButton::_getWidthForHeight(FXint h) { return FXCheckButton::getWidthForHeight(h); }

FXint FXPyCheckButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyCheckButton::_getHeightForWidth(FXint w) { return FXCheckButton::getHeightForWidth(w); }

void FXPyCheckButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyCheckButton::_layout() { FXCheckButton::layout(); }

void FXPyCheckButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyCheckButton::_recalc() { FXCheckButton::recalc(); }

FXbool FXPyCheckButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyCheckButton::_isComposite() const { return FXCheckButton::isComposite(); }

void FXPyCheckButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyCheckButton::_move(FXint x,FXint y){ FXCheckButton::move(x,y); }

void FXPyCheckButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyCheckButton::_position(FXint x,FXint y,FXint w,FXint h){ FXCheckButton::position(x,y,w,h); }

FXbool FXPyCheckButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyCheckButton::_canFocus() const { return FXCheckButton::canFocus(); }

void FXPyCheckButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyCheckButton::_setFocus(){ FXCheckButton::setFocus(); }

void FXPyCheckButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyCheckButton::_killFocus(){ FXCheckButton::killFocus(); }

void FXPyCheckButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyCheckButton::_setDefault(FXbool enable){ FXCheckButton::setDefault(enable); }

FXbool FXPyCheckButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyCheckButton::_contains(FXint x,FXint y) const { return FXCheckButton::contains(x,y); }

FXbool FXPyCheckButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyCheckButton::_doesSaveUnder() const { return FXCheckButton::doesSaveUnder(); }

void FXPyCheckButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyCheckButton::_reparent(FXComposite* newparent) { FXCheckButton::reparent(newparent); }

void FXPyCheckButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyCheckButton::_setBackColor(FXColor clr) { FXCheckButton::setBackColor(clr); }

long FXPyPicker::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPicker::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPicker::onDefault(sender,sel,ptr);
  }

void FXPyPicker::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPicker::_create(){ FXPicker::create(); }

void FXPyPicker::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPicker::_destroy(){ FXPicker::destroy(); }

void FXPyPicker::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPicker::_detach(){ FXPicker::detach(); }

void FXPyPicker::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPicker::_resize(FXint w,FXint h){ FXPicker::resize(w,h); }

void FXPyPicker::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyPicker::_enable(){ FXPicker::enable(); }

void FXPyPicker::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyPicker::_disable(){ FXPicker::disable(); }

void FXPyPicker::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyPicker::_show(){ FXPicker::show(); }

void FXPyPicker::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyPicker::_hide(){ FXPicker::hide(); }

void FXPyPicker::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyPicker::_lowerWindow(){ FXPicker::lower(); }

FXint FXPyPicker::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyPicker::_getDefaultHeight() { return FXPicker::getDefaultHeight(); }

FXint FXPyPicker::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyPicker::_getDefaultWidth() { return FXPicker::getDefaultWidth(); }

FXint FXPyPicker::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyPicker::_getWidthForHeight(FXint h) { return FXPicker::getWidthForHeight(h); }

FXint FXPyPicker::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyPicker::_getHeightForWidth(FXint w) { return FXPicker::getHeightForWidth(w); }

void FXPyPicker::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyPicker::_layout() { FXPicker::layout(); }

void FXPyPicker::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyPicker::_recalc() { FXPicker::recalc(); }

FXbool FXPyPicker::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyPicker::_isComposite() const { return FXPicker::isComposite(); }

void FXPyPicker::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyPicker::_move(FXint x,FXint y){ FXPicker::move(x,y); }

void FXPyPicker::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyPicker::_position(FXint x,FXint y,FXint w,FXint h){ FXPicker::position(x,y,w,h); }

FXbool FXPyPicker::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyPicker::_canFocus() const { return FXPicker::canFocus(); }

void FXPyPicker::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyPicker::_setFocus(){ FXPicker::setFocus(); }

void FXPyPicker::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyPicker::_killFocus(){ FXPicker::killFocus(); }

void FXPyPicker::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyPicker::_setDefault(FXbool enable){ FXPicker::setDefault(enable); }

FXbool FXPyPicker::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyPicker::_contains(FXint x,FXint y) const { return FXPicker::contains(x,y); }

FXbool FXPyPicker::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyPicker::_doesSaveUnder() const { return FXPicker::doesSaveUnder(); }

void FXPyPicker::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyPicker::_reparent(FXComposite* newparent) { FXPicker::reparent(newparent); }

void FXPyPicker::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyPicker::_setBackColor(FXColor clr) { FXPicker::setBackColor(clr); }

long FXPyRadioButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyRadioButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXRadioButton::onDefault(sender,sel,ptr);
  }

void FXPyRadioButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyRadioButton::_create(){ FXRadioButton::create(); }

void FXPyRadioButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyRadioButton::_destroy(){ FXRadioButton::destroy(); }

void FXPyRadioButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyRadioButton::_detach(){ FXRadioButton::detach(); }

void FXPyRadioButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyRadioButton::_resize(FXint w,FXint h){ FXRadioButton::resize(w,h); }

void FXPyRadioButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyRadioButton::_enable(){ FXRadioButton::enable(); }

void FXPyRadioButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyRadioButton::_disable(){ FXRadioButton::disable(); }

void FXPyRadioButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyRadioButton::_show(){ FXRadioButton::show(); }

void FXPyRadioButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyRadioButton::_hide(){ FXRadioButton::hide(); }

void FXPyRadioButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyRadioButton::_lowerWindow(){ FXRadioButton::lower(); }

FXint FXPyRadioButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyRadioButton::_getDefaultHeight() { return FXRadioButton::getDefaultHeight(); }

FXint FXPyRadioButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyRadioButton::_getDefaultWidth() { return FXRadioButton::getDefaultWidth(); }

FXint FXPyRadioButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyRadioButton::_getWidthForHeight(FXint h) { return FXRadioButton::getWidthForHeight(h); }

FXint FXPyRadioButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyRadioButton::_getHeightForWidth(FXint w) { return FXRadioButton::getHeightForWidth(w); }

void FXPyRadioButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyRadioButton::_layout() { FXRadioButton::layout(); }

void FXPyRadioButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyRadioButton::_recalc() { FXRadioButton::recalc(); }

FXbool FXPyRadioButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyRadioButton::_isComposite() const { return FXRadioButton::isComposite(); }

void FXPyRadioButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyRadioButton::_move(FXint x,FXint y){ FXRadioButton::move(x,y); }

void FXPyRadioButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyRadioButton::_position(FXint x,FXint y,FXint w,FXint h){ FXRadioButton::position(x,y,w,h); }

FXbool FXPyRadioButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyRadioButton::_canFocus() const { return FXRadioButton::canFocus(); }

void FXPyRadioButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyRadioButton::_setFocus(){ FXRadioButton::setFocus(); }

void FXPyRadioButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyRadioButton::_killFocus(){ FXRadioButton::killFocus(); }

void FXPyRadioButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyRadioButton::_setDefault(FXbool enable){ FXRadioButton::setDefault(enable); }

FXbool FXPyRadioButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyRadioButton::_contains(FXint x,FXint y) const { return FXRadioButton::contains(x,y); }

FXbool FXPyRadioButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyRadioButton::_doesSaveUnder() const { return FXRadioButton::doesSaveUnder(); }

void FXPyRadioButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyRadioButton::_reparent(FXComposite* newparent) { FXRadioButton::reparent(newparent); }

void FXPyRadioButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyRadioButton::_setBackColor(FXColor clr) { FXRadioButton::setBackColor(clr); }

long FXPyMenuSeparator::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuSeparator::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuSeparator::onDefault(sender,sel,ptr);
  }

void FXPyMenuSeparator::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuSeparator::_create(){ FXMenuSeparator::create(); }

void FXPyMenuSeparator::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuSeparator::_destroy(){ FXMenuSeparator::destroy(); }

void FXPyMenuSeparator::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuSeparator::_detach(){ FXMenuSeparator::detach(); }

void FXPyMenuSeparator::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuSeparator::_resize(FXint w,FXint h){ FXMenuSeparator::resize(w,h); }

void FXPyMenuSeparator::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuSeparator::_enable(){ FXMenuSeparator::enable(); }

void FXPyMenuSeparator::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuSeparator::_disable(){ FXMenuSeparator::disable(); }

void FXPyMenuSeparator::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuSeparator::_show(){ FXMenuSeparator::show(); }

void FXPyMenuSeparator::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuSeparator::_hide(){ FXMenuSeparator::hide(); }

void FXPyMenuSeparator::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuSeparator::_lowerWindow(){ FXMenuSeparator::lower(); }

FXint FXPyMenuSeparator::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuSeparator::_getDefaultHeight() { return FXMenuSeparator::getDefaultHeight(); }

FXint FXPyMenuSeparator::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuSeparator::_getDefaultWidth() { return FXMenuSeparator::getDefaultWidth(); }

FXint FXPyMenuSeparator::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuSeparator::_getWidthForHeight(FXint h) { return FXMenuSeparator::getWidthForHeight(h); }

FXint FXPyMenuSeparator::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuSeparator::_getHeightForWidth(FXint w) { return FXMenuSeparator::getHeightForWidth(w); }

void FXPyMenuSeparator::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuSeparator::_layout() { FXMenuSeparator::layout(); }

void FXPyMenuSeparator::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuSeparator::_recalc() { FXMenuSeparator::recalc(); }

FXbool FXPyMenuSeparator::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuSeparator::_isComposite() const { return FXMenuSeparator::isComposite(); }

void FXPyMenuSeparator::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuSeparator::_move(FXint x,FXint y){ FXMenuSeparator::move(x,y); }

void FXPyMenuSeparator::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuSeparator::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuSeparator::position(x,y,w,h); }

FXbool FXPyMenuSeparator::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuSeparator::_canFocus() const { return FXMenuSeparator::canFocus(); }

void FXPyMenuSeparator::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuSeparator::_setFocus(){ FXMenuSeparator::setFocus(); }

void FXPyMenuSeparator::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuSeparator::_killFocus(){ FXMenuSeparator::killFocus(); }

void FXPyMenuSeparator::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuSeparator::_setDefault(FXbool enable){ FXMenuSeparator::setDefault(enable); }

FXbool FXPyMenuSeparator::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuSeparator::_contains(FXint x,FXint y) const { return FXMenuSeparator::contains(x,y); }

FXbool FXPyMenuSeparator::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuSeparator::_doesSaveUnder() const { return FXMenuSeparator::doesSaveUnder(); }

void FXPyMenuSeparator::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuSeparator::_reparent(FXComposite* newparent) { FXMenuSeparator::reparent(newparent); }

void FXPyMenuSeparator::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuSeparator::_setBackColor(FXColor clr) { FXMenuSeparator::setBackColor(clr); }

long FXPyMenuCaption::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuCaption::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuCaption::onDefault(sender,sel,ptr);
  }

void FXPyMenuCaption::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuCaption::_create(){ FXMenuCaption::create(); }

void FXPyMenuCaption::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuCaption::_destroy(){ FXMenuCaption::destroy(); }

void FXPyMenuCaption::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuCaption::_detach(){ FXMenuCaption::detach(); }

void FXPyMenuCaption::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuCaption::_resize(FXint w,FXint h){ FXMenuCaption::resize(w,h); }

void FXPyMenuCaption::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuCaption::_enable(){ FXMenuCaption::enable(); }

void FXPyMenuCaption::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuCaption::_disable(){ FXMenuCaption::disable(); }

void FXPyMenuCaption::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuCaption::_show(){ FXMenuCaption::show(); }

void FXPyMenuCaption::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuCaption::_hide(){ FXMenuCaption::hide(); }

void FXPyMenuCaption::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuCaption::_lowerWindow(){ FXMenuCaption::lower(); }

FXint FXPyMenuCaption::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuCaption::_getDefaultHeight() { return FXMenuCaption::getDefaultHeight(); }

FXint FXPyMenuCaption::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuCaption::_getDefaultWidth() { return FXMenuCaption::getDefaultWidth(); }

FXint FXPyMenuCaption::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuCaption::_getWidthForHeight(FXint h) { return FXMenuCaption::getWidthForHeight(h); }

FXint FXPyMenuCaption::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuCaption::_getHeightForWidth(FXint w) { return FXMenuCaption::getHeightForWidth(w); }

void FXPyMenuCaption::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuCaption::_layout() { FXMenuCaption::layout(); }

void FXPyMenuCaption::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuCaption::_recalc() { FXMenuCaption::recalc(); }

FXbool FXPyMenuCaption::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuCaption::_isComposite() const { return FXMenuCaption::isComposite(); }

void FXPyMenuCaption::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuCaption::_move(FXint x,FXint y){ FXMenuCaption::move(x,y); }

void FXPyMenuCaption::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuCaption::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuCaption::position(x,y,w,h); }

FXbool FXPyMenuCaption::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuCaption::_canFocus() const { return FXMenuCaption::canFocus(); }

void FXPyMenuCaption::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuCaption::_setFocus(){ FXMenuCaption::setFocus(); }

void FXPyMenuCaption::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuCaption::_killFocus(){ FXMenuCaption::killFocus(); }

void FXPyMenuCaption::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuCaption::_setDefault(FXbool enable){ FXMenuCaption::setDefault(enable); }

FXbool FXPyMenuCaption::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuCaption::_contains(FXint x,FXint y) const { return FXMenuCaption::contains(x,y); }

FXbool FXPyMenuCaption::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuCaption::_doesSaveUnder() const { return FXMenuCaption::doesSaveUnder(); }

void FXPyMenuCaption::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuCaption::_reparent(FXComposite* newparent) { FXMenuCaption::reparent(newparent); }

void FXPyMenuCaption::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuCaption::_setBackColor(FXColor clr) { FXMenuCaption::setBackColor(clr); }

long FXPyMenuPane::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuPane::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuPane::onDefault(sender,sel,ptr);
  }

void FXPyMenuPane::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuPane::_create(){ FXMenuPane::create(); }

void FXPyMenuPane::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuPane::_destroy(){ FXMenuPane::destroy(); }

void FXPyMenuPane::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuPane::_detach(){ FXMenuPane::detach(); }

void FXPyMenuPane::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuPane::_resize(FXint w,FXint h){ FXMenuPane::resize(w,h); }

void FXPyMenuPane::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuPane::_enable(){ FXMenuPane::enable(); }

void FXPyMenuPane::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuPane::_disable(){ FXMenuPane::disable(); }

void FXPyMenuPane::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuPane::_show(){ FXMenuPane::show(); }

void FXPyMenuPane::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuPane::_hide(){ FXMenuPane::hide(); }

void FXPyMenuPane::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuPane::_lowerWindow(){ FXMenuPane::lower(); }

FXint FXPyMenuPane::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuPane::_getDefaultHeight() { return FXMenuPane::getDefaultHeight(); }

FXint FXPyMenuPane::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuPane::_getDefaultWidth() { return FXMenuPane::getDefaultWidth(); }

FXint FXPyMenuPane::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuPane::_getWidthForHeight(FXint h) { return FXMenuPane::getWidthForHeight(h); }

FXint FXPyMenuPane::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuPane::_getHeightForWidth(FXint w) { return FXMenuPane::getHeightForWidth(w); }

void FXPyMenuPane::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuPane::_layout() { FXMenuPane::layout(); }

void FXPyMenuPane::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuPane::_recalc() { FXMenuPane::recalc(); }

FXbool FXPyMenuPane::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuPane::_isComposite() const { return FXMenuPane::isComposite(); }

void FXPyMenuPane::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuPane::_move(FXint x,FXint y){ FXMenuPane::move(x,y); }

void FXPyMenuPane::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuPane::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuPane::position(x,y,w,h); }

FXbool FXPyMenuPane::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuPane::_canFocus() const { return FXMenuPane::canFocus(); }

void FXPyMenuPane::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuPane::_setFocus(){ FXMenuPane::setFocus(); }

void FXPyMenuPane::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuPane::_killFocus(){ FXMenuPane::killFocus(); }

void FXPyMenuPane::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuPane::_setDefault(FXbool enable){ FXMenuPane::setDefault(enable); }

FXbool FXPyMenuPane::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuPane::_contains(FXint x,FXint y) const { return FXMenuPane::contains(x,y); }

FXbool FXPyMenuPane::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuPane::_doesSaveUnder() const { return FXMenuPane::doesSaveUnder(); }

void FXPyMenuPane::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuPane::_reparent(FXComposite* newparent) { FXMenuPane::reparent(newparent); }

void FXPyMenuPane::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuPane::_setBackColor(FXColor clr) { FXMenuPane::setBackColor(clr); }

void FXPyMenuPane::popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { FXPyCallVoidFunction(this,"popup",grabto,x,y,w,h); }
void FXPyMenuPane::_popup(FXWindow* grabto,FXint x,FXint y,FXint w,FXint h) { FXMenuPane::popup(grabto,x,y,w,h); }

void FXPyMenuPane::popdown() { FXPyCallVoidFunction(this,"popdown"); }
void FXPyMenuPane::_popdown() { FXMenuPane::popdown(); }

long FXPyMenuTitle::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuTitle::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuTitle::onDefault(sender,sel,ptr);
  }

void FXPyMenuTitle::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuTitle::_create(){ FXMenuTitle::create(); }

void FXPyMenuTitle::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuTitle::_destroy(){ FXMenuTitle::destroy(); }

void FXPyMenuTitle::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuTitle::_detach(){ FXMenuTitle::detach(); }

void FXPyMenuTitle::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuTitle::_resize(FXint w,FXint h){ FXMenuTitle::resize(w,h); }

void FXPyMenuTitle::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuTitle::_enable(){ FXMenuTitle::enable(); }

void FXPyMenuTitle::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuTitle::_disable(){ FXMenuTitle::disable(); }

void FXPyMenuTitle::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuTitle::_show(){ FXMenuTitle::show(); }

void FXPyMenuTitle::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuTitle::_hide(){ FXMenuTitle::hide(); }

void FXPyMenuTitle::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuTitle::_lowerWindow(){ FXMenuTitle::lower(); }

FXint FXPyMenuTitle::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuTitle::_getDefaultHeight() { return FXMenuTitle::getDefaultHeight(); }

FXint FXPyMenuTitle::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuTitle::_getDefaultWidth() { return FXMenuTitle::getDefaultWidth(); }

FXint FXPyMenuTitle::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuTitle::_getWidthForHeight(FXint h) { return FXMenuTitle::getWidthForHeight(h); }

FXint FXPyMenuTitle::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuTitle::_getHeightForWidth(FXint w) { return FXMenuTitle::getHeightForWidth(w); }

void FXPyMenuTitle::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuTitle::_layout() { FXMenuTitle::layout(); }

void FXPyMenuTitle::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuTitle::_recalc() { FXMenuTitle::recalc(); }

FXbool FXPyMenuTitle::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuTitle::_isComposite() const { return FXMenuTitle::isComposite(); }

void FXPyMenuTitle::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuTitle::_move(FXint x,FXint y){ FXMenuTitle::move(x,y); }

void FXPyMenuTitle::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuTitle::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuTitle::position(x,y,w,h); }

FXbool FXPyMenuTitle::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuTitle::_canFocus() const { return FXMenuTitle::canFocus(); }

void FXPyMenuTitle::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuTitle::_setFocus(){ FXMenuTitle::setFocus(); }

void FXPyMenuTitle::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuTitle::_killFocus(){ FXMenuTitle::killFocus(); }

void FXPyMenuTitle::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuTitle::_setDefault(FXbool enable){ FXMenuTitle::setDefault(enable); }

FXbool FXPyMenuTitle::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuTitle::_contains(FXint x,FXint y) const { return FXMenuTitle::contains(x,y); }

FXbool FXPyMenuTitle::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuTitle::_doesSaveUnder() const { return FXMenuTitle::doesSaveUnder(); }

void FXPyMenuTitle::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuTitle::_reparent(FXComposite* newparent) { FXMenuTitle::reparent(newparent); }

void FXPyMenuTitle::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuTitle::_setBackColor(FXColor clr) { FXMenuTitle::setBackColor(clr); }

long FXPyMenuCascade::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuCascade::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuCascade::onDefault(sender,sel,ptr);
  }

void FXPyMenuCascade::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuCascade::_create(){ FXMenuCascade::create(); }

void FXPyMenuCascade::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuCascade::_destroy(){ FXMenuCascade::destroy(); }

void FXPyMenuCascade::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuCascade::_detach(){ FXMenuCascade::detach(); }

void FXPyMenuCascade::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuCascade::_resize(FXint w,FXint h){ FXMenuCascade::resize(w,h); }

void FXPyMenuCascade::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuCascade::_enable(){ FXMenuCascade::enable(); }

void FXPyMenuCascade::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuCascade::_disable(){ FXMenuCascade::disable(); }

void FXPyMenuCascade::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuCascade::_show(){ FXMenuCascade::show(); }

void FXPyMenuCascade::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuCascade::_hide(){ FXMenuCascade::hide(); }

void FXPyMenuCascade::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuCascade::_lowerWindow(){ FXMenuCascade::lower(); }

FXint FXPyMenuCascade::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuCascade::_getDefaultHeight() { return FXMenuCascade::getDefaultHeight(); }

FXint FXPyMenuCascade::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuCascade::_getDefaultWidth() { return FXMenuCascade::getDefaultWidth(); }

FXint FXPyMenuCascade::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuCascade::_getWidthForHeight(FXint h) { return FXMenuCascade::getWidthForHeight(h); }

FXint FXPyMenuCascade::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuCascade::_getHeightForWidth(FXint w) { return FXMenuCascade::getHeightForWidth(w); }

void FXPyMenuCascade::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuCascade::_layout() { FXMenuCascade::layout(); }

void FXPyMenuCascade::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuCascade::_recalc() { FXMenuCascade::recalc(); }

FXbool FXPyMenuCascade::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuCascade::_isComposite() const { return FXMenuCascade::isComposite(); }

void FXPyMenuCascade::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuCascade::_move(FXint x,FXint y){ FXMenuCascade::move(x,y); }

void FXPyMenuCascade::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuCascade::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuCascade::position(x,y,w,h); }

FXbool FXPyMenuCascade::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuCascade::_canFocus() const { return FXMenuCascade::canFocus(); }

void FXPyMenuCascade::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuCascade::_setFocus(){ FXMenuCascade::setFocus(); }

void FXPyMenuCascade::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuCascade::_killFocus(){ FXMenuCascade::killFocus(); }

void FXPyMenuCascade::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuCascade::_setDefault(FXbool enable){ FXMenuCascade::setDefault(enable); }

FXbool FXPyMenuCascade::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuCascade::_contains(FXint x,FXint y) const { return FXMenuCascade::contains(x,y); }

FXbool FXPyMenuCascade::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuCascade::_doesSaveUnder() const { return FXMenuCascade::doesSaveUnder(); }

void FXPyMenuCascade::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuCascade::_reparent(FXComposite* newparent) { FXMenuCascade::reparent(newparent); }

void FXPyMenuCascade::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuCascade::_setBackColor(FXColor clr) { FXMenuCascade::setBackColor(clr); }

long FXPyMenuCommand::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuCommand::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuCommand::onDefault(sender,sel,ptr);
  }

void FXPyMenuCommand::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuCommand::_create(){ FXMenuCommand::create(); }

void FXPyMenuCommand::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuCommand::_destroy(){ FXMenuCommand::destroy(); }

void FXPyMenuCommand::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuCommand::_detach(){ FXMenuCommand::detach(); }

void FXPyMenuCommand::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuCommand::_resize(FXint w,FXint h){ FXMenuCommand::resize(w,h); }

void FXPyMenuCommand::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuCommand::_enable(){ FXMenuCommand::enable(); }

void FXPyMenuCommand::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuCommand::_disable(){ FXMenuCommand::disable(); }

void FXPyMenuCommand::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuCommand::_show(){ FXMenuCommand::show(); }

void FXPyMenuCommand::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuCommand::_hide(){ FXMenuCommand::hide(); }

void FXPyMenuCommand::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuCommand::_lowerWindow(){ FXMenuCommand::lower(); }

FXint FXPyMenuCommand::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuCommand::_getDefaultHeight() { return FXMenuCommand::getDefaultHeight(); }

FXint FXPyMenuCommand::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuCommand::_getDefaultWidth() { return FXMenuCommand::getDefaultWidth(); }

FXint FXPyMenuCommand::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuCommand::_getWidthForHeight(FXint h) { return FXMenuCommand::getWidthForHeight(h); }

FXint FXPyMenuCommand::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuCommand::_getHeightForWidth(FXint w) { return FXMenuCommand::getHeightForWidth(w); }

void FXPyMenuCommand::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuCommand::_layout() { FXMenuCommand::layout(); }

void FXPyMenuCommand::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuCommand::_recalc() { FXMenuCommand::recalc(); }

FXbool FXPyMenuCommand::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuCommand::_isComposite() const { return FXMenuCommand::isComposite(); }

void FXPyMenuCommand::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuCommand::_move(FXint x,FXint y){ FXMenuCommand::move(x,y); }

void FXPyMenuCommand::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuCommand::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuCommand::position(x,y,w,h); }

FXbool FXPyMenuCommand::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuCommand::_canFocus() const { return FXMenuCommand::canFocus(); }

void FXPyMenuCommand::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuCommand::_setFocus(){ FXMenuCommand::setFocus(); }

void FXPyMenuCommand::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuCommand::_killFocus(){ FXMenuCommand::killFocus(); }

void FXPyMenuCommand::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuCommand::_setDefault(FXbool enable){ FXMenuCommand::setDefault(enable); }

FXbool FXPyMenuCommand::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuCommand::_contains(FXint x,FXint y) const { return FXMenuCommand::contains(x,y); }

FXbool FXPyMenuCommand::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuCommand::_doesSaveUnder() const { return FXMenuCommand::doesSaveUnder(); }

void FXPyMenuCommand::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuCommand::_reparent(FXComposite* newparent) { FXMenuCommand::reparent(newparent); }

void FXPyMenuCommand::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuCommand::_setBackColor(FXColor clr) { FXMenuCommand::setBackColor(clr); }

long FXPyMenubar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenubar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenubar::onDefault(sender,sel,ptr);
  }

void FXPyMenubar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenubar::_create(){ FXMenubar::create(); }

void FXPyMenubar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenubar::_destroy(){ FXMenubar::destroy(); }

void FXPyMenubar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenubar::_detach(){ FXMenubar::detach(); }

void FXPyMenubar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenubar::_resize(FXint w,FXint h){ FXMenubar::resize(w,h); }

void FXPyMenubar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenubar::_enable(){ FXMenubar::enable(); }

void FXPyMenubar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenubar::_disable(){ FXMenubar::disable(); }

void FXPyMenubar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenubar::_show(){ FXMenubar::show(); }

void FXPyMenubar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenubar::_hide(){ FXMenubar::hide(); }

void FXPyMenubar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenubar::_lowerWindow(){ FXMenubar::lower(); }

FXint FXPyMenubar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenubar::_getDefaultHeight() { return FXMenubar::getDefaultHeight(); }

FXint FXPyMenubar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenubar::_getDefaultWidth() { return FXMenubar::getDefaultWidth(); }

FXint FXPyMenubar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenubar::_getWidthForHeight(FXint h) { return FXMenubar::getWidthForHeight(h); }

FXint FXPyMenubar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenubar::_getHeightForWidth(FXint w) { return FXMenubar::getHeightForWidth(w); }

void FXPyMenubar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenubar::_layout() { FXMenubar::layout(); }

void FXPyMenubar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenubar::_recalc() { FXMenubar::recalc(); }

FXbool FXPyMenubar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenubar::_isComposite() const { return FXMenubar::isComposite(); }

void FXPyMenubar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenubar::_move(FXint x,FXint y){ FXMenubar::move(x,y); }

void FXPyMenubar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenubar::_position(FXint x,FXint y,FXint w,FXint h){ FXMenubar::position(x,y,w,h); }

FXbool FXPyMenubar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenubar::_canFocus() const { return FXMenubar::canFocus(); }

void FXPyMenubar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenubar::_setFocus(){ FXMenubar::setFocus(); }

void FXPyMenubar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenubar::_killFocus(){ FXMenubar::killFocus(); }

void FXPyMenubar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenubar::_setDefault(FXbool enable){ FXMenubar::setDefault(enable); }

FXbool FXPyMenubar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenubar::_contains(FXint x,FXint y) const { return FXMenubar::contains(x,y); }

FXbool FXPyMenubar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenubar::_doesSaveUnder() const { return FXMenubar::doesSaveUnder(); }

void FXPyMenubar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenubar::_reparent(FXComposite* newparent) { FXMenubar::reparent(newparent); }

void FXPyMenubar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenubar::_setBackColor(FXColor clr) { FXMenubar::setBackColor(clr); }

void FXPyMenubar::dock(FXuint side,FXWindow* after){ FXPyCallVoidFunction(this,"dock",side,after); }
void FXPyMenubar::_dock(FXuint side,FXWindow* after){ FXMenubar::dock(side,after); }

void FXPyMenubar::undock(){ FXPyCallVoidFunction(this,"undock"); }
void FXPyMenubar::_undock(){ FXMenubar::undock(); }

long FXPy4Splitter::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPy4Splitter::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FX4Splitter::onDefault(sender,sel,ptr);
  }

void FXPy4Splitter::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPy4Splitter::_create(){ FX4Splitter::create(); }

void FXPy4Splitter::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPy4Splitter::_destroy(){ FX4Splitter::destroy(); }

void FXPy4Splitter::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPy4Splitter::_detach(){ FX4Splitter::detach(); }

void FXPy4Splitter::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPy4Splitter::_resize(FXint w,FXint h){ FX4Splitter::resize(w,h); }

void FXPy4Splitter::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPy4Splitter::_enable(){ FX4Splitter::enable(); }

void FXPy4Splitter::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPy4Splitter::_disable(){ FX4Splitter::disable(); }

void FXPy4Splitter::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPy4Splitter::_show(){ FX4Splitter::show(); }

void FXPy4Splitter::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPy4Splitter::_hide(){ FX4Splitter::hide(); }

void FXPy4Splitter::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPy4Splitter::_lowerWindow(){ FX4Splitter::lower(); }

FXint FXPy4Splitter::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPy4Splitter::_getDefaultHeight() { return FX4Splitter::getDefaultHeight(); }

FXint FXPy4Splitter::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPy4Splitter::_getDefaultWidth() { return FX4Splitter::getDefaultWidth(); }

FXint FXPy4Splitter::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPy4Splitter::_getWidthForHeight(FXint h) { return FX4Splitter::getWidthForHeight(h); }

FXint FXPy4Splitter::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPy4Splitter::_getHeightForWidth(FXint w) { return FX4Splitter::getHeightForWidth(w); }

void FXPy4Splitter::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPy4Splitter::_layout() { FX4Splitter::layout(); }

void FXPy4Splitter::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPy4Splitter::_recalc() { FX4Splitter::recalc(); }

FXbool FXPy4Splitter::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPy4Splitter::_isComposite() const { return FX4Splitter::isComposite(); }

void FXPy4Splitter::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPy4Splitter::_move(FXint x,FXint y){ FX4Splitter::move(x,y); }

void FXPy4Splitter::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPy4Splitter::_position(FXint x,FXint y,FXint w,FXint h){ FX4Splitter::position(x,y,w,h); }

FXbool FXPy4Splitter::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPy4Splitter::_canFocus() const { return FX4Splitter::canFocus(); }

void FXPy4Splitter::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPy4Splitter::_setFocus(){ FX4Splitter::setFocus(); }

void FXPy4Splitter::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPy4Splitter::_killFocus(){ FX4Splitter::killFocus(); }

void FXPy4Splitter::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPy4Splitter::_setDefault(FXbool enable){ FX4Splitter::setDefault(enable); }

FXbool FXPy4Splitter::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPy4Splitter::_contains(FXint x,FXint y) const { return FX4Splitter::contains(x,y); }

FXbool FXPy4Splitter::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPy4Splitter::_doesSaveUnder() const { return FX4Splitter::doesSaveUnder(); }

void FXPy4Splitter::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPy4Splitter::_reparent(FXComposite* newparent) { FX4Splitter::reparent(newparent); }

void FXPy4Splitter::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPy4Splitter::_setBackColor(FXColor clr) { FX4Splitter::setBackColor(clr); }

long FXPyMatrix::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMatrix::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMatrix::onDefault(sender,sel,ptr);
  }

void FXPyMatrix::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMatrix::_create(){ FXMatrix::create(); }

void FXPyMatrix::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMatrix::_destroy(){ FXMatrix::destroy(); }

void FXPyMatrix::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMatrix::_detach(){ FXMatrix::detach(); }

void FXPyMatrix::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMatrix::_resize(FXint w,FXint h){ FXMatrix::resize(w,h); }

void FXPyMatrix::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMatrix::_enable(){ FXMatrix::enable(); }

void FXPyMatrix::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMatrix::_disable(){ FXMatrix::disable(); }

void FXPyMatrix::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMatrix::_show(){ FXMatrix::show(); }

void FXPyMatrix::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMatrix::_hide(){ FXMatrix::hide(); }

void FXPyMatrix::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMatrix::_lowerWindow(){ FXMatrix::lower(); }

FXint FXPyMatrix::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMatrix::_getDefaultHeight() { return FXMatrix::getDefaultHeight(); }

FXint FXPyMatrix::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMatrix::_getDefaultWidth() { return FXMatrix::getDefaultWidth(); }

FXint FXPyMatrix::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMatrix::_getWidthForHeight(FXint h) { return FXMatrix::getWidthForHeight(h); }

FXint FXPyMatrix::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMatrix::_getHeightForWidth(FXint w) { return FXMatrix::getHeightForWidth(w); }

void FXPyMatrix::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMatrix::_layout() { FXMatrix::layout(); }

void FXPyMatrix::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMatrix::_recalc() { FXMatrix::recalc(); }

FXbool FXPyMatrix::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMatrix::_isComposite() const { return FXMatrix::isComposite(); }

void FXPyMatrix::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMatrix::_move(FXint x,FXint y){ FXMatrix::move(x,y); }

void FXPyMatrix::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMatrix::_position(FXint x,FXint y,FXint w,FXint h){ FXMatrix::position(x,y,w,h); }

FXbool FXPyMatrix::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMatrix::_canFocus() const { return FXMatrix::canFocus(); }

void FXPyMatrix::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMatrix::_setFocus(){ FXMatrix::setFocus(); }

void FXPyMatrix::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMatrix::_killFocus(){ FXMatrix::killFocus(); }

void FXPyMatrix::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMatrix::_setDefault(FXbool enable){ FXMatrix::setDefault(enable); }

FXbool FXPyMatrix::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMatrix::_contains(FXint x,FXint y) const { return FXMatrix::contains(x,y); }

FXbool FXPyMatrix::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMatrix::_doesSaveUnder() const { return FXMatrix::doesSaveUnder(); }

void FXPyMatrix::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMatrix::_reparent(FXComposite* newparent) { FXMatrix::reparent(newparent); }

void FXPyMatrix::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMatrix::_setBackColor(FXColor clr) { FXMatrix::setBackColor(clr); }

long FXPyDial::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDial::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDial::onDefault(sender,sel,ptr);
  }

void FXPyDial::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDial::_create(){ FXDial::create(); }

void FXPyDial::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDial::_destroy(){ FXDial::destroy(); }

void FXPyDial::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDial::_detach(){ FXDial::detach(); }

void FXPyDial::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDial::_resize(FXint w,FXint h){ FXDial::resize(w,h); }

void FXPyDial::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDial::_enable(){ FXDial::enable(); }

void FXPyDial::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDial::_disable(){ FXDial::disable(); }

void FXPyDial::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDial::_show(){ FXDial::show(); }

void FXPyDial::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDial::_hide(){ FXDial::hide(); }

void FXPyDial::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDial::_lowerWindow(){ FXDial::lower(); }

FXint FXPyDial::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDial::_getDefaultHeight() { return FXDial::getDefaultHeight(); }

FXint FXPyDial::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDial::_getDefaultWidth() { return FXDial::getDefaultWidth(); }

FXint FXPyDial::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDial::_getWidthForHeight(FXint h) { return FXDial::getWidthForHeight(h); }

FXint FXPyDial::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDial::_getHeightForWidth(FXint w) { return FXDial::getHeightForWidth(w); }

void FXPyDial::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDial::_layout() { FXDial::layout(); }

void FXPyDial::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDial::_recalc() { FXDial::recalc(); }

FXbool FXPyDial::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDial::_isComposite() const { return FXDial::isComposite(); }

void FXPyDial::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDial::_move(FXint x,FXint y){ FXDial::move(x,y); }

void FXPyDial::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDial::_position(FXint x,FXint y,FXint w,FXint h){ FXDial::position(x,y,w,h); }

FXbool FXPyDial::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDial::_canFocus() const { return FXDial::canFocus(); }

void FXPyDial::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDial::_setFocus(){ FXDial::setFocus(); }

void FXPyDial::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDial::_killFocus(){ FXDial::killFocus(); }

void FXPyDial::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDial::_setDefault(FXbool enable){ FXDial::setDefault(enable); }

FXbool FXPyDial::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDial::_contains(FXint x,FXint y) const { return FXDial::contains(x,y); }

FXbool FXPyDial::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDial::_doesSaveUnder() const { return FXDial::doesSaveUnder(); }

void FXPyDial::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDial::_reparent(FXComposite* newparent) { FXDial::reparent(newparent); }

void FXPyDial::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDial::_setBackColor(FXColor clr) { FXDial::setBackColor(clr); }

long FXPyTextField::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTextField::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTextField::onDefault(sender,sel,ptr);
  }

void FXPyTextField::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTextField::_create(){ FXTextField::create(); }

void FXPyTextField::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTextField::_destroy(){ FXTextField::destroy(); }

void FXPyTextField::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTextField::_detach(){ FXTextField::detach(); }

void FXPyTextField::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTextField::_resize(FXint w,FXint h){ FXTextField::resize(w,h); }

void FXPyTextField::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTextField::_enable(){ FXTextField::enable(); }

void FXPyTextField::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTextField::_disable(){ FXTextField::disable(); }

void FXPyTextField::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTextField::_show(){ FXTextField::show(); }

void FXPyTextField::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTextField::_hide(){ FXTextField::hide(); }

void FXPyTextField::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTextField::_lowerWindow(){ FXTextField::lower(); }

FXint FXPyTextField::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTextField::_getDefaultHeight() { return FXTextField::getDefaultHeight(); }

FXint FXPyTextField::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTextField::_getDefaultWidth() { return FXTextField::getDefaultWidth(); }

FXint FXPyTextField::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTextField::_getWidthForHeight(FXint h) { return FXTextField::getWidthForHeight(h); }

FXint FXPyTextField::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTextField::_getHeightForWidth(FXint w) { return FXTextField::getHeightForWidth(w); }

void FXPyTextField::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTextField::_layout() { FXTextField::layout(); }

void FXPyTextField::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTextField::_recalc() { FXTextField::recalc(); }

FXbool FXPyTextField::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTextField::_isComposite() const { return FXTextField::isComposite(); }

void FXPyTextField::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTextField::_move(FXint x,FXint y){ FXTextField::move(x,y); }

void FXPyTextField::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTextField::_position(FXint x,FXint y,FXint w,FXint h){ FXTextField::position(x,y,w,h); }

FXbool FXPyTextField::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTextField::_canFocus() const { return FXTextField::canFocus(); }

void FXPyTextField::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTextField::_setFocus(){ FXTextField::setFocus(); }

void FXPyTextField::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTextField::_killFocus(){ FXTextField::killFocus(); }

void FXPyTextField::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTextField::_setDefault(FXbool enable){ FXTextField::setDefault(enable); }

FXbool FXPyTextField::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTextField::_contains(FXint x,FXint y) const { return FXTextField::contains(x,y); }

FXbool FXPyTextField::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTextField::_doesSaveUnder() const { return FXTextField::doesSaveUnder(); }

void FXPyTextField::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTextField::_reparent(FXComposite* newparent) { FXTextField::reparent(newparent); }

void FXPyTextField::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTextField::_setBackColor(FXColor clr) { FXTextField::setBackColor(clr); }

long FXPySlider::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPySlider::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXSlider::onDefault(sender,sel,ptr);
  }

void FXPySlider::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPySlider::_create(){ FXSlider::create(); }

void FXPySlider::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPySlider::_destroy(){ FXSlider::destroy(); }

void FXPySlider::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPySlider::_detach(){ FXSlider::detach(); }

void FXPySlider::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPySlider::_resize(FXint w,FXint h){ FXSlider::resize(w,h); }

void FXPySlider::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPySlider::_enable(){ FXSlider::enable(); }

void FXPySlider::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPySlider::_disable(){ FXSlider::disable(); }

void FXPySlider::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPySlider::_show(){ FXSlider::show(); }

void FXPySlider::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPySlider::_hide(){ FXSlider::hide(); }

void FXPySlider::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPySlider::_lowerWindow(){ FXSlider::lower(); }

FXint FXPySlider::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPySlider::_getDefaultHeight() { return FXSlider::getDefaultHeight(); }

FXint FXPySlider::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPySlider::_getDefaultWidth() { return FXSlider::getDefaultWidth(); }

FXint FXPySlider::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPySlider::_getWidthForHeight(FXint h) { return FXSlider::getWidthForHeight(h); }

FXint FXPySlider::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPySlider::_getHeightForWidth(FXint w) { return FXSlider::getHeightForWidth(w); }

void FXPySlider::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPySlider::_layout() { FXSlider::layout(); }

void FXPySlider::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPySlider::_recalc() { FXSlider::recalc(); }

FXbool FXPySlider::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPySlider::_isComposite() const { return FXSlider::isComposite(); }

void FXPySlider::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPySlider::_move(FXint x,FXint y){ FXSlider::move(x,y); }

void FXPySlider::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPySlider::_position(FXint x,FXint y,FXint w,FXint h){ FXSlider::position(x,y,w,h); }

FXbool FXPySlider::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPySlider::_canFocus() const { return FXSlider::canFocus(); }

void FXPySlider::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPySlider::_setFocus(){ FXSlider::setFocus(); }

void FXPySlider::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPySlider::_killFocus(){ FXSlider::killFocus(); }

void FXPySlider::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPySlider::_setDefault(FXbool enable){ FXSlider::setDefault(enable); }

FXbool FXPySlider::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPySlider::_contains(FXint x,FXint y) const { return FXSlider::contains(x,y); }

FXbool FXPySlider::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPySlider::_doesSaveUnder() const { return FXSlider::doesSaveUnder(); }

void FXPySlider::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPySlider::_reparent(FXComposite* newparent) { FXSlider::reparent(newparent); }

void FXPySlider::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPySlider::_setBackColor(FXColor clr) { FXSlider::setBackColor(clr); }

long FXPyOption::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyOption::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXOption::onDefault(sender,sel,ptr);
  }

void FXPyOption::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyOption::_create(){ FXOption::create(); }

void FXPyOption::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyOption::_destroy(){ FXOption::destroy(); }

void FXPyOption::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyOption::_detach(){ FXOption::detach(); }

void FXPyOption::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyOption::_resize(FXint w,FXint h){ FXOption::resize(w,h); }

void FXPyOption::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyOption::_enable(){ FXOption::enable(); }

void FXPyOption::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyOption::_disable(){ FXOption::disable(); }

void FXPyOption::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyOption::_show(){ FXOption::show(); }

void FXPyOption::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyOption::_hide(){ FXOption::hide(); }

void FXPyOption::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyOption::_lowerWindow(){ FXOption::lower(); }

FXint FXPyOption::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyOption::_getDefaultHeight() { return FXOption::getDefaultHeight(); }

FXint FXPyOption::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyOption::_getDefaultWidth() { return FXOption::getDefaultWidth(); }

FXint FXPyOption::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyOption::_getWidthForHeight(FXint h) { return FXOption::getWidthForHeight(h); }

FXint FXPyOption::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyOption::_getHeightForWidth(FXint w) { return FXOption::getHeightForWidth(w); }

void FXPyOption::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyOption::_layout() { FXOption::layout(); }

void FXPyOption::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyOption::_recalc() { FXOption::recalc(); }

FXbool FXPyOption::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyOption::_isComposite() const { return FXOption::isComposite(); }

void FXPyOption::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyOption::_move(FXint x,FXint y){ FXOption::move(x,y); }

void FXPyOption::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyOption::_position(FXint x,FXint y,FXint w,FXint h){ FXOption::position(x,y,w,h); }

FXbool FXPyOption::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyOption::_canFocus() const { return FXOption::canFocus(); }

void FXPyOption::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyOption::_setFocus(){ FXOption::setFocus(); }

void FXPyOption::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyOption::_killFocus(){ FXOption::killFocus(); }

void FXPyOption::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyOption::_setDefault(FXbool enable){ FXOption::setDefault(enable); }

FXbool FXPyOption::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyOption::_contains(FXint x,FXint y) const { return FXOption::contains(x,y); }

FXbool FXPyOption::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyOption::_doesSaveUnder() const { return FXOption::doesSaveUnder(); }

void FXPyOption::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyOption::_reparent(FXComposite* newparent) { FXOption::reparent(newparent); }

void FXPyOption::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyOption::_setBackColor(FXColor clr) { FXOption::setBackColor(clr); }

long FXPyOptionMenu::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyOptionMenu::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXOptionMenu::onDefault(sender,sel,ptr);
  }

void FXPyOptionMenu::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyOptionMenu::_create(){ FXOptionMenu::create(); }

void FXPyOptionMenu::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyOptionMenu::_destroy(){ FXOptionMenu::destroy(); }

void FXPyOptionMenu::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyOptionMenu::_detach(){ FXOptionMenu::detach(); }

void FXPyOptionMenu::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyOptionMenu::_resize(FXint w,FXint h){ FXOptionMenu::resize(w,h); }

void FXPyOptionMenu::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyOptionMenu::_enable(){ FXOptionMenu::enable(); }

void FXPyOptionMenu::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyOptionMenu::_disable(){ FXOptionMenu::disable(); }

void FXPyOptionMenu::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyOptionMenu::_show(){ FXOptionMenu::show(); }

void FXPyOptionMenu::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyOptionMenu::_hide(){ FXOptionMenu::hide(); }

void FXPyOptionMenu::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyOptionMenu::_lowerWindow(){ FXOptionMenu::lower(); }

FXint FXPyOptionMenu::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyOptionMenu::_getDefaultHeight() { return FXOptionMenu::getDefaultHeight(); }

FXint FXPyOptionMenu::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyOptionMenu::_getDefaultWidth() { return FXOptionMenu::getDefaultWidth(); }

FXint FXPyOptionMenu::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyOptionMenu::_getWidthForHeight(FXint h) { return FXOptionMenu::getWidthForHeight(h); }

FXint FXPyOptionMenu::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyOptionMenu::_getHeightForWidth(FXint w) { return FXOptionMenu::getHeightForWidth(w); }

void FXPyOptionMenu::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyOptionMenu::_layout() { FXOptionMenu::layout(); }

void FXPyOptionMenu::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyOptionMenu::_recalc() { FXOptionMenu::recalc(); }

FXbool FXPyOptionMenu::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyOptionMenu::_isComposite() const { return FXOptionMenu::isComposite(); }

void FXPyOptionMenu::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyOptionMenu::_move(FXint x,FXint y){ FXOptionMenu::move(x,y); }

void FXPyOptionMenu::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyOptionMenu::_position(FXint x,FXint y,FXint w,FXint h){ FXOptionMenu::position(x,y,w,h); }

FXbool FXPyOptionMenu::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyOptionMenu::_canFocus() const { return FXOptionMenu::canFocus(); }

void FXPyOptionMenu::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyOptionMenu::_setFocus(){ FXOptionMenu::setFocus(); }

void FXPyOptionMenu::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyOptionMenu::_killFocus(){ FXOptionMenu::killFocus(); }

void FXPyOptionMenu::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyOptionMenu::_setDefault(FXbool enable){ FXOptionMenu::setDefault(enable); }

FXbool FXPyOptionMenu::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyOptionMenu::_contains(FXint x,FXint y) const { return FXOptionMenu::contains(x,y); }

FXbool FXPyOptionMenu::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyOptionMenu::_doesSaveUnder() const { return FXOptionMenu::doesSaveUnder(); }

void FXPyOptionMenu::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyOptionMenu::_reparent(FXComposite* newparent) { FXOptionMenu::reparent(newparent); }

void FXPyOptionMenu::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyOptionMenu::_setBackColor(FXColor clr) { FXOptionMenu::setBackColor(clr); }

long FXPyMenuButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMenuButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMenuButton::onDefault(sender,sel,ptr);
  }

void FXPyMenuButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMenuButton::_create(){ FXMenuButton::create(); }

void FXPyMenuButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMenuButton::_destroy(){ FXMenuButton::destroy(); }

void FXPyMenuButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMenuButton::_detach(){ FXMenuButton::detach(); }

void FXPyMenuButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMenuButton::_resize(FXint w,FXint h){ FXMenuButton::resize(w,h); }

void FXPyMenuButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMenuButton::_enable(){ FXMenuButton::enable(); }

void FXPyMenuButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMenuButton::_disable(){ FXMenuButton::disable(); }

void FXPyMenuButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMenuButton::_show(){ FXMenuButton::show(); }

void FXPyMenuButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMenuButton::_hide(){ FXMenuButton::hide(); }

void FXPyMenuButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMenuButton::_lowerWindow(){ FXMenuButton::lower(); }

FXint FXPyMenuButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMenuButton::_getDefaultHeight() { return FXMenuButton::getDefaultHeight(); }

FXint FXPyMenuButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMenuButton::_getDefaultWidth() { return FXMenuButton::getDefaultWidth(); }

FXint FXPyMenuButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMenuButton::_getWidthForHeight(FXint h) { return FXMenuButton::getWidthForHeight(h); }

FXint FXPyMenuButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMenuButton::_getHeightForWidth(FXint w) { return FXMenuButton::getHeightForWidth(w); }

void FXPyMenuButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMenuButton::_layout() { FXMenuButton::layout(); }

void FXPyMenuButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMenuButton::_recalc() { FXMenuButton::recalc(); }

FXbool FXPyMenuButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMenuButton::_isComposite() const { return FXMenuButton::isComposite(); }

void FXPyMenuButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMenuButton::_move(FXint x,FXint y){ FXMenuButton::move(x,y); }

void FXPyMenuButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMenuButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMenuButton::position(x,y,w,h); }

FXbool FXPyMenuButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMenuButton::_canFocus() const { return FXMenuButton::canFocus(); }

void FXPyMenuButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMenuButton::_setFocus(){ FXMenuButton::setFocus(); }

void FXPyMenuButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMenuButton::_killFocus(){ FXMenuButton::killFocus(); }

void FXPyMenuButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMenuButton::_setDefault(FXbool enable){ FXMenuButton::setDefault(enable); }

FXbool FXPyMenuButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMenuButton::_contains(FXint x,FXint y) const { return FXMenuButton::contains(x,y); }

FXbool FXPyMenuButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMenuButton::_doesSaveUnder() const { return FXMenuButton::doesSaveUnder(); }

void FXPyMenuButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMenuButton::_reparent(FXComposite* newparent) { FXMenuButton::reparent(newparent); }

void FXPyMenuButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMenuButton::_setBackColor(FXColor clr) { FXMenuButton::setBackColor(clr); }

long FXPySplitter::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPySplitter::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXSplitter::onDefault(sender,sel,ptr);
  }

void FXPySplitter::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPySplitter::_create(){ FXSplitter::create(); }

void FXPySplitter::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPySplitter::_destroy(){ FXSplitter::destroy(); }

void FXPySplitter::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPySplitter::_detach(){ FXSplitter::detach(); }

void FXPySplitter::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPySplitter::_resize(FXint w,FXint h){ FXSplitter::resize(w,h); }

void FXPySplitter::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPySplitter::_enable(){ FXSplitter::enable(); }

void FXPySplitter::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPySplitter::_disable(){ FXSplitter::disable(); }

void FXPySplitter::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPySplitter::_show(){ FXSplitter::show(); }

void FXPySplitter::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPySplitter::_hide(){ FXSplitter::hide(); }

void FXPySplitter::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPySplitter::_lowerWindow(){ FXSplitter::lower(); }

FXint FXPySplitter::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPySplitter::_getDefaultHeight() { return FXSplitter::getDefaultHeight(); }

FXint FXPySplitter::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPySplitter::_getDefaultWidth() { return FXSplitter::getDefaultWidth(); }

FXint FXPySplitter::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPySplitter::_getWidthForHeight(FXint h) { return FXSplitter::getWidthForHeight(h); }

FXint FXPySplitter::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPySplitter::_getHeightForWidth(FXint w) { return FXSplitter::getHeightForWidth(w); }

void FXPySplitter::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPySplitter::_layout() { FXSplitter::layout(); }

void FXPySplitter::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPySplitter::_recalc() { FXSplitter::recalc(); }

FXbool FXPySplitter::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPySplitter::_isComposite() const { return FXSplitter::isComposite(); }

void FXPySplitter::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPySplitter::_move(FXint x,FXint y){ FXSplitter::move(x,y); }

void FXPySplitter::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPySplitter::_position(FXint x,FXint y,FXint w,FXint h){ FXSplitter::position(x,y,w,h); }

FXbool FXPySplitter::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPySplitter::_canFocus() const { return FXSplitter::canFocus(); }

void FXPySplitter::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPySplitter::_setFocus(){ FXSplitter::setFocus(); }

void FXPySplitter::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPySplitter::_killFocus(){ FXSplitter::killFocus(); }

void FXPySplitter::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPySplitter::_setDefault(FXbool enable){ FXSplitter::setDefault(enable); }

FXbool FXPySplitter::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPySplitter::_contains(FXint x,FXint y) const { return FXSplitter::contains(x,y); }

FXbool FXPySplitter::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPySplitter::_doesSaveUnder() const { return FXSplitter::doesSaveUnder(); }

void FXPySplitter::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPySplitter::_reparent(FXComposite* newparent) { FXSplitter::reparent(newparent); }

void FXPySplitter::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPySplitter::_setBackColor(FXColor clr) { FXSplitter::setBackColor(clr); }

long FXPyScrollArea::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyScrollArea::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXScrollArea::onDefault(sender,sel,ptr);
  }

void FXPyScrollArea::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyScrollArea::_create(){ FXScrollArea::create(); }

void FXPyScrollArea::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyScrollArea::_destroy(){ FXScrollArea::destroy(); }

void FXPyScrollArea::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyScrollArea::_detach(){ FXScrollArea::detach(); }

void FXPyScrollArea::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyScrollArea::_resize(FXint w,FXint h){ FXScrollArea::resize(w,h); }

void FXPyScrollArea::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyScrollArea::_enable(){ FXScrollArea::enable(); }

void FXPyScrollArea::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyScrollArea::_disable(){ FXScrollArea::disable(); }

void FXPyScrollArea::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyScrollArea::_show(){ FXScrollArea::show(); }

void FXPyScrollArea::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyScrollArea::_hide(){ FXScrollArea::hide(); }

void FXPyScrollArea::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyScrollArea::_lowerWindow(){ FXScrollArea::lower(); }

FXint FXPyScrollArea::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyScrollArea::_getDefaultHeight() { return FXScrollArea::getDefaultHeight(); }

FXint FXPyScrollArea::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyScrollArea::_getDefaultWidth() { return FXScrollArea::getDefaultWidth(); }

FXint FXPyScrollArea::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyScrollArea::_getWidthForHeight(FXint h) { return FXScrollArea::getWidthForHeight(h); }

FXint FXPyScrollArea::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyScrollArea::_getHeightForWidth(FXint w) { return FXScrollArea::getHeightForWidth(w); }

void FXPyScrollArea::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyScrollArea::_layout() { FXScrollArea::layout(); }

void FXPyScrollArea::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyScrollArea::_recalc() { FXScrollArea::recalc(); }

FXbool FXPyScrollArea::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyScrollArea::_isComposite() const { return FXScrollArea::isComposite(); }

void FXPyScrollArea::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyScrollArea::_move(FXint x,FXint y){ FXScrollArea::move(x,y); }

void FXPyScrollArea::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyScrollArea::_position(FXint x,FXint y,FXint w,FXint h){ FXScrollArea::position(x,y,w,h); }

FXbool FXPyScrollArea::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyScrollArea::_canFocus() const { return FXScrollArea::canFocus(); }

void FXPyScrollArea::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyScrollArea::_setFocus(){ FXScrollArea::setFocus(); }

void FXPyScrollArea::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyScrollArea::_killFocus(){ FXScrollArea::killFocus(); }

void FXPyScrollArea::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyScrollArea::_setDefault(FXbool enable){ FXScrollArea::setDefault(enable); }

FXbool FXPyScrollArea::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyScrollArea::_contains(FXint x,FXint y) const { return FXScrollArea::contains(x,y); }

FXbool FXPyScrollArea::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyScrollArea::_doesSaveUnder() const { return FXScrollArea::doesSaveUnder(); }

void FXPyScrollArea::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyScrollArea::_reparent(FXComposite* newparent) { FXScrollArea::reparent(newparent); }

void FXPyScrollArea::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyScrollArea::_setBackColor(FXColor clr) { FXScrollArea::setBackColor(clr); }

FXint FXPyScrollArea::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyScrollArea::_getContentWidth() { return FXScrollArea::getContentWidth(); }

FXint FXPyScrollArea::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyScrollArea::_getContentHeight() { return FXScrollArea::getContentHeight(); }

FXint FXPyScrollArea::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyScrollArea::_getViewportWidth() { return FXScrollArea::getViewportWidth(); }

FXint FXPyScrollArea::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyScrollArea::_getViewportHeight() { return FXScrollArea::getViewportHeight(); }

void FXPyScrollArea::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyScrollArea::_moveContents(FXint x,FXint y) { FXScrollArea::moveContents(x,y); }

long FXPyScrollWindow::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyScrollWindow::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXScrollWindow::onDefault(sender,sel,ptr);
  }

void FXPyScrollWindow::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyScrollWindow::_create(){ FXScrollWindow::create(); }

void FXPyScrollWindow::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyScrollWindow::_destroy(){ FXScrollWindow::destroy(); }

void FXPyScrollWindow::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyScrollWindow::_detach(){ FXScrollWindow::detach(); }

void FXPyScrollWindow::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyScrollWindow::_resize(FXint w,FXint h){ FXScrollWindow::resize(w,h); }

void FXPyScrollWindow::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyScrollWindow::_enable(){ FXScrollWindow::enable(); }

void FXPyScrollWindow::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyScrollWindow::_disable(){ FXScrollWindow::disable(); }

void FXPyScrollWindow::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyScrollWindow::_show(){ FXScrollWindow::show(); }

void FXPyScrollWindow::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyScrollWindow::_hide(){ FXScrollWindow::hide(); }

void FXPyScrollWindow::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyScrollWindow::_lowerWindow(){ FXScrollWindow::lower(); }

FXint FXPyScrollWindow::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyScrollWindow::_getDefaultHeight() { return FXScrollWindow::getDefaultHeight(); }

FXint FXPyScrollWindow::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyScrollWindow::_getDefaultWidth() { return FXScrollWindow::getDefaultWidth(); }

FXint FXPyScrollWindow::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyScrollWindow::_getWidthForHeight(FXint h) { return FXScrollWindow::getWidthForHeight(h); }

FXint FXPyScrollWindow::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyScrollWindow::_getHeightForWidth(FXint w) { return FXScrollWindow::getHeightForWidth(w); }

void FXPyScrollWindow::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyScrollWindow::_layout() { FXScrollWindow::layout(); }

void FXPyScrollWindow::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyScrollWindow::_recalc() { FXScrollWindow::recalc(); }

FXbool FXPyScrollWindow::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyScrollWindow::_isComposite() const { return FXScrollWindow::isComposite(); }

void FXPyScrollWindow::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyScrollWindow::_move(FXint x,FXint y){ FXScrollWindow::move(x,y); }

void FXPyScrollWindow::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyScrollWindow::_position(FXint x,FXint y,FXint w,FXint h){ FXScrollWindow::position(x,y,w,h); }

FXbool FXPyScrollWindow::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyScrollWindow::_canFocus() const { return FXScrollWindow::canFocus(); }

void FXPyScrollWindow::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyScrollWindow::_setFocus(){ FXScrollWindow::setFocus(); }

void FXPyScrollWindow::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyScrollWindow::_killFocus(){ FXScrollWindow::killFocus(); }

void FXPyScrollWindow::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyScrollWindow::_setDefault(FXbool enable){ FXScrollWindow::setDefault(enable); }

FXbool FXPyScrollWindow::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyScrollWindow::_contains(FXint x,FXint y) const { return FXScrollWindow::contains(x,y); }

FXbool FXPyScrollWindow::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyScrollWindow::_doesSaveUnder() const { return FXScrollWindow::doesSaveUnder(); }

void FXPyScrollWindow::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyScrollWindow::_reparent(FXComposite* newparent) { FXScrollWindow::reparent(newparent); }

void FXPyScrollWindow::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyScrollWindow::_setBackColor(FXColor clr) { FXScrollWindow::setBackColor(clr); }

FXint FXPyScrollWindow::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyScrollWindow::_getContentWidth() { return FXScrollWindow::getContentWidth(); }

FXint FXPyScrollWindow::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyScrollWindow::_getContentHeight() { return FXScrollWindow::getContentHeight(); }

FXint FXPyScrollWindow::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyScrollWindow::_getViewportWidth() { return FXScrollWindow::getViewportWidth(); }

FXint FXPyScrollWindow::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyScrollWindow::_getViewportHeight() { return FXScrollWindow::getViewportHeight(); }

void FXPyScrollWindow::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyScrollWindow::_moveContents(FXint x,FXint y) { FXScrollWindow::moveContents(x,y); }

long FXPyTreeItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTreeItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTreeItem::onDefault(sender,sel,ptr);
  }

void FXPyTreeItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyTreeItem::_setText(const FXString& text) { FXTreeItem::setText(text); }

void FXPyTreeItem::setOpenIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setOpenIcon",icn); }
void FXPyTreeItem::_setOpenIcon(FXIcon *icn) { FXTreeItem::setOpenIcon(icn); }

void FXPyTreeItem::setClosedIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setClosedIcon",icn); }
void FXPyTreeItem::_setClosedIcon(FXIcon *icn) { FXTreeItem::setClosedIcon(icn); }

void FXPyTreeItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyTreeItem::_setFocus(FXbool focus) { FXTreeItem::setFocus(focus); }

void FXPyTreeItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyTreeItem::_setSelected(FXbool selected) { FXTreeItem::setSelected(selected); }

void FXPyTreeItem::setOpened(FXbool opened) { FXPyCallVoidFunction(this,"setOpened",opened); }
void FXPyTreeItem::_setOpened(FXbool opened) { FXTreeItem::setOpened(opened); }

void FXPyTreeItem::setExpanded(FXbool expanded) { FXPyCallVoidFunction(this,"setExpanded",expanded); }
void FXPyTreeItem::_setExpanded(FXbool expanded) { FXTreeItem::setExpanded(expanded); }

void FXPyTreeItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyTreeItem::_setEnabled(FXbool enabled) { FXTreeItem::setEnabled(enabled); }

void FXPyTreeItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyTreeItem::_setDraggable(FXbool draggable) { FXTreeItem::setDraggable(draggable); }

void FXPyTreeItem::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }
void FXPyTreeItem::_setIconOwned(FXuint owned) { FXTreeItem::setIconOwned(owned); }

FXint FXPyTreeItem::getWidth(const FXTreeList* list) const { return ::_getWidth(this, list); }
FXint FXPyTreeItem::_getWidth(const FXTreeList* list) const { return FXTreeItem::getWidth(list); }

FXint FXPyTreeItem::getHeight(const FXTreeList* list) const { return ::_getHeight(this, list); }
FXint FXPyTreeItem::_getHeight(const FXTreeList* list) const { return FXTreeItem::getHeight(list); }

void FXPyTreeItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTreeItem::_create(){ FXTreeItem::create(); }

void FXPyTreeItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTreeItem::_detach(){ FXTreeItem::detach(); }

void FXPyTreeItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTreeItem::_destroy(){ FXTreeItem::destroy(); }

long FXPyTreeList::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTreeList::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTreeList::onDefault(sender,sel,ptr);
  }

void FXPyTreeList::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTreeList::_create(){ FXTreeList::create(); }

void FXPyTreeList::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTreeList::_destroy(){ FXTreeList::destroy(); }

void FXPyTreeList::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTreeList::_detach(){ FXTreeList::detach(); }

void FXPyTreeList::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTreeList::_resize(FXint w,FXint h){ FXTreeList::resize(w,h); }

void FXPyTreeList::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTreeList::_enable(){ FXTreeList::enable(); }

void FXPyTreeList::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTreeList::_disable(){ FXTreeList::disable(); }

void FXPyTreeList::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTreeList::_show(){ FXTreeList::show(); }

void FXPyTreeList::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTreeList::_hide(){ FXTreeList::hide(); }

void FXPyTreeList::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTreeList::_lowerWindow(){ FXTreeList::lower(); }

FXint FXPyTreeList::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTreeList::_getDefaultHeight() { return FXTreeList::getDefaultHeight(); }

FXint FXPyTreeList::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTreeList::_getDefaultWidth() { return FXTreeList::getDefaultWidth(); }

FXint FXPyTreeList::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTreeList::_getWidthForHeight(FXint h) { return FXTreeList::getWidthForHeight(h); }

FXint FXPyTreeList::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTreeList::_getHeightForWidth(FXint w) { return FXTreeList::getHeightForWidth(w); }

void FXPyTreeList::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTreeList::_layout() { FXTreeList::layout(); }

void FXPyTreeList::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTreeList::_recalc() { FXTreeList::recalc(); }

FXbool FXPyTreeList::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTreeList::_isComposite() const { return FXTreeList::isComposite(); }

void FXPyTreeList::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTreeList::_move(FXint x,FXint y){ FXTreeList::move(x,y); }

void FXPyTreeList::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTreeList::_position(FXint x,FXint y,FXint w,FXint h){ FXTreeList::position(x,y,w,h); }

FXbool FXPyTreeList::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTreeList::_canFocus() const { return FXTreeList::canFocus(); }

void FXPyTreeList::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTreeList::_setFocus(){ FXTreeList::setFocus(); }

void FXPyTreeList::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTreeList::_killFocus(){ FXTreeList::killFocus(); }

void FXPyTreeList::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTreeList::_setDefault(FXbool enable){ FXTreeList::setDefault(enable); }

FXbool FXPyTreeList::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTreeList::_contains(FXint x,FXint y) const { return FXTreeList::contains(x,y); }

FXbool FXPyTreeList::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTreeList::_doesSaveUnder() const { return FXTreeList::doesSaveUnder(); }

void FXPyTreeList::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTreeList::_reparent(FXComposite* newparent) { FXTreeList::reparent(newparent); }

void FXPyTreeList::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTreeList::_setBackColor(FXColor clr) { FXTreeList::setBackColor(clr); }

FXint FXPyTreeList::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyTreeList::_getContentWidth() { return FXTreeList::getContentWidth(); }

FXint FXPyTreeList::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyTreeList::_getContentHeight() { return FXTreeList::getContentHeight(); }

FXint FXPyTreeList::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyTreeList::_getViewportWidth() { return FXTreeList::getViewportWidth(); }

FXint FXPyTreeList::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyTreeList::_getViewportHeight() { return FXTreeList::getViewportHeight(); }

void FXPyTreeList::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyTreeList::_moveContents(FXint x,FXint y) { FXTreeList::moveContents(x,y); }

long FXPyTreeListBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTreeListBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTreeListBox::onDefault(sender,sel,ptr);
  }

void FXPyTreeListBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTreeListBox::_create(){ FXTreeListBox::create(); }

void FXPyTreeListBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTreeListBox::_destroy(){ FXTreeListBox::destroy(); }

void FXPyTreeListBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTreeListBox::_detach(){ FXTreeListBox::detach(); }

void FXPyTreeListBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTreeListBox::_resize(FXint w,FXint h){ FXTreeListBox::resize(w,h); }

void FXPyTreeListBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTreeListBox::_enable(){ FXTreeListBox::enable(); }

void FXPyTreeListBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTreeListBox::_disable(){ FXTreeListBox::disable(); }

void FXPyTreeListBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTreeListBox::_show(){ FXTreeListBox::show(); }

void FXPyTreeListBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTreeListBox::_hide(){ FXTreeListBox::hide(); }

void FXPyTreeListBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTreeListBox::_lowerWindow(){ FXTreeListBox::lower(); }

FXint FXPyTreeListBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTreeListBox::_getDefaultHeight() { return FXTreeListBox::getDefaultHeight(); }

FXint FXPyTreeListBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTreeListBox::_getDefaultWidth() { return FXTreeListBox::getDefaultWidth(); }

FXint FXPyTreeListBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTreeListBox::_getWidthForHeight(FXint h) { return FXTreeListBox::getWidthForHeight(h); }

FXint FXPyTreeListBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTreeListBox::_getHeightForWidth(FXint w) { return FXTreeListBox::getHeightForWidth(w); }

void FXPyTreeListBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTreeListBox::_layout() { FXTreeListBox::layout(); }

void FXPyTreeListBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTreeListBox::_recalc() { FXTreeListBox::recalc(); }

FXbool FXPyTreeListBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTreeListBox::_isComposite() const { return FXTreeListBox::isComposite(); }

void FXPyTreeListBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTreeListBox::_move(FXint x,FXint y){ FXTreeListBox::move(x,y); }

void FXPyTreeListBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTreeListBox::_position(FXint x,FXint y,FXint w,FXint h){ FXTreeListBox::position(x,y,w,h); }

FXbool FXPyTreeListBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTreeListBox::_canFocus() const { return FXTreeListBox::canFocus(); }

void FXPyTreeListBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTreeListBox::_setFocus(){ FXTreeListBox::setFocus(); }

void FXPyTreeListBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTreeListBox::_killFocus(){ FXTreeListBox::killFocus(); }

void FXPyTreeListBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTreeListBox::_setDefault(FXbool enable){ FXTreeListBox::setDefault(enable); }

FXbool FXPyTreeListBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTreeListBox::_contains(FXint x,FXint y) const { return FXTreeListBox::contains(x,y); }

FXbool FXPyTreeListBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTreeListBox::_doesSaveUnder() const { return FXTreeListBox::doesSaveUnder(); }

void FXPyTreeListBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTreeListBox::_reparent(FXComposite* newparent) { FXTreeListBox::reparent(newparent); }

void FXPyTreeListBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTreeListBox::_setBackColor(FXColor clr) { FXTreeListBox::setBackColor(clr); }

long FXPyToolbarTab::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyToolbarTab::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXToolbarTab::onDefault(sender,sel,ptr);
  }

void FXPyToolbarTab::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyToolbarTab::_create(){ FXToolbarTab::create(); }

void FXPyToolbarTab::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyToolbarTab::_destroy(){ FXToolbarTab::destroy(); }

void FXPyToolbarTab::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyToolbarTab::_detach(){ FXToolbarTab::detach(); }

void FXPyToolbarTab::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyToolbarTab::_resize(FXint w,FXint h){ FXToolbarTab::resize(w,h); }

void FXPyToolbarTab::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyToolbarTab::_enable(){ FXToolbarTab::enable(); }

void FXPyToolbarTab::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyToolbarTab::_disable(){ FXToolbarTab::disable(); }

void FXPyToolbarTab::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyToolbarTab::_show(){ FXToolbarTab::show(); }

void FXPyToolbarTab::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyToolbarTab::_hide(){ FXToolbarTab::hide(); }

void FXPyToolbarTab::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyToolbarTab::_lowerWindow(){ FXToolbarTab::lower(); }

FXint FXPyToolbarTab::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyToolbarTab::_getDefaultHeight() { return FXToolbarTab::getDefaultHeight(); }

FXint FXPyToolbarTab::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyToolbarTab::_getDefaultWidth() { return FXToolbarTab::getDefaultWidth(); }

FXint FXPyToolbarTab::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyToolbarTab::_getWidthForHeight(FXint h) { return FXToolbarTab::getWidthForHeight(h); }

FXint FXPyToolbarTab::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyToolbarTab::_getHeightForWidth(FXint w) { return FXToolbarTab::getHeightForWidth(w); }

void FXPyToolbarTab::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyToolbarTab::_layout() { FXToolbarTab::layout(); }

void FXPyToolbarTab::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyToolbarTab::_recalc() { FXToolbarTab::recalc(); }

FXbool FXPyToolbarTab::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyToolbarTab::_isComposite() const { return FXToolbarTab::isComposite(); }

void FXPyToolbarTab::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyToolbarTab::_move(FXint x,FXint y){ FXToolbarTab::move(x,y); }

void FXPyToolbarTab::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyToolbarTab::_position(FXint x,FXint y,FXint w,FXint h){ FXToolbarTab::position(x,y,w,h); }

FXbool FXPyToolbarTab::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyToolbarTab::_canFocus() const { return FXToolbarTab::canFocus(); }

void FXPyToolbarTab::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyToolbarTab::_setFocus(){ FXToolbarTab::setFocus(); }

void FXPyToolbarTab::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyToolbarTab::_killFocus(){ FXToolbarTab::killFocus(); }

void FXPyToolbarTab::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyToolbarTab::_setDefault(FXbool enable){ FXToolbarTab::setDefault(enable); }

FXbool FXPyToolbarTab::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyToolbarTab::_contains(FXint x,FXint y) const { return FXToolbarTab::contains(x,y); }

FXbool FXPyToolbarTab::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyToolbarTab::_doesSaveUnder() const { return FXToolbarTab::doesSaveUnder(); }

void FXPyToolbarTab::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyToolbarTab::_reparent(FXComposite* newparent) { FXToolbarTab::reparent(newparent); }

void FXPyToolbarTab::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyToolbarTab::_setBackColor(FXColor clr) { FXToolbarTab::setBackColor(clr); }

long FXPyTabBar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTabBar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTabBar::onDefault(sender,sel,ptr);
  }

void FXPyTabBar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTabBar::_create(){ FXTabBar::create(); }

void FXPyTabBar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTabBar::_destroy(){ FXTabBar::destroy(); }

void FXPyTabBar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTabBar::_detach(){ FXTabBar::detach(); }

void FXPyTabBar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTabBar::_resize(FXint w,FXint h){ FXTabBar::resize(w,h); }

void FXPyTabBar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTabBar::_enable(){ FXTabBar::enable(); }

void FXPyTabBar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTabBar::_disable(){ FXTabBar::disable(); }

void FXPyTabBar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTabBar::_show(){ FXTabBar::show(); }

void FXPyTabBar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTabBar::_hide(){ FXTabBar::hide(); }

void FXPyTabBar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTabBar::_lowerWindow(){ FXTabBar::lower(); }

FXint FXPyTabBar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTabBar::_getDefaultHeight() { return FXTabBar::getDefaultHeight(); }

FXint FXPyTabBar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTabBar::_getDefaultWidth() { return FXTabBar::getDefaultWidth(); }

FXint FXPyTabBar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTabBar::_getWidthForHeight(FXint h) { return FXTabBar::getWidthForHeight(h); }

FXint FXPyTabBar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTabBar::_getHeightForWidth(FXint w) { return FXTabBar::getHeightForWidth(w); }

void FXPyTabBar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTabBar::_layout() { FXTabBar::layout(); }

void FXPyTabBar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTabBar::_recalc() { FXTabBar::recalc(); }

FXbool FXPyTabBar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTabBar::_isComposite() const { return FXTabBar::isComposite(); }

void FXPyTabBar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTabBar::_move(FXint x,FXint y){ FXTabBar::move(x,y); }

void FXPyTabBar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTabBar::_position(FXint x,FXint y,FXint w,FXint h){ FXTabBar::position(x,y,w,h); }

FXbool FXPyTabBar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTabBar::_canFocus() const { return FXTabBar::canFocus(); }

void FXPyTabBar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTabBar::_setFocus(){ FXTabBar::setFocus(); }

void FXPyTabBar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTabBar::_killFocus(){ FXTabBar::killFocus(); }

void FXPyTabBar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTabBar::_setDefault(FXbool enable){ FXTabBar::setDefault(enable); }

FXbool FXPyTabBar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTabBar::_contains(FXint x,FXint y) const { return FXTabBar::contains(x,y); }

FXbool FXPyTabBar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTabBar::_doesSaveUnder() const { return FXTabBar::doesSaveUnder(); }

void FXPyTabBar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTabBar::_reparent(FXComposite* newparent) { FXTabBar::reparent(newparent); }

void FXPyTabBar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTabBar::_setBackColor(FXColor clr) { FXTabBar::setBackColor(clr); }

void FXPyTabBar::setCurrent(FXint panel,FXbool notify) { FXPyCallVoidFunction(this,"setCurrent",panel,notify); }
void FXPyTabBar::_setCurrent(FXint panel,FXbool notify) { FXTabBar::setCurrent(panel,notify); }

long FXPyTabItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTabItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTabItem::onDefault(sender,sel,ptr);
  }

void FXPyTabItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTabItem::_create(){ FXTabItem::create(); }

void FXPyTabItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTabItem::_destroy(){ FXTabItem::destroy(); }

void FXPyTabItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTabItem::_detach(){ FXTabItem::detach(); }

void FXPyTabItem::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTabItem::_resize(FXint w,FXint h){ FXTabItem::resize(w,h); }

void FXPyTabItem::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTabItem::_enable(){ FXTabItem::enable(); }

void FXPyTabItem::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTabItem::_disable(){ FXTabItem::disable(); }

void FXPyTabItem::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTabItem::_show(){ FXTabItem::show(); }

void FXPyTabItem::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTabItem::_hide(){ FXTabItem::hide(); }

void FXPyTabItem::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTabItem::_lowerWindow(){ FXTabItem::lower(); }

FXint FXPyTabItem::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTabItem::_getDefaultHeight() { return FXTabItem::getDefaultHeight(); }

FXint FXPyTabItem::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTabItem::_getDefaultWidth() { return FXTabItem::getDefaultWidth(); }

FXint FXPyTabItem::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTabItem::_getWidthForHeight(FXint h) { return FXTabItem::getWidthForHeight(h); }

FXint FXPyTabItem::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTabItem::_getHeightForWidth(FXint w) { return FXTabItem::getHeightForWidth(w); }

void FXPyTabItem::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTabItem::_layout() { FXTabItem::layout(); }

void FXPyTabItem::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTabItem::_recalc() { FXTabItem::recalc(); }

FXbool FXPyTabItem::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTabItem::_isComposite() const { return FXTabItem::isComposite(); }

void FXPyTabItem::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTabItem::_move(FXint x,FXint y){ FXTabItem::move(x,y); }

void FXPyTabItem::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTabItem::_position(FXint x,FXint y,FXint w,FXint h){ FXTabItem::position(x,y,w,h); }

FXbool FXPyTabItem::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTabItem::_canFocus() const { return FXTabItem::canFocus(); }

void FXPyTabItem::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTabItem::_setFocus(){ FXTabItem::setFocus(); }

void FXPyTabItem::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTabItem::_killFocus(){ FXTabItem::killFocus(); }

void FXPyTabItem::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTabItem::_setDefault(FXbool enable){ FXTabItem::setDefault(enable); }

FXbool FXPyTabItem::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTabItem::_contains(FXint x,FXint y) const { return FXTabItem::contains(x,y); }

FXbool FXPyTabItem::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTabItem::_doesSaveUnder() const { return FXTabItem::doesSaveUnder(); }

void FXPyTabItem::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTabItem::_reparent(FXComposite* newparent) { FXTabItem::reparent(newparent); }

void FXPyTabItem::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTabItem::_setBackColor(FXColor clr) { FXTabItem::setBackColor(clr); }

long FXPyTabBook::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTabBook::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTabBook::onDefault(sender,sel,ptr);
  }

void FXPyTabBook::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTabBook::_create(){ FXTabBook::create(); }

void FXPyTabBook::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTabBook::_destroy(){ FXTabBook::destroy(); }

void FXPyTabBook::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTabBook::_detach(){ FXTabBook::detach(); }

void FXPyTabBook::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTabBook::_resize(FXint w,FXint h){ FXTabBook::resize(w,h); }

void FXPyTabBook::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTabBook::_enable(){ FXTabBook::enable(); }

void FXPyTabBook::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTabBook::_disable(){ FXTabBook::disable(); }

void FXPyTabBook::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTabBook::_show(){ FXTabBook::show(); }

void FXPyTabBook::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTabBook::_hide(){ FXTabBook::hide(); }

void FXPyTabBook::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTabBook::_lowerWindow(){ FXTabBook::lower(); }

FXint FXPyTabBook::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTabBook::_getDefaultHeight() { return FXTabBook::getDefaultHeight(); }

FXint FXPyTabBook::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTabBook::_getDefaultWidth() { return FXTabBook::getDefaultWidth(); }

FXint FXPyTabBook::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTabBook::_getWidthForHeight(FXint h) { return FXTabBook::getWidthForHeight(h); }

FXint FXPyTabBook::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTabBook::_getHeightForWidth(FXint w) { return FXTabBook::getHeightForWidth(w); }

void FXPyTabBook::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTabBook::_layout() { FXTabBook::layout(); }

void FXPyTabBook::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTabBook::_recalc() { FXTabBook::recalc(); }

FXbool FXPyTabBook::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTabBook::_isComposite() const { return FXTabBook::isComposite(); }

void FXPyTabBook::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTabBook::_move(FXint x,FXint y){ FXTabBook::move(x,y); }

void FXPyTabBook::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTabBook::_position(FXint x,FXint y,FXint w,FXint h){ FXTabBook::position(x,y,w,h); }

FXbool FXPyTabBook::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTabBook::_canFocus() const { return FXTabBook::canFocus(); }

void FXPyTabBook::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTabBook::_setFocus(){ FXTabBook::setFocus(); }

void FXPyTabBook::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTabBook::_killFocus(){ FXTabBook::killFocus(); }

void FXPyTabBook::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTabBook::_setDefault(FXbool enable){ FXTabBook::setDefault(enable); }

FXbool FXPyTabBook::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTabBook::_contains(FXint x,FXint y) const { return FXTabBook::contains(x,y); }

FXbool FXPyTabBook::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTabBook::_doesSaveUnder() const { return FXTabBook::doesSaveUnder(); }

void FXPyTabBook::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTabBook::_reparent(FXComposite* newparent) { FXTabBook::reparent(newparent); }

void FXPyTabBook::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTabBook::_setBackColor(FXColor clr) { FXTabBook::setBackColor(clr); }

void FXPyTabBook::setCurrent(FXint panel,FXbool notify) { FXPyCallVoidFunction(this,"setCurrent",panel,notify); }
void FXPyTabBook::_setCurrent(FXint panel,FXbool notify) { FXTabBook::setCurrent(panel,notify); }

long FXPyScrollbar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyScrollbar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXScrollbar::onDefault(sender,sel,ptr);
  }

void FXPyScrollbar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyScrollbar::_create(){ FXScrollbar::create(); }

void FXPyScrollbar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyScrollbar::_destroy(){ FXScrollbar::destroy(); }

void FXPyScrollbar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyScrollbar::_detach(){ FXScrollbar::detach(); }

void FXPyScrollbar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyScrollbar::_resize(FXint w,FXint h){ FXScrollbar::resize(w,h); }

void FXPyScrollbar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyScrollbar::_enable(){ FXScrollbar::enable(); }

void FXPyScrollbar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyScrollbar::_disable(){ FXScrollbar::disable(); }

void FXPyScrollbar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyScrollbar::_show(){ FXScrollbar::show(); }

void FXPyScrollbar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyScrollbar::_hide(){ FXScrollbar::hide(); }

void FXPyScrollbar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyScrollbar::_lowerWindow(){ FXScrollbar::lower(); }

FXint FXPyScrollbar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyScrollbar::_getDefaultHeight() { return FXScrollbar::getDefaultHeight(); }

FXint FXPyScrollbar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyScrollbar::_getDefaultWidth() { return FXScrollbar::getDefaultWidth(); }

FXint FXPyScrollbar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyScrollbar::_getWidthForHeight(FXint h) { return FXScrollbar::getWidthForHeight(h); }

FXint FXPyScrollbar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyScrollbar::_getHeightForWidth(FXint w) { return FXScrollbar::getHeightForWidth(w); }

void FXPyScrollbar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyScrollbar::_layout() { FXScrollbar::layout(); }

void FXPyScrollbar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyScrollbar::_recalc() { FXScrollbar::recalc(); }

FXbool FXPyScrollbar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyScrollbar::_isComposite() const { return FXScrollbar::isComposite(); }

void FXPyScrollbar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyScrollbar::_move(FXint x,FXint y){ FXScrollbar::move(x,y); }

void FXPyScrollbar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyScrollbar::_position(FXint x,FXint y,FXint w,FXint h){ FXScrollbar::position(x,y,w,h); }

FXbool FXPyScrollbar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyScrollbar::_canFocus() const { return FXScrollbar::canFocus(); }

void FXPyScrollbar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyScrollbar::_setFocus(){ FXScrollbar::setFocus(); }

void FXPyScrollbar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyScrollbar::_killFocus(){ FXScrollbar::killFocus(); }

void FXPyScrollbar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyScrollbar::_setDefault(FXbool enable){ FXScrollbar::setDefault(enable); }

FXbool FXPyScrollbar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyScrollbar::_contains(FXint x,FXint y) const { return FXScrollbar::contains(x,y); }

FXbool FXPyScrollbar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyScrollbar::_doesSaveUnder() const { return FXScrollbar::doesSaveUnder(); }

void FXPyScrollbar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyScrollbar::_reparent(FXComposite* newparent) { FXScrollbar::reparent(newparent); }

void FXPyScrollbar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyScrollbar::_setBackColor(FXColor clr) { FXScrollbar::setBackColor(clr); }

long FXPyScrollCorner::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyScrollCorner::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXScrollCorner::onDefault(sender,sel,ptr);
  }

void FXPyScrollCorner::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyScrollCorner::_create(){ FXScrollCorner::create(); }

void FXPyScrollCorner::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyScrollCorner::_destroy(){ FXScrollCorner::destroy(); }

void FXPyScrollCorner::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyScrollCorner::_detach(){ FXScrollCorner::detach(); }

void FXPyScrollCorner::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyScrollCorner::_resize(FXint w,FXint h){ FXScrollCorner::resize(w,h); }

void FXPyScrollCorner::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyScrollCorner::_enable(){ FXScrollCorner::enable(); }

void FXPyScrollCorner::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyScrollCorner::_disable(){ FXScrollCorner::disable(); }

void FXPyScrollCorner::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyScrollCorner::_show(){ FXScrollCorner::show(); }

void FXPyScrollCorner::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyScrollCorner::_hide(){ FXScrollCorner::hide(); }

void FXPyScrollCorner::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyScrollCorner::_lowerWindow(){ FXScrollCorner::lower(); }

FXint FXPyScrollCorner::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyScrollCorner::_getDefaultHeight() { return FXScrollCorner::getDefaultHeight(); }

FXint FXPyScrollCorner::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyScrollCorner::_getDefaultWidth() { return FXScrollCorner::getDefaultWidth(); }

FXint FXPyScrollCorner::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyScrollCorner::_getWidthForHeight(FXint h) { return FXScrollCorner::getWidthForHeight(h); }

FXint FXPyScrollCorner::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyScrollCorner::_getHeightForWidth(FXint w) { return FXScrollCorner::getHeightForWidth(w); }

void FXPyScrollCorner::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyScrollCorner::_layout() { FXScrollCorner::layout(); }

void FXPyScrollCorner::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyScrollCorner::_recalc() { FXScrollCorner::recalc(); }

FXbool FXPyScrollCorner::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyScrollCorner::_isComposite() const { return FXScrollCorner::isComposite(); }

void FXPyScrollCorner::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyScrollCorner::_move(FXint x,FXint y){ FXScrollCorner::move(x,y); }

void FXPyScrollCorner::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyScrollCorner::_position(FXint x,FXint y,FXint w,FXint h){ FXScrollCorner::position(x,y,w,h); }

FXbool FXPyScrollCorner::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyScrollCorner::_canFocus() const { return FXScrollCorner::canFocus(); }

void FXPyScrollCorner::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyScrollCorner::_setFocus(){ FXScrollCorner::setFocus(); }

void FXPyScrollCorner::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyScrollCorner::_killFocus(){ FXScrollCorner::killFocus(); }

void FXPyScrollCorner::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyScrollCorner::_setDefault(FXbool enable){ FXScrollCorner::setDefault(enable); }

FXbool FXPyScrollCorner::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyScrollCorner::_contains(FXint x,FXint y) const { return FXScrollCorner::contains(x,y); }

FXbool FXPyScrollCorner::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyScrollCorner::_doesSaveUnder() const { return FXScrollCorner::doesSaveUnder(); }

void FXPyScrollCorner::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyScrollCorner::_reparent(FXComposite* newparent) { FXScrollCorner::reparent(newparent); }

void FXPyScrollCorner::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyScrollCorner::_setBackColor(FXColor clr) { FXScrollCorner::setBackColor(clr); }

long FXPyProgressBar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyProgressBar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXProgressBar::onDefault(sender,sel,ptr);
  }

void FXPyProgressBar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyProgressBar::_create(){ FXProgressBar::create(); }

void FXPyProgressBar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyProgressBar::_destroy(){ FXProgressBar::destroy(); }

void FXPyProgressBar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyProgressBar::_detach(){ FXProgressBar::detach(); }

void FXPyProgressBar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyProgressBar::_resize(FXint w,FXint h){ FXProgressBar::resize(w,h); }

void FXPyProgressBar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyProgressBar::_enable(){ FXProgressBar::enable(); }

void FXPyProgressBar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyProgressBar::_disable(){ FXProgressBar::disable(); }

void FXPyProgressBar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyProgressBar::_show(){ FXProgressBar::show(); }

void FXPyProgressBar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyProgressBar::_hide(){ FXProgressBar::hide(); }

void FXPyProgressBar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyProgressBar::_lowerWindow(){ FXProgressBar::lower(); }

FXint FXPyProgressBar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyProgressBar::_getDefaultHeight() { return FXProgressBar::getDefaultHeight(); }

FXint FXPyProgressBar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyProgressBar::_getDefaultWidth() { return FXProgressBar::getDefaultWidth(); }

FXint FXPyProgressBar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyProgressBar::_getWidthForHeight(FXint h) { return FXProgressBar::getWidthForHeight(h); }

FXint FXPyProgressBar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyProgressBar::_getHeightForWidth(FXint w) { return FXProgressBar::getHeightForWidth(w); }

void FXPyProgressBar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyProgressBar::_layout() { FXProgressBar::layout(); }

void FXPyProgressBar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyProgressBar::_recalc() { FXProgressBar::recalc(); }

FXbool FXPyProgressBar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyProgressBar::_isComposite() const { return FXProgressBar::isComposite(); }

void FXPyProgressBar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyProgressBar::_move(FXint x,FXint y){ FXProgressBar::move(x,y); }

void FXPyProgressBar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyProgressBar::_position(FXint x,FXint y,FXint w,FXint h){ FXProgressBar::position(x,y,w,h); }

FXbool FXPyProgressBar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyProgressBar::_canFocus() const { return FXProgressBar::canFocus(); }

void FXPyProgressBar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyProgressBar::_setFocus(){ FXProgressBar::setFocus(); }

void FXPyProgressBar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyProgressBar::_killFocus(){ FXProgressBar::killFocus(); }

void FXPyProgressBar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyProgressBar::_setDefault(FXbool enable){ FXProgressBar::setDefault(enable); }

FXbool FXPyProgressBar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyProgressBar::_contains(FXint x,FXint y) const { return FXProgressBar::contains(x,y); }

FXbool FXPyProgressBar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyProgressBar::_doesSaveUnder() const { return FXProgressBar::doesSaveUnder(); }

void FXPyProgressBar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyProgressBar::_reparent(FXComposite* newparent) { FXProgressBar::reparent(newparent); }

void FXPyProgressBar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyProgressBar::_setBackColor(FXColor clr) { FXProgressBar::setBackColor(clr); }

long FXPyPrintDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPrintDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPrintDialog::onDefault(sender,sel,ptr);
  }

void FXPyPrintDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPrintDialog::_create(){ FXPrintDialog::create(); }

void FXPyPrintDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPrintDialog::_destroy(){ FXPrintDialog::destroy(); }

void FXPyPrintDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPrintDialog::_detach(){ FXPrintDialog::detach(); }

void FXPyPrintDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPrintDialog::_resize(FXint w,FXint h){ FXPrintDialog::resize(w,h); }

void FXPyPrintDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyPrintDialog::_enable(){ FXPrintDialog::enable(); }

void FXPyPrintDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyPrintDialog::_disable(){ FXPrintDialog::disable(); }

void FXPyPrintDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyPrintDialog::_show(){ FXPrintDialog::show(); }

void FXPyPrintDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyPrintDialog::_hide(){ FXPrintDialog::hide(); }

void FXPyPrintDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyPrintDialog::_lowerWindow(){ FXPrintDialog::lower(); }

FXint FXPyPrintDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyPrintDialog::_getDefaultHeight() { return FXPrintDialog::getDefaultHeight(); }

FXint FXPyPrintDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyPrintDialog::_getDefaultWidth() { return FXPrintDialog::getDefaultWidth(); }

FXint FXPyPrintDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyPrintDialog::_getWidthForHeight(FXint h) { return FXPrintDialog::getWidthForHeight(h); }

FXint FXPyPrintDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyPrintDialog::_getHeightForWidth(FXint w) { return FXPrintDialog::getHeightForWidth(w); }

void FXPyPrintDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyPrintDialog::_layout() { FXPrintDialog::layout(); }

void FXPyPrintDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyPrintDialog::_recalc() { FXPrintDialog::recalc(); }

FXbool FXPyPrintDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyPrintDialog::_isComposite() const { return FXPrintDialog::isComposite(); }

void FXPyPrintDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyPrintDialog::_move(FXint x,FXint y){ FXPrintDialog::move(x,y); }

void FXPyPrintDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyPrintDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXPrintDialog::position(x,y,w,h); }

FXbool FXPyPrintDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyPrintDialog::_canFocus() const { return FXPrintDialog::canFocus(); }

void FXPyPrintDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyPrintDialog::_setFocus(){ FXPrintDialog::setFocus(); }

void FXPyPrintDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyPrintDialog::_killFocus(){ FXPrintDialog::killFocus(); }

void FXPyPrintDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyPrintDialog::_setDefault(FXbool enable){ FXPrintDialog::setDefault(enable); }

FXbool FXPyPrintDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyPrintDialog::_contains(FXint x,FXint y) const { return FXPrintDialog::contains(x,y); }

FXbool FXPyPrintDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyPrintDialog::_doesSaveUnder() const { return FXPrintDialog::doesSaveUnder(); }

void FXPyPrintDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyPrintDialog::_reparent(FXComposite* newparent) { FXPrintDialog::reparent(newparent); }

void FXPyPrintDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyPrintDialog::_setBackColor(FXColor clr) { FXPrintDialog::setBackColor(clr); }

void FXPyPrintDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyPrintDialog::_iconify() { FXPrintDialog::iconify(); }

void FXPyPrintDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyPrintDialog::_deiconify() { FXPrintDialog::deiconify(); }

void FXPyPrintDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyPrintDialog::_show(FXuint placement) { FXPrintDialog::show(placement); }

long FXPyVisual::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyVisual::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXVisual::onDefault(sender,sel,ptr);
  }

void FXPyVisual::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyVisual::_create(){ FXVisual::create(); }

void FXPyVisual::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyVisual::_destroy(){ FXVisual::destroy(); }

void FXPyVisual::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyVisual::_detach(){ FXVisual::detach(); }

long FXPyBMPImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyBMPImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXBMPImage::onDefault(sender,sel,ptr);
  }

void FXPyBMPImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyBMPImage::_create(){ FXBMPImage::create(); }

void FXPyBMPImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyBMPImage::_destroy(){ FXBMPImage::destroy(); }

void FXPyBMPImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyBMPImage::_detach(){ FXBMPImage::detach(); }

void FXPyBMPImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyBMPImage::_resize(FXint w,FXint h){ FXBMPImage::resize(w,h); }

void FXPyBMPImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyBMPImage::_restore() { FXBMPImage::restore(); }

void FXPyBMPImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyBMPImage::_render() { FXBMPImage::render(); }

void FXPyBMPImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyBMPImage::_scale(FXint w,FXint h) { FXBMPImage::scale(w,h); }

void FXPyBMPImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyBMPImage::_mirror(FXbool horizontal,FXbool vertical) { FXBMPImage::mirror(horizontal,vertical); }

void FXPyBMPImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyBMPImage::_rotate(FXint degrees) { FXBMPImage::rotate(degrees); }

void FXPyBMPImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyBMPImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXBMPImage::crop(x,y,w,h); }

void FXPyBMPImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyBMPImage::_savePixels(FXStream& store) const { FXBMPImage::savePixels(store); }

void FXPyBMPImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyBMPImage::_loadPixels(FXStream& store) { FXBMPImage::loadPixels(store); }

long FXPyGIFImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGIFImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGIFImage::onDefault(sender,sel,ptr);
  }

void FXPyGIFImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGIFImage::_create(){ FXGIFImage::create(); }

void FXPyGIFImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGIFImage::_destroy(){ FXGIFImage::destroy(); }

void FXPyGIFImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGIFImage::_detach(){ FXGIFImage::detach(); }

void FXPyGIFImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyGIFImage::_resize(FXint w,FXint h){ FXGIFImage::resize(w,h); }

void FXPyGIFImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyGIFImage::_restore() { FXGIFImage::restore(); }

void FXPyGIFImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyGIFImage::_render() { FXGIFImage::render(); }

void FXPyGIFImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyGIFImage::_scale(FXint w,FXint h) { FXGIFImage::scale(w,h); }

void FXPyGIFImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyGIFImage::_mirror(FXbool horizontal,FXbool vertical) { FXGIFImage::mirror(horizontal,vertical); }

void FXPyGIFImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyGIFImage::_rotate(FXint degrees) { FXGIFImage::rotate(degrees); }

void FXPyGIFImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyGIFImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXGIFImage::crop(x,y,w,h); }

void FXPyGIFImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyGIFImage::_savePixels(FXStream& store) const { FXGIFImage::savePixels(store); }

void FXPyGIFImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyGIFImage::_loadPixels(FXStream& store) { FXGIFImage::loadPixels(store); }

long FXPyPNGImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPNGImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPNGImage::onDefault(sender,sel,ptr);
  }

void FXPyPNGImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPNGImage::_create(){ FXPNGImage::create(); }

void FXPyPNGImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPNGImage::_destroy(){ FXPNGImage::destroy(); }

void FXPyPNGImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPNGImage::_detach(){ FXPNGImage::detach(); }

void FXPyPNGImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPNGImage::_resize(FXint w,FXint h){ FXPNGImage::resize(w,h); }

void FXPyPNGImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyPNGImage::_restore() { FXPNGImage::restore(); }

void FXPyPNGImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyPNGImage::_render() { FXPNGImage::render(); }

void FXPyPNGImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyPNGImage::_scale(FXint w,FXint h) { FXPNGImage::scale(w,h); }

void FXPyPNGImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyPNGImage::_mirror(FXbool horizontal,FXbool vertical) { FXPNGImage::mirror(horizontal,vertical); }

void FXPyPNGImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyPNGImage::_rotate(FXint degrees) { FXPNGImage::rotate(degrees); }

void FXPyPNGImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyPNGImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXPNGImage::crop(x,y,w,h); }

void FXPyPNGImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyPNGImage::_savePixels(FXStream& store) const { FXPNGImage::savePixels(store); }

void FXPyPNGImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyPNGImage::_loadPixels(FXStream& store) { FXPNGImage::loadPixels(store); }

long FXPyJPGImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyJPGImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXJPGImage::onDefault(sender,sel,ptr);
  }

void FXPyJPGImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyJPGImage::_create(){ FXJPGImage::create(); }

void FXPyJPGImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyJPGImage::_destroy(){ FXJPGImage::destroy(); }

void FXPyJPGImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyJPGImage::_detach(){ FXJPGImage::detach(); }

void FXPyJPGImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyJPGImage::_resize(FXint w,FXint h){ FXJPGImage::resize(w,h); }

void FXPyJPGImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyJPGImage::_restore() { FXJPGImage::restore(); }

void FXPyJPGImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyJPGImage::_render() { FXJPGImage::render(); }

void FXPyJPGImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyJPGImage::_scale(FXint w,FXint h) { FXJPGImage::scale(w,h); }

void FXPyJPGImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyJPGImage::_mirror(FXbool horizontal,FXbool vertical) { FXJPGImage::mirror(horizontal,vertical); }

void FXPyJPGImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyJPGImage::_rotate(FXint degrees) { FXJPGImage::rotate(degrees); }

void FXPyJPGImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyJPGImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXJPGImage::crop(x,y,w,h); }

void FXPyJPGImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyJPGImage::_savePixels(FXStream& store) const { FXJPGImage::savePixels(store); }

void FXPyJPGImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyJPGImage::_loadPixels(FXStream& store) { FXJPGImage::loadPixels(store); }

long FXPyColorWell::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyColorWell::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXColorWell::onDefault(sender,sel,ptr);
  }

void FXPyColorWell::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyColorWell::_create(){ FXColorWell::create(); }

void FXPyColorWell::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyColorWell::_destroy(){ FXColorWell::destroy(); }

void FXPyColorWell::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyColorWell::_detach(){ FXColorWell::detach(); }

void FXPyColorWell::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyColorWell::_resize(FXint w,FXint h){ FXColorWell::resize(w,h); }

void FXPyColorWell::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyColorWell::_enable(){ FXColorWell::enable(); }

void FXPyColorWell::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyColorWell::_disable(){ FXColorWell::disable(); }

void FXPyColorWell::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyColorWell::_show(){ FXColorWell::show(); }

void FXPyColorWell::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyColorWell::_hide(){ FXColorWell::hide(); }

void FXPyColorWell::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyColorWell::_lowerWindow(){ FXColorWell::lower(); }

FXint FXPyColorWell::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyColorWell::_getDefaultHeight() { return FXColorWell::getDefaultHeight(); }

FXint FXPyColorWell::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyColorWell::_getDefaultWidth() { return FXColorWell::getDefaultWidth(); }

FXint FXPyColorWell::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyColorWell::_getWidthForHeight(FXint h) { return FXColorWell::getWidthForHeight(h); }

FXint FXPyColorWell::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyColorWell::_getHeightForWidth(FXint w) { return FXColorWell::getHeightForWidth(w); }

void FXPyColorWell::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyColorWell::_layout() { FXColorWell::layout(); }

void FXPyColorWell::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyColorWell::_recalc() { FXColorWell::recalc(); }

FXbool FXPyColorWell::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyColorWell::_isComposite() const { return FXColorWell::isComposite(); }

void FXPyColorWell::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyColorWell::_move(FXint x,FXint y){ FXColorWell::move(x,y); }

void FXPyColorWell::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyColorWell::_position(FXint x,FXint y,FXint w,FXint h){ FXColorWell::position(x,y,w,h); }

FXbool FXPyColorWell::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyColorWell::_canFocus() const { return FXColorWell::canFocus(); }

void FXPyColorWell::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyColorWell::_setFocus(){ FXColorWell::setFocus(); }

void FXPyColorWell::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyColorWell::_killFocus(){ FXColorWell::killFocus(); }

void FXPyColorWell::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyColorWell::_setDefault(FXbool enable){ FXColorWell::setDefault(enable); }

FXbool FXPyColorWell::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyColorWell::_contains(FXint x,FXint y) const { return FXColorWell::contains(x,y); }

FXbool FXPyColorWell::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyColorWell::_doesSaveUnder() const { return FXColorWell::doesSaveUnder(); }

void FXPyColorWell::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyColorWell::_reparent(FXComposite* newparent) { FXColorWell::reparent(newparent); }

void FXPyColorWell::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyColorWell::_setBackColor(FXColor clr) { FXColorWell::setBackColor(clr); }

long FXPyColorWheel::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyColorWheel::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXColorWheel::onDefault(sender,sel,ptr);
  }

void FXPyColorWheel::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyColorWheel::_create(){ FXColorWheel::create(); }

void FXPyColorWheel::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyColorWheel::_destroy(){ FXColorWheel::destroy(); }

void FXPyColorWheel::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyColorWheel::_detach(){ FXColorWheel::detach(); }

void FXPyColorWheel::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyColorWheel::_resize(FXint w,FXint h){ FXColorWheel::resize(w,h); }

void FXPyColorWheel::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyColorWheel::_enable(){ FXColorWheel::enable(); }

void FXPyColorWheel::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyColorWheel::_disable(){ FXColorWheel::disable(); }

void FXPyColorWheel::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyColorWheel::_show(){ FXColorWheel::show(); }

void FXPyColorWheel::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyColorWheel::_hide(){ FXColorWheel::hide(); }

void FXPyColorWheel::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyColorWheel::_lowerWindow(){ FXColorWheel::lower(); }

FXint FXPyColorWheel::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyColorWheel::_getDefaultHeight() { return FXColorWheel::getDefaultHeight(); }

FXint FXPyColorWheel::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyColorWheel::_getDefaultWidth() { return FXColorWheel::getDefaultWidth(); }

FXint FXPyColorWheel::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyColorWheel::_getWidthForHeight(FXint h) { return FXColorWheel::getWidthForHeight(h); }

FXint FXPyColorWheel::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyColorWheel::_getHeightForWidth(FXint w) { return FXColorWheel::getHeightForWidth(w); }

void FXPyColorWheel::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyColorWheel::_layout() { FXColorWheel::layout(); }

void FXPyColorWheel::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyColorWheel::_recalc() { FXColorWheel::recalc(); }

FXbool FXPyColorWheel::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyColorWheel::_isComposite() const { return FXColorWheel::isComposite(); }

void FXPyColorWheel::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyColorWheel::_move(FXint x,FXint y){ FXColorWheel::move(x,y); }

void FXPyColorWheel::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyColorWheel::_position(FXint x,FXint y,FXint w,FXint h){ FXColorWheel::position(x,y,w,h); }

FXbool FXPyColorWheel::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyColorWheel::_canFocus() const { return FXColorWheel::canFocus(); }

void FXPyColorWheel::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyColorWheel::_setFocus(){ FXColorWheel::setFocus(); }

void FXPyColorWheel::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyColorWheel::_killFocus(){ FXColorWheel::killFocus(); }

void FXPyColorWheel::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyColorWheel::_setDefault(FXbool enable){ FXColorWheel::setDefault(enable); }

FXbool FXPyColorWheel::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyColorWheel::_contains(FXint x,FXint y) const { return FXColorWheel::contains(x,y); }

FXbool FXPyColorWheel::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyColorWheel::_doesSaveUnder() const { return FXColorWheel::doesSaveUnder(); }

void FXPyColorWheel::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyColorWheel::_reparent(FXComposite* newparent) { FXColorWheel::reparent(newparent); }

void FXPyColorWheel::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyColorWheel::_setBackColor(FXColor clr) { FXColorWheel::setBackColor(clr); }

long FXPyColorBar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyColorBar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXColorBar::onDefault(sender,sel,ptr);
  }

void FXPyColorBar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyColorBar::_create(){ FXColorBar::create(); }

void FXPyColorBar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyColorBar::_destroy(){ FXColorBar::destroy(); }

void FXPyColorBar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyColorBar::_detach(){ FXColorBar::detach(); }

void FXPyColorBar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyColorBar::_resize(FXint w,FXint h){ FXColorBar::resize(w,h); }

void FXPyColorBar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyColorBar::_enable(){ FXColorBar::enable(); }

void FXPyColorBar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyColorBar::_disable(){ FXColorBar::disable(); }

void FXPyColorBar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyColorBar::_show(){ FXColorBar::show(); }

void FXPyColorBar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyColorBar::_hide(){ FXColorBar::hide(); }

void FXPyColorBar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyColorBar::_lowerWindow(){ FXColorBar::lower(); }

FXint FXPyColorBar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyColorBar::_getDefaultHeight() { return FXColorBar::getDefaultHeight(); }

FXint FXPyColorBar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyColorBar::_getDefaultWidth() { return FXColorBar::getDefaultWidth(); }

FXint FXPyColorBar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyColorBar::_getWidthForHeight(FXint h) { return FXColorBar::getWidthForHeight(h); }

FXint FXPyColorBar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyColorBar::_getHeightForWidth(FXint w) { return FXColorBar::getHeightForWidth(w); }

void FXPyColorBar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyColorBar::_layout() { FXColorBar::layout(); }

void FXPyColorBar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyColorBar::_recalc() { FXColorBar::recalc(); }

FXbool FXPyColorBar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyColorBar::_isComposite() const { return FXColorBar::isComposite(); }

void FXPyColorBar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyColorBar::_move(FXint x,FXint y){ FXColorBar::move(x,y); }

void FXPyColorBar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyColorBar::_position(FXint x,FXint y,FXint w,FXint h){ FXColorBar::position(x,y,w,h); }

FXbool FXPyColorBar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyColorBar::_canFocus() const { return FXColorBar::canFocus(); }

void FXPyColorBar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyColorBar::_setFocus(){ FXColorBar::setFocus(); }

void FXPyColorBar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyColorBar::_killFocus(){ FXColorBar::killFocus(); }

void FXPyColorBar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyColorBar::_setDefault(FXbool enable){ FXColorBar::setDefault(enable); }

FXbool FXPyColorBar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyColorBar::_contains(FXint x,FXint y) const { return FXColorBar::contains(x,y); }

FXbool FXPyColorBar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyColorBar::_doesSaveUnder() const { return FXColorBar::doesSaveUnder(); }

void FXPyColorBar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyColorBar::_reparent(FXComposite* newparent) { FXColorBar::reparent(newparent); }

void FXPyColorBar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyColorBar::_setBackColor(FXColor clr) { FXColorBar::setBackColor(clr); }

long FXPyArrowButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyArrowButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXArrowButton::onDefault(sender,sel,ptr);
  }

void FXPyArrowButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyArrowButton::_create(){ FXArrowButton::create(); }

void FXPyArrowButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyArrowButton::_destroy(){ FXArrowButton::destroy(); }

void FXPyArrowButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyArrowButton::_detach(){ FXArrowButton::detach(); }

void FXPyArrowButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyArrowButton::_resize(FXint w,FXint h){ FXArrowButton::resize(w,h); }

void FXPyArrowButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyArrowButton::_enable(){ FXArrowButton::enable(); }

void FXPyArrowButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyArrowButton::_disable(){ FXArrowButton::disable(); }

void FXPyArrowButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyArrowButton::_show(){ FXArrowButton::show(); }

void FXPyArrowButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyArrowButton::_hide(){ FXArrowButton::hide(); }

void FXPyArrowButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyArrowButton::_lowerWindow(){ FXArrowButton::lower(); }

FXint FXPyArrowButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyArrowButton::_getDefaultHeight() { return FXArrowButton::getDefaultHeight(); }

FXint FXPyArrowButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyArrowButton::_getDefaultWidth() { return FXArrowButton::getDefaultWidth(); }

FXint FXPyArrowButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyArrowButton::_getWidthForHeight(FXint h) { return FXArrowButton::getWidthForHeight(h); }

FXint FXPyArrowButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyArrowButton::_getHeightForWidth(FXint w) { return FXArrowButton::getHeightForWidth(w); }

void FXPyArrowButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyArrowButton::_layout() { FXArrowButton::layout(); }

void FXPyArrowButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyArrowButton::_recalc() { FXArrowButton::recalc(); }

FXbool FXPyArrowButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyArrowButton::_isComposite() const { return FXArrowButton::isComposite(); }

void FXPyArrowButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyArrowButton::_move(FXint x,FXint y){ FXArrowButton::move(x,y); }

void FXPyArrowButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyArrowButton::_position(FXint x,FXint y,FXint w,FXint h){ FXArrowButton::position(x,y,w,h); }

FXbool FXPyArrowButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyArrowButton::_canFocus() const { return FXArrowButton::canFocus(); }

void FXPyArrowButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyArrowButton::_setFocus(){ FXArrowButton::setFocus(); }

void FXPyArrowButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyArrowButton::_killFocus(){ FXArrowButton::killFocus(); }

void FXPyArrowButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyArrowButton::_setDefault(FXbool enable){ FXArrowButton::setDefault(enable); }

FXbool FXPyArrowButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyArrowButton::_contains(FXint x,FXint y) const { return FXArrowButton::contains(x,y); }

FXbool FXPyArrowButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyArrowButton::_doesSaveUnder() const { return FXArrowButton::doesSaveUnder(); }

void FXPyArrowButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyArrowButton::_reparent(FXComposite* newparent) { FXArrowButton::reparent(newparent); }

void FXPyArrowButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyArrowButton::_setBackColor(FXColor clr) { FXArrowButton::setBackColor(clr); }

long FXPyToggleButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyToggleButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXToggleButton::onDefault(sender,sel,ptr);
  }

void FXPyToggleButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyToggleButton::_create(){ FXToggleButton::create(); }

void FXPyToggleButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyToggleButton::_destroy(){ FXToggleButton::destroy(); }

void FXPyToggleButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyToggleButton::_detach(){ FXToggleButton::detach(); }

void FXPyToggleButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyToggleButton::_resize(FXint w,FXint h){ FXToggleButton::resize(w,h); }

void FXPyToggleButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyToggleButton::_enable(){ FXToggleButton::enable(); }

void FXPyToggleButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyToggleButton::_disable(){ FXToggleButton::disable(); }

void FXPyToggleButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyToggleButton::_show(){ FXToggleButton::show(); }

void FXPyToggleButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyToggleButton::_hide(){ FXToggleButton::hide(); }

void FXPyToggleButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyToggleButton::_lowerWindow(){ FXToggleButton::lower(); }

FXint FXPyToggleButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyToggleButton::_getDefaultHeight() { return FXToggleButton::getDefaultHeight(); }

FXint FXPyToggleButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyToggleButton::_getDefaultWidth() { return FXToggleButton::getDefaultWidth(); }

FXint FXPyToggleButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyToggleButton::_getWidthForHeight(FXint h) { return FXToggleButton::getWidthForHeight(h); }

FXint FXPyToggleButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyToggleButton::_getHeightForWidth(FXint w) { return FXToggleButton::getHeightForWidth(w); }

void FXPyToggleButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyToggleButton::_layout() { FXToggleButton::layout(); }

void FXPyToggleButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyToggleButton::_recalc() { FXToggleButton::recalc(); }

FXbool FXPyToggleButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyToggleButton::_isComposite() const { return FXToggleButton::isComposite(); }

void FXPyToggleButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyToggleButton::_move(FXint x,FXint y){ FXToggleButton::move(x,y); }

void FXPyToggleButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyToggleButton::_position(FXint x,FXint y,FXint w,FXint h){ FXToggleButton::position(x,y,w,h); }

FXbool FXPyToggleButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyToggleButton::_canFocus() const { return FXToggleButton::canFocus(); }

void FXPyToggleButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyToggleButton::_setFocus(){ FXToggleButton::setFocus(); }

void FXPyToggleButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyToggleButton::_killFocus(){ FXToggleButton::killFocus(); }

void FXPyToggleButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyToggleButton::_setDefault(FXbool enable){ FXToggleButton::setDefault(enable); }

FXbool FXPyToggleButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyToggleButton::_contains(FXint x,FXint y) const { return FXToggleButton::contains(x,y); }

FXbool FXPyToggleButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyToggleButton::_doesSaveUnder() const { return FXToggleButton::doesSaveUnder(); }

void FXPyToggleButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyToggleButton::_reparent(FXComposite* newparent) { FXToggleButton::reparent(newparent); }

void FXPyToggleButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyToggleButton::_setBackColor(FXColor clr) { FXToggleButton::setBackColor(clr); }

long FXPyRootWindow::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyRootWindow::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXRootWindow::onDefault(sender,sel,ptr);
  }

void FXPyRootWindow::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyRootWindow::_create(){ FXRootWindow::create(); }

void FXPyRootWindow::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyRootWindow::_destroy(){ FXRootWindow::destroy(); }

void FXPyRootWindow::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyRootWindow::_detach(){ FXRootWindow::detach(); }

void FXPyRootWindow::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyRootWindow::_resize(FXint w,FXint h){ FXRootWindow::resize(w,h); }

void FXPyRootWindow::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyRootWindow::_enable(){ FXRootWindow::enable(); }

void FXPyRootWindow::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyRootWindow::_disable(){ FXRootWindow::disable(); }

void FXPyRootWindow::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyRootWindow::_show(){ FXRootWindow::show(); }

void FXPyRootWindow::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyRootWindow::_hide(){ FXRootWindow::hide(); }

void FXPyRootWindow::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyRootWindow::_lowerWindow(){ FXRootWindow::lower(); }

FXint FXPyRootWindow::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyRootWindow::_getDefaultHeight() { return FXRootWindow::getDefaultHeight(); }

FXint FXPyRootWindow::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyRootWindow::_getDefaultWidth() { return FXRootWindow::getDefaultWidth(); }

FXint FXPyRootWindow::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyRootWindow::_getWidthForHeight(FXint h) { return FXRootWindow::getWidthForHeight(h); }

FXint FXPyRootWindow::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyRootWindow::_getHeightForWidth(FXint w) { return FXRootWindow::getHeightForWidth(w); }

void FXPyRootWindow::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyRootWindow::_layout() { FXRootWindow::layout(); }

void FXPyRootWindow::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyRootWindow::_recalc() { FXRootWindow::recalc(); }

FXbool FXPyRootWindow::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyRootWindow::_isComposite() const { return FXRootWindow::isComposite(); }

void FXPyRootWindow::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyRootWindow::_move(FXint x,FXint y){ FXRootWindow::move(x,y); }

void FXPyRootWindow::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyRootWindow::_position(FXint x,FXint y,FXint w,FXint h){ FXRootWindow::position(x,y,w,h); }

FXbool FXPyRootWindow::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyRootWindow::_canFocus() const { return FXRootWindow::canFocus(); }

void FXPyRootWindow::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyRootWindow::_setFocus(){ FXRootWindow::setFocus(); }

void FXPyRootWindow::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyRootWindow::_killFocus(){ FXRootWindow::killFocus(); }

void FXPyRootWindow::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyRootWindow::_setDefault(FXbool enable){ FXRootWindow::setDefault(enable); }

FXbool FXPyRootWindow::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyRootWindow::_contains(FXint x,FXint y) const { return FXRootWindow::contains(x,y); }

FXbool FXPyRootWindow::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyRootWindow::_doesSaveUnder() const { return FXRootWindow::doesSaveUnder(); }

void FXPyRootWindow::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyRootWindow::_reparent(FXComposite* newparent) { FXRootWindow::reparent(newparent); }

void FXPyRootWindow::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyRootWindow::_setBackColor(FXColor clr) { FXRootWindow::setBackColor(clr); }

long FXPySpinner::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPySpinner::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXSpinner::onDefault(sender,sel,ptr);
  }

void FXPySpinner::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPySpinner::_create(){ FXSpinner::create(); }

void FXPySpinner::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPySpinner::_destroy(){ FXSpinner::destroy(); }

void FXPySpinner::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPySpinner::_detach(){ FXSpinner::detach(); }

void FXPySpinner::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPySpinner::_resize(FXint w,FXint h){ FXSpinner::resize(w,h); }

void FXPySpinner::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPySpinner::_enable(){ FXSpinner::enable(); }

void FXPySpinner::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPySpinner::_disable(){ FXSpinner::disable(); }

void FXPySpinner::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPySpinner::_show(){ FXSpinner::show(); }

void FXPySpinner::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPySpinner::_hide(){ FXSpinner::hide(); }

void FXPySpinner::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPySpinner::_lowerWindow(){ FXSpinner::lower(); }

FXint FXPySpinner::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPySpinner::_getDefaultHeight() { return FXSpinner::getDefaultHeight(); }

FXint FXPySpinner::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPySpinner::_getDefaultWidth() { return FXSpinner::getDefaultWidth(); }

FXint FXPySpinner::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPySpinner::_getWidthForHeight(FXint h) { return FXSpinner::getWidthForHeight(h); }

FXint FXPySpinner::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPySpinner::_getHeightForWidth(FXint w) { return FXSpinner::getHeightForWidth(w); }

void FXPySpinner::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPySpinner::_layout() { FXSpinner::layout(); }

void FXPySpinner::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPySpinner::_recalc() { FXSpinner::recalc(); }

FXbool FXPySpinner::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPySpinner::_isComposite() const { return FXSpinner::isComposite(); }

void FXPySpinner::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPySpinner::_move(FXint x,FXint y){ FXSpinner::move(x,y); }

void FXPySpinner::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPySpinner::_position(FXint x,FXint y,FXint w,FXint h){ FXSpinner::position(x,y,w,h); }

FXbool FXPySpinner::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPySpinner::_canFocus() const { return FXSpinner::canFocus(); }

void FXPySpinner::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPySpinner::_setFocus(){ FXSpinner::setFocus(); }

void FXPySpinner::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPySpinner::_killFocus(){ FXSpinner::killFocus(); }

void FXPySpinner::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPySpinner::_setDefault(FXbool enable){ FXSpinner::setDefault(enable); }

FXbool FXPySpinner::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPySpinner::_contains(FXint x,FXint y) const { return FXSpinner::contains(x,y); }

FXbool FXPySpinner::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPySpinner::_doesSaveUnder() const { return FXSpinner::doesSaveUnder(); }

void FXPySpinner::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPySpinner::_reparent(FXComposite* newparent) { FXSpinner::reparent(newparent); }

void FXPySpinner::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPySpinner::_setBackColor(FXColor clr) { FXSpinner::setBackColor(clr); }

long FXPySwitcher::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPySwitcher::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXSwitcher::onDefault(sender,sel,ptr);
  }

void FXPySwitcher::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPySwitcher::_create(){ FXSwitcher::create(); }

void FXPySwitcher::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPySwitcher::_destroy(){ FXSwitcher::destroy(); }

void FXPySwitcher::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPySwitcher::_detach(){ FXSwitcher::detach(); }

void FXPySwitcher::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPySwitcher::_resize(FXint w,FXint h){ FXSwitcher::resize(w,h); }

void FXPySwitcher::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPySwitcher::_enable(){ FXSwitcher::enable(); }

void FXPySwitcher::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPySwitcher::_disable(){ FXSwitcher::disable(); }

void FXPySwitcher::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPySwitcher::_show(){ FXSwitcher::show(); }

void FXPySwitcher::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPySwitcher::_hide(){ FXSwitcher::hide(); }

void FXPySwitcher::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPySwitcher::_lowerWindow(){ FXSwitcher::lower(); }

FXint FXPySwitcher::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPySwitcher::_getDefaultHeight() { return FXSwitcher::getDefaultHeight(); }

FXint FXPySwitcher::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPySwitcher::_getDefaultWidth() { return FXSwitcher::getDefaultWidth(); }

FXint FXPySwitcher::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPySwitcher::_getWidthForHeight(FXint h) { return FXSwitcher::getWidthForHeight(h); }

FXint FXPySwitcher::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPySwitcher::_getHeightForWidth(FXint w) { return FXSwitcher::getHeightForWidth(w); }

void FXPySwitcher::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPySwitcher::_layout() { FXSwitcher::layout(); }

void FXPySwitcher::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPySwitcher::_recalc() { FXSwitcher::recalc(); }

FXbool FXPySwitcher::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPySwitcher::_isComposite() const { return FXSwitcher::isComposite(); }

void FXPySwitcher::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPySwitcher::_move(FXint x,FXint y){ FXSwitcher::move(x,y); }

void FXPySwitcher::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPySwitcher::_position(FXint x,FXint y,FXint w,FXint h){ FXSwitcher::position(x,y,w,h); }

FXbool FXPySwitcher::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPySwitcher::_canFocus() const { return FXSwitcher::canFocus(); }

void FXPySwitcher::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPySwitcher::_setFocus(){ FXSwitcher::setFocus(); }

void FXPySwitcher::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPySwitcher::_killFocus(){ FXSwitcher::killFocus(); }

void FXPySwitcher::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPySwitcher::_setDefault(FXbool enable){ FXSwitcher::setDefault(enable); }

FXbool FXPySwitcher::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPySwitcher::_contains(FXint x,FXint y) const { return FXSwitcher::contains(x,y); }

FXbool FXPySwitcher::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPySwitcher::_doesSaveUnder() const { return FXSwitcher::doesSaveUnder(); }

void FXPySwitcher::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPySwitcher::_reparent(FXComposite* newparent) { FXSwitcher::reparent(newparent); }

void FXPySwitcher::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPySwitcher::_setBackColor(FXColor clr) { FXSwitcher::setBackColor(clr); }

long FXPyList::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyList::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXList::onDefault(sender,sel,ptr);
  }

void FXPyList::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyList::_create(){ FXList::create(); }

void FXPyList::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyList::_destroy(){ FXList::destroy(); }

void FXPyList::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyList::_detach(){ FXList::detach(); }

void FXPyList::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyList::_resize(FXint w,FXint h){ FXList::resize(w,h); }

void FXPyList::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyList::_enable(){ FXList::enable(); }

void FXPyList::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyList::_disable(){ FXList::disable(); }

void FXPyList::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyList::_show(){ FXList::show(); }

void FXPyList::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyList::_hide(){ FXList::hide(); }

void FXPyList::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyList::_lowerWindow(){ FXList::lower(); }

FXint FXPyList::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyList::_getDefaultHeight() { return FXList::getDefaultHeight(); }

FXint FXPyList::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyList::_getDefaultWidth() { return FXList::getDefaultWidth(); }

FXint FXPyList::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyList::_getWidthForHeight(FXint h) { return FXList::getWidthForHeight(h); }

FXint FXPyList::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyList::_getHeightForWidth(FXint w) { return FXList::getHeightForWidth(w); }

void FXPyList::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyList::_layout() { FXList::layout(); }

void FXPyList::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyList::_recalc() { FXList::recalc(); }

FXbool FXPyList::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyList::_isComposite() const { return FXList::isComposite(); }

void FXPyList::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyList::_move(FXint x,FXint y){ FXList::move(x,y); }

void FXPyList::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyList::_position(FXint x,FXint y,FXint w,FXint h){ FXList::position(x,y,w,h); }

FXbool FXPyList::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyList::_canFocus() const { return FXList::canFocus(); }

void FXPyList::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyList::_setFocus(){ FXList::setFocus(); }

void FXPyList::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyList::_killFocus(){ FXList::killFocus(); }

void FXPyList::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyList::_setDefault(FXbool enable){ FXList::setDefault(enable); }

FXbool FXPyList::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyList::_contains(FXint x,FXint y) const { return FXList::contains(x,y); }

FXbool FXPyList::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyList::_doesSaveUnder() const { return FXList::doesSaveUnder(); }

void FXPyList::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyList::_reparent(FXComposite* newparent) { FXList::reparent(newparent); }

void FXPyList::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyList::_setBackColor(FXColor clr) { FXList::setBackColor(clr); }

FXint FXPyList::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyList::_getContentWidth() { return FXList::getContentWidth(); }

FXint FXPyList::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyList::_getContentHeight() { return FXList::getContentHeight(); }

FXint FXPyList::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyList::_getViewportWidth() { return FXList::getViewportWidth(); }

FXint FXPyList::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyList::_getViewportHeight() { return FXList::getViewportHeight(); }

void FXPyList::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyList::_moveContents(FXint x,FXint y) { FXList::moveContents(x,y); }

long FXPyListItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyListItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXListItem::onDefault(sender,sel,ptr);
  }

void FXPyListItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyListItem::_setText(const FXString& text) { FXListItem::setText(text); }

void FXPyListItem::setIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setIcon",icn); }
void FXPyListItem::_setIcon(FXIcon *icn) { FXListItem::setIcon(icn); }

void FXPyListItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyListItem::_setFocus(FXbool focus) { FXListItem::setFocus(focus); }

void FXPyListItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyListItem::_setSelected(FXbool selected) { FXListItem::setSelected(selected); }

void FXPyListItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyListItem::_setEnabled(FXbool enabled) { FXListItem::setEnabled(enabled); }

void FXPyListItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyListItem::_setDraggable(FXbool draggable) { FXListItem::setDraggable(draggable); }

void FXPyListItem::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }
void FXPyListItem::_setIconOwned(FXuint owned) { FXListItem::setIconOwned(owned); }

FXint FXPyListItem::getWidth(const FXList* list) const { return ::_getWidth(this, list); }
FXint FXPyListItem::_getWidth(const FXList* list) const { return FXListItem::getWidth(list); }

FXint FXPyListItem::getHeight(const FXList* list) const { return ::_getHeight(this, list); }
FXint FXPyListItem::_getHeight(const FXList* list) const { return FXListItem::getHeight(list); }

void FXPyListItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyListItem::_create(){ FXListItem::create(); }

void FXPyListItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyListItem::_detach(){ FXListItem::detach(); }

void FXPyListItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyListItem::_destroy(){ FXListItem::destroy(); }

long FXPyComboBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyComboBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXComboBox::onDefault(sender,sel,ptr);
  }

void FXPyComboBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyComboBox::_create(){ FXComboBox::create(); }

void FXPyComboBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyComboBox::_destroy(){ FXComboBox::destroy(); }

void FXPyComboBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyComboBox::_detach(){ FXComboBox::detach(); }

void FXPyComboBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyComboBox::_resize(FXint w,FXint h){ FXComboBox::resize(w,h); }

void FXPyComboBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyComboBox::_enable(){ FXComboBox::enable(); }

void FXPyComboBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyComboBox::_disable(){ FXComboBox::disable(); }

void FXPyComboBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyComboBox::_show(){ FXComboBox::show(); }

void FXPyComboBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyComboBox::_hide(){ FXComboBox::hide(); }

void FXPyComboBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyComboBox::_lowerWindow(){ FXComboBox::lower(); }

FXint FXPyComboBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyComboBox::_getDefaultHeight() { return FXComboBox::getDefaultHeight(); }

FXint FXPyComboBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyComboBox::_getDefaultWidth() { return FXComboBox::getDefaultWidth(); }

FXint FXPyComboBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyComboBox::_getWidthForHeight(FXint h) { return FXComboBox::getWidthForHeight(h); }

FXint FXPyComboBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyComboBox::_getHeightForWidth(FXint w) { return FXComboBox::getHeightForWidth(w); }

void FXPyComboBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyComboBox::_layout() { FXComboBox::layout(); }

void FXPyComboBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyComboBox::_recalc() { FXComboBox::recalc(); }

FXbool FXPyComboBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyComboBox::_isComposite() const { return FXComboBox::isComposite(); }

void FXPyComboBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyComboBox::_move(FXint x,FXint y){ FXComboBox::move(x,y); }

void FXPyComboBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyComboBox::_position(FXint x,FXint y,FXint w,FXint h){ FXComboBox::position(x,y,w,h); }

FXbool FXPyComboBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyComboBox::_canFocus() const { return FXComboBox::canFocus(); }

void FXPyComboBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyComboBox::_setFocus(){ FXComboBox::setFocus(); }

void FXPyComboBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyComboBox::_killFocus(){ FXComboBox::killFocus(); }

void FXPyComboBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyComboBox::_setDefault(FXbool enable){ FXComboBox::setDefault(enable); }

FXbool FXPyComboBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyComboBox::_contains(FXint x,FXint y) const { return FXComboBox::contains(x,y); }

FXbool FXPyComboBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyComboBox::_doesSaveUnder() const { return FXComboBox::doesSaveUnder(); }

void FXPyComboBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyComboBox::_reparent(FXComposite* newparent) { FXComboBox::reparent(newparent); }

void FXPyComboBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyComboBox::_setBackColor(FXColor clr) { FXComboBox::setBackColor(clr); }

long FXPyMessageBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMessageBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMessageBox::onDefault(sender,sel,ptr);
  }

void FXPyMessageBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMessageBox::_create(){ FXMessageBox::create(); }

void FXPyMessageBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMessageBox::_destroy(){ FXMessageBox::destroy(); }

void FXPyMessageBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMessageBox::_detach(){ FXMessageBox::detach(); }

void FXPyMessageBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMessageBox::_resize(FXint w,FXint h){ FXMessageBox::resize(w,h); }

void FXPyMessageBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMessageBox::_enable(){ FXMessageBox::enable(); }

void FXPyMessageBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMessageBox::_disable(){ FXMessageBox::disable(); }

void FXPyMessageBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMessageBox::_show(){ FXMessageBox::show(); }

void FXPyMessageBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMessageBox::_hide(){ FXMessageBox::hide(); }

void FXPyMessageBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMessageBox::_lowerWindow(){ FXMessageBox::lower(); }

FXint FXPyMessageBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMessageBox::_getDefaultHeight() { return FXMessageBox::getDefaultHeight(); }

FXint FXPyMessageBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMessageBox::_getDefaultWidth() { return FXMessageBox::getDefaultWidth(); }

FXint FXPyMessageBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMessageBox::_getWidthForHeight(FXint h) { return FXMessageBox::getWidthForHeight(h); }

FXint FXPyMessageBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMessageBox::_getHeightForWidth(FXint w) { return FXMessageBox::getHeightForWidth(w); }

void FXPyMessageBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMessageBox::_layout() { FXMessageBox::layout(); }

void FXPyMessageBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMessageBox::_recalc() { FXMessageBox::recalc(); }

FXbool FXPyMessageBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMessageBox::_isComposite() const { return FXMessageBox::isComposite(); }

void FXPyMessageBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMessageBox::_move(FXint x,FXint y){ FXMessageBox::move(x,y); }

void FXPyMessageBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMessageBox::_position(FXint x,FXint y,FXint w,FXint h){ FXMessageBox::position(x,y,w,h); }

FXbool FXPyMessageBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMessageBox::_canFocus() const { return FXMessageBox::canFocus(); }

void FXPyMessageBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMessageBox::_setFocus(){ FXMessageBox::setFocus(); }

void FXPyMessageBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMessageBox::_killFocus(){ FXMessageBox::killFocus(); }

void FXPyMessageBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMessageBox::_setDefault(FXbool enable){ FXMessageBox::setDefault(enable); }

FXbool FXPyMessageBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMessageBox::_contains(FXint x,FXint y) const { return FXMessageBox::contains(x,y); }

FXbool FXPyMessageBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMessageBox::_doesSaveUnder() const { return FXMessageBox::doesSaveUnder(); }

void FXPyMessageBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMessageBox::_reparent(FXComposite* newparent) { FXMessageBox::reparent(newparent); }

void FXPyMessageBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMessageBox::_setBackColor(FXColor clr) { FXMessageBox::setBackColor(clr); }

void FXPyMessageBox::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyMessageBox::_iconify() { FXMessageBox::iconify(); }

void FXPyMessageBox::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyMessageBox::_deiconify() { FXMessageBox::deiconify(); }

void FXPyMessageBox::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyMessageBox::_show(FXuint placement) { FXMessageBox::show(placement); }

long FXPyDirItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDirItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDirItem::onDefault(sender,sel,ptr);
  }

void FXPyDirItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyDirItem::_setText(const FXString& text) { FXDirItem::setText(text); }

void FXPyDirItem::setOpenIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setOpenIcon",icn); }
void FXPyDirItem::_setOpenIcon(FXIcon *icn) { FXDirItem::setOpenIcon(icn); }

void FXPyDirItem::setClosedIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setClosedIcon",icn); }
void FXPyDirItem::_setClosedIcon(FXIcon *icn) { FXDirItem::setClosedIcon(icn); }

void FXPyDirItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyDirItem::_setFocus(FXbool focus) { FXDirItem::setFocus(focus); }

void FXPyDirItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyDirItem::_setSelected(FXbool selected) { FXDirItem::setSelected(selected); }

void FXPyDirItem::setOpened(FXbool opened) { FXPyCallVoidFunction(this,"setOpened",opened); }
void FXPyDirItem::_setOpened(FXbool opened) { FXDirItem::setOpened(opened); }

void FXPyDirItem::setExpanded(FXbool expanded) { FXPyCallVoidFunction(this,"setExpanded",expanded); }
void FXPyDirItem::_setExpanded(FXbool expanded) { FXDirItem::setExpanded(expanded); }

void FXPyDirItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyDirItem::_setEnabled(FXbool enabled) { FXDirItem::setEnabled(enabled); }

void FXPyDirItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyDirItem::_setDraggable(FXbool draggable) { FXDirItem::setDraggable(draggable); }

void FXPyDirItem::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }
void FXPyDirItem::_setIconOwned(FXuint owned) { FXDirItem::setIconOwned(owned); }

FXint FXPyDirItem::getWidth(const FXTreeList* list) const { return ::_getWidth(this, list); }
FXint FXPyDirItem::_getWidth(const FXTreeList* list) const { return FXDirItem::getWidth(list); }

FXint FXPyDirItem::getHeight(const FXTreeList* list) const { return ::_getHeight(this, list); }
FXint FXPyDirItem::_getHeight(const FXTreeList* list) const { return FXDirItem::getHeight(list); }

void FXPyDirItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDirItem::_create(){ FXDirItem::create(); }

void FXPyDirItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDirItem::_detach(){ FXDirItem::detach(); }

void FXPyDirItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDirItem::_destroy(){ FXDirItem::destroy(); }

long FXPyDirList::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDirList::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDirList::onDefault(sender,sel,ptr);
  }

void FXPyDirList::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDirList::_create(){ FXDirList::create(); }

void FXPyDirList::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDirList::_destroy(){ FXDirList::destroy(); }

void FXPyDirList::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDirList::_detach(){ FXDirList::detach(); }

void FXPyDirList::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDirList::_resize(FXint w,FXint h){ FXDirList::resize(w,h); }

void FXPyDirList::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDirList::_enable(){ FXDirList::enable(); }

void FXPyDirList::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDirList::_disable(){ FXDirList::disable(); }

void FXPyDirList::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDirList::_show(){ FXDirList::show(); }

void FXPyDirList::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDirList::_hide(){ FXDirList::hide(); }

void FXPyDirList::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDirList::_lowerWindow(){ FXDirList::lower(); }

FXint FXPyDirList::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDirList::_getDefaultHeight() { return FXDirList::getDefaultHeight(); }

FXint FXPyDirList::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDirList::_getDefaultWidth() { return FXDirList::getDefaultWidth(); }

FXint FXPyDirList::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDirList::_getWidthForHeight(FXint h) { return FXDirList::getWidthForHeight(h); }

FXint FXPyDirList::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDirList::_getHeightForWidth(FXint w) { return FXDirList::getHeightForWidth(w); }

void FXPyDirList::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDirList::_layout() { FXDirList::layout(); }

void FXPyDirList::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDirList::_recalc() { FXDirList::recalc(); }

FXbool FXPyDirList::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDirList::_isComposite() const { return FXDirList::isComposite(); }

void FXPyDirList::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDirList::_move(FXint x,FXint y){ FXDirList::move(x,y); }

void FXPyDirList::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDirList::_position(FXint x,FXint y,FXint w,FXint h){ FXDirList::position(x,y,w,h); }

FXbool FXPyDirList::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDirList::_canFocus() const { return FXDirList::canFocus(); }

void FXPyDirList::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDirList::_setFocus(){ FXDirList::setFocus(); }

void FXPyDirList::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDirList::_killFocus(){ FXDirList::killFocus(); }

void FXPyDirList::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDirList::_setDefault(FXbool enable){ FXDirList::setDefault(enable); }

FXbool FXPyDirList::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDirList::_contains(FXint x,FXint y) const { return FXDirList::contains(x,y); }

FXbool FXPyDirList::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDirList::_doesSaveUnder() const { return FXDirList::doesSaveUnder(); }

void FXPyDirList::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDirList::_reparent(FXComposite* newparent) { FXDirList::reparent(newparent); }

void FXPyDirList::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDirList::_setBackColor(FXColor clr) { FXDirList::setBackColor(clr); }

FXint FXPyDirList::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyDirList::_getContentWidth() { return FXDirList::getContentWidth(); }

FXint FXPyDirList::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyDirList::_getContentHeight() { return FXDirList::getContentHeight(); }

FXint FXPyDirList::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyDirList::_getViewportWidth() { return FXDirList::getViewportWidth(); }

FXint FXPyDirList::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyDirList::_getViewportHeight() { return FXDirList::getViewportHeight(); }

void FXPyDirList::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyDirList::_moveContents(FXint x,FXint y) { FXDirList::moveContents(x,y); }

long FXPyHeaderItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyHeaderItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXHeaderItem::onDefault(sender,sel,ptr);
  }

void FXPyHeaderItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyHeaderItem::_setText(const FXString& text) { FXHeaderItem::setText(text); }

void FXPyHeaderItem::setIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setIcon",icn); }
void FXPyHeaderItem::_setIcon(FXIcon *icn) { FXHeaderItem::setIcon(icn); }

FXint FXPyHeaderItem::getWidth(const FXHeader* header) const { return ::_getWidth(this, header); }
FXint FXPyHeaderItem::_getWidth(const FXHeader* header) const { return FXHeaderItem::getWidth(header); }

FXint FXPyHeaderItem::getHeight(const FXHeader* header) const { return ::_getHeight(this, header); }
FXint FXPyHeaderItem::_getHeight(const FXHeader* header) const { return FXHeaderItem::getHeight(header); }

void FXPyHeaderItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyHeaderItem::_create(){ FXHeaderItem::create(); }

void FXPyHeaderItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyHeaderItem::_detach(){ FXHeaderItem::detach(); }

void FXPyHeaderItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyHeaderItem::_destroy(){ FXHeaderItem::destroy(); }

long FXPyHeader::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyHeader::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXHeader::onDefault(sender,sel,ptr);
  }

void FXPyHeader::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyHeader::_create(){ FXHeader::create(); }

void FXPyHeader::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyHeader::_destroy(){ FXHeader::destroy(); }

void FXPyHeader::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyHeader::_detach(){ FXHeader::detach(); }

void FXPyHeader::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyHeader::_resize(FXint w,FXint h){ FXHeader::resize(w,h); }

void FXPyHeader::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyHeader::_enable(){ FXHeader::enable(); }

void FXPyHeader::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyHeader::_disable(){ FXHeader::disable(); }

void FXPyHeader::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyHeader::_show(){ FXHeader::show(); }

void FXPyHeader::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyHeader::_hide(){ FXHeader::hide(); }

void FXPyHeader::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyHeader::_lowerWindow(){ FXHeader::lower(); }

FXint FXPyHeader::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyHeader::_getDefaultHeight() { return FXHeader::getDefaultHeight(); }

FXint FXPyHeader::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyHeader::_getDefaultWidth() { return FXHeader::getDefaultWidth(); }

FXint FXPyHeader::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyHeader::_getWidthForHeight(FXint h) { return FXHeader::getWidthForHeight(h); }

FXint FXPyHeader::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyHeader::_getHeightForWidth(FXint w) { return FXHeader::getHeightForWidth(w); }

void FXPyHeader::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyHeader::_layout() { FXHeader::layout(); }

void FXPyHeader::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyHeader::_recalc() { FXHeader::recalc(); }

FXbool FXPyHeader::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyHeader::_isComposite() const { return FXHeader::isComposite(); }

void FXPyHeader::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyHeader::_move(FXint x,FXint y){ FXHeader::move(x,y); }

void FXPyHeader::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyHeader::_position(FXint x,FXint y,FXint w,FXint h){ FXHeader::position(x,y,w,h); }

FXbool FXPyHeader::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyHeader::_canFocus() const { return FXHeader::canFocus(); }

void FXPyHeader::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyHeader::_setFocus(){ FXHeader::setFocus(); }

void FXPyHeader::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyHeader::_killFocus(){ FXHeader::killFocus(); }

void FXPyHeader::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyHeader::_setDefault(FXbool enable){ FXHeader::setDefault(enable); }

FXbool FXPyHeader::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyHeader::_contains(FXint x,FXint y) const { return FXHeader::contains(x,y); }

FXbool FXPyHeader::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyHeader::_doesSaveUnder() const { return FXHeader::doesSaveUnder(); }

void FXPyHeader::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyHeader::_reparent(FXComposite* newparent) { FXHeader::reparent(newparent); }

void FXPyHeader::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyHeader::_setBackColor(FXColor clr) { FXHeader::setBackColor(clr); }

long FXPyShutter::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyShutter::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXShutter::onDefault(sender,sel,ptr);
  }

void FXPyShutter::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyShutter::_create(){ FXShutter::create(); }

void FXPyShutter::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyShutter::_destroy(){ FXShutter::destroy(); }

void FXPyShutter::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyShutter::_detach(){ FXShutter::detach(); }

void FXPyShutter::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyShutter::_resize(FXint w,FXint h){ FXShutter::resize(w,h); }

void FXPyShutter::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyShutter::_enable(){ FXShutter::enable(); }

void FXPyShutter::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyShutter::_disable(){ FXShutter::disable(); }

void FXPyShutter::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyShutter::_show(){ FXShutter::show(); }

void FXPyShutter::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyShutter::_hide(){ FXShutter::hide(); }

void FXPyShutter::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyShutter::_lowerWindow(){ FXShutter::lower(); }

FXint FXPyShutter::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyShutter::_getDefaultHeight() { return FXShutter::getDefaultHeight(); }

FXint FXPyShutter::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyShutter::_getDefaultWidth() { return FXShutter::getDefaultWidth(); }

FXint FXPyShutter::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyShutter::_getWidthForHeight(FXint h) { return FXShutter::getWidthForHeight(h); }

FXint FXPyShutter::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyShutter::_getHeightForWidth(FXint w) { return FXShutter::getHeightForWidth(w); }

void FXPyShutter::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyShutter::_layout() { FXShutter::layout(); }

void FXPyShutter::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyShutter::_recalc() { FXShutter::recalc(); }

FXbool FXPyShutter::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyShutter::_isComposite() const { return FXShutter::isComposite(); }

void FXPyShutter::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyShutter::_move(FXint x,FXint y){ FXShutter::move(x,y); }

void FXPyShutter::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyShutter::_position(FXint x,FXint y,FXint w,FXint h){ FXShutter::position(x,y,w,h); }

FXbool FXPyShutter::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyShutter::_canFocus() const { return FXShutter::canFocus(); }

void FXPyShutter::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyShutter::_setFocus(){ FXShutter::setFocus(); }

void FXPyShutter::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyShutter::_killFocus(){ FXShutter::killFocus(); }

void FXPyShutter::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyShutter::_setDefault(FXbool enable){ FXShutter::setDefault(enable); }

FXbool FXPyShutter::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyShutter::_contains(FXint x,FXint y) const { return FXShutter::contains(x,y); }

FXbool FXPyShutter::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyShutter::_doesSaveUnder() const { return FXShutter::doesSaveUnder(); }

void FXPyShutter::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyShutter::_reparent(FXComposite* newparent) { FXShutter::reparent(newparent); }

void FXPyShutter::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyShutter::_setBackColor(FXColor clr) { FXShutter::setBackColor(clr); }

void FXPyShutter::setCurrent(FXint panel) { FXPyCallVoidFunction(this,"setCurrent",panel); }
void FXPyShutter::_setCurrent(FXint panel) { FXShutter::setCurrent(panel); }

long FXPyShutterItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyShutterItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXShutterItem::onDefault(sender,sel,ptr);
  }

void FXPyShutterItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyShutterItem::_create(){ FXShutterItem::create(); }

void FXPyShutterItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyShutterItem::_destroy(){ FXShutterItem::destroy(); }

void FXPyShutterItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyShutterItem::_detach(){ FXShutterItem::detach(); }

void FXPyShutterItem::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyShutterItem::_resize(FXint w,FXint h){ FXShutterItem::resize(w,h); }

void FXPyShutterItem::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyShutterItem::_enable(){ FXShutterItem::enable(); }

void FXPyShutterItem::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyShutterItem::_disable(){ FXShutterItem::disable(); }

void FXPyShutterItem::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyShutterItem::_show(){ FXShutterItem::show(); }

void FXPyShutterItem::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyShutterItem::_hide(){ FXShutterItem::hide(); }

void FXPyShutterItem::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyShutterItem::_lowerWindow(){ FXShutterItem::lower(); }

FXint FXPyShutterItem::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyShutterItem::_getDefaultHeight() { return FXShutterItem::getDefaultHeight(); }

FXint FXPyShutterItem::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyShutterItem::_getDefaultWidth() { return FXShutterItem::getDefaultWidth(); }

FXint FXPyShutterItem::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyShutterItem::_getWidthForHeight(FXint h) { return FXShutterItem::getWidthForHeight(h); }

FXint FXPyShutterItem::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyShutterItem::_getHeightForWidth(FXint w) { return FXShutterItem::getHeightForWidth(w); }

void FXPyShutterItem::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyShutterItem::_layout() { FXShutterItem::layout(); }

void FXPyShutterItem::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyShutterItem::_recalc() { FXShutterItem::recalc(); }

FXbool FXPyShutterItem::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyShutterItem::_isComposite() const { return FXShutterItem::isComposite(); }

void FXPyShutterItem::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyShutterItem::_move(FXint x,FXint y){ FXShutterItem::move(x,y); }

void FXPyShutterItem::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyShutterItem::_position(FXint x,FXint y,FXint w,FXint h){ FXShutterItem::position(x,y,w,h); }

FXbool FXPyShutterItem::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyShutterItem::_canFocus() const { return FXShutterItem::canFocus(); }

void FXPyShutterItem::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyShutterItem::_setFocus(){ FXShutterItem::setFocus(); }

void FXPyShutterItem::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyShutterItem::_killFocus(){ FXShutterItem::killFocus(); }

void FXPyShutterItem::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyShutterItem::_setDefault(FXbool enable){ FXShutterItem::setDefault(enable); }

FXbool FXPyShutterItem::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyShutterItem::_contains(FXint x,FXint y) const { return FXShutterItem::contains(x,y); }

FXbool FXPyShutterItem::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyShutterItem::_doesSaveUnder() const { return FXShutterItem::doesSaveUnder(); }

void FXPyShutterItem::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyShutterItem::_reparent(FXComposite* newparent) { FXShutterItem::reparent(newparent); }

void FXPyShutterItem::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyShutterItem::_setBackColor(FXColor clr) { FXShutterItem::setBackColor(clr); }

long FXPyIconItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyIconItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXIconItem::onDefault(sender,sel,ptr);
  }

void FXPyIconItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyIconItem::_setText(const FXString& text) { FXIconItem::setText(text); }

void FXPyIconItem::setBigIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setBigIcon",icn); }
void FXPyIconItem::_setBigIcon(FXIcon *icn) { FXIconItem::setBigIcon(icn); }

void FXPyIconItem::setMiniIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setMiniIcon",icn); }
void FXPyIconItem::_setMiniIcon(FXIcon *icn) { FXIconItem::setMiniIcon(icn); }

void FXPyIconItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyIconItem::_setFocus(FXbool focus) { FXIconItem::setFocus(focus); }

void FXPyIconItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyIconItem::_setSelected(FXbool selected) { FXIconItem::setSelected(selected); }

void FXPyIconItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyIconItem::_setEnabled(FXbool enabled) { FXIconItem::setEnabled(enabled); }

void FXPyIconItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyIconItem::_setDraggable(FXbool draggable) { FXIconItem::setDraggable(draggable); }

void FXPyIconItem::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }
void FXPyIconItem::_setIconOwned(FXuint owned) { FXIconItem::setIconOwned(owned); }

FXint FXPyIconItem::getWidth(const FXIconList* list) const { return ::_getWidth(this, list); }
FXint FXPyIconItem::_getWidth(const FXIconList* list) const { return FXIconItem::getWidth(list); }

FXint FXPyIconItem::getHeight(const FXIconList* list) const { return ::_getHeight(this, list); }
FXint FXPyIconItem::_getHeight(const FXIconList* list) const { return FXIconItem::getHeight(list); }

void FXPyIconItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyIconItem::_create(){ FXIconItem::create(); }

void FXPyIconItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyIconItem::_detach(){ FXIconItem::detach(); }

void FXPyIconItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyIconItem::_destroy(){ FXIconItem::destroy(); }

long FXPyIconList::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyIconList::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXIconList::onDefault(sender,sel,ptr);
  }

void FXPyIconList::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyIconList::_create(){ FXIconList::create(); }

void FXPyIconList::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyIconList::_destroy(){ FXIconList::destroy(); }

void FXPyIconList::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyIconList::_detach(){ FXIconList::detach(); }

void FXPyIconList::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyIconList::_resize(FXint w,FXint h){ FXIconList::resize(w,h); }

void FXPyIconList::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyIconList::_enable(){ FXIconList::enable(); }

void FXPyIconList::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyIconList::_disable(){ FXIconList::disable(); }

void FXPyIconList::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyIconList::_show(){ FXIconList::show(); }

void FXPyIconList::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyIconList::_hide(){ FXIconList::hide(); }

void FXPyIconList::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyIconList::_lowerWindow(){ FXIconList::lower(); }

FXint FXPyIconList::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyIconList::_getDefaultHeight() { return FXIconList::getDefaultHeight(); }

FXint FXPyIconList::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyIconList::_getDefaultWidth() { return FXIconList::getDefaultWidth(); }

FXint FXPyIconList::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyIconList::_getWidthForHeight(FXint h) { return FXIconList::getWidthForHeight(h); }

FXint FXPyIconList::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyIconList::_getHeightForWidth(FXint w) { return FXIconList::getHeightForWidth(w); }

void FXPyIconList::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyIconList::_layout() { FXIconList::layout(); }

void FXPyIconList::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyIconList::_recalc() { FXIconList::recalc(); }

FXbool FXPyIconList::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyIconList::_isComposite() const { return FXIconList::isComposite(); }

void FXPyIconList::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyIconList::_move(FXint x,FXint y){ FXIconList::move(x,y); }

void FXPyIconList::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyIconList::_position(FXint x,FXint y,FXint w,FXint h){ FXIconList::position(x,y,w,h); }

FXbool FXPyIconList::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyIconList::_canFocus() const { return FXIconList::canFocus(); }

void FXPyIconList::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyIconList::_setFocus(){ FXIconList::setFocus(); }

void FXPyIconList::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyIconList::_killFocus(){ FXIconList::killFocus(); }

void FXPyIconList::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyIconList::_setDefault(FXbool enable){ FXIconList::setDefault(enable); }

FXbool FXPyIconList::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyIconList::_contains(FXint x,FXint y) const { return FXIconList::contains(x,y); }

FXbool FXPyIconList::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyIconList::_doesSaveUnder() const { return FXIconList::doesSaveUnder(); }

void FXPyIconList::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyIconList::_reparent(FXComposite* newparent) { FXIconList::reparent(newparent); }

void FXPyIconList::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyIconList::_setBackColor(FXColor clr) { FXIconList::setBackColor(clr); }

FXint FXPyIconList::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyIconList::_getContentWidth() { return FXIconList::getContentWidth(); }

FXint FXPyIconList::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyIconList::_getContentHeight() { return FXIconList::getContentHeight(); }

FXint FXPyIconList::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyIconList::_getViewportWidth() { return FXIconList::getViewportWidth(); }

FXint FXPyIconList::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyIconList::_getViewportHeight() { return FXIconList::getViewportHeight(); }

void FXPyIconList::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyIconList::_moveContents(FXint x,FXint y) { FXIconList::moveContents(x,y); }

long FXPyFileItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFileItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFileItem::onDefault(sender,sel,ptr);
  }

void FXPyFileItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyFileItem::_setText(const FXString& text) { FXFileItem::setText(text); }

void FXPyFileItem::setBigIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setBigIcon",icn); }
void FXPyFileItem::_setBigIcon(FXIcon *icn) { FXFileItem::setBigIcon(icn); }

void FXPyFileItem::setMiniIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setMiniIcon",icn); }
void FXPyFileItem::_setMiniIcon(FXIcon *icn) { FXFileItem::setMiniIcon(icn); }

void FXPyFileItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyFileItem::_setFocus(FXbool focus) { FXFileItem::setFocus(focus); }

void FXPyFileItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyFileItem::_setSelected(FXbool selected) { FXFileItem::setSelected(selected); }

void FXPyFileItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyFileItem::_setEnabled(FXbool enabled) { FXFileItem::setEnabled(enabled); }

void FXPyFileItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyFileItem::_setDraggable(FXbool draggable) { FXFileItem::setDraggable(draggable); }

void FXPyFileItem::setIconOwned(FXuint owned) { FXPyCallVoidFunction(this,"setIconOwned",owned); }
void FXPyFileItem::_setIconOwned(FXuint owned) { FXFileItem::setIconOwned(owned); }

FXint FXPyFileItem::getWidth(const FXIconList* list) const { return ::_getWidth(this, list); }
FXint FXPyFileItem::_getWidth(const FXIconList* list) const { return FXFileItem::getWidth(list); }

FXint FXPyFileItem::getHeight(const FXIconList* list) const { return ::_getHeight(this, list); }
FXint FXPyFileItem::_getHeight(const FXIconList* list) const { return FXFileItem::getHeight(list); }

void FXPyFileItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFileItem::_create(){ FXFileItem::create(); }

void FXPyFileItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFileItem::_detach(){ FXFileItem::detach(); }

void FXPyFileItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFileItem::_destroy(){ FXFileItem::destroy(); }

long FXPyFileList::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFileList::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFileList::onDefault(sender,sel,ptr);
  }

void FXPyFileList::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFileList::_create(){ FXFileList::create(); }

void FXPyFileList::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFileList::_destroy(){ FXFileList::destroy(); }

void FXPyFileList::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFileList::_detach(){ FXFileList::detach(); }

void FXPyFileList::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFileList::_resize(FXint w,FXint h){ FXFileList::resize(w,h); }

void FXPyFileList::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFileList::_enable(){ FXFileList::enable(); }

void FXPyFileList::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFileList::_disable(){ FXFileList::disable(); }

void FXPyFileList::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFileList::_show(){ FXFileList::show(); }

void FXPyFileList::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFileList::_hide(){ FXFileList::hide(); }

void FXPyFileList::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFileList::_lowerWindow(){ FXFileList::lower(); }

FXint FXPyFileList::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFileList::_getDefaultHeight() { return FXFileList::getDefaultHeight(); }

FXint FXPyFileList::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFileList::_getDefaultWidth() { return FXFileList::getDefaultWidth(); }

FXint FXPyFileList::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFileList::_getWidthForHeight(FXint h) { return FXFileList::getWidthForHeight(h); }

FXint FXPyFileList::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFileList::_getHeightForWidth(FXint w) { return FXFileList::getHeightForWidth(w); }

void FXPyFileList::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFileList::_layout() { FXFileList::layout(); }

void FXPyFileList::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFileList::_recalc() { FXFileList::recalc(); }

FXbool FXPyFileList::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFileList::_isComposite() const { return FXFileList::isComposite(); }

void FXPyFileList::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFileList::_move(FXint x,FXint y){ FXFileList::move(x,y); }

void FXPyFileList::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFileList::_position(FXint x,FXint y,FXint w,FXint h){ FXFileList::position(x,y,w,h); }

FXbool FXPyFileList::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFileList::_canFocus() const { return FXFileList::canFocus(); }

void FXPyFileList::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFileList::_setFocus(){ FXFileList::setFocus(); }

void FXPyFileList::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFileList::_killFocus(){ FXFileList::killFocus(); }

void FXPyFileList::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFileList::_setDefault(FXbool enable){ FXFileList::setDefault(enable); }

FXbool FXPyFileList::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFileList::_contains(FXint x,FXint y) const { return FXFileList::contains(x,y); }

FXbool FXPyFileList::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFileList::_doesSaveUnder() const { return FXFileList::doesSaveUnder(); }

void FXPyFileList::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFileList::_reparent(FXComposite* newparent) { FXFileList::reparent(newparent); }

void FXPyFileList::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFileList::_setBackColor(FXColor clr) { FXFileList::setBackColor(clr); }

FXint FXPyFileList::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyFileList::_getContentWidth() { return FXFileList::getContentWidth(); }

FXint FXPyFileList::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyFileList::_getContentHeight() { return FXFileList::getContentHeight(); }

FXint FXPyFileList::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyFileList::_getViewportWidth() { return FXFileList::getViewportWidth(); }

FXint FXPyFileList::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyFileList::_getViewportHeight() { return FXFileList::getViewportHeight(); }

void FXPyFileList::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyFileList::_moveContents(FXint x,FXint y) { FXFileList::moveContents(x,y); }

long FXPyDirBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDirBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDirBox::onDefault(sender,sel,ptr);
  }

void FXPyDirBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDirBox::_create(){ FXDirBox::create(); }

void FXPyDirBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDirBox::_destroy(){ FXDirBox::destroy(); }

void FXPyDirBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDirBox::_detach(){ FXDirBox::detach(); }

void FXPyDirBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDirBox::_resize(FXint w,FXint h){ FXDirBox::resize(w,h); }

void FXPyDirBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDirBox::_enable(){ FXDirBox::enable(); }

void FXPyDirBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDirBox::_disable(){ FXDirBox::disable(); }

void FXPyDirBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDirBox::_show(){ FXDirBox::show(); }

void FXPyDirBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDirBox::_hide(){ FXDirBox::hide(); }

void FXPyDirBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDirBox::_lowerWindow(){ FXDirBox::lower(); }

FXint FXPyDirBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDirBox::_getDefaultHeight() { return FXDirBox::getDefaultHeight(); }

FXint FXPyDirBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDirBox::_getDefaultWidth() { return FXDirBox::getDefaultWidth(); }

FXint FXPyDirBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDirBox::_getWidthForHeight(FXint h) { return FXDirBox::getWidthForHeight(h); }

FXint FXPyDirBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDirBox::_getHeightForWidth(FXint w) { return FXDirBox::getHeightForWidth(w); }

void FXPyDirBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDirBox::_layout() { FXDirBox::layout(); }

void FXPyDirBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDirBox::_recalc() { FXDirBox::recalc(); }

FXbool FXPyDirBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDirBox::_isComposite() const { return FXDirBox::isComposite(); }

void FXPyDirBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDirBox::_move(FXint x,FXint y){ FXDirBox::move(x,y); }

void FXPyDirBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDirBox::_position(FXint x,FXint y,FXint w,FXint h){ FXDirBox::position(x,y,w,h); }

FXbool FXPyDirBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDirBox::_canFocus() const { return FXDirBox::canFocus(); }

void FXPyDirBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDirBox::_setFocus(){ FXDirBox::setFocus(); }

void FXPyDirBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDirBox::_killFocus(){ FXDirBox::killFocus(); }

void FXPyDirBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDirBox::_setDefault(FXbool enable){ FXDirBox::setDefault(enable); }

FXbool FXPyDirBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDirBox::_contains(FXint x,FXint y) const { return FXDirBox::contains(x,y); }

FXbool FXPyDirBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDirBox::_doesSaveUnder() const { return FXDirBox::doesSaveUnder(); }

void FXPyDirBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDirBox::_reparent(FXComposite* newparent) { FXDirBox::reparent(newparent); }

void FXPyDirBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDirBox::_setBackColor(FXColor clr) { FXDirBox::setBackColor(clr); }

long FXPyFileSelector::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFileSelector::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFileSelector::onDefault(sender,sel,ptr);
  }

void FXPyFileSelector::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFileSelector::_create(){ FXFileSelector::create(); }

void FXPyFileSelector::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFileSelector::_destroy(){ FXFileSelector::destroy(); }

void FXPyFileSelector::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFileSelector::_detach(){ FXFileSelector::detach(); }

void FXPyFileSelector::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFileSelector::_resize(FXint w,FXint h){ FXFileSelector::resize(w,h); }

void FXPyFileSelector::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFileSelector::_enable(){ FXFileSelector::enable(); }

void FXPyFileSelector::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFileSelector::_disable(){ FXFileSelector::disable(); }

void FXPyFileSelector::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFileSelector::_show(){ FXFileSelector::show(); }

void FXPyFileSelector::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFileSelector::_hide(){ FXFileSelector::hide(); }

void FXPyFileSelector::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFileSelector::_lowerWindow(){ FXFileSelector::lower(); }

FXint FXPyFileSelector::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFileSelector::_getDefaultHeight() { return FXFileSelector::getDefaultHeight(); }

FXint FXPyFileSelector::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFileSelector::_getDefaultWidth() { return FXFileSelector::getDefaultWidth(); }

FXint FXPyFileSelector::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFileSelector::_getWidthForHeight(FXint h) { return FXFileSelector::getWidthForHeight(h); }

FXint FXPyFileSelector::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFileSelector::_getHeightForWidth(FXint w) { return FXFileSelector::getHeightForWidth(w); }

void FXPyFileSelector::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFileSelector::_layout() { FXFileSelector::layout(); }

void FXPyFileSelector::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFileSelector::_recalc() { FXFileSelector::recalc(); }

FXbool FXPyFileSelector::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFileSelector::_isComposite() const { return FXFileSelector::isComposite(); }

void FXPyFileSelector::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFileSelector::_move(FXint x,FXint y){ FXFileSelector::move(x,y); }

void FXPyFileSelector::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFileSelector::_position(FXint x,FXint y,FXint w,FXint h){ FXFileSelector::position(x,y,w,h); }

FXbool FXPyFileSelector::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFileSelector::_canFocus() const { return FXFileSelector::canFocus(); }

void FXPyFileSelector::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFileSelector::_setFocus(){ FXFileSelector::setFocus(); }

void FXPyFileSelector::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFileSelector::_killFocus(){ FXFileSelector::killFocus(); }

void FXPyFileSelector::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFileSelector::_setDefault(FXbool enable){ FXFileSelector::setDefault(enable); }

FXbool FXPyFileSelector::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFileSelector::_contains(FXint x,FXint y) const { return FXFileSelector::contains(x,y); }

FXbool FXPyFileSelector::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFileSelector::_doesSaveUnder() const { return FXFileSelector::doesSaveUnder(); }

void FXPyFileSelector::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFileSelector::_reparent(FXComposite* newparent) { FXFileSelector::reparent(newparent); }

void FXPyFileSelector::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFileSelector::_setBackColor(FXColor clr) { FXFileSelector::setBackColor(clr); }

long FXPyFileDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFileDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFileDialog::onDefault(sender,sel,ptr);
  }

void FXPyFileDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFileDialog::_create(){ FXFileDialog::create(); }

void FXPyFileDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFileDialog::_destroy(){ FXFileDialog::destroy(); }

void FXPyFileDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFileDialog::_detach(){ FXFileDialog::detach(); }

void FXPyFileDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFileDialog::_resize(FXint w,FXint h){ FXFileDialog::resize(w,h); }

void FXPyFileDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFileDialog::_enable(){ FXFileDialog::enable(); }

void FXPyFileDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFileDialog::_disable(){ FXFileDialog::disable(); }

void FXPyFileDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFileDialog::_show(){ FXFileDialog::show(); }

void FXPyFileDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFileDialog::_hide(){ FXFileDialog::hide(); }

void FXPyFileDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFileDialog::_lowerWindow(){ FXFileDialog::lower(); }

FXint FXPyFileDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFileDialog::_getDefaultHeight() { return FXFileDialog::getDefaultHeight(); }

FXint FXPyFileDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFileDialog::_getDefaultWidth() { return FXFileDialog::getDefaultWidth(); }

FXint FXPyFileDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFileDialog::_getWidthForHeight(FXint h) { return FXFileDialog::getWidthForHeight(h); }

FXint FXPyFileDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFileDialog::_getHeightForWidth(FXint w) { return FXFileDialog::getHeightForWidth(w); }

void FXPyFileDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFileDialog::_layout() { FXFileDialog::layout(); }

void FXPyFileDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFileDialog::_recalc() { FXFileDialog::recalc(); }

FXbool FXPyFileDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFileDialog::_isComposite() const { return FXFileDialog::isComposite(); }

void FXPyFileDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFileDialog::_move(FXint x,FXint y){ FXFileDialog::move(x,y); }

void FXPyFileDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFileDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXFileDialog::position(x,y,w,h); }

FXbool FXPyFileDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFileDialog::_canFocus() const { return FXFileDialog::canFocus(); }

void FXPyFileDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFileDialog::_setFocus(){ FXFileDialog::setFocus(); }

void FXPyFileDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFileDialog::_killFocus(){ FXFileDialog::killFocus(); }

void FXPyFileDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFileDialog::_setDefault(FXbool enable){ FXFileDialog::setDefault(enable); }

FXbool FXPyFileDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFileDialog::_contains(FXint x,FXint y) const { return FXFileDialog::contains(x,y); }

FXbool FXPyFileDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFileDialog::_doesSaveUnder() const { return FXFileDialog::doesSaveUnder(); }

void FXPyFileDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFileDialog::_reparent(FXComposite* newparent) { FXFileDialog::reparent(newparent); }

void FXPyFileDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFileDialog::_setBackColor(FXColor clr) { FXFileDialog::setBackColor(clr); }

void FXPyFileDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyFileDialog::_iconify() { FXFileDialog::iconify(); }

void FXPyFileDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyFileDialog::_deiconify() { FXFileDialog::deiconify(); }

void FXPyFileDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyFileDialog::_show(FXuint placement) { FXFileDialog::show(placement); }

long FXPyColorSelector::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyColorSelector::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXColorSelector::onDefault(sender,sel,ptr);
  }

void FXPyColorSelector::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyColorSelector::_create(){ FXColorSelector::create(); }

void FXPyColorSelector::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyColorSelector::_destroy(){ FXColorSelector::destroy(); }

void FXPyColorSelector::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyColorSelector::_detach(){ FXColorSelector::detach(); }

void FXPyColorSelector::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyColorSelector::_resize(FXint w,FXint h){ FXColorSelector::resize(w,h); }

void FXPyColorSelector::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyColorSelector::_enable(){ FXColorSelector::enable(); }

void FXPyColorSelector::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyColorSelector::_disable(){ FXColorSelector::disable(); }

void FXPyColorSelector::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyColorSelector::_show(){ FXColorSelector::show(); }

void FXPyColorSelector::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyColorSelector::_hide(){ FXColorSelector::hide(); }

void FXPyColorSelector::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyColorSelector::_lowerWindow(){ FXColorSelector::lower(); }

FXint FXPyColorSelector::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyColorSelector::_getDefaultHeight() { return FXColorSelector::getDefaultHeight(); }

FXint FXPyColorSelector::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyColorSelector::_getDefaultWidth() { return FXColorSelector::getDefaultWidth(); }

FXint FXPyColorSelector::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyColorSelector::_getWidthForHeight(FXint h) { return FXColorSelector::getWidthForHeight(h); }

FXint FXPyColorSelector::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyColorSelector::_getHeightForWidth(FXint w) { return FXColorSelector::getHeightForWidth(w); }

void FXPyColorSelector::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyColorSelector::_layout() { FXColorSelector::layout(); }

void FXPyColorSelector::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyColorSelector::_recalc() { FXColorSelector::recalc(); }

FXbool FXPyColorSelector::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyColorSelector::_isComposite() const { return FXColorSelector::isComposite(); }

void FXPyColorSelector::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyColorSelector::_move(FXint x,FXint y){ FXColorSelector::move(x,y); }

void FXPyColorSelector::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyColorSelector::_position(FXint x,FXint y,FXint w,FXint h){ FXColorSelector::position(x,y,w,h); }

FXbool FXPyColorSelector::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyColorSelector::_canFocus() const { return FXColorSelector::canFocus(); }

void FXPyColorSelector::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyColorSelector::_setFocus(){ FXColorSelector::setFocus(); }

void FXPyColorSelector::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyColorSelector::_killFocus(){ FXColorSelector::killFocus(); }

void FXPyColorSelector::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyColorSelector::_setDefault(FXbool enable){ FXColorSelector::setDefault(enable); }

FXbool FXPyColorSelector::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyColorSelector::_contains(FXint x,FXint y) const { return FXColorSelector::contains(x,y); }

FXbool FXPyColorSelector::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyColorSelector::_doesSaveUnder() const { return FXColorSelector::doesSaveUnder(); }

void FXPyColorSelector::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyColorSelector::_reparent(FXComposite* newparent) { FXColorSelector::reparent(newparent); }

void FXPyColorSelector::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyColorSelector::_setBackColor(FXColor clr) { FXColorSelector::setBackColor(clr); }

long FXPyColorDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyColorDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXColorDialog::onDefault(sender,sel,ptr);
  }

void FXPyColorDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyColorDialog::_create(){ FXColorDialog::create(); }

void FXPyColorDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyColorDialog::_destroy(){ FXColorDialog::destroy(); }

void FXPyColorDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyColorDialog::_detach(){ FXColorDialog::detach(); }

void FXPyColorDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyColorDialog::_resize(FXint w,FXint h){ FXColorDialog::resize(w,h); }

void FXPyColorDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyColorDialog::_enable(){ FXColorDialog::enable(); }

void FXPyColorDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyColorDialog::_disable(){ FXColorDialog::disable(); }

void FXPyColorDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyColorDialog::_show(){ FXColorDialog::show(); }

void FXPyColorDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyColorDialog::_hide(){ FXColorDialog::hide(); }

void FXPyColorDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyColorDialog::_lowerWindow(){ FXColorDialog::lower(); }

FXint FXPyColorDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyColorDialog::_getDefaultHeight() { return FXColorDialog::getDefaultHeight(); }

FXint FXPyColorDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyColorDialog::_getDefaultWidth() { return FXColorDialog::getDefaultWidth(); }

FXint FXPyColorDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyColorDialog::_getWidthForHeight(FXint h) { return FXColorDialog::getWidthForHeight(h); }

FXint FXPyColorDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyColorDialog::_getHeightForWidth(FXint w) { return FXColorDialog::getHeightForWidth(w); }

void FXPyColorDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyColorDialog::_layout() { FXColorDialog::layout(); }

void FXPyColorDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyColorDialog::_recalc() { FXColorDialog::recalc(); }

FXbool FXPyColorDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyColorDialog::_isComposite() const { return FXColorDialog::isComposite(); }

void FXPyColorDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyColorDialog::_move(FXint x,FXint y){ FXColorDialog::move(x,y); }

void FXPyColorDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyColorDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXColorDialog::position(x,y,w,h); }

FXbool FXPyColorDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyColorDialog::_canFocus() const { return FXColorDialog::canFocus(); }

void FXPyColorDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyColorDialog::_setFocus(){ FXColorDialog::setFocus(); }

void FXPyColorDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyColorDialog::_killFocus(){ FXColorDialog::killFocus(); }

void FXPyColorDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyColorDialog::_setDefault(FXbool enable){ FXColorDialog::setDefault(enable); }

FXbool FXPyColorDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyColorDialog::_contains(FXint x,FXint y) const { return FXColorDialog::contains(x,y); }

FXbool FXPyColorDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyColorDialog::_doesSaveUnder() const { return FXColorDialog::doesSaveUnder(); }

void FXPyColorDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyColorDialog::_reparent(FXComposite* newparent) { FXColorDialog::reparent(newparent); }

void FXPyColorDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyColorDialog::_setBackColor(FXColor clr) { FXColorDialog::setBackColor(clr); }

void FXPyColorDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyColorDialog::_iconify() { FXColorDialog::iconify(); }

void FXPyColorDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyColorDialog::_deiconify() { FXColorDialog::deiconify(); }

void FXPyColorDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyColorDialog::_show(FXuint placement) { FXColorDialog::show(placement); }

long FXPyFontSelector::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFontSelector::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFontSelector::onDefault(sender,sel,ptr);
  }

void FXPyFontSelector::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFontSelector::_create(){ FXFontSelector::create(); }

void FXPyFontSelector::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFontSelector::_destroy(){ FXFontSelector::destroy(); }

void FXPyFontSelector::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFontSelector::_detach(){ FXFontSelector::detach(); }

void FXPyFontSelector::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFontSelector::_resize(FXint w,FXint h){ FXFontSelector::resize(w,h); }

void FXPyFontSelector::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFontSelector::_enable(){ FXFontSelector::enable(); }

void FXPyFontSelector::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFontSelector::_disable(){ FXFontSelector::disable(); }

void FXPyFontSelector::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFontSelector::_show(){ FXFontSelector::show(); }

void FXPyFontSelector::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFontSelector::_hide(){ FXFontSelector::hide(); }

void FXPyFontSelector::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFontSelector::_lowerWindow(){ FXFontSelector::lower(); }

FXint FXPyFontSelector::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFontSelector::_getDefaultHeight() { return FXFontSelector::getDefaultHeight(); }

FXint FXPyFontSelector::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFontSelector::_getDefaultWidth() { return FXFontSelector::getDefaultWidth(); }

FXint FXPyFontSelector::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFontSelector::_getWidthForHeight(FXint h) { return FXFontSelector::getWidthForHeight(h); }

FXint FXPyFontSelector::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFontSelector::_getHeightForWidth(FXint w) { return FXFontSelector::getHeightForWidth(w); }

void FXPyFontSelector::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFontSelector::_layout() { FXFontSelector::layout(); }

void FXPyFontSelector::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFontSelector::_recalc() { FXFontSelector::recalc(); }

FXbool FXPyFontSelector::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFontSelector::_isComposite() const { return FXFontSelector::isComposite(); }

void FXPyFontSelector::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFontSelector::_move(FXint x,FXint y){ FXFontSelector::move(x,y); }

void FXPyFontSelector::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFontSelector::_position(FXint x,FXint y,FXint w,FXint h){ FXFontSelector::position(x,y,w,h); }

FXbool FXPyFontSelector::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFontSelector::_canFocus() const { return FXFontSelector::canFocus(); }

void FXPyFontSelector::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFontSelector::_setFocus(){ FXFontSelector::setFocus(); }

void FXPyFontSelector::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFontSelector::_killFocus(){ FXFontSelector::killFocus(); }

void FXPyFontSelector::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFontSelector::_setDefault(FXbool enable){ FXFontSelector::setDefault(enable); }

FXbool FXPyFontSelector::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFontSelector::_contains(FXint x,FXint y) const { return FXFontSelector::contains(x,y); }

FXbool FXPyFontSelector::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFontSelector::_doesSaveUnder() const { return FXFontSelector::doesSaveUnder(); }

void FXPyFontSelector::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFontSelector::_reparent(FXComposite* newparent) { FXFontSelector::reparent(newparent); }

void FXPyFontSelector::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFontSelector::_setBackColor(FXColor clr) { FXFontSelector::setBackColor(clr); }

long FXPyFontDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFontDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFontDialog::onDefault(sender,sel,ptr);
  }

void FXPyFontDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyFontDialog::_create(){ FXFontDialog::create(); }

void FXPyFontDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyFontDialog::_destroy(){ FXFontDialog::destroy(); }

void FXPyFontDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyFontDialog::_detach(){ FXFontDialog::detach(); }

void FXPyFontDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyFontDialog::_resize(FXint w,FXint h){ FXFontDialog::resize(w,h); }

void FXPyFontDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyFontDialog::_enable(){ FXFontDialog::enable(); }

void FXPyFontDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyFontDialog::_disable(){ FXFontDialog::disable(); }

void FXPyFontDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyFontDialog::_show(){ FXFontDialog::show(); }

void FXPyFontDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyFontDialog::_hide(){ FXFontDialog::hide(); }

void FXPyFontDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyFontDialog::_lowerWindow(){ FXFontDialog::lower(); }

FXint FXPyFontDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyFontDialog::_getDefaultHeight() { return FXFontDialog::getDefaultHeight(); }

FXint FXPyFontDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyFontDialog::_getDefaultWidth() { return FXFontDialog::getDefaultWidth(); }

FXint FXPyFontDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyFontDialog::_getWidthForHeight(FXint h) { return FXFontDialog::getWidthForHeight(h); }

FXint FXPyFontDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyFontDialog::_getHeightForWidth(FXint w) { return FXFontDialog::getHeightForWidth(w); }

void FXPyFontDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyFontDialog::_layout() { FXFontDialog::layout(); }

void FXPyFontDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyFontDialog::_recalc() { FXFontDialog::recalc(); }

FXbool FXPyFontDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyFontDialog::_isComposite() const { return FXFontDialog::isComposite(); }

void FXPyFontDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyFontDialog::_move(FXint x,FXint y){ FXFontDialog::move(x,y); }

void FXPyFontDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyFontDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXFontDialog::position(x,y,w,h); }

FXbool FXPyFontDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyFontDialog::_canFocus() const { return FXFontDialog::canFocus(); }

void FXPyFontDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyFontDialog::_setFocus(){ FXFontDialog::setFocus(); }

void FXPyFontDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyFontDialog::_killFocus(){ FXFontDialog::killFocus(); }

void FXPyFontDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyFontDialog::_setDefault(FXbool enable){ FXFontDialog::setDefault(enable); }

FXbool FXPyFontDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyFontDialog::_contains(FXint x,FXint y) const { return FXFontDialog::contains(x,y); }

FXbool FXPyFontDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyFontDialog::_doesSaveUnder() const { return FXFontDialog::doesSaveUnder(); }

void FXPyFontDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyFontDialog::_reparent(FXComposite* newparent) { FXFontDialog::reparent(newparent); }

void FXPyFontDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyFontDialog::_setBackColor(FXColor clr) { FXFontDialog::setBackColor(clr); }

void FXPyFontDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyFontDialog::_iconify() { FXFontDialog::iconify(); }

void FXPyFontDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyFontDialog::_deiconify() { FXFontDialog::deiconify(); }

void FXPyFontDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyFontDialog::_show(FXuint placement) { FXFontDialog::show(placement); }

long FXPyText::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyText::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXText::onDefault(sender,sel,ptr);
  }

void FXPyText::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyText::_create(){ FXText::create(); }

void FXPyText::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyText::_destroy(){ FXText::destroy(); }

void FXPyText::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyText::_detach(){ FXText::detach(); }

void FXPyText::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyText::_resize(FXint w,FXint h){ FXText::resize(w,h); }

void FXPyText::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyText::_enable(){ FXText::enable(); }

void FXPyText::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyText::_disable(){ FXText::disable(); }

void FXPyText::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyText::_show(){ FXText::show(); }

void FXPyText::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyText::_hide(){ FXText::hide(); }

void FXPyText::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyText::_lowerWindow(){ FXText::lower(); }

FXint FXPyText::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyText::_getDefaultHeight() { return FXText::getDefaultHeight(); }

FXint FXPyText::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyText::_getDefaultWidth() { return FXText::getDefaultWidth(); }

FXint FXPyText::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyText::_getWidthForHeight(FXint h) { return FXText::getWidthForHeight(h); }

FXint FXPyText::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyText::_getHeightForWidth(FXint w) { return FXText::getHeightForWidth(w); }

void FXPyText::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyText::_layout() { FXText::layout(); }

void FXPyText::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyText::_recalc() { FXText::recalc(); }

FXbool FXPyText::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyText::_isComposite() const { return FXText::isComposite(); }

void FXPyText::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyText::_move(FXint x,FXint y){ FXText::move(x,y); }

void FXPyText::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyText::_position(FXint x,FXint y,FXint w,FXint h){ FXText::position(x,y,w,h); }

FXbool FXPyText::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyText::_canFocus() const { return FXText::canFocus(); }

void FXPyText::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyText::_setFocus(){ FXText::setFocus(); }

void FXPyText::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyText::_killFocus(){ FXText::killFocus(); }

void FXPyText::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyText::_setDefault(FXbool enable){ FXText::setDefault(enable); }

FXbool FXPyText::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyText::_contains(FXint x,FXint y) const { return FXText::contains(x,y); }

FXbool FXPyText::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyText::_doesSaveUnder() const { return FXText::doesSaveUnder(); }

void FXPyText::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyText::_reparent(FXComposite* newparent) { FXText::reparent(newparent); }

void FXPyText::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyText::_setBackColor(FXColor clr) { FXText::setBackColor(clr); }

FXint FXPyText::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyText::_getContentWidth() { return FXText::getContentWidth(); }

FXint FXPyText::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyText::_getContentHeight() { return FXText::getContentHeight(); }

FXint FXPyText::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyText::_getViewportWidth() { return FXText::getViewportWidth(); }

FXint FXPyText::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyText::_getViewportHeight() { return FXText::getViewportHeight(); }

void FXPyText::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyText::_moveContents(FXint x,FXint y) { FXText::moveContents(x,y); }

void FXPyText::setCursorPos(FXint pos,FXbool notify) { FXPyCallVoidFunction(this,"setCursorPos",pos,notify); }
void FXPyText::_setCursorPos(FXint pos,FXbool notify) { FXText::setCursorPos(pos,notify); }

FXbool FXPyText::extendSelection(FXint pos,FXTextSelectionMode mode,FXbool notify) { return FXPyCallBoolFunction(this,"extendSelection",pos,mode,notify); }
FXbool FXPyText::_extendSelection(FXint pos,FXTextSelectionMode mode,FXbool notify) { return FXText::extendSelection(pos,mode,notify); }

FXbool FXPyText::killSelection(FXbool notify) { return FXPyCallBoolFunction(this,"killSelection",notify); }
FXbool FXPyText::_killSelection(FXbool notify) { return FXText::killSelection(notify); }

long FXPyDocument::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDocument::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDocument::onDefault(sender,sel,ptr);
  }

long FXPyMDIDeleteButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIDeleteButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIDeleteButton::onDefault(sender,sel,ptr);
  }

void FXPyMDIDeleteButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIDeleteButton::_create(){ FXMDIDeleteButton::create(); }

void FXPyMDIDeleteButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIDeleteButton::_destroy(){ FXMDIDeleteButton::destroy(); }

void FXPyMDIDeleteButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIDeleteButton::_detach(){ FXMDIDeleteButton::detach(); }

void FXPyMDIDeleteButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIDeleteButton::_resize(FXint w,FXint h){ FXMDIDeleteButton::resize(w,h); }

void FXPyMDIDeleteButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIDeleteButton::_enable(){ FXMDIDeleteButton::enable(); }

void FXPyMDIDeleteButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIDeleteButton::_disable(){ FXMDIDeleteButton::disable(); }

void FXPyMDIDeleteButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIDeleteButton::_show(){ FXMDIDeleteButton::show(); }

void FXPyMDIDeleteButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIDeleteButton::_hide(){ FXMDIDeleteButton::hide(); }

void FXPyMDIDeleteButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIDeleteButton::_lowerWindow(){ FXMDIDeleteButton::lower(); }

FXint FXPyMDIDeleteButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIDeleteButton::_getDefaultHeight() { return FXMDIDeleteButton::getDefaultHeight(); }

FXint FXPyMDIDeleteButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIDeleteButton::_getDefaultWidth() { return FXMDIDeleteButton::getDefaultWidth(); }

FXint FXPyMDIDeleteButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIDeleteButton::_getWidthForHeight(FXint h) { return FXMDIDeleteButton::getWidthForHeight(h); }

FXint FXPyMDIDeleteButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIDeleteButton::_getHeightForWidth(FXint w) { return FXMDIDeleteButton::getHeightForWidth(w); }

void FXPyMDIDeleteButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIDeleteButton::_layout() { FXMDIDeleteButton::layout(); }

void FXPyMDIDeleteButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIDeleteButton::_recalc() { FXMDIDeleteButton::recalc(); }

FXbool FXPyMDIDeleteButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIDeleteButton::_isComposite() const { return FXMDIDeleteButton::isComposite(); }

void FXPyMDIDeleteButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIDeleteButton::_move(FXint x,FXint y){ FXMDIDeleteButton::move(x,y); }

void FXPyMDIDeleteButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIDeleteButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIDeleteButton::position(x,y,w,h); }

FXbool FXPyMDIDeleteButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIDeleteButton::_canFocus() const { return FXMDIDeleteButton::canFocus(); }

void FXPyMDIDeleteButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIDeleteButton::_setFocus(){ FXMDIDeleteButton::setFocus(); }

void FXPyMDIDeleteButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIDeleteButton::_killFocus(){ FXMDIDeleteButton::killFocus(); }

void FXPyMDIDeleteButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIDeleteButton::_setDefault(FXbool enable){ FXMDIDeleteButton::setDefault(enable); }

FXbool FXPyMDIDeleteButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIDeleteButton::_contains(FXint x,FXint y) const { return FXMDIDeleteButton::contains(x,y); }

FXbool FXPyMDIDeleteButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIDeleteButton::_doesSaveUnder() const { return FXMDIDeleteButton::doesSaveUnder(); }

void FXPyMDIDeleteButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIDeleteButton::_reparent(FXComposite* newparent) { FXMDIDeleteButton::reparent(newparent); }

void FXPyMDIDeleteButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIDeleteButton::_setBackColor(FXColor clr) { FXMDIDeleteButton::setBackColor(clr); }

long FXPyMDIMaximizeButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIMaximizeButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIMaximizeButton::onDefault(sender,sel,ptr);
  }

void FXPyMDIMaximizeButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIMaximizeButton::_create(){ FXMDIMaximizeButton::create(); }

void FXPyMDIMaximizeButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIMaximizeButton::_destroy(){ FXMDIMaximizeButton::destroy(); }

void FXPyMDIMaximizeButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIMaximizeButton::_detach(){ FXMDIMaximizeButton::detach(); }

void FXPyMDIMaximizeButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIMaximizeButton::_resize(FXint w,FXint h){ FXMDIMaximizeButton::resize(w,h); }

void FXPyMDIMaximizeButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIMaximizeButton::_enable(){ FXMDIMaximizeButton::enable(); }

void FXPyMDIMaximizeButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIMaximizeButton::_disable(){ FXMDIMaximizeButton::disable(); }

void FXPyMDIMaximizeButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIMaximizeButton::_show(){ FXMDIMaximizeButton::show(); }

void FXPyMDIMaximizeButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIMaximizeButton::_hide(){ FXMDIMaximizeButton::hide(); }

void FXPyMDIMaximizeButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIMaximizeButton::_lowerWindow(){ FXMDIMaximizeButton::lower(); }

FXint FXPyMDIMaximizeButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIMaximizeButton::_getDefaultHeight() { return FXMDIMaximizeButton::getDefaultHeight(); }

FXint FXPyMDIMaximizeButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIMaximizeButton::_getDefaultWidth() { return FXMDIMaximizeButton::getDefaultWidth(); }

FXint FXPyMDIMaximizeButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIMaximizeButton::_getWidthForHeight(FXint h) { return FXMDIMaximizeButton::getWidthForHeight(h); }

FXint FXPyMDIMaximizeButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIMaximizeButton::_getHeightForWidth(FXint w) { return FXMDIMaximizeButton::getHeightForWidth(w); }

void FXPyMDIMaximizeButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIMaximizeButton::_layout() { FXMDIMaximizeButton::layout(); }

void FXPyMDIMaximizeButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIMaximizeButton::_recalc() { FXMDIMaximizeButton::recalc(); }

FXbool FXPyMDIMaximizeButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIMaximizeButton::_isComposite() const { return FXMDIMaximizeButton::isComposite(); }

void FXPyMDIMaximizeButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIMaximizeButton::_move(FXint x,FXint y){ FXMDIMaximizeButton::move(x,y); }

void FXPyMDIMaximizeButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIMaximizeButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIMaximizeButton::position(x,y,w,h); }

FXbool FXPyMDIMaximizeButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIMaximizeButton::_canFocus() const { return FXMDIMaximizeButton::canFocus(); }

void FXPyMDIMaximizeButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIMaximizeButton::_setFocus(){ FXMDIMaximizeButton::setFocus(); }

void FXPyMDIMaximizeButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIMaximizeButton::_killFocus(){ FXMDIMaximizeButton::killFocus(); }

void FXPyMDIMaximizeButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIMaximizeButton::_setDefault(FXbool enable){ FXMDIMaximizeButton::setDefault(enable); }

FXbool FXPyMDIMaximizeButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIMaximizeButton::_contains(FXint x,FXint y) const { return FXMDIMaximizeButton::contains(x,y); }

FXbool FXPyMDIMaximizeButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIMaximizeButton::_doesSaveUnder() const { return FXMDIMaximizeButton::doesSaveUnder(); }

void FXPyMDIMaximizeButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIMaximizeButton::_reparent(FXComposite* newparent) { FXMDIMaximizeButton::reparent(newparent); }

void FXPyMDIMaximizeButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIMaximizeButton::_setBackColor(FXColor clr) { FXMDIMaximizeButton::setBackColor(clr); }

long FXPyMDIMenu::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIMenu::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIMenu::onDefault(sender,sel,ptr);
  }

void FXPyMDIMenu::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIMenu::_create(){ FXMDIMenu::create(); }

void FXPyMDIMenu::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIMenu::_destroy(){ FXMDIMenu::destroy(); }

void FXPyMDIMenu::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIMenu::_detach(){ FXMDIMenu::detach(); }

void FXPyMDIMenu::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIMenu::_resize(FXint w,FXint h){ FXMDIMenu::resize(w,h); }

void FXPyMDIMenu::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIMenu::_enable(){ FXMDIMenu::enable(); }

void FXPyMDIMenu::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIMenu::_disable(){ FXMDIMenu::disable(); }

void FXPyMDIMenu::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIMenu::_show(){ FXMDIMenu::show(); }

void FXPyMDIMenu::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIMenu::_hide(){ FXMDIMenu::hide(); }

void FXPyMDIMenu::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIMenu::_lowerWindow(){ FXMDIMenu::lower(); }

FXint FXPyMDIMenu::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIMenu::_getDefaultHeight() { return FXMDIMenu::getDefaultHeight(); }

FXint FXPyMDIMenu::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIMenu::_getDefaultWidth() { return FXMDIMenu::getDefaultWidth(); }

FXint FXPyMDIMenu::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIMenu::_getWidthForHeight(FXint h) { return FXMDIMenu::getWidthForHeight(h); }

FXint FXPyMDIMenu::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIMenu::_getHeightForWidth(FXint w) { return FXMDIMenu::getHeightForWidth(w); }

void FXPyMDIMenu::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIMenu::_layout() { FXMDIMenu::layout(); }

void FXPyMDIMenu::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIMenu::_recalc() { FXMDIMenu::recalc(); }

FXbool FXPyMDIMenu::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIMenu::_isComposite() const { return FXMDIMenu::isComposite(); }

void FXPyMDIMenu::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIMenu::_move(FXint x,FXint y){ FXMDIMenu::move(x,y); }

void FXPyMDIMenu::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIMenu::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIMenu::position(x,y,w,h); }

FXbool FXPyMDIMenu::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIMenu::_canFocus() const { return FXMDIMenu::canFocus(); }

void FXPyMDIMenu::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIMenu::_setFocus(){ FXMDIMenu::setFocus(); }

void FXPyMDIMenu::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIMenu::_killFocus(){ FXMDIMenu::killFocus(); }

void FXPyMDIMenu::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIMenu::_setDefault(FXbool enable){ FXMDIMenu::setDefault(enable); }

FXbool FXPyMDIMenu::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIMenu::_contains(FXint x,FXint y) const { return FXMDIMenu::contains(x,y); }

FXbool FXPyMDIMenu::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIMenu::_doesSaveUnder() const { return FXMDIMenu::doesSaveUnder(); }

void FXPyMDIMenu::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIMenu::_reparent(FXComposite* newparent) { FXMDIMenu::reparent(newparent); }

void FXPyMDIMenu::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIMenu::_setBackColor(FXColor clr) { FXMDIMenu::setBackColor(clr); }

long FXPyMDIMinimizeButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIMinimizeButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIMinimizeButton::onDefault(sender,sel,ptr);
  }

void FXPyMDIMinimizeButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIMinimizeButton::_create(){ FXMDIMinimizeButton::create(); }

void FXPyMDIMinimizeButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIMinimizeButton::_destroy(){ FXMDIMinimizeButton::destroy(); }

void FXPyMDIMinimizeButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIMinimizeButton::_detach(){ FXMDIMinimizeButton::detach(); }

void FXPyMDIMinimizeButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIMinimizeButton::_resize(FXint w,FXint h){ FXMDIMinimizeButton::resize(w,h); }

void FXPyMDIMinimizeButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIMinimizeButton::_enable(){ FXMDIMinimizeButton::enable(); }

void FXPyMDIMinimizeButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIMinimizeButton::_disable(){ FXMDIMinimizeButton::disable(); }

void FXPyMDIMinimizeButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIMinimizeButton::_show(){ FXMDIMinimizeButton::show(); }

void FXPyMDIMinimizeButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIMinimizeButton::_hide(){ FXMDIMinimizeButton::hide(); }

void FXPyMDIMinimizeButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIMinimizeButton::_lowerWindow(){ FXMDIMinimizeButton::lower(); }

FXint FXPyMDIMinimizeButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIMinimizeButton::_getDefaultHeight() { return FXMDIMinimizeButton::getDefaultHeight(); }

FXint FXPyMDIMinimizeButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIMinimizeButton::_getDefaultWidth() { return FXMDIMinimizeButton::getDefaultWidth(); }

FXint FXPyMDIMinimizeButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIMinimizeButton::_getWidthForHeight(FXint h) { return FXMDIMinimizeButton::getWidthForHeight(h); }

FXint FXPyMDIMinimizeButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIMinimizeButton::_getHeightForWidth(FXint w) { return FXMDIMinimizeButton::getHeightForWidth(w); }

void FXPyMDIMinimizeButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIMinimizeButton::_layout() { FXMDIMinimizeButton::layout(); }

void FXPyMDIMinimizeButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIMinimizeButton::_recalc() { FXMDIMinimizeButton::recalc(); }

FXbool FXPyMDIMinimizeButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIMinimizeButton::_isComposite() const { return FXMDIMinimizeButton::isComposite(); }

void FXPyMDIMinimizeButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIMinimizeButton::_move(FXint x,FXint y){ FXMDIMinimizeButton::move(x,y); }

void FXPyMDIMinimizeButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIMinimizeButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIMinimizeButton::position(x,y,w,h); }

FXbool FXPyMDIMinimizeButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIMinimizeButton::_canFocus() const { return FXMDIMinimizeButton::canFocus(); }

void FXPyMDIMinimizeButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIMinimizeButton::_setFocus(){ FXMDIMinimizeButton::setFocus(); }

void FXPyMDIMinimizeButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIMinimizeButton::_killFocus(){ FXMDIMinimizeButton::killFocus(); }

void FXPyMDIMinimizeButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIMinimizeButton::_setDefault(FXbool enable){ FXMDIMinimizeButton::setDefault(enable); }

FXbool FXPyMDIMinimizeButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIMinimizeButton::_contains(FXint x,FXint y) const { return FXMDIMinimizeButton::contains(x,y); }

FXbool FXPyMDIMinimizeButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIMinimizeButton::_doesSaveUnder() const { return FXMDIMinimizeButton::doesSaveUnder(); }

void FXPyMDIMinimizeButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIMinimizeButton::_reparent(FXComposite* newparent) { FXMDIMinimizeButton::reparent(newparent); }

void FXPyMDIMinimizeButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIMinimizeButton::_setBackColor(FXColor clr) { FXMDIMinimizeButton::setBackColor(clr); }

long FXPyMDIRestoreButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIRestoreButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIRestoreButton::onDefault(sender,sel,ptr);
  }

void FXPyMDIRestoreButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIRestoreButton::_create(){ FXMDIRestoreButton::create(); }

void FXPyMDIRestoreButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIRestoreButton::_destroy(){ FXMDIRestoreButton::destroy(); }

void FXPyMDIRestoreButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIRestoreButton::_detach(){ FXMDIRestoreButton::detach(); }

void FXPyMDIRestoreButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIRestoreButton::_resize(FXint w,FXint h){ FXMDIRestoreButton::resize(w,h); }

void FXPyMDIRestoreButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIRestoreButton::_enable(){ FXMDIRestoreButton::enable(); }

void FXPyMDIRestoreButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIRestoreButton::_disable(){ FXMDIRestoreButton::disable(); }

void FXPyMDIRestoreButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIRestoreButton::_show(){ FXMDIRestoreButton::show(); }

void FXPyMDIRestoreButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIRestoreButton::_hide(){ FXMDIRestoreButton::hide(); }

void FXPyMDIRestoreButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIRestoreButton::_lowerWindow(){ FXMDIRestoreButton::lower(); }

FXint FXPyMDIRestoreButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIRestoreButton::_getDefaultHeight() { return FXMDIRestoreButton::getDefaultHeight(); }

FXint FXPyMDIRestoreButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIRestoreButton::_getDefaultWidth() { return FXMDIRestoreButton::getDefaultWidth(); }

FXint FXPyMDIRestoreButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIRestoreButton::_getWidthForHeight(FXint h) { return FXMDIRestoreButton::getWidthForHeight(h); }

FXint FXPyMDIRestoreButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIRestoreButton::_getHeightForWidth(FXint w) { return FXMDIRestoreButton::getHeightForWidth(w); }

void FXPyMDIRestoreButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIRestoreButton::_layout() { FXMDIRestoreButton::layout(); }

void FXPyMDIRestoreButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIRestoreButton::_recalc() { FXMDIRestoreButton::recalc(); }

FXbool FXPyMDIRestoreButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIRestoreButton::_isComposite() const { return FXMDIRestoreButton::isComposite(); }

void FXPyMDIRestoreButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIRestoreButton::_move(FXint x,FXint y){ FXMDIRestoreButton::move(x,y); }

void FXPyMDIRestoreButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIRestoreButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIRestoreButton::position(x,y,w,h); }

FXbool FXPyMDIRestoreButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIRestoreButton::_canFocus() const { return FXMDIRestoreButton::canFocus(); }

void FXPyMDIRestoreButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIRestoreButton::_setFocus(){ FXMDIRestoreButton::setFocus(); }

void FXPyMDIRestoreButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIRestoreButton::_killFocus(){ FXMDIRestoreButton::killFocus(); }

void FXPyMDIRestoreButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIRestoreButton::_setDefault(FXbool enable){ FXMDIRestoreButton::setDefault(enable); }

FXbool FXPyMDIRestoreButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIRestoreButton::_contains(FXint x,FXint y) const { return FXMDIRestoreButton::contains(x,y); }

FXbool FXPyMDIRestoreButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIRestoreButton::_doesSaveUnder() const { return FXMDIRestoreButton::doesSaveUnder(); }

void FXPyMDIRestoreButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIRestoreButton::_reparent(FXComposite* newparent) { FXMDIRestoreButton::reparent(newparent); }

void FXPyMDIRestoreButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIRestoreButton::_setBackColor(FXColor clr) { FXMDIRestoreButton::setBackColor(clr); }

long FXPyMDIWindowButton::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIWindowButton::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIWindowButton::onDefault(sender,sel,ptr);
  }

void FXPyMDIWindowButton::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIWindowButton::_create(){ FXMDIWindowButton::create(); }

void FXPyMDIWindowButton::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIWindowButton::_destroy(){ FXMDIWindowButton::destroy(); }

void FXPyMDIWindowButton::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIWindowButton::_detach(){ FXMDIWindowButton::detach(); }

void FXPyMDIWindowButton::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIWindowButton::_resize(FXint w,FXint h){ FXMDIWindowButton::resize(w,h); }

void FXPyMDIWindowButton::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIWindowButton::_enable(){ FXMDIWindowButton::enable(); }

void FXPyMDIWindowButton::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIWindowButton::_disable(){ FXMDIWindowButton::disable(); }

void FXPyMDIWindowButton::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIWindowButton::_show(){ FXMDIWindowButton::show(); }

void FXPyMDIWindowButton::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIWindowButton::_hide(){ FXMDIWindowButton::hide(); }

void FXPyMDIWindowButton::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIWindowButton::_lowerWindow(){ FXMDIWindowButton::lower(); }

FXint FXPyMDIWindowButton::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIWindowButton::_getDefaultHeight() { return FXMDIWindowButton::getDefaultHeight(); }

FXint FXPyMDIWindowButton::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIWindowButton::_getDefaultWidth() { return FXMDIWindowButton::getDefaultWidth(); }

FXint FXPyMDIWindowButton::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIWindowButton::_getWidthForHeight(FXint h) { return FXMDIWindowButton::getWidthForHeight(h); }

FXint FXPyMDIWindowButton::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIWindowButton::_getHeightForWidth(FXint w) { return FXMDIWindowButton::getHeightForWidth(w); }

void FXPyMDIWindowButton::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIWindowButton::_layout() { FXMDIWindowButton::layout(); }

void FXPyMDIWindowButton::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIWindowButton::_recalc() { FXMDIWindowButton::recalc(); }

FXbool FXPyMDIWindowButton::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIWindowButton::_isComposite() const { return FXMDIWindowButton::isComposite(); }

void FXPyMDIWindowButton::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIWindowButton::_move(FXint x,FXint y){ FXMDIWindowButton::move(x,y); }

void FXPyMDIWindowButton::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIWindowButton::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIWindowButton::position(x,y,w,h); }

FXbool FXPyMDIWindowButton::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIWindowButton::_canFocus() const { return FXMDIWindowButton::canFocus(); }

void FXPyMDIWindowButton::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIWindowButton::_setFocus(){ FXMDIWindowButton::setFocus(); }

void FXPyMDIWindowButton::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIWindowButton::_killFocus(){ FXMDIWindowButton::killFocus(); }

void FXPyMDIWindowButton::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIWindowButton::_setDefault(FXbool enable){ FXMDIWindowButton::setDefault(enable); }

FXbool FXPyMDIWindowButton::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIWindowButton::_contains(FXint x,FXint y) const { return FXMDIWindowButton::contains(x,y); }

FXbool FXPyMDIWindowButton::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIWindowButton::_doesSaveUnder() const { return FXMDIWindowButton::doesSaveUnder(); }

void FXPyMDIWindowButton::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIWindowButton::_reparent(FXComposite* newparent) { FXMDIWindowButton::reparent(newparent); }

void FXPyMDIWindowButton::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIWindowButton::_setBackColor(FXColor clr) { FXMDIWindowButton::setBackColor(clr); }

long FXPyMDIClient::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIClient::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIClient::onDefault(sender,sel,ptr);
  }

void FXPyMDIClient::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIClient::_create(){ FXMDIClient::create(); }

void FXPyMDIClient::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIClient::_destroy(){ FXMDIClient::destroy(); }

void FXPyMDIClient::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIClient::_detach(){ FXMDIClient::detach(); }

void FXPyMDIClient::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIClient::_resize(FXint w,FXint h){ FXMDIClient::resize(w,h); }

void FXPyMDIClient::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIClient::_enable(){ FXMDIClient::enable(); }

void FXPyMDIClient::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIClient::_disable(){ FXMDIClient::disable(); }

void FXPyMDIClient::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIClient::_show(){ FXMDIClient::show(); }

void FXPyMDIClient::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIClient::_hide(){ FXMDIClient::hide(); }

void FXPyMDIClient::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIClient::_lowerWindow(){ FXMDIClient::lower(); }

FXint FXPyMDIClient::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIClient::_getDefaultHeight() { return FXMDIClient::getDefaultHeight(); }

FXint FXPyMDIClient::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIClient::_getDefaultWidth() { return FXMDIClient::getDefaultWidth(); }

FXint FXPyMDIClient::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIClient::_getWidthForHeight(FXint h) { return FXMDIClient::getWidthForHeight(h); }

FXint FXPyMDIClient::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIClient::_getHeightForWidth(FXint w) { return FXMDIClient::getHeightForWidth(w); }

void FXPyMDIClient::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIClient::_layout() { FXMDIClient::layout(); }

void FXPyMDIClient::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIClient::_recalc() { FXMDIClient::recalc(); }

FXbool FXPyMDIClient::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIClient::_isComposite() const { return FXMDIClient::isComposite(); }

void FXPyMDIClient::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIClient::_move(FXint x,FXint y){ FXMDIClient::move(x,y); }

void FXPyMDIClient::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIClient::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIClient::position(x,y,w,h); }

FXbool FXPyMDIClient::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIClient::_canFocus() const { return FXMDIClient::canFocus(); }

void FXPyMDIClient::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIClient::_setFocus(){ FXMDIClient::setFocus(); }

void FXPyMDIClient::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIClient::_killFocus(){ FXMDIClient::killFocus(); }

void FXPyMDIClient::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIClient::_setDefault(FXbool enable){ FXMDIClient::setDefault(enable); }

FXbool FXPyMDIClient::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIClient::_contains(FXint x,FXint y) const { return FXMDIClient::contains(x,y); }

FXbool FXPyMDIClient::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIClient::_doesSaveUnder() const { return FXMDIClient::doesSaveUnder(); }

void FXPyMDIClient::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIClient::_reparent(FXComposite* newparent) { FXMDIClient::reparent(newparent); }

void FXPyMDIClient::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIClient::_setBackColor(FXColor clr) { FXMDIClient::setBackColor(clr); }

FXint FXPyMDIClient::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyMDIClient::_getContentWidth() { return FXMDIClient::getContentWidth(); }

FXint FXPyMDIClient::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyMDIClient::_getContentHeight() { return FXMDIClient::getContentHeight(); }

FXint FXPyMDIClient::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyMDIClient::_getViewportWidth() { return FXMDIClient::getViewportWidth(); }

FXint FXPyMDIClient::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyMDIClient::_getViewportHeight() { return FXMDIClient::getViewportHeight(); }

void FXPyMDIClient::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyMDIClient::_moveContents(FXint x,FXint y) { FXMDIClient::moveContents(x,y); }

long FXPyMDIChild::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyMDIChild::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXMDIChild::onDefault(sender,sel,ptr);
  }

void FXPyMDIChild::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyMDIChild::_create(){ FXMDIChild::create(); }

void FXPyMDIChild::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyMDIChild::_destroy(){ FXMDIChild::destroy(); }

void FXPyMDIChild::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyMDIChild::_detach(){ FXMDIChild::detach(); }

void FXPyMDIChild::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyMDIChild::_resize(FXint w,FXint h){ FXMDIChild::resize(w,h); }

void FXPyMDIChild::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyMDIChild::_enable(){ FXMDIChild::enable(); }

void FXPyMDIChild::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyMDIChild::_disable(){ FXMDIChild::disable(); }

void FXPyMDIChild::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyMDIChild::_show(){ FXMDIChild::show(); }

void FXPyMDIChild::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyMDIChild::_hide(){ FXMDIChild::hide(); }

void FXPyMDIChild::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyMDIChild::_lowerWindow(){ FXMDIChild::lower(); }

FXint FXPyMDIChild::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyMDIChild::_getDefaultHeight() { return FXMDIChild::getDefaultHeight(); }

FXint FXPyMDIChild::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyMDIChild::_getDefaultWidth() { return FXMDIChild::getDefaultWidth(); }

FXint FXPyMDIChild::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyMDIChild::_getWidthForHeight(FXint h) { return FXMDIChild::getWidthForHeight(h); }

FXint FXPyMDIChild::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyMDIChild::_getHeightForWidth(FXint w) { return FXMDIChild::getHeightForWidth(w); }

void FXPyMDIChild::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyMDIChild::_layout() { FXMDIChild::layout(); }

void FXPyMDIChild::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyMDIChild::_recalc() { FXMDIChild::recalc(); }

FXbool FXPyMDIChild::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyMDIChild::_isComposite() const { return FXMDIChild::isComposite(); }

void FXPyMDIChild::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyMDIChild::_move(FXint x,FXint y){ FXMDIChild::move(x,y); }

void FXPyMDIChild::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyMDIChild::_position(FXint x,FXint y,FXint w,FXint h){ FXMDIChild::position(x,y,w,h); }

FXbool FXPyMDIChild::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyMDIChild::_canFocus() const { return FXMDIChild::canFocus(); }

void FXPyMDIChild::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyMDIChild::_setFocus(){ FXMDIChild::setFocus(); }

void FXPyMDIChild::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyMDIChild::_killFocus(){ FXMDIChild::killFocus(); }

void FXPyMDIChild::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyMDIChild::_setDefault(FXbool enable){ FXMDIChild::setDefault(enable); }

FXbool FXPyMDIChild::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyMDIChild::_contains(FXint x,FXint y) const { return FXMDIChild::contains(x,y); }

FXbool FXPyMDIChild::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyMDIChild::_doesSaveUnder() const { return FXMDIChild::doesSaveUnder(); }

void FXPyMDIChild::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyMDIChild::_reparent(FXComposite* newparent) { FXMDIChild::reparent(newparent); }

void FXPyMDIChild::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyMDIChild::_setBackColor(FXColor clr) { FXMDIChild::setBackColor(clr); }

void FXPyMDIChild::minimize(FXbool notify) { FXPyCallVoidFunction(this,"minimize",notify); }
void FXPyMDIChild::_minimize(FXbool notify) { FXMDIChild::minimize(notify); }

void FXPyMDIChild::maximize(FXbool notify) { FXPyCallVoidFunction(this,"maximize",notify); }
void FXPyMDIChild::_maximize(FXbool notify) { FXMDIChild::maximize(notify); }

void FXPyMDIChild::restore(FXbool notify) { FXPyCallVoidFunction(this,"restore",notify); }
void FXPyMDIChild::_restore(FXbool notify) { FXMDIChild::restore(notify); }

long FXPyGLObject::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLObject::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLObject::onDefault(sender,sel,ptr);
  }

void FXPyGLObject::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLObject::_draw(FXGLViewer* viewer) { FXGLObject::draw(viewer); }

void FXPyGLObject::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLObject::_hit(FXGLViewer* viewer) { FXGLObject::hit(viewer); }

FXbool FXPyGLObject::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLObject::_canDrag() const { return FXGLObject::canDrag(); }

FXbool FXPyGLObject::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLObject::_canDelete() const { return FXGLObject::canDelete(); }

FXbool FXPyGLObject::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLObject::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLObject::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLObject::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLObject::_copy() { return FXGLObject::copy(); }

FXGLObject* FXPyGLObject::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLObject::_identify(FXuint* path) { return FXGLObject::identify(path); }

long FXPyGLShape::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLShape::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLShape::onDefault(sender,sel,ptr);
  }

void FXPyGLShape::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLShape::_draw(FXGLViewer* viewer) { FXGLShape::draw(viewer); }

void FXPyGLShape::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLShape::_hit(FXGLViewer* viewer) { FXGLShape::hit(viewer); }

FXbool FXPyGLShape::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLShape::_canDrag() const { return FXGLShape::canDrag(); }

FXbool FXPyGLShape::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLShape::_canDelete() const { return FXGLShape::canDelete(); }

FXbool FXPyGLShape::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLShape::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLShape::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLShape::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLShape::_copy() { return FXGLShape::copy(); }

FXGLObject* FXPyGLShape::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLShape::_identify(FXuint* path) { return FXGLShape::identify(path); }

long FXPyGLCone::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLCone::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLCone::onDefault(sender,sel,ptr);
  }

void FXPyGLCone::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLCone::_draw(FXGLViewer* viewer) { FXGLCone::draw(viewer); }

void FXPyGLCone::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLCone::_hit(FXGLViewer* viewer) { FXGLCone::hit(viewer); }

FXbool FXPyGLCone::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLCone::_canDrag() const { return FXGLCone::canDrag(); }

FXbool FXPyGLCone::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLCone::_canDelete() const { return FXGLCone::canDelete(); }

FXbool FXPyGLCone::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLCone::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLCone::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLCone::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLCone::_copy() { return FXGLCone::copy(); }

FXGLObject* FXPyGLCone::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLCone::_identify(FXuint* path) { return FXGLCone::identify(path); }

long FXPyGLCylinder::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLCylinder::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLCylinder::onDefault(sender,sel,ptr);
  }

void FXPyGLCylinder::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLCylinder::_draw(FXGLViewer* viewer) { FXGLCylinder::draw(viewer); }

void FXPyGLCylinder::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLCylinder::_hit(FXGLViewer* viewer) { FXGLCylinder::hit(viewer); }

FXbool FXPyGLCylinder::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLCylinder::_canDrag() const { return FXGLCylinder::canDrag(); }

FXbool FXPyGLCylinder::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLCylinder::_canDelete() const { return FXGLCylinder::canDelete(); }

FXbool FXPyGLCylinder::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLCylinder::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLCylinder::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLCylinder::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLCylinder::_copy() { return FXGLCylinder::copy(); }

FXGLObject* FXPyGLCylinder::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLCylinder::_identify(FXuint* path) { return FXGLCylinder::identify(path); }

long FXPyGLTriangleMesh::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLTriangleMesh::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLTriangleMesh::onDefault(sender,sel,ptr);
  }

void FXPyGLTriangleMesh::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLTriangleMesh::_draw(FXGLViewer* viewer) { FXGLTriangleMesh::draw(viewer); }

void FXPyGLTriangleMesh::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLTriangleMesh::_hit(FXGLViewer* viewer) { FXGLTriangleMesh::hit(viewer); }

FXbool FXPyGLTriangleMesh::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLTriangleMesh::_canDrag() const { return FXGLTriangleMesh::canDrag(); }

FXbool FXPyGLTriangleMesh::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLTriangleMesh::_canDelete() const { return FXGLTriangleMesh::canDelete(); }

FXbool FXPyGLTriangleMesh::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLTriangleMesh::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLTriangleMesh::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLTriangleMesh::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLTriangleMesh::_copy() { return FXGLTriangleMesh::copy(); }

FXGLObject* FXPyGLTriangleMesh::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLTriangleMesh::_identify(FXuint* path) { return FXGLTriangleMesh::identify(path); }

long FXPyGLVisual::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLVisual::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLVisual::onDefault(sender,sel,ptr);
  }

long FXPyGLCanvas::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLCanvas::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLCanvas::onDefault(sender,sel,ptr);
  }

void FXPyGLCanvas::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGLCanvas::_create(){ FXGLCanvas::create(); }

void FXPyGLCanvas::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGLCanvas::_destroy(){ FXGLCanvas::destroy(); }

void FXPyGLCanvas::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGLCanvas::_detach(){ FXGLCanvas::detach(); }

void FXPyGLCanvas::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyGLCanvas::_resize(FXint w,FXint h){ FXGLCanvas::resize(w,h); }

void FXPyGLCanvas::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyGLCanvas::_enable(){ FXGLCanvas::enable(); }

void FXPyGLCanvas::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyGLCanvas::_disable(){ FXGLCanvas::disable(); }

void FXPyGLCanvas::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyGLCanvas::_show(){ FXGLCanvas::show(); }

void FXPyGLCanvas::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyGLCanvas::_hide(){ FXGLCanvas::hide(); }

void FXPyGLCanvas::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyGLCanvas::_lowerWindow(){ FXGLCanvas::lower(); }

FXint FXPyGLCanvas::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyGLCanvas::_getDefaultHeight() { return FXGLCanvas::getDefaultHeight(); }

FXint FXPyGLCanvas::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyGLCanvas::_getDefaultWidth() { return FXGLCanvas::getDefaultWidth(); }

FXint FXPyGLCanvas::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyGLCanvas::_getWidthForHeight(FXint h) { return FXGLCanvas::getWidthForHeight(h); }

FXint FXPyGLCanvas::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyGLCanvas::_getHeightForWidth(FXint w) { return FXGLCanvas::getHeightForWidth(w); }

void FXPyGLCanvas::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyGLCanvas::_layout() { FXGLCanvas::layout(); }

void FXPyGLCanvas::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyGLCanvas::_recalc() { FXGLCanvas::recalc(); }

FXbool FXPyGLCanvas::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyGLCanvas::_isComposite() const { return FXGLCanvas::isComposite(); }

void FXPyGLCanvas::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyGLCanvas::_move(FXint x,FXint y){ FXGLCanvas::move(x,y); }

void FXPyGLCanvas::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyGLCanvas::_position(FXint x,FXint y,FXint w,FXint h){ FXGLCanvas::position(x,y,w,h); }

FXbool FXPyGLCanvas::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyGLCanvas::_canFocus() const { return FXGLCanvas::canFocus(); }

void FXPyGLCanvas::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyGLCanvas::_setFocus(){ FXGLCanvas::setFocus(); }

void FXPyGLCanvas::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyGLCanvas::_killFocus(){ FXGLCanvas::killFocus(); }

void FXPyGLCanvas::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyGLCanvas::_setDefault(FXbool enable){ FXGLCanvas::setDefault(enable); }

FXbool FXPyGLCanvas::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyGLCanvas::_contains(FXint x,FXint y) const { return FXGLCanvas::contains(x,y); }

FXbool FXPyGLCanvas::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyGLCanvas::_doesSaveUnder() const { return FXGLCanvas::doesSaveUnder(); }

void FXPyGLCanvas::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyGLCanvas::_reparent(FXComposite* newparent) { FXGLCanvas::reparent(newparent); }

void FXPyGLCanvas::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyGLCanvas::_setBackColor(FXColor clr) { FXGLCanvas::setBackColor(clr); }

FXbool FXPyGLCanvas::isCurrent() const { return FXPyCallBoolFunction(this,"isCurrent"); }
FXbool FXPyGLCanvas::_isCurrent() const { return FXGLCanvas::isCurrent(); }

FXbool FXPyGLCanvas::makeCurrent() { return FXPyCallBoolFunction(this,"makeCurrent"); }
FXbool FXPyGLCanvas::_makeCurrent() { return FXGLCanvas::makeCurrent(); }

FXbool FXPyGLCanvas::makeNonCurrent() { return FXPyCallBoolFunction(this,"makeNonCurrent"); }
FXbool FXPyGLCanvas::_makeNonCurrent() { return FXGLCanvas::makeNonCurrent(); }

void FXPyGLCanvas::swapBuffers() { FXPyCallVoidFunction(this,"swapBuffers"); }
void FXPyGLCanvas::_swapBuffers() { FXGLCanvas::swapBuffers(); }

long FXPyGLCube::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLCube::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLCube::onDefault(sender,sel,ptr);
  }

void FXPyGLCube::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLCube::_draw(FXGLViewer* viewer) { FXGLCube::draw(viewer); }

void FXPyGLCube::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLCube::_hit(FXGLViewer* viewer) { FXGLCube::hit(viewer); }

FXbool FXPyGLCube::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLCube::_canDrag() const { return FXGLCube::canDrag(); }

FXbool FXPyGLCube::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLCube::_canDelete() const { return FXGLCube::canDelete(); }

FXbool FXPyGLCube::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLCube::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLCube::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLCube::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLCube::_copy() { return FXGLCube::copy(); }

FXGLObject* FXPyGLCube::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLCube::_identify(FXuint* path) { return FXGLCube::identify(path); }

long FXPyGLGroup::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLGroup::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLGroup::onDefault(sender,sel,ptr);
  }

void FXPyGLGroup::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLGroup::_draw(FXGLViewer* viewer) { FXGLGroup::draw(viewer); }

void FXPyGLGroup::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLGroup::_hit(FXGLViewer* viewer) { FXGLGroup::hit(viewer); }

FXbool FXPyGLGroup::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLGroup::_canDrag() const { return FXGLGroup::canDrag(); }

FXbool FXPyGLGroup::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLGroup::_canDelete() const { return FXGLGroup::canDelete(); }

FXbool FXPyGLGroup::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLGroup::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLGroup::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLGroup::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLGroup::_copy() { return FXGLGroup::copy(); }

FXGLObject* FXPyGLGroup::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLGroup::_identify(FXuint* path) { return FXGLGroup::identify(path); }

long FXPyGLLine::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLLine::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLLine::onDefault(sender,sel,ptr);
  }

void FXPyGLLine::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLLine::_draw(FXGLViewer* viewer) { FXGLLine::draw(viewer); }

void FXPyGLLine::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLLine::_hit(FXGLViewer* viewer) { FXGLLine::hit(viewer); }

FXbool FXPyGLLine::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLLine::_canDrag() const { return FXGLLine::canDrag(); }

FXbool FXPyGLLine::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLLine::_canDelete() const { return FXGLLine::canDelete(); }

FXbool FXPyGLLine::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLLine::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLLine::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLLine::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLLine::_copy() { return FXGLLine::copy(); }

FXGLObject* FXPyGLLine::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLLine::_identify(FXuint* path) { return FXGLLine::identify(path); }

long FXPyGLPoint::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLPoint::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLPoint::onDefault(sender,sel,ptr);
  }

void FXPyGLPoint::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLPoint::_draw(FXGLViewer* viewer) { FXGLPoint::draw(viewer); }

void FXPyGLPoint::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLPoint::_hit(FXGLViewer* viewer) { FXGLPoint::hit(viewer); }

FXbool FXPyGLPoint::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLPoint::_canDrag() const { return FXGLPoint::canDrag(); }

FXbool FXPyGLPoint::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLPoint::_canDelete() const { return FXGLPoint::canDelete(); }

FXbool FXPyGLPoint::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLPoint::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLPoint::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLPoint::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLPoint::_copy() { return FXGLPoint::copy(); }

FXGLObject* FXPyGLPoint::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLPoint::_identify(FXuint* path) { return FXGLPoint::identify(path); }

long FXPyGLSphere::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLSphere::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLSphere::onDefault(sender,sel,ptr);
  }

void FXPyGLSphere::draw(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"draw",viewer); }
void FXPyGLSphere::_draw(FXGLViewer* viewer) { FXGLSphere::draw(viewer); }

void FXPyGLSphere::hit(FXGLViewer* viewer) { FXPyCallVoidFunction(this,"hit",viewer); }
void FXPyGLSphere::_hit(FXGLViewer* viewer) { FXGLSphere::hit(viewer); }

FXbool FXPyGLSphere::canDrag() const { return FXPyCallBoolFunction(this,"canDrag"); }
FXbool FXPyGLSphere::_canDrag() const { return FXGLSphere::canDrag(); }

FXbool FXPyGLSphere::canDelete() const { return FXPyCallBoolFunction(this,"canDelete"); }
FXbool FXPyGLSphere::_canDelete() const { return FXGLSphere::canDelete(); }

FXbool FXPyGLSphere::drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXPyCallBoolFunction(this,"drag",viewer,fx,fy,tx,ty); }
FXbool FXPyGLSphere::_drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty) { return FXGLSphere::drag(viewer,fx,fy,tx,ty); }

FXGLObject* FXPyGLSphere::copy() { return FXPyCallGLObjectFunction(this,"copy"); }
FXGLObject* FXPyGLSphere::_copy() { return FXGLSphere::copy(); }

FXGLObject* FXPyGLSphere::identify(FXuint* path) { return FXPyCallGLObjectFunction(this,"identify",path); }
FXGLObject* FXPyGLSphere::_identify(FXuint* path) { return FXGLSphere::identify(path); }

long FXPyGLViewer::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLViewer::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLViewer::onDefault(sender,sel,ptr);
  }

void FXPyGLViewer::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGLViewer::_create(){ FXGLViewer::create(); }

void FXPyGLViewer::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGLViewer::_destroy(){ FXGLViewer::destroy(); }

void FXPyGLViewer::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGLViewer::_detach(){ FXGLViewer::detach(); }

void FXPyGLViewer::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyGLViewer::_resize(FXint w,FXint h){ FXGLViewer::resize(w,h); }

void FXPyGLViewer::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyGLViewer::_enable(){ FXGLViewer::enable(); }

void FXPyGLViewer::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyGLViewer::_disable(){ FXGLViewer::disable(); }

void FXPyGLViewer::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyGLViewer::_show(){ FXGLViewer::show(); }

void FXPyGLViewer::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyGLViewer::_hide(){ FXGLViewer::hide(); }

void FXPyGLViewer::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyGLViewer::_lowerWindow(){ FXGLViewer::lower(); }

FXint FXPyGLViewer::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyGLViewer::_getDefaultHeight() { return FXGLViewer::getDefaultHeight(); }

FXint FXPyGLViewer::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyGLViewer::_getDefaultWidth() { return FXGLViewer::getDefaultWidth(); }

FXint FXPyGLViewer::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyGLViewer::_getWidthForHeight(FXint h) { return FXGLViewer::getWidthForHeight(h); }

FXint FXPyGLViewer::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyGLViewer::_getHeightForWidth(FXint w) { return FXGLViewer::getHeightForWidth(w); }

void FXPyGLViewer::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyGLViewer::_layout() { FXGLViewer::layout(); }

void FXPyGLViewer::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyGLViewer::_recalc() { FXGLViewer::recalc(); }

FXbool FXPyGLViewer::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyGLViewer::_isComposite() const { return FXGLViewer::isComposite(); }

void FXPyGLViewer::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyGLViewer::_move(FXint x,FXint y){ FXGLViewer::move(x,y); }

void FXPyGLViewer::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyGLViewer::_position(FXint x,FXint y,FXint w,FXint h){ FXGLViewer::position(x,y,w,h); }

FXbool FXPyGLViewer::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyGLViewer::_canFocus() const { return FXGLViewer::canFocus(); }

void FXPyGLViewer::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyGLViewer::_setFocus(){ FXGLViewer::setFocus(); }

void FXPyGLViewer::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyGLViewer::_killFocus(){ FXGLViewer::killFocus(); }

void FXPyGLViewer::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyGLViewer::_setDefault(FXbool enable){ FXGLViewer::setDefault(enable); }

FXbool FXPyGLViewer::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyGLViewer::_contains(FXint x,FXint y) const { return FXGLViewer::contains(x,y); }

FXbool FXPyGLViewer::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyGLViewer::_doesSaveUnder() const { return FXGLViewer::doesSaveUnder(); }

void FXPyGLViewer::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyGLViewer::_reparent(FXComposite* newparent) { FXGLViewer::reparent(newparent); }

void FXPyGLViewer::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyGLViewer::_setBackColor(FXColor clr) { FXGLViewer::setBackColor(clr); }

FXbool FXPyGLViewer::isCurrent() const { return FXPyCallBoolFunction(this,"isCurrent"); }
FXbool FXPyGLViewer::_isCurrent() const { return FXGLViewer::isCurrent(); }

FXbool FXPyGLViewer::makeCurrent() { return FXPyCallBoolFunction(this,"makeCurrent"); }
FXbool FXPyGLViewer::_makeCurrent() { return FXGLViewer::makeCurrent(); }

FXbool FXPyGLViewer::makeNonCurrent() { return FXPyCallBoolFunction(this,"makeNonCurrent"); }
FXbool FXPyGLViewer::_makeNonCurrent() { return FXGLViewer::makeNonCurrent(); }

void FXPyGLViewer::swapBuffers() { FXPyCallVoidFunction(this,"swapBuffers"); }
void FXPyGLViewer::_swapBuffers() { FXGLViewer::swapBuffers(); }

FXGLObject** FXPyGLViewer::select(FXint x,FXint y,FXint w,FXint h) { return FXPyCallGLObjectListFunction(this,"select",x,y,w,h); }
FXGLObject** FXPyGLViewer::_select(FXint x,FXint y,FXint w,FXint h) { return FXGLViewer::select(x,y,w,h); }

FXGLObject* FXPyGLViewer::pick(FXint x,FXint y) { return FXPyCallGLObjectFunction(this,"pick",x,y); }
FXGLObject* FXPyGLViewer::_pick(FXint x,FXint y) { return FXGLViewer::pick(x,y); }

long FXPyTable::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTable::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTable::onDefault(sender,sel,ptr);
  }

void FXPyTable::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTable::_create(){ FXTable::create(); }

void FXPyTable::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTable::_destroy(){ FXTable::destroy(); }

void FXPyTable::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTable::_detach(){ FXTable::detach(); }

void FXPyTable::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTable::_resize(FXint w,FXint h){ FXTable::resize(w,h); }

void FXPyTable::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyTable::_enable(){ FXTable::enable(); }

void FXPyTable::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyTable::_disable(){ FXTable::disable(); }

void FXPyTable::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyTable::_show(){ FXTable::show(); }

void FXPyTable::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyTable::_hide(){ FXTable::hide(); }

void FXPyTable::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyTable::_lowerWindow(){ FXTable::lower(); }

FXint FXPyTable::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyTable::_getDefaultHeight() { return FXTable::getDefaultHeight(); }

FXint FXPyTable::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyTable::_getDefaultWidth() { return FXTable::getDefaultWidth(); }

FXint FXPyTable::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyTable::_getWidthForHeight(FXint h) { return FXTable::getWidthForHeight(h); }

FXint FXPyTable::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyTable::_getHeightForWidth(FXint w) { return FXTable::getHeightForWidth(w); }

void FXPyTable::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyTable::_layout() { FXTable::layout(); }

void FXPyTable::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyTable::_recalc() { FXTable::recalc(); }

FXbool FXPyTable::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyTable::_isComposite() const { return FXTable::isComposite(); }

void FXPyTable::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyTable::_move(FXint x,FXint y){ FXTable::move(x,y); }

void FXPyTable::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyTable::_position(FXint x,FXint y,FXint w,FXint h){ FXTable::position(x,y,w,h); }

FXbool FXPyTable::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyTable::_canFocus() const { return FXTable::canFocus(); }

void FXPyTable::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyTable::_setFocus(){ FXTable::setFocus(); }

void FXPyTable::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyTable::_killFocus(){ FXTable::killFocus(); }

void FXPyTable::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyTable::_setDefault(FXbool enable){ FXTable::setDefault(enable); }

FXbool FXPyTable::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyTable::_contains(FXint x,FXint y) const { return FXTable::contains(x,y); }

FXbool FXPyTable::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyTable::_doesSaveUnder() const { return FXTable::doesSaveUnder(); }

void FXPyTable::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyTable::_reparent(FXComposite* newparent) { FXTable::reparent(newparent); }

void FXPyTable::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyTable::_setBackColor(FXColor clr) { FXTable::setBackColor(clr); }

FXint FXPyTable::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyTable::_getContentWidth() { return FXTable::getContentWidth(); }

FXint FXPyTable::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyTable::_getContentHeight() { return FXTable::getContentHeight(); }

FXint FXPyTable::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyTable::_getViewportWidth() { return FXTable::getViewportWidth(); }

FXint FXPyTable::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyTable::_getViewportHeight() { return FXTable::getViewportHeight(); }

void FXPyTable::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyTable::_moveContents(FXint x,FXint y) { FXTable::moveContents(x,y); }

long FXPyTableItem::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTableItem::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTableItem::onDefault(sender,sel,ptr);
  }

void FXPyTableItem::setText(const FXString& text) { FXPyCallVoidFunction(this,"setText",text); }
void FXPyTableItem::_setText(const FXString& text) { FXTableItem::setText(text); }

void FXPyTableItem::setIcon(FXIcon *icn) { FXPyCallVoidFunction(this,"setIcon",icn); }
void FXPyTableItem::_setIcon(FXIcon *icn) { FXTableItem::setIcon(icn); }

void FXPyTableItem::setFocus(FXbool focus) { FXPyCallVoidFunction(this,"setFocus",focus); }
void FXPyTableItem::_setFocus(FXbool focus) { FXTableItem::setFocus(focus); }

void FXPyTableItem::setSelected(FXbool selected) { FXPyCallVoidFunction(this,"setSelected",selected); }
void FXPyTableItem::_setSelected(FXbool selected) { FXTableItem::setSelected(selected); }

void FXPyTableItem::setEnabled(FXbool enabled) { FXPyCallVoidFunction(this,"setEnabled",enabled); }
void FXPyTableItem::_setEnabled(FXbool enabled) { FXTableItem::setEnabled(enabled); }

void FXPyTableItem::setDraggable(FXbool draggable) { FXPyCallVoidFunction(this,"setDraggable",draggable); }
void FXPyTableItem::_setDraggable(FXbool draggable) { FXTableItem::setDraggable(draggable); }

void FXPyTableItem::setJustify(FXuint justify) { FXPyCallVoidFunction(this,"setJustify",justify); }
void FXPyTableItem::_setJustify(FXuint justify) { FXTableItem::setJustify(justify); }

FXint FXPyTableItem::getWidth(const FXTable* table) const { return ::_getWidth(this, table); }
FXint FXPyTableItem::_getWidth(const FXTable* table) const { return FXTableItem::getWidth(table); }

FXint FXPyTableItem::getHeight(const FXTable* table) const { return ::_getHeight(this, table); }
FXint FXPyTableItem::_getHeight(const FXTable* table) const { return FXTableItem::getHeight(table); }

void FXPyTableItem::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTableItem::_create(){ FXTableItem::create(); }

void FXPyTableItem::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTableItem::_detach(){ FXTableItem::detach(); }

void FXPyTableItem::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTableItem::_destroy(){ FXTableItem::destroy(); }

long FXPyBitmap::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyBitmap::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXBitmap::onDefault(sender,sel,ptr);
  }

void FXPyBitmap::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyBitmap::_create(){ FXBitmap::create(); }

void FXPyBitmap::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyBitmap::_destroy(){ FXBitmap::destroy(); }

void FXPyBitmap::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyBitmap::_detach(){ FXBitmap::detach(); }

void FXPyBitmap::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyBitmap::_resize(FXint w,FXint h){ FXBitmap::resize(w,h); }

long FXPyDict::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDict::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDict::onDefault(sender,sel,ptr);
  }

long FXPyIconDict::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyIconDict::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXIconDict::onDefault(sender,sel,ptr);
  }

long FXPyFileDict::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyFileDict::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXFileDict::onDefault(sender,sel,ptr);
  }

long FXPyStringDict::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyStringDict::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXStringDict::onDefault(sender,sel,ptr);
  }

long FXPyStatusline::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyStatusline::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXStatusline::onDefault(sender,sel,ptr);
  }

void FXPyStatusline::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyStatusline::_create(){ FXStatusline::create(); }

void FXPyStatusline::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyStatusline::_destroy(){ FXStatusline::destroy(); }

void FXPyStatusline::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyStatusline::_detach(){ FXStatusline::detach(); }

void FXPyStatusline::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyStatusline::_resize(FXint w,FXint h){ FXStatusline::resize(w,h); }

void FXPyStatusline::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyStatusline::_enable(){ FXStatusline::enable(); }

void FXPyStatusline::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyStatusline::_disable(){ FXStatusline::disable(); }

void FXPyStatusline::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyStatusline::_show(){ FXStatusline::show(); }

void FXPyStatusline::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyStatusline::_hide(){ FXStatusline::hide(); }

void FXPyStatusline::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyStatusline::_lowerWindow(){ FXStatusline::lower(); }

FXint FXPyStatusline::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyStatusline::_getDefaultHeight() { return FXStatusline::getDefaultHeight(); }

FXint FXPyStatusline::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyStatusline::_getDefaultWidth() { return FXStatusline::getDefaultWidth(); }

FXint FXPyStatusline::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyStatusline::_getWidthForHeight(FXint h) { return FXStatusline::getWidthForHeight(h); }

FXint FXPyStatusline::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyStatusline::_getHeightForWidth(FXint w) { return FXStatusline::getHeightForWidth(w); }

void FXPyStatusline::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyStatusline::_layout() { FXStatusline::layout(); }

void FXPyStatusline::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyStatusline::_recalc() { FXStatusline::recalc(); }

FXbool FXPyStatusline::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyStatusline::_isComposite() const { return FXStatusline::isComposite(); }

void FXPyStatusline::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyStatusline::_move(FXint x,FXint y){ FXStatusline::move(x,y); }

void FXPyStatusline::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyStatusline::_position(FXint x,FXint y,FXint w,FXint h){ FXStatusline::position(x,y,w,h); }

FXbool FXPyStatusline::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyStatusline::_canFocus() const { return FXStatusline::canFocus(); }

void FXPyStatusline::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyStatusline::_setFocus(){ FXStatusline::setFocus(); }

void FXPyStatusline::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyStatusline::_killFocus(){ FXStatusline::killFocus(); }

void FXPyStatusline::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyStatusline::_setDefault(FXbool enable){ FXStatusline::setDefault(enable); }

FXbool FXPyStatusline::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyStatusline::_contains(FXint x,FXint y) const { return FXStatusline::contains(x,y); }

FXbool FXPyStatusline::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyStatusline::_doesSaveUnder() const { return FXStatusline::doesSaveUnder(); }

void FXPyStatusline::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyStatusline::_reparent(FXComposite* newparent) { FXStatusline::reparent(newparent); }

void FXPyStatusline::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyStatusline::_setBackColor(FXColor clr) { FXStatusline::setBackColor(clr); }

long FXPyDragCorner::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDragCorner::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDragCorner::onDefault(sender,sel,ptr);
  }

void FXPyDragCorner::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDragCorner::_create(){ FXDragCorner::create(); }

void FXPyDragCorner::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDragCorner::_destroy(){ FXDragCorner::destroy(); }

void FXPyDragCorner::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDragCorner::_detach(){ FXDragCorner::detach(); }

void FXPyDragCorner::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDragCorner::_resize(FXint w,FXint h){ FXDragCorner::resize(w,h); }

void FXPyDragCorner::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDragCorner::_enable(){ FXDragCorner::enable(); }

void FXPyDragCorner::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDragCorner::_disable(){ FXDragCorner::disable(); }

void FXPyDragCorner::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDragCorner::_show(){ FXDragCorner::show(); }

void FXPyDragCorner::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDragCorner::_hide(){ FXDragCorner::hide(); }

void FXPyDragCorner::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDragCorner::_lowerWindow(){ FXDragCorner::lower(); }

FXint FXPyDragCorner::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDragCorner::_getDefaultHeight() { return FXDragCorner::getDefaultHeight(); }

FXint FXPyDragCorner::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDragCorner::_getDefaultWidth() { return FXDragCorner::getDefaultWidth(); }

FXint FXPyDragCorner::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDragCorner::_getWidthForHeight(FXint h) { return FXDragCorner::getWidthForHeight(h); }

FXint FXPyDragCorner::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDragCorner::_getHeightForWidth(FXint w) { return FXDragCorner::getHeightForWidth(w); }

void FXPyDragCorner::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDragCorner::_layout() { FXDragCorner::layout(); }

void FXPyDragCorner::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDragCorner::_recalc() { FXDragCorner::recalc(); }

FXbool FXPyDragCorner::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDragCorner::_isComposite() const { return FXDragCorner::isComposite(); }

void FXPyDragCorner::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDragCorner::_move(FXint x,FXint y){ FXDragCorner::move(x,y); }

void FXPyDragCorner::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDragCorner::_position(FXint x,FXint y,FXint w,FXint h){ FXDragCorner::position(x,y,w,h); }

FXbool FXPyDragCorner::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDragCorner::_canFocus() const { return FXDragCorner::canFocus(); }

void FXPyDragCorner::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDragCorner::_setFocus(){ FXDragCorner::setFocus(); }

void FXPyDragCorner::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDragCorner::_killFocus(){ FXDragCorner::killFocus(); }

void FXPyDragCorner::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDragCorner::_setDefault(FXbool enable){ FXDragCorner::setDefault(enable); }

FXbool FXPyDragCorner::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDragCorner::_contains(FXint x,FXint y) const { return FXDragCorner::contains(x,y); }

FXbool FXPyDragCorner::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDragCorner::_doesSaveUnder() const { return FXDragCorner::doesSaveUnder(); }

void FXPyDragCorner::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDragCorner::_reparent(FXComposite* newparent) { FXDragCorner::reparent(newparent); }

void FXPyDragCorner::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDragCorner::_setBackColor(FXColor clr) { FXDragCorner::setBackColor(clr); }

long FXPyRecentFiles::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyRecentFiles::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXRecentFiles::onDefault(sender,sel,ptr);
  }

long FXPyXPMIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyXPMIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXXPMIcon::onDefault(sender,sel,ptr);
  }

void FXPyXPMIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyXPMIcon::_create(){ FXXPMIcon::create(); }

void FXPyXPMIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyXPMIcon::_destroy(){ FXXPMIcon::destroy(); }

void FXPyXPMIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyXPMIcon::_detach(){ FXXPMIcon::detach(); }

void FXPyXPMIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyXPMIcon::_resize(FXint w,FXint h){ FXXPMIcon::resize(w,h); }

void FXPyXPMIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyXPMIcon::_restore() { FXXPMIcon::restore(); }

void FXPyXPMIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyXPMIcon::_render() { FXXPMIcon::render(); }

void FXPyXPMIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyXPMIcon::_scale(FXint w,FXint h) { FXXPMIcon::scale(w,h); }

void FXPyXPMIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyXPMIcon::_mirror(FXbool horizontal,FXbool vertical) { FXXPMIcon::mirror(horizontal,vertical); }

void FXPyXPMIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyXPMIcon::_rotate(FXint degrees) { FXXPMIcon::rotate(degrees); }

void FXPyXPMIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyXPMIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXXPMIcon::crop(x,y,w,h); }

void FXPyXPMIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyXPMIcon::_savePixels(FXStream& store) const { FXXPMIcon::savePixels(store); }

void FXPyXPMIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyXPMIcon::_loadPixels(FXStream& store) { FXXPMIcon::loadPixels(store); }

long FXPyXPMImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyXPMImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXXPMImage::onDefault(sender,sel,ptr);
  }

void FXPyXPMImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyXPMImage::_create(){ FXXPMImage::create(); }

void FXPyXPMImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyXPMImage::_destroy(){ FXXPMImage::destroy(); }

void FXPyXPMImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyXPMImage::_detach(){ FXXPMImage::detach(); }

void FXPyXPMImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyXPMImage::_resize(FXint w,FXint h){ FXXPMImage::resize(w,h); }

void FXPyXPMImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyXPMImage::_restore() { FXXPMImage::restore(); }

void FXPyXPMImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyXPMImage::_render() { FXXPMImage::render(); }

void FXPyXPMImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyXPMImage::_scale(FXint w,FXint h) { FXXPMImage::scale(w,h); }

void FXPyXPMImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyXPMImage::_mirror(FXbool horizontal,FXbool vertical) { FXXPMImage::mirror(horizontal,vertical); }

void FXPyXPMImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyXPMImage::_rotate(FXint degrees) { FXXPMImage::rotate(degrees); }

void FXPyXPMImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyXPMImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXXPMImage::crop(x,y,w,h); }

void FXPyXPMImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyXPMImage::_savePixels(FXStream& store) const { FXXPMImage::savePixels(store); }

void FXPyXPMImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyXPMImage::_loadPixels(FXStream& store) { FXXPMImage::loadPixels(store); }

long FXPyPCXIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPCXIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPCXIcon::onDefault(sender,sel,ptr);
  }

void FXPyPCXIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPCXIcon::_create(){ FXPCXIcon::create(); }

void FXPyPCXIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPCXIcon::_destroy(){ FXPCXIcon::destroy(); }

void FXPyPCXIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPCXIcon::_detach(){ FXPCXIcon::detach(); }

void FXPyPCXIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPCXIcon::_resize(FXint w,FXint h){ FXPCXIcon::resize(w,h); }

void FXPyPCXIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyPCXIcon::_restore() { FXPCXIcon::restore(); }

void FXPyPCXIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyPCXIcon::_render() { FXPCXIcon::render(); }

void FXPyPCXIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyPCXIcon::_scale(FXint w,FXint h) { FXPCXIcon::scale(w,h); }

void FXPyPCXIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyPCXIcon::_mirror(FXbool horizontal,FXbool vertical) { FXPCXIcon::mirror(horizontal,vertical); }

void FXPyPCXIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyPCXIcon::_rotate(FXint degrees) { FXPCXIcon::rotate(degrees); }

void FXPyPCXIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyPCXIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXPCXIcon::crop(x,y,w,h); }

void FXPyPCXIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyPCXIcon::_savePixels(FXStream& store) const { FXPCXIcon::savePixels(store); }

void FXPyPCXIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyPCXIcon::_loadPixels(FXStream& store) { FXPCXIcon::loadPixels(store); }

long FXPyPCXImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyPCXImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXPCXImage::onDefault(sender,sel,ptr);
  }

void FXPyPCXImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyPCXImage::_create(){ FXPCXImage::create(); }

void FXPyPCXImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyPCXImage::_destroy(){ FXPCXImage::destroy(); }

void FXPyPCXImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyPCXImage::_detach(){ FXPCXImage::detach(); }

void FXPyPCXImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyPCXImage::_resize(FXint w,FXint h){ FXPCXImage::resize(w,h); }

void FXPyPCXImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyPCXImage::_restore() { FXPCXImage::restore(); }

void FXPyPCXImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyPCXImage::_render() { FXPCXImage::render(); }

void FXPyPCXImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyPCXImage::_scale(FXint w,FXint h) { FXPCXImage::scale(w,h); }

void FXPyPCXImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyPCXImage::_mirror(FXbool horizontal,FXbool vertical) { FXPCXImage::mirror(horizontal,vertical); }

void FXPyPCXImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyPCXImage::_rotate(FXint degrees) { FXPCXImage::rotate(degrees); }

void FXPyPCXImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyPCXImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXPCXImage::crop(x,y,w,h); }

void FXPyPCXImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyPCXImage::_savePixels(FXStream& store) const { FXPCXImage::savePixels(store); }

void FXPyPCXImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyPCXImage::_loadPixels(FXStream& store) { FXPCXImage::loadPixels(store); }

long FXPyTIFIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTIFIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTIFIcon::onDefault(sender,sel,ptr);
  }

void FXPyTIFIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTIFIcon::_create(){ FXTIFIcon::create(); }

void FXPyTIFIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTIFIcon::_destroy(){ FXTIFIcon::destroy(); }

void FXPyTIFIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTIFIcon::_detach(){ FXTIFIcon::detach(); }

void FXPyTIFIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTIFIcon::_resize(FXint w,FXint h){ FXTIFIcon::resize(w,h); }

void FXPyTIFIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyTIFIcon::_restore() { FXTIFIcon::restore(); }

void FXPyTIFIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyTIFIcon::_render() { FXTIFIcon::render(); }

void FXPyTIFIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyTIFIcon::_scale(FXint w,FXint h) { FXTIFIcon::scale(w,h); }

void FXPyTIFIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyTIFIcon::_mirror(FXbool horizontal,FXbool vertical) { FXTIFIcon::mirror(horizontal,vertical); }

void FXPyTIFIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyTIFIcon::_rotate(FXint degrees) { FXTIFIcon::rotate(degrees); }

void FXPyTIFIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyTIFIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXTIFIcon::crop(x,y,w,h); }

void FXPyTIFIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyTIFIcon::_savePixels(FXStream& store) const { FXTIFIcon::savePixels(store); }

void FXPyTIFIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyTIFIcon::_loadPixels(FXStream& store) { FXTIFIcon::loadPixels(store); }

long FXPyTIFImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTIFImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTIFImage::onDefault(sender,sel,ptr);
  }

void FXPyTIFImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTIFImage::_create(){ FXTIFImage::create(); }

void FXPyTIFImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTIFImage::_destroy(){ FXTIFImage::destroy(); }

void FXPyTIFImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTIFImage::_detach(){ FXTIFImage::detach(); }

void FXPyTIFImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTIFImage::_resize(FXint w,FXint h){ FXTIFImage::resize(w,h); }

void FXPyTIFImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyTIFImage::_restore() { FXTIFImage::restore(); }

void FXPyTIFImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyTIFImage::_render() { FXTIFImage::render(); }

void FXPyTIFImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyTIFImage::_scale(FXint w,FXint h) { FXTIFImage::scale(w,h); }

void FXPyTIFImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyTIFImage::_mirror(FXbool horizontal,FXbool vertical) { FXTIFImage::mirror(horizontal,vertical); }

void FXPyTIFImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyTIFImage::_rotate(FXint degrees) { FXTIFImage::rotate(degrees); }

void FXPyTIFImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyTIFImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXTIFImage::crop(x,y,w,h); }

void FXPyTIFImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyTIFImage::_savePixels(FXStream& store) const { FXTIFImage::savePixels(store); }

void FXPyTIFImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyTIFImage::_loadPixels(FXStream& store) { FXTIFImage::loadPixels(store); }

long FXPyTGAIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTGAIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTGAIcon::onDefault(sender,sel,ptr);
  }

void FXPyTGAIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTGAIcon::_create(){ FXTGAIcon::create(); }

void FXPyTGAIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTGAIcon::_destroy(){ FXTGAIcon::destroy(); }

void FXPyTGAIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTGAIcon::_detach(){ FXTGAIcon::detach(); }

void FXPyTGAIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTGAIcon::_resize(FXint w,FXint h){ FXTGAIcon::resize(w,h); }

void FXPyTGAIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyTGAIcon::_restore() { FXTGAIcon::restore(); }

void FXPyTGAIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyTGAIcon::_render() { FXTGAIcon::render(); }

void FXPyTGAIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyTGAIcon::_scale(FXint w,FXint h) { FXTGAIcon::scale(w,h); }

void FXPyTGAIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyTGAIcon::_mirror(FXbool horizontal,FXbool vertical) { FXTGAIcon::mirror(horizontal,vertical); }

void FXPyTGAIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyTGAIcon::_rotate(FXint degrees) { FXTGAIcon::rotate(degrees); }

void FXPyTGAIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyTGAIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXTGAIcon::crop(x,y,w,h); }

void FXPyTGAIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyTGAIcon::_savePixels(FXStream& store) const { FXTGAIcon::savePixels(store); }

void FXPyTGAIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyTGAIcon::_loadPixels(FXStream& store) { FXTGAIcon::loadPixels(store); }

long FXPyTGAImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyTGAImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXTGAImage::onDefault(sender,sel,ptr);
  }

void FXPyTGAImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyTGAImage::_create(){ FXTGAImage::create(); }

void FXPyTGAImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyTGAImage::_destroy(){ FXTGAImage::destroy(); }

void FXPyTGAImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyTGAImage::_detach(){ FXTGAImage::detach(); }

void FXPyTGAImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyTGAImage::_resize(FXint w,FXint h){ FXTGAImage::resize(w,h); }

void FXPyTGAImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyTGAImage::_restore() { FXTGAImage::restore(); }

void FXPyTGAImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyTGAImage::_render() { FXTGAImage::render(); }

void FXPyTGAImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyTGAImage::_scale(FXint w,FXint h) { FXTGAImage::scale(w,h); }

void FXPyTGAImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyTGAImage::_mirror(FXbool horizontal,FXbool vertical) { FXTGAImage::mirror(horizontal,vertical); }

void FXPyTGAImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyTGAImage::_rotate(FXint degrees) { FXTGAImage::rotate(degrees); }

void FXPyTGAImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyTGAImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXTGAImage::crop(x,y,w,h); }

void FXPyTGAImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyTGAImage::_savePixels(FXStream& store) const { FXTGAImage::savePixels(store); }

void FXPyTGAImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyTGAImage::_loadPixels(FXStream& store) { FXTGAImage::loadPixels(store); }

long FXPyRGBIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyRGBIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXRGBIcon::onDefault(sender,sel,ptr);
  }

void FXPyRGBIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyRGBIcon::_create(){ FXRGBIcon::create(); }

void FXPyRGBIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyRGBIcon::_destroy(){ FXRGBIcon::destroy(); }

void FXPyRGBIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyRGBIcon::_detach(){ FXRGBIcon::detach(); }

void FXPyRGBIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyRGBIcon::_resize(FXint w,FXint h){ FXRGBIcon::resize(w,h); }

void FXPyRGBIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyRGBIcon::_restore() { FXRGBIcon::restore(); }

void FXPyRGBIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyRGBIcon::_render() { FXRGBIcon::render(); }

void FXPyRGBIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyRGBIcon::_scale(FXint w,FXint h) { FXRGBIcon::scale(w,h); }

void FXPyRGBIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyRGBIcon::_mirror(FXbool horizontal,FXbool vertical) { FXRGBIcon::mirror(horizontal,vertical); }

void FXPyRGBIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyRGBIcon::_rotate(FXint degrees) { FXRGBIcon::rotate(degrees); }

void FXPyRGBIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyRGBIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXRGBIcon::crop(x,y,w,h); }

void FXPyRGBIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyRGBIcon::_savePixels(FXStream& store) const { FXRGBIcon::savePixels(store); }

void FXPyRGBIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyRGBIcon::_loadPixels(FXStream& store) { FXRGBIcon::loadPixels(store); }

long FXPyRGBImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyRGBImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXRGBImage::onDefault(sender,sel,ptr);
  }

void FXPyRGBImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyRGBImage::_create(){ FXRGBImage::create(); }

void FXPyRGBImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyRGBImage::_destroy(){ FXRGBImage::destroy(); }

void FXPyRGBImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyRGBImage::_detach(){ FXRGBImage::detach(); }

void FXPyRGBImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyRGBImage::_resize(FXint w,FXint h){ FXRGBImage::resize(w,h); }

void FXPyRGBImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyRGBImage::_restore() { FXRGBImage::restore(); }

void FXPyRGBImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyRGBImage::_render() { FXRGBImage::render(); }

void FXPyRGBImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyRGBImage::_scale(FXint w,FXint h) { FXRGBImage::scale(w,h); }

void FXPyRGBImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyRGBImage::_mirror(FXbool horizontal,FXbool vertical) { FXRGBImage::mirror(horizontal,vertical); }

void FXPyRGBImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyRGBImage::_rotate(FXint degrees) { FXRGBImage::rotate(degrees); }

void FXPyRGBImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyRGBImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXRGBImage::crop(x,y,w,h); }

void FXPyRGBImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyRGBImage::_savePixels(FXStream& store) const { FXRGBImage::savePixels(store); }

void FXPyRGBImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyRGBImage::_loadPixels(FXStream& store) { FXRGBImage::loadPixels(store); }

long FXPyICOIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyICOIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXICOIcon::onDefault(sender,sel,ptr);
  }

void FXPyICOIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyICOIcon::_create(){ FXICOIcon::create(); }

void FXPyICOIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyICOIcon::_destroy(){ FXICOIcon::destroy(); }

void FXPyICOIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyICOIcon::_detach(){ FXICOIcon::detach(); }

void FXPyICOIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyICOIcon::_resize(FXint w,FXint h){ FXICOIcon::resize(w,h); }

void FXPyICOIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyICOIcon::_restore() { FXICOIcon::restore(); }

void FXPyICOIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyICOIcon::_render() { FXICOIcon::render(); }

void FXPyICOIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyICOIcon::_scale(FXint w,FXint h) { FXICOIcon::scale(w,h); }

void FXPyICOIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyICOIcon::_mirror(FXbool horizontal,FXbool vertical) { FXICOIcon::mirror(horizontal,vertical); }

void FXPyICOIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyICOIcon::_rotate(FXint degrees) { FXICOIcon::rotate(degrees); }

void FXPyICOIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyICOIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXICOIcon::crop(x,y,w,h); }

void FXPyICOIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyICOIcon::_savePixels(FXStream& store) const { FXICOIcon::savePixels(store); }

void FXPyICOIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyICOIcon::_loadPixels(FXStream& store) { FXICOIcon::loadPixels(store); }

long FXPyICOImage::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyICOImage::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXICOImage::onDefault(sender,sel,ptr);
  }

void FXPyICOImage::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyICOImage::_create(){ FXICOImage::create(); }

void FXPyICOImage::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyICOImage::_destroy(){ FXICOImage::destroy(); }

void FXPyICOImage::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyICOImage::_detach(){ FXICOImage::detach(); }

void FXPyICOImage::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyICOImage::_resize(FXint w,FXint h){ FXICOImage::resize(w,h); }

void FXPyICOImage::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyICOImage::_restore() { FXICOImage::restore(); }

void FXPyICOImage::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyICOImage::_render() { FXICOImage::render(); }

void FXPyICOImage::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyICOImage::_scale(FXint w,FXint h) { FXICOImage::scale(w,h); }

void FXPyICOImage::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyICOImage::_mirror(FXbool horizontal,FXbool vertical) { FXICOImage::mirror(horizontal,vertical); }

void FXPyICOImage::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyICOImage::_rotate(FXint degrees) { FXICOImage::rotate(degrees); }

void FXPyICOImage::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyICOImage::_crop(FXint x,FXint y,FXint w,FXint h) { FXICOImage::crop(x,y,w,h); }

void FXPyICOImage::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyICOImage::_savePixels(FXStream& store) const { FXICOImage::savePixels(store); }

void FXPyICOImage::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyICOImage::_loadPixels(FXStream& store) { FXICOImage::loadPixels(store); }

long FXPyDelegator::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDelegator::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDelegator::onDefault(sender,sel,ptr);
  }

long FXPyImageView::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyImageView::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXImageView::onDefault(sender,sel,ptr);
  }

void FXPyImageView::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyImageView::_create(){ FXImageView::create(); }

void FXPyImageView::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyImageView::_destroy(){ FXImageView::destroy(); }

void FXPyImageView::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyImageView::_detach(){ FXImageView::detach(); }

void FXPyImageView::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyImageView::_resize(FXint w,FXint h){ FXImageView::resize(w,h); }

void FXPyImageView::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyImageView::_enable(){ FXImageView::enable(); }

void FXPyImageView::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyImageView::_disable(){ FXImageView::disable(); }

void FXPyImageView::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyImageView::_show(){ FXImageView::show(); }

void FXPyImageView::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyImageView::_hide(){ FXImageView::hide(); }

void FXPyImageView::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyImageView::_lowerWindow(){ FXImageView::lower(); }

FXint FXPyImageView::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyImageView::_getDefaultHeight() { return FXImageView::getDefaultHeight(); }

FXint FXPyImageView::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyImageView::_getDefaultWidth() { return FXImageView::getDefaultWidth(); }

FXint FXPyImageView::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyImageView::_getWidthForHeight(FXint h) { return FXImageView::getWidthForHeight(h); }

FXint FXPyImageView::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyImageView::_getHeightForWidth(FXint w) { return FXImageView::getHeightForWidth(w); }

void FXPyImageView::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyImageView::_layout() { FXImageView::layout(); }

void FXPyImageView::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyImageView::_recalc() { FXImageView::recalc(); }

FXbool FXPyImageView::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyImageView::_isComposite() const { return FXImageView::isComposite(); }

void FXPyImageView::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyImageView::_move(FXint x,FXint y){ FXImageView::move(x,y); }

void FXPyImageView::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyImageView::_position(FXint x,FXint y,FXint w,FXint h){ FXImageView::position(x,y,w,h); }

FXbool FXPyImageView::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyImageView::_canFocus() const { return FXImageView::canFocus(); }

void FXPyImageView::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyImageView::_setFocus(){ FXImageView::setFocus(); }

void FXPyImageView::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyImageView::_killFocus(){ FXImageView::killFocus(); }

void FXPyImageView::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyImageView::_setDefault(FXbool enable){ FXImageView::setDefault(enable); }

FXbool FXPyImageView::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyImageView::_contains(FXint x,FXint y) const { return FXImageView::contains(x,y); }

FXbool FXPyImageView::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyImageView::_doesSaveUnder() const { return FXImageView::doesSaveUnder(); }

void FXPyImageView::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyImageView::_reparent(FXComposite* newparent) { FXImageView::reparent(newparent); }

void FXPyImageView::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyImageView::_setBackColor(FXColor clr) { FXImageView::setBackColor(clr); }

FXint FXPyImageView::getContentWidth() { return FXPyCallIntFunction(this,"getContentWidth"); }
FXint FXPyImageView::_getContentWidth() { return FXImageView::getContentWidth(); }

FXint FXPyImageView::getContentHeight() { return FXPyCallIntFunction(this,"getContentHeight"); }
FXint FXPyImageView::_getContentHeight() { return FXImageView::getContentHeight(); }

FXint FXPyImageView::getViewportWidth() { return FXPyCallIntFunction(this,"getViewportWidth"); }
FXint FXPyImageView::_getViewportWidth() { return FXImageView::getViewportWidth(); }

FXint FXPyImageView::getViewportHeight() { return FXPyCallIntFunction(this,"getViewportHeight"); }
FXint FXPyImageView::_getViewportHeight() { return FXImageView::getViewportHeight(); }

void FXPyImageView::moveContents(FXint x,FXint y) { FXPyCallVoidFunction(this,"moveContents",x,y); }
void FXPyImageView::_moveContents(FXint x,FXint y) { FXImageView::moveContents(x,y); }

long FXPyToolbar::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyToolbar::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXToolbar::onDefault(sender,sel,ptr);
  }

void FXPyToolbar::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyToolbar::_create(){ FXToolbar::create(); }

void FXPyToolbar::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyToolbar::_destroy(){ FXToolbar::destroy(); }

void FXPyToolbar::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyToolbar::_detach(){ FXToolbar::detach(); }

void FXPyToolbar::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyToolbar::_resize(FXint w,FXint h){ FXToolbar::resize(w,h); }

void FXPyToolbar::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyToolbar::_enable(){ FXToolbar::enable(); }

void FXPyToolbar::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyToolbar::_disable(){ FXToolbar::disable(); }

void FXPyToolbar::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyToolbar::_show(){ FXToolbar::show(); }

void FXPyToolbar::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyToolbar::_hide(){ FXToolbar::hide(); }

void FXPyToolbar::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyToolbar::_lowerWindow(){ FXToolbar::lower(); }

FXint FXPyToolbar::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyToolbar::_getDefaultHeight() { return FXToolbar::getDefaultHeight(); }

FXint FXPyToolbar::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyToolbar::_getDefaultWidth() { return FXToolbar::getDefaultWidth(); }

FXint FXPyToolbar::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyToolbar::_getWidthForHeight(FXint h) { return FXToolbar::getWidthForHeight(h); }

FXint FXPyToolbar::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyToolbar::_getHeightForWidth(FXint w) { return FXToolbar::getHeightForWidth(w); }

void FXPyToolbar::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyToolbar::_layout() { FXToolbar::layout(); }

void FXPyToolbar::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyToolbar::_recalc() { FXToolbar::recalc(); }

FXbool FXPyToolbar::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyToolbar::_isComposite() const { return FXToolbar::isComposite(); }

void FXPyToolbar::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyToolbar::_move(FXint x,FXint y){ FXToolbar::move(x,y); }

void FXPyToolbar::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyToolbar::_position(FXint x,FXint y,FXint w,FXint h){ FXToolbar::position(x,y,w,h); }

FXbool FXPyToolbar::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyToolbar::_canFocus() const { return FXToolbar::canFocus(); }

void FXPyToolbar::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyToolbar::_setFocus(){ FXToolbar::setFocus(); }

void FXPyToolbar::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyToolbar::_killFocus(){ FXToolbar::killFocus(); }

void FXPyToolbar::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyToolbar::_setDefault(FXbool enable){ FXToolbar::setDefault(enable); }

FXbool FXPyToolbar::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyToolbar::_contains(FXint x,FXint y) const { return FXToolbar::contains(x,y); }

FXbool FXPyToolbar::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyToolbar::_doesSaveUnder() const { return FXToolbar::doesSaveUnder(); }

void FXPyToolbar::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyToolbar::_reparent(FXComposite* newparent) { FXToolbar::reparent(newparent); }

void FXPyToolbar::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyToolbar::_setBackColor(FXColor clr) { FXToolbar::setBackColor(clr); }

void FXPyToolbar::dock(FXuint side,FXWindow* after){ FXPyCallVoidFunction(this,"dock",side,after); }
void FXPyToolbar::_dock(FXuint side,FXWindow* after){ FXToolbar::dock(side,after); }

void FXPyToolbar::undock(){ FXPyCallVoidFunction(this,"undock"); }
void FXPyToolbar::_undock(){ FXToolbar::undock(); }

long FXPyToolbarShell::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyToolbarShell::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXToolbarShell::onDefault(sender,sel,ptr);
  }

void FXPyToolbarShell::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyToolbarShell::_create(){ FXToolbarShell::create(); }

void FXPyToolbarShell::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyToolbarShell::_destroy(){ FXToolbarShell::destroy(); }

void FXPyToolbarShell::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyToolbarShell::_detach(){ FXToolbarShell::detach(); }

void FXPyToolbarShell::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyToolbarShell::_resize(FXint w,FXint h){ FXToolbarShell::resize(w,h); }

void FXPyToolbarShell::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyToolbarShell::_enable(){ FXToolbarShell::enable(); }

void FXPyToolbarShell::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyToolbarShell::_disable(){ FXToolbarShell::disable(); }

void FXPyToolbarShell::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyToolbarShell::_show(){ FXToolbarShell::show(); }

void FXPyToolbarShell::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyToolbarShell::_hide(){ FXToolbarShell::hide(); }

void FXPyToolbarShell::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyToolbarShell::_lowerWindow(){ FXToolbarShell::lower(); }

FXint FXPyToolbarShell::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyToolbarShell::_getDefaultHeight() { return FXToolbarShell::getDefaultHeight(); }

FXint FXPyToolbarShell::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyToolbarShell::_getDefaultWidth() { return FXToolbarShell::getDefaultWidth(); }

FXint FXPyToolbarShell::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyToolbarShell::_getWidthForHeight(FXint h) { return FXToolbarShell::getWidthForHeight(h); }

FXint FXPyToolbarShell::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyToolbarShell::_getHeightForWidth(FXint w) { return FXToolbarShell::getHeightForWidth(w); }

void FXPyToolbarShell::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyToolbarShell::_layout() { FXToolbarShell::layout(); }

void FXPyToolbarShell::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyToolbarShell::_recalc() { FXToolbarShell::recalc(); }

FXbool FXPyToolbarShell::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyToolbarShell::_isComposite() const { return FXToolbarShell::isComposite(); }

void FXPyToolbarShell::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyToolbarShell::_move(FXint x,FXint y){ FXToolbarShell::move(x,y); }

void FXPyToolbarShell::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyToolbarShell::_position(FXint x,FXint y,FXint w,FXint h){ FXToolbarShell::position(x,y,w,h); }

FXbool FXPyToolbarShell::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyToolbarShell::_canFocus() const { return FXToolbarShell::canFocus(); }

void FXPyToolbarShell::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyToolbarShell::_setFocus(){ FXToolbarShell::setFocus(); }

void FXPyToolbarShell::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyToolbarShell::_killFocus(){ FXToolbarShell::killFocus(); }

void FXPyToolbarShell::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyToolbarShell::_setDefault(FXbool enable){ FXToolbarShell::setDefault(enable); }

FXbool FXPyToolbarShell::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyToolbarShell::_contains(FXint x,FXint y) const { return FXToolbarShell::contains(x,y); }

FXbool FXPyToolbarShell::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyToolbarShell::_doesSaveUnder() const { return FXToolbarShell::doesSaveUnder(); }

void FXPyToolbarShell::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyToolbarShell::_reparent(FXComposite* newparent) { FXToolbarShell::reparent(newparent); }

void FXPyToolbarShell::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyToolbarShell::_setBackColor(FXColor clr) { FXToolbarShell::setBackColor(clr); }

void FXPyToolbarShell::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyToolbarShell::_iconify() { FXToolbarShell::iconify(); }

void FXPyToolbarShell::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyToolbarShell::_deiconify() { FXToolbarShell::deiconify(); }

void FXPyToolbarShell::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyToolbarShell::_show(FXuint placement) { FXToolbarShell::show(placement); }

long FXPyDirDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDirDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDirDialog::onDefault(sender,sel,ptr);
  }

void FXPyDirDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDirDialog::_create(){ FXDirDialog::create(); }

void FXPyDirDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDirDialog::_destroy(){ FXDirDialog::destroy(); }

void FXPyDirDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDirDialog::_detach(){ FXDirDialog::detach(); }

void FXPyDirDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDirDialog::_resize(FXint w,FXint h){ FXDirDialog::resize(w,h); }

void FXPyDirDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDirDialog::_enable(){ FXDirDialog::enable(); }

void FXPyDirDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDirDialog::_disable(){ FXDirDialog::disable(); }

void FXPyDirDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDirDialog::_show(){ FXDirDialog::show(); }

void FXPyDirDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDirDialog::_hide(){ FXDirDialog::hide(); }

void FXPyDirDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDirDialog::_lowerWindow(){ FXDirDialog::lower(); }

FXint FXPyDirDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDirDialog::_getDefaultHeight() { return FXDirDialog::getDefaultHeight(); }

FXint FXPyDirDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDirDialog::_getDefaultWidth() { return FXDirDialog::getDefaultWidth(); }

FXint FXPyDirDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDirDialog::_getWidthForHeight(FXint h) { return FXDirDialog::getWidthForHeight(h); }

FXint FXPyDirDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDirDialog::_getHeightForWidth(FXint w) { return FXDirDialog::getHeightForWidth(w); }

void FXPyDirDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDirDialog::_layout() { FXDirDialog::layout(); }

void FXPyDirDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDirDialog::_recalc() { FXDirDialog::recalc(); }

FXbool FXPyDirDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDirDialog::_isComposite() const { return FXDirDialog::isComposite(); }

void FXPyDirDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDirDialog::_move(FXint x,FXint y){ FXDirDialog::move(x,y); }

void FXPyDirDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDirDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXDirDialog::position(x,y,w,h); }

FXbool FXPyDirDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDirDialog::_canFocus() const { return FXDirDialog::canFocus(); }

void FXPyDirDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDirDialog::_setFocus(){ FXDirDialog::setFocus(); }

void FXPyDirDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDirDialog::_killFocus(){ FXDirDialog::killFocus(); }

void FXPyDirDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDirDialog::_setDefault(FXbool enable){ FXDirDialog::setDefault(enable); }

FXbool FXPyDirDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDirDialog::_contains(FXint x,FXint y) const { return FXDirDialog::contains(x,y); }

FXbool FXPyDirDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDirDialog::_doesSaveUnder() const { return FXDirDialog::doesSaveUnder(); }

void FXPyDirDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDirDialog::_reparent(FXComposite* newparent) { FXDirDialog::reparent(newparent); }

void FXPyDirDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDirDialog::_setBackColor(FXColor clr) { FXDirDialog::setBackColor(clr); }

void FXPyDirDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyDirDialog::_iconify() { FXDirDialog::iconify(); }

void FXPyDirDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyDirDialog::_deiconify() { FXDirDialog::deiconify(); }

void FXPyDirDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyDirDialog::_show(FXuint placement) { FXDirDialog::show(placement); }

long FXPyDirSelector::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDirSelector::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDirSelector::onDefault(sender,sel,ptr);
  }

void FXPyDirSelector::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDirSelector::_create(){ FXDirSelector::create(); }

void FXPyDirSelector::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDirSelector::_destroy(){ FXDirSelector::destroy(); }

void FXPyDirSelector::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDirSelector::_detach(){ FXDirSelector::detach(); }

void FXPyDirSelector::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDirSelector::_resize(FXint w,FXint h){ FXDirSelector::resize(w,h); }

void FXPyDirSelector::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDirSelector::_enable(){ FXDirSelector::enable(); }

void FXPyDirSelector::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDirSelector::_disable(){ FXDirSelector::disable(); }

void FXPyDirSelector::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDirSelector::_show(){ FXDirSelector::show(); }

void FXPyDirSelector::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDirSelector::_hide(){ FXDirSelector::hide(); }

void FXPyDirSelector::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDirSelector::_lowerWindow(){ FXDirSelector::lower(); }

FXint FXPyDirSelector::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDirSelector::_getDefaultHeight() { return FXDirSelector::getDefaultHeight(); }

FXint FXPyDirSelector::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDirSelector::_getDefaultWidth() { return FXDirSelector::getDefaultWidth(); }

FXint FXPyDirSelector::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDirSelector::_getWidthForHeight(FXint h) { return FXDirSelector::getWidthForHeight(h); }

FXint FXPyDirSelector::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDirSelector::_getHeightForWidth(FXint w) { return FXDirSelector::getHeightForWidth(w); }

void FXPyDirSelector::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDirSelector::_layout() { FXDirSelector::layout(); }

void FXPyDirSelector::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDirSelector::_recalc() { FXDirSelector::recalc(); }

FXbool FXPyDirSelector::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDirSelector::_isComposite() const { return FXDirSelector::isComposite(); }

void FXPyDirSelector::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDirSelector::_move(FXint x,FXint y){ FXDirSelector::move(x,y); }

void FXPyDirSelector::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDirSelector::_position(FXint x,FXint y,FXint w,FXint h){ FXDirSelector::position(x,y,w,h); }

FXbool FXPyDirSelector::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDirSelector::_canFocus() const { return FXDirSelector::canFocus(); }

void FXPyDirSelector::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDirSelector::_setFocus(){ FXDirSelector::setFocus(); }

void FXPyDirSelector::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDirSelector::_killFocus(){ FXDirSelector::killFocus(); }

void FXPyDirSelector::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDirSelector::_setDefault(FXbool enable){ FXDirSelector::setDefault(enable); }

FXbool FXPyDirSelector::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDirSelector::_contains(FXint x,FXint y) const { return FXDirSelector::contains(x,y); }

FXbool FXPyDirSelector::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDirSelector::_doesSaveUnder() const { return FXDirSelector::doesSaveUnder(); }

void FXPyDirSelector::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDirSelector::_reparent(FXComposite* newparent) { FXDirSelector::reparent(newparent); }

void FXPyDirSelector::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDirSelector::_setBackColor(FXColor clr) { FXDirSelector::setBackColor(clr); }

long FXPyReplaceDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyReplaceDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXReplaceDialog::onDefault(sender,sel,ptr);
  }

void FXPyReplaceDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyReplaceDialog::_create(){ FXReplaceDialog::create(); }

void FXPyReplaceDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyReplaceDialog::_destroy(){ FXReplaceDialog::destroy(); }

void FXPyReplaceDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyReplaceDialog::_detach(){ FXReplaceDialog::detach(); }

void FXPyReplaceDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyReplaceDialog::_resize(FXint w,FXint h){ FXReplaceDialog::resize(w,h); }

void FXPyReplaceDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyReplaceDialog::_enable(){ FXReplaceDialog::enable(); }

void FXPyReplaceDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyReplaceDialog::_disable(){ FXReplaceDialog::disable(); }

void FXPyReplaceDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyReplaceDialog::_show(){ FXReplaceDialog::show(); }

void FXPyReplaceDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyReplaceDialog::_hide(){ FXReplaceDialog::hide(); }

void FXPyReplaceDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyReplaceDialog::_lowerWindow(){ FXReplaceDialog::lower(); }

FXint FXPyReplaceDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyReplaceDialog::_getDefaultHeight() { return FXReplaceDialog::getDefaultHeight(); }

FXint FXPyReplaceDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyReplaceDialog::_getDefaultWidth() { return FXReplaceDialog::getDefaultWidth(); }

FXint FXPyReplaceDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyReplaceDialog::_getWidthForHeight(FXint h) { return FXReplaceDialog::getWidthForHeight(h); }

FXint FXPyReplaceDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyReplaceDialog::_getHeightForWidth(FXint w) { return FXReplaceDialog::getHeightForWidth(w); }

void FXPyReplaceDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyReplaceDialog::_layout() { FXReplaceDialog::layout(); }

void FXPyReplaceDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyReplaceDialog::_recalc() { FXReplaceDialog::recalc(); }

FXbool FXPyReplaceDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyReplaceDialog::_isComposite() const { return FXReplaceDialog::isComposite(); }

void FXPyReplaceDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyReplaceDialog::_move(FXint x,FXint y){ FXReplaceDialog::move(x,y); }

void FXPyReplaceDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyReplaceDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXReplaceDialog::position(x,y,w,h); }

FXbool FXPyReplaceDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyReplaceDialog::_canFocus() const { return FXReplaceDialog::canFocus(); }

void FXPyReplaceDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyReplaceDialog::_setFocus(){ FXReplaceDialog::setFocus(); }

void FXPyReplaceDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyReplaceDialog::_killFocus(){ FXReplaceDialog::killFocus(); }

void FXPyReplaceDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyReplaceDialog::_setDefault(FXbool enable){ FXReplaceDialog::setDefault(enable); }

FXbool FXPyReplaceDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyReplaceDialog::_contains(FXint x,FXint y) const { return FXReplaceDialog::contains(x,y); }

FXbool FXPyReplaceDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyReplaceDialog::_doesSaveUnder() const { return FXReplaceDialog::doesSaveUnder(); }

void FXPyReplaceDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyReplaceDialog::_reparent(FXComposite* newparent) { FXReplaceDialog::reparent(newparent); }

void FXPyReplaceDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyReplaceDialog::_setBackColor(FXColor clr) { FXReplaceDialog::setBackColor(clr); }

void FXPyReplaceDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyReplaceDialog::_iconify() { FXReplaceDialog::iconify(); }

void FXPyReplaceDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyReplaceDialog::_deiconify() { FXReplaceDialog::deiconify(); }

void FXPyReplaceDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyReplaceDialog::_show(FXuint placement) { FXReplaceDialog::show(placement); }

long FXPySearchDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPySearchDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXSearchDialog::onDefault(sender,sel,ptr);
  }

void FXPySearchDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPySearchDialog::_create(){ FXSearchDialog::create(); }

void FXPySearchDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPySearchDialog::_destroy(){ FXSearchDialog::destroy(); }

void FXPySearchDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPySearchDialog::_detach(){ FXSearchDialog::detach(); }

void FXPySearchDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPySearchDialog::_resize(FXint w,FXint h){ FXSearchDialog::resize(w,h); }

void FXPySearchDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPySearchDialog::_enable(){ FXSearchDialog::enable(); }

void FXPySearchDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPySearchDialog::_disable(){ FXSearchDialog::disable(); }

void FXPySearchDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPySearchDialog::_show(){ FXSearchDialog::show(); }

void FXPySearchDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPySearchDialog::_hide(){ FXSearchDialog::hide(); }

void FXPySearchDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPySearchDialog::_lowerWindow(){ FXSearchDialog::lower(); }

FXint FXPySearchDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPySearchDialog::_getDefaultHeight() { return FXSearchDialog::getDefaultHeight(); }

FXint FXPySearchDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPySearchDialog::_getDefaultWidth() { return FXSearchDialog::getDefaultWidth(); }

FXint FXPySearchDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPySearchDialog::_getWidthForHeight(FXint h) { return FXSearchDialog::getWidthForHeight(h); }

FXint FXPySearchDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPySearchDialog::_getHeightForWidth(FXint w) { return FXSearchDialog::getHeightForWidth(w); }

void FXPySearchDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPySearchDialog::_layout() { FXSearchDialog::layout(); }

void FXPySearchDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPySearchDialog::_recalc() { FXSearchDialog::recalc(); }

FXbool FXPySearchDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPySearchDialog::_isComposite() const { return FXSearchDialog::isComposite(); }

void FXPySearchDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPySearchDialog::_move(FXint x,FXint y){ FXSearchDialog::move(x,y); }

void FXPySearchDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPySearchDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXSearchDialog::position(x,y,w,h); }

FXbool FXPySearchDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPySearchDialog::_canFocus() const { return FXSearchDialog::canFocus(); }

void FXPySearchDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPySearchDialog::_setFocus(){ FXSearchDialog::setFocus(); }

void FXPySearchDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPySearchDialog::_killFocus(){ FXSearchDialog::killFocus(); }

void FXPySearchDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPySearchDialog::_setDefault(FXbool enable){ FXSearchDialog::setDefault(enable); }

FXbool FXPySearchDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPySearchDialog::_contains(FXint x,FXint y) const { return FXSearchDialog::contains(x,y); }

FXbool FXPySearchDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPySearchDialog::_doesSaveUnder() const { return FXSearchDialog::doesSaveUnder(); }

void FXPySearchDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPySearchDialog::_reparent(FXComposite* newparent) { FXSearchDialog::reparent(newparent); }

void FXPySearchDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPySearchDialog::_setBackColor(FXColor clr) { FXSearchDialog::setBackColor(clr); }

void FXPySearchDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPySearchDialog::_iconify() { FXSearchDialog::iconify(); }

void FXPySearchDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPySearchDialog::_deiconify() { FXSearchDialog::deiconify(); }

void FXPySearchDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPySearchDialog::_show(FXuint placement) { FXSearchDialog::show(placement); }

long FXPyGLContext::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyGLContext::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXGLContext::onDefault(sender,sel,ptr);
  }

void FXPyGLContext::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyGLContext::_create(){ FXGLContext::create(); }

void FXPyGLContext::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyGLContext::_detach(){ FXGLContext::detach(); }

void FXPyGLContext::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyGLContext::_destroy(){ FXGLContext::destroy(); }

long FXPyToolbarGrip::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyToolbarGrip::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXToolbarGrip::onDefault(sender,sel,ptr);
  }

void FXPyToolbarGrip::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyToolbarGrip::_create(){ FXToolbarGrip::create(); }

void FXPyToolbarGrip::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyToolbarGrip::_destroy(){ FXToolbarGrip::destroy(); }

void FXPyToolbarGrip::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyToolbarGrip::_detach(){ FXToolbarGrip::detach(); }

void FXPyToolbarGrip::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyToolbarGrip::_resize(FXint w,FXint h){ FXToolbarGrip::resize(w,h); }

void FXPyToolbarGrip::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyToolbarGrip::_enable(){ FXToolbarGrip::enable(); }

void FXPyToolbarGrip::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyToolbarGrip::_disable(){ FXToolbarGrip::disable(); }

void FXPyToolbarGrip::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyToolbarGrip::_show(){ FXToolbarGrip::show(); }

void FXPyToolbarGrip::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyToolbarGrip::_hide(){ FXToolbarGrip::hide(); }

void FXPyToolbarGrip::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyToolbarGrip::_lowerWindow(){ FXToolbarGrip::lower(); }

FXint FXPyToolbarGrip::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyToolbarGrip::_getDefaultHeight() { return FXToolbarGrip::getDefaultHeight(); }

FXint FXPyToolbarGrip::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyToolbarGrip::_getDefaultWidth() { return FXToolbarGrip::getDefaultWidth(); }

FXint FXPyToolbarGrip::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyToolbarGrip::_getWidthForHeight(FXint h) { return FXToolbarGrip::getWidthForHeight(h); }

FXint FXPyToolbarGrip::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyToolbarGrip::_getHeightForWidth(FXint w) { return FXToolbarGrip::getHeightForWidth(w); }

void FXPyToolbarGrip::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyToolbarGrip::_layout() { FXToolbarGrip::layout(); }

void FXPyToolbarGrip::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyToolbarGrip::_recalc() { FXToolbarGrip::recalc(); }

FXbool FXPyToolbarGrip::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyToolbarGrip::_isComposite() const { return FXToolbarGrip::isComposite(); }

void FXPyToolbarGrip::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyToolbarGrip::_move(FXint x,FXint y){ FXToolbarGrip::move(x,y); }

void FXPyToolbarGrip::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyToolbarGrip::_position(FXint x,FXint y,FXint w,FXint h){ FXToolbarGrip::position(x,y,w,h); }

FXbool FXPyToolbarGrip::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyToolbarGrip::_canFocus() const { return FXToolbarGrip::canFocus(); }

void FXPyToolbarGrip::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyToolbarGrip::_setFocus(){ FXToolbarGrip::setFocus(); }

void FXPyToolbarGrip::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyToolbarGrip::_killFocus(){ FXToolbarGrip::killFocus(); }

void FXPyToolbarGrip::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyToolbarGrip::_setDefault(FXbool enable){ FXToolbarGrip::setDefault(enable); }

FXbool FXPyToolbarGrip::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyToolbarGrip::_contains(FXint x,FXint y) const { return FXToolbarGrip::contains(x,y); }

FXbool FXPyToolbarGrip::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyToolbarGrip::_doesSaveUnder() const { return FXToolbarGrip::doesSaveUnder(); }

void FXPyToolbarGrip::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyToolbarGrip::_reparent(FXComposite* newparent) { FXToolbarGrip::reparent(newparent); }

void FXPyToolbarGrip::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyToolbarGrip::_setBackColor(FXColor clr) { FXToolbarGrip::setBackColor(clr); }

long FXPyJPGIcon::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyJPGIcon::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXJPGIcon::onDefault(sender,sel,ptr);
  }

void FXPyJPGIcon::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyJPGIcon::_create(){ FXJPGIcon::create(); }

void FXPyJPGIcon::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyJPGIcon::_destroy(){ FXJPGIcon::destroy(); }

void FXPyJPGIcon::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyJPGIcon::_detach(){ FXJPGIcon::detach(); }

void FXPyJPGIcon::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyJPGIcon::_resize(FXint w,FXint h){ FXJPGIcon::resize(w,h); }

void FXPyJPGIcon::restore()  { FXPyCallVoidFunction(this,"restore"); }
void FXPyJPGIcon::_restore() { FXJPGIcon::restore(); }

void FXPyJPGIcon::render()  { FXPyCallVoidFunction(this,"render"); }
void FXPyJPGIcon::_render() { FXJPGIcon::render(); }

void FXPyJPGIcon::scale(FXint w,FXint h)  { FXPyCallVoidFunction(this,"scale",w,h); }
void FXPyJPGIcon::_scale(FXint w,FXint h) { FXJPGIcon::scale(w,h); }

void FXPyJPGIcon::mirror(FXbool horizontal,FXbool vertical)  { FXPyCallVoidFunction(this,"mirror",horizontal,vertical); }
void FXPyJPGIcon::_mirror(FXbool horizontal,FXbool vertical) { FXJPGIcon::mirror(horizontal,vertical); }

void FXPyJPGIcon::rotate(FXint degrees)  { FXPyCallVoidFunction(this,"rotate",degrees); }
void FXPyJPGIcon::_rotate(FXint degrees) { FXJPGIcon::rotate(degrees); }

void FXPyJPGIcon::crop(FXint x,FXint y,FXint w,FXint h)  { FXPyCallVoidFunction(this,"crop",x,y,w,h); }
void FXPyJPGIcon::_crop(FXint x,FXint y,FXint w,FXint h) { FXJPGIcon::crop(x,y,w,h); }

void FXPyJPGIcon::savePixels(FXStream& store) const { FXPyCallVoidFunction(this,"savePixels",store); }
void FXPyJPGIcon::_savePixels(FXStream& store) const { FXJPGIcon::savePixels(store); }

void FXPyJPGIcon::loadPixels(FXStream& store) { FXPyCallVoidFunction(this,"loadPixels",store); }
void FXPyJPGIcon::_loadPixels(FXStream& store) { FXJPGIcon::loadPixels(store); }

long FXPyListBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyListBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXListBox::onDefault(sender,sel,ptr);
  }

void FXPyListBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyListBox::_create(){ FXListBox::create(); }

void FXPyListBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyListBox::_destroy(){ FXListBox::destroy(); }

void FXPyListBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyListBox::_detach(){ FXListBox::detach(); }

void FXPyListBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyListBox::_resize(FXint w,FXint h){ FXListBox::resize(w,h); }

void FXPyListBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyListBox::_enable(){ FXListBox::enable(); }

void FXPyListBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyListBox::_disable(){ FXListBox::disable(); }

void FXPyListBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyListBox::_show(){ FXListBox::show(); }

void FXPyListBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyListBox::_hide(){ FXListBox::hide(); }

void FXPyListBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyListBox::_lowerWindow(){ FXListBox::lower(); }

FXint FXPyListBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyListBox::_getDefaultHeight() { return FXListBox::getDefaultHeight(); }

FXint FXPyListBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyListBox::_getDefaultWidth() { return FXListBox::getDefaultWidth(); }

FXint FXPyListBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyListBox::_getWidthForHeight(FXint h) { return FXListBox::getWidthForHeight(h); }

FXint FXPyListBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyListBox::_getHeightForWidth(FXint w) { return FXListBox::getHeightForWidth(w); }

void FXPyListBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyListBox::_layout() { FXListBox::layout(); }

void FXPyListBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyListBox::_recalc() { FXListBox::recalc(); }

FXbool FXPyListBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyListBox::_isComposite() const { return FXListBox::isComposite(); }

void FXPyListBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyListBox::_move(FXint x,FXint y){ FXListBox::move(x,y); }

void FXPyListBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyListBox::_position(FXint x,FXint y,FXint w,FXint h){ FXListBox::position(x,y,w,h); }

FXbool FXPyListBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyListBox::_canFocus() const { return FXListBox::canFocus(); }

void FXPyListBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyListBox::_setFocus(){ FXListBox::setFocus(); }

void FXPyListBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyListBox::_killFocus(){ FXListBox::killFocus(); }

void FXPyListBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyListBox::_setDefault(FXbool enable){ FXListBox::setDefault(enable); }

FXbool FXPyListBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyListBox::_contains(FXint x,FXint y) const { return FXListBox::contains(x,y); }

FXbool FXPyListBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyListBox::_doesSaveUnder() const { return FXListBox::doesSaveUnder(); }

void FXPyListBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyListBox::_reparent(FXComposite* newparent) { FXListBox::reparent(newparent); }

void FXPyListBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyListBox::_setBackColor(FXColor clr) { FXListBox::setBackColor(clr); }

long FXPyDriveBox::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDriveBox::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDriveBox::onDefault(sender,sel,ptr);
  }

void FXPyDriveBox::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyDriveBox::_create(){ FXDriveBox::create(); }

void FXPyDriveBox::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyDriveBox::_destroy(){ FXDriveBox::destroy(); }

void FXPyDriveBox::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyDriveBox::_detach(){ FXDriveBox::detach(); }

void FXPyDriveBox::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyDriveBox::_resize(FXint w,FXint h){ FXDriveBox::resize(w,h); }

void FXPyDriveBox::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyDriveBox::_enable(){ FXDriveBox::enable(); }

void FXPyDriveBox::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyDriveBox::_disable(){ FXDriveBox::disable(); }

void FXPyDriveBox::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyDriveBox::_show(){ FXDriveBox::show(); }

void FXPyDriveBox::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyDriveBox::_hide(){ FXDriveBox::hide(); }

void FXPyDriveBox::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyDriveBox::_lowerWindow(){ FXDriveBox::lower(); }

FXint FXPyDriveBox::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyDriveBox::_getDefaultHeight() { return FXDriveBox::getDefaultHeight(); }

FXint FXPyDriveBox::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyDriveBox::_getDefaultWidth() { return FXDriveBox::getDefaultWidth(); }

FXint FXPyDriveBox::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyDriveBox::_getWidthForHeight(FXint h) { return FXDriveBox::getWidthForHeight(h); }

FXint FXPyDriveBox::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyDriveBox::_getHeightForWidth(FXint w) { return FXDriveBox::getHeightForWidth(w); }

void FXPyDriveBox::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyDriveBox::_layout() { FXDriveBox::layout(); }

void FXPyDriveBox::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyDriveBox::_recalc() { FXDriveBox::recalc(); }

FXbool FXPyDriveBox::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyDriveBox::_isComposite() const { return FXDriveBox::isComposite(); }

void FXPyDriveBox::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyDriveBox::_move(FXint x,FXint y){ FXDriveBox::move(x,y); }

void FXPyDriveBox::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyDriveBox::_position(FXint x,FXint y,FXint w,FXint h){ FXDriveBox::position(x,y,w,h); }

FXbool FXPyDriveBox::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyDriveBox::_canFocus() const { return FXDriveBox::canFocus(); }

void FXPyDriveBox::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyDriveBox::_setFocus(){ FXDriveBox::setFocus(); }

void FXPyDriveBox::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyDriveBox::_killFocus(){ FXDriveBox::killFocus(); }

void FXPyDriveBox::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyDriveBox::_setDefault(FXbool enable){ FXDriveBox::setDefault(enable); }

FXbool FXPyDriveBox::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyDriveBox::_contains(FXint x,FXint y) const { return FXDriveBox::contains(x,y); }

FXbool FXPyDriveBox::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyDriveBox::_doesSaveUnder() const { return FXDriveBox::doesSaveUnder(); }

void FXPyDriveBox::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyDriveBox::_reparent(FXComposite* newparent) { FXDriveBox::reparent(newparent); }

void FXPyDriveBox::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyDriveBox::_setBackColor(FXColor clr) { FXDriveBox::setBackColor(clr); }

long FXPyInputDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyInputDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXInputDialog::onDefault(sender,sel,ptr);
  }

void FXPyInputDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyInputDialog::_create(){ FXInputDialog::create(); }

void FXPyInputDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyInputDialog::_destroy(){ FXInputDialog::destroy(); }

void FXPyInputDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyInputDialog::_detach(){ FXInputDialog::detach(); }

void FXPyInputDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyInputDialog::_resize(FXint w,FXint h){ FXInputDialog::resize(w,h); }

void FXPyInputDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyInputDialog::_enable(){ FXInputDialog::enable(); }

void FXPyInputDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyInputDialog::_disable(){ FXInputDialog::disable(); }

void FXPyInputDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyInputDialog::_show(){ FXInputDialog::show(); }

void FXPyInputDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyInputDialog::_hide(){ FXInputDialog::hide(); }

void FXPyInputDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyInputDialog::_lowerWindow(){ FXInputDialog::lower(); }

FXint FXPyInputDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyInputDialog::_getDefaultHeight() { return FXInputDialog::getDefaultHeight(); }

FXint FXPyInputDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyInputDialog::_getDefaultWidth() { return FXInputDialog::getDefaultWidth(); }

FXint FXPyInputDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyInputDialog::_getWidthForHeight(FXint h) { return FXInputDialog::getWidthForHeight(h); }

FXint FXPyInputDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyInputDialog::_getHeightForWidth(FXint w) { return FXInputDialog::getHeightForWidth(w); }

void FXPyInputDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyInputDialog::_layout() { FXInputDialog::layout(); }

void FXPyInputDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyInputDialog::_recalc() { FXInputDialog::recalc(); }

FXbool FXPyInputDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyInputDialog::_isComposite() const { return FXInputDialog::isComposite(); }

void FXPyInputDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyInputDialog::_move(FXint x,FXint y){ FXInputDialog::move(x,y); }

void FXPyInputDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyInputDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXInputDialog::position(x,y,w,h); }

FXbool FXPyInputDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyInputDialog::_canFocus() const { return FXInputDialog::canFocus(); }

void FXPyInputDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyInputDialog::_setFocus(){ FXInputDialog::setFocus(); }

void FXPyInputDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyInputDialog::_killFocus(){ FXInputDialog::killFocus(); }

void FXPyInputDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyInputDialog::_setDefault(FXbool enable){ FXInputDialog::setDefault(enable); }

FXbool FXPyInputDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyInputDialog::_contains(FXint x,FXint y) const { return FXInputDialog::contains(x,y); }

FXbool FXPyInputDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyInputDialog::_doesSaveUnder() const { return FXInputDialog::doesSaveUnder(); }

void FXPyInputDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyInputDialog::_reparent(FXComposite* newparent) { FXInputDialog::reparent(newparent); }

void FXPyInputDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyInputDialog::_setBackColor(FXColor clr) { FXInputDialog::setBackColor(clr); }

void FXPyInputDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyInputDialog::_iconify() { FXInputDialog::iconify(); }

void FXPyInputDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyInputDialog::_deiconify() { FXInputDialog::deiconify(); }

void FXPyInputDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyInputDialog::_show(FXuint placement) { FXInputDialog::show(placement); }

long FXPyProgressDialog::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyProgressDialog::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXProgressDialog::onDefault(sender,sel,ptr);
  }

void FXPyProgressDialog::create(){ FXPyCallVoidFunction(this,"create"); }
void FXPyProgressDialog::_create(){ FXProgressDialog::create(); }

void FXPyProgressDialog::destroy(){ FXPyCallVoidFunction(this,"destroy"); }
void FXPyProgressDialog::_destroy(){ FXProgressDialog::destroy(); }

void FXPyProgressDialog::detach(){ FXPyCallVoidFunction(this,"detach"); }
void FXPyProgressDialog::_detach(){ FXProgressDialog::detach(); }

void FXPyProgressDialog::resize(FXint w,FXint h){ FXPyCallVoidFunction(this,"resize",w,h); }
void FXPyProgressDialog::_resize(FXint w,FXint h){ FXProgressDialog::resize(w,h); }

void FXPyProgressDialog::enable(){ FXPyCallVoidFunction(this,"enable"); }
void FXPyProgressDialog::_enable(){ FXProgressDialog::enable(); }

void FXPyProgressDialog::disable(){ FXPyCallVoidFunction(this,"disable"); }
void FXPyProgressDialog::_disable(){ FXProgressDialog::disable(); }

void FXPyProgressDialog::show(){ FXPyCallVoidFunction(this,"show"); }
void FXPyProgressDialog::_show(){ FXProgressDialog::show(); }

void FXPyProgressDialog::hide(){ FXPyCallVoidFunction(this,"hide"); }
void FXPyProgressDialog::_hide(){ FXProgressDialog::hide(); }

void FXPyProgressDialog::lower(){ FXPyCallVoidFunction(this,"lower"); }
void FXPyProgressDialog::_lowerWindow(){ FXProgressDialog::lower(); }

FXint FXPyProgressDialog::getDefaultHeight() { return FXPyCallIntFunction(this,"getDefaultHeight"); }
FXint FXPyProgressDialog::_getDefaultHeight() { return FXProgressDialog::getDefaultHeight(); }

FXint FXPyProgressDialog::getDefaultWidth() { return FXPyCallIntFunction(this,"getDefaultWidth"); }
FXint FXPyProgressDialog::_getDefaultWidth() { return FXProgressDialog::getDefaultWidth(); }

FXint FXPyProgressDialog::getWidthForHeight(FXint h) { return FXPyCallIntFunction(this,"getWidthForHeight",h); }
FXint FXPyProgressDialog::_getWidthForHeight(FXint h) { return FXProgressDialog::getWidthForHeight(h); }

FXint FXPyProgressDialog::getHeightForWidth(FXint w) { return FXPyCallIntFunction(this,"getHeightForWidth",w); }
FXint FXPyProgressDialog::_getHeightForWidth(FXint w) { return FXProgressDialog::getHeightForWidth(w); }

void FXPyProgressDialog::layout() { FXPyCallVoidFunction(this,"layout"); }
void FXPyProgressDialog::_layout() { FXProgressDialog::layout(); }

void FXPyProgressDialog::recalc() { FXPyCallVoidFunction(this,"recalc"); }
void FXPyProgressDialog::_recalc() { FXProgressDialog::recalc(); }

FXbool FXPyProgressDialog::isComposite() const { return FXPyCallBoolFunction(this,"isComposite"); }
FXbool FXPyProgressDialog::_isComposite() const { return FXProgressDialog::isComposite(); }

void FXPyProgressDialog::move(FXint x,FXint y){ FXPyCallVoidFunction(this,"move",x,y); }
void FXPyProgressDialog::_move(FXint x,FXint y){ FXProgressDialog::move(x,y); }

void FXPyProgressDialog::position(FXint x,FXint y,FXint w,FXint h){ FXPyCallVoidFunction(this,"position",x,y,w,h); }
void FXPyProgressDialog::_position(FXint x,FXint y,FXint w,FXint h){ FXProgressDialog::position(x,y,w,h); }

FXbool FXPyProgressDialog::canFocus() const { return FXPyCallBoolFunction(this,"canFocus"); }
FXbool FXPyProgressDialog::_canFocus() const { return FXProgressDialog::canFocus(); }

void FXPyProgressDialog::setFocus(){ FXPyCallVoidFunction(this,"setFocus"); }
void FXPyProgressDialog::_setFocus(){ FXProgressDialog::setFocus(); }

void FXPyProgressDialog::killFocus(){ FXPyCallVoidFunction(this,"killFocus"); }
void FXPyProgressDialog::_killFocus(){ FXProgressDialog::killFocus(); }

void FXPyProgressDialog::setDefault(FXbool enable){ FXPyCallVoidFunction(this,"setDefault",enable); }
void FXPyProgressDialog::_setDefault(FXbool enable){ FXProgressDialog::setDefault(enable); }

FXbool FXPyProgressDialog::contains(FXint x,FXint y) const { return FXPyCallBoolFunction(this,"contains",x,y); }
FXbool FXPyProgressDialog::_contains(FXint x,FXint y) const { return FXProgressDialog::contains(x,y); }

FXbool FXPyProgressDialog::doesSaveUnder() const { return FXPyCallBoolFunction(this,"doesSaveUnder"); }
FXbool FXPyProgressDialog::_doesSaveUnder() const { return FXProgressDialog::doesSaveUnder(); }

void FXPyProgressDialog::reparent(FXComposite* newparent) { FXPyCallVoidFunction(this,"reparent",newparent); }
void FXPyProgressDialog::_reparent(FXComposite* newparent) { FXProgressDialog::reparent(newparent); }

void FXPyProgressDialog::setBackColor(FXColor clr) { FXPyCallVoidFunction(this,"setBackColor",clr); }
void FXPyProgressDialog::_setBackColor(FXColor clr) { FXProgressDialog::setBackColor(clr); }

void FXPyProgressDialog::iconify() { FXPyCallVoidFunction(this, "iconify"); }
void FXPyProgressDialog::_iconify() { FXProgressDialog::iconify(); }

void FXPyProgressDialog::deiconify() { FXPyCallVoidFunction(this, "deiconify"); }
void FXPyProgressDialog::_deiconify() { FXProgressDialog::deiconify(); }

void FXPyProgressDialog::show(FXuint placement) { FXPyCallVoidFunction(this, "show", placement); }
void FXPyProgressDialog::_show(FXuint placement) { FXProgressDialog::show(placement); }

long FXPyDataTarget::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDataTarget::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDataTarget::onDefault(sender,sel,ptr);
  }

long FXPyDebugTarget::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return ::_onDefault(this,sender,sel,ptr);
  }

long FXPyDebugTarget::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXDebugTarget::onDefault(sender,sel,ptr);
  }

