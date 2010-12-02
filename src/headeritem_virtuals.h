public:
  virtual void setText(const FXString& text);
  virtual void setIcon(FXIcon *ic);
  virtual FXint getWidth(const FXHeader* header) const;
  virtual FXint getHeight(const FXHeader* header) const;
  virtual void create();
  virtual void detach();
  virtual void destroy();
public:
  void _setText(const FXString& text);
  void _setIcon(FXIcon *ic);
  FXint _getWidth(const FXHeader* header) const;
  FXint _getHeight(const FXHeader* header) const;
  void _create();
  void _detach();
  void _destroy();
