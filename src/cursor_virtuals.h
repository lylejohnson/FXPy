public:
  // Overrides the base class version of savePixels()
  virtual void savePixels(FXStream& store) const;

  // Calls the base class version of savePixels()
  void _savePixels(FXStream& store) const;

  // Overrides the base class version of loadPixels()
  virtual void loadPixels(FXStream& store);

  // Calls the base class version of loadPixels()
  void _loadPixels(FXStream& store);
