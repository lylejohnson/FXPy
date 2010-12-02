public:
  virtual void enable();
  void _enable();

  virtual void disable();
  void _disable();

  virtual void show();
  void _show();

  virtual void hide();
  void _hide();

  virtual void lower();
  void _lowerWindow();

  virtual FXint getDefaultHeight();
  FXint _getDefaultHeight();

  virtual FXint getDefaultWidth();
  FXint _getDefaultWidth();

  virtual FXint getWidthForHeight(FXint h);
  FXint _getWidthForHeight(FXint h);

  virtual FXint getHeightForWidth(FXint w);
  FXint _getHeightForWidth(FXint w);

  virtual void layout();
  void _layout();

  virtual void recalc();
  void _recalc();

  virtual FXbool isComposite() const;
  FXbool _isComposite() const;

  virtual void move(FXint x,FXint y);
  void _move(FXint x,FXint y);

  virtual void position(FXint x,FXint y,FXint w,FXint h);
  void _position(FXint x,FXint y,FXint w,FXint h);

  virtual FXbool canFocus() const;
  FXbool _canFocus() const;

  virtual void setFocus();
  void _setFocus();

  virtual void killFocus();
  void _killFocus();
  
  virtual void setDefault(FXbool enable=TRUE);
  void _setDefault(FXbool enable=TRUE);

  virtual FXbool contains(FXint x,FXint y) const;
  FXbool _contains(FXint x,FXint y) const;

  virtual FXbool doesSaveUnder() const;
  FXbool _doesSaveUnder() const;

  virtual void reparent(FXComposite* newparent);
  void _reparent(FXComposite* newparent);

  virtual void setBackColor(FXColor clr);
  void _setBackColor(FXColor clr);
