public:
  virtual void setText(const FXString& text);
  virtual void setBigIcon(FXIcon *ic);
  virtual void setMiniIcon(FXIcon *ic);
  virtual void setFocus(FXbool focus);
  virtual void setSelected(FXbool selected);
  virtual void setEnabled(FXbool enabled);
  virtual void setDraggable(FXbool draggable);
  virtual void setIconOwned(FXuint owned);
  virtual FXint getWidth(const FXIconList* list) const;
  virtual FXint getHeight(const FXIconList* list) const;
  virtual void create();
  virtual void detach();
  virtual void destroy();
public:
  void _setText(const FXString& text);
  void _setBigIcon(FXIcon *ic);
  void _setMiniIcon(FXIcon *ic);
  void _setFocus(FXbool focus);
  void _setSelected(FXbool selected);
  void _setEnabled(FXbool enabled);
  void _setDraggable(FXbool draggable);
  void _setIconOwned(FXuint owned);
  FXint _getWidth(const FXIconList* list) const;
  FXint _getHeight(const FXIconList* list) const;
  void _create();
  void _detach();
  void _destroy();
