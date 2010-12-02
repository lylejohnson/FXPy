/***********************************************************************
 * $Id: FXPyApp.h,v 1.4 2001/03/02 00:04:44 ljohnson Exp $
 ***********************************************************************/

#ifndef FXPYAPP_H
#define FXPYAPP_H


class FXPyApp : public FXApp {
  FXDECLARE(FXPyApp)
private:
  FXPyApp(const FXPyApp&);
  FXPyApp& operator=(const FXPyApp&);
  static int eventHook();
public:
  static  FXbool pythonExceptionRaised;
  static  PyObject *errorObject;
public:
  long onCmdQuit(FXObject*,FXSelector,void*);
public:
  // Constructor
  FXPyApp(const FXString& appname="Application",const FXString& vendor="FoxDefault");

  // Create application's windows
  virtual void create();
  void _create();

  // Destroy application's windows
  virtual void destroy();
  void _destroy();

  // Detach application's windows
  virtual void detach();
  void _detach();

  // Overrides base class handle function
  long _handle(FXObject*,FXSelector,void*);

  // Default message handler
  virtual long onDefault(FXObject* sender,FXSelector sel,void* ptr);
  long _onDefault(FXObject* sender,FXSelector sel,void* ptr);

  // Main application event loop
  PyObject* FXPyRunApp();

  // This replaces FXApp::exit()
  void exit(FXint code=0);

  // Special for FXPy; enables event sharing with GNU readline module
  void enableEventHook();

  // Special for FXPy; disables event sharing with GNU readline module
  void disableEventHook();
  };


extern PyObject* FXPyRunApp(PyObject* self,PyObject* args,PyObject* kwargs);


#endif
