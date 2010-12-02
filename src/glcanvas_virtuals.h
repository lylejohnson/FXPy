public:
  // Overrides the base class version of isCurrent()
  virtual FXbool isCurrent() const;

  // Calls the base class version of isCurrent()
  FXbool _isCurrent() const;

  // Overrides the base class version of makeCurrent()
  virtual FXbool makeCurrent();

  // Calls the base class version of makeCurrent()
  FXbool _makeCurrent();

  // Overrides the base class version of makeNonCurrent()
  virtual FXbool makeNonCurrent();

  // Calls the base class version of makeNonCurrent()
  FXbool _makeNonCurrent();

  // Overrides the base class version of swapBuffers()
  virtual void swapBuffers();

  // Calls the base class version of swapBuffers()
  void _swapBuffers();
