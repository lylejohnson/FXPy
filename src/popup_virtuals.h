public:
  // Overrides the base class version of popup()
  virtual void popup(FXWindow* grabto,FXint x,FXint y,FXint w=0,FXint h=0);

  // Calls the base class version of popup()
  void _popup(FXWindow* grabto,FXint x,FXint y,FXint w=0,FXint h=0);

  // Overrides the base class version of popdown()
  virtual void popdown();

  // Calls the base class version of popdown()
  void _popdown();
