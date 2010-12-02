public:
  // Overrides the base class version of select()
  virtual FXGLObject** select(FXint x,FXint y,FXint w,FXint h);

  // Calls the base class version of select()
  FXGLObject** _select(FXint x,FXint y,FXint w,FXint h);

  // Overrides the base class version of pick()
  virtual FXGLObject* pick(FXint x,FXint y);

  // Calls the base class version of pick()
  FXGLObject* _pick(FXint x,FXint y);
