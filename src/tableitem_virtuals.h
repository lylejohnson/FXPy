public:
  virtual void setText(const FXString& text);
  virtual void setIcon(FXIcon *ic);
  virtual void setFocus(FXbool focus);
  virtual void setSelected(FXbool selected);
  virtual void setEnabled(FXbool enabled);
  virtual void setDraggable(FXbool draggable);
  virtual void setJustify(FXuint justify);
  virtual FXint getWidth(const FXTable* table) const;
  virtual FXint getHeight(const FXTable* table) const;
  virtual void create();
  virtual void detach();
  virtual void destroy();
public:
  void _setText(const FXString& text);
  void _setIcon(FXIcon *ic);
  void _setFocus(FXbool focus);
  void _setSelected(FXbool selected);
  void _setEnabled(FXbool enabled);
  void _setDraggable(FXbool draggable);
  void _setMarked(FXbool marked);
  void _setJustify(FXuint justify);
  FXint _getWidth(const FXTable* table) const;
  FXint _getHeight(const FXTable* table) const;
  void _create();
  void _detach();
  void _destroy();
