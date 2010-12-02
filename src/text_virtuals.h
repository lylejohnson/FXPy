public:
  virtual void setCursorPos(FXint pos,FXbool notify=FALSE);
  void _setCursorPos(FXint pos,FXbool notify=FALSE);

  virtual FXbool extendSelection(FXint pos,FXTextSelectionMode mode=SELECT_CHARS,FXbool notify=FALSE);
  FXbool _extendSelection(FXint pos,FXTextSelectionMode mode=SELECT_CHARS,FXbool notify=FALSE);

  virtual FXbool killSelection(FXbool notify=FALSE);
  FXbool _killSelection(FXbool notify=FALSE);

