public:
  // Overrides the base class version of draw()
  virtual void draw(FXGLViewer* viewer);

  // Overrides the base class version of hit()
  virtual void hit(FXGLViewer* viewer);

  // Overrides the base class version of canDrag()
  virtual FXbool canDrag() const;

  // Overrides the base class version of canDelete()
  virtual FXbool canDelete() const;

  // Overrides the base class version of drag()
  virtual FXbool drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty);

  // Overrides the base class version of copy()
  virtual FXGLObject* copy();

  // Overrides the base class version of identify()
  virtual FXGLObject* identify(FXuint* path);

public:
  // Calls the base class version of draw()
  void _draw(FXGLViewer* viewer);

  // Calls the base class version of hit()
  void _hit(FXGLViewer* viewer);

  // Calls the base class version of canDrag()
  FXbool _canDrag() const;

  // Calls the base class version of canDelete()
  FXbool _canDelete() const;

  // Calls the base class version of drag()
  FXbool _drag(FXGLViewer* viewer,FXint fx,FXint fy,FXint tx,FXint ty);

  // Calls the base class version of copy()
  FXGLObject* _copy();

  // Calls the base class version of identify
  FXGLObject* _identify(FXuint* path);
