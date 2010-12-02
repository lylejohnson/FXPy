public:
  virtual void restore();
  void _restore();

  virtual void render();
  void _render();

  virtual void scale(FXint w,FXint h);
  void _scale(FXint w,FXint h);

  virtual void mirror(FXbool horizontal,FXbool vertical);
  void _mirror(FXbool horizontal,FXbool vertical);

  virtual void rotate(FXint degrees);
  void _rotate(FXint degrees);

  virtual void crop(FXint x,FXint y,FXint w,FXint h);
  void _crop(FXint x,FXint y,FXint w,FXint h);

  virtual void savePixels(FXStream& store) const;
  void _savePixels(FXStream& store) const;

  virtual void loadPixels(FXStream& store);
  void _loadPixels(FXStream& store);

