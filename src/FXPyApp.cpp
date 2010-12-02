/***********************************************************************
 * $Id: FXPyApp.cpp,v 1.9 2002/02/11 09:58:49 calvin Exp $
 ***********************************************************************/

#include "xincs.h"
#include "fx.h"
#include "fx3d.h"
#include "FXCURCursor.h"
#include "FXJPGImage.h"
#include "FXJPGIcon.h"
#include "FXPNGIcon.h"
#include "FXPNGImage.h"
#include "FXTIFIcon.h"
#include "FXTIFImage.h"
#include "FXRGBIcon.h"
#include "FXRGBImage.h"
#include "FXICOIcon.h"
#include "FXICOImage.h"
#include "Python.h"
#include "FXPyApp.h"
#include "FXPy.h"

static FXPyApp *theApp=NULL;

FXbool		FXPyApp::pythonExceptionRaised=FALSE;
PyObject	*FXPyApp::errorObject = NULL;


// Message map
FXDEFMAP(FXPyApp) FXPyAppMap[]={
  FXMAPFUNC(SEL_COMMAND,FXPyApp::ID_QUIT,FXPyApp::onCmdQuit),
  };


// Class implementation
FXPy_IMPLEMENT(FXPyApp,FXApp,FXPyAppMap,ARRAYNUMBER(FXPyAppMap))


// Constructor
FXPyApp::FXPyApp(const FXString& appname,const FXString& vendor) : FXApp(appname,vendor){
  theApp=this;
  }


// Run application
PyObject* FXPyApp::FXPyRunApp(){
  FXint result=run();
  if(!pythonExceptionRaised)
    return Py_BuildValue("i",result);
  else
    return NULL;
  }


// Our version of exit(); different from C++ FOX's
void FXPyApp::exit(FXint code){
  
#ifndef WIN32
  destroy();
  closeDisplay();
#else
  destroy();
#endif

  // Write the registry
  reg().write();
  
  // Dump profile data
#ifdef FX_ENABLE_PROFILING
  FXProfiler::speak();
#endif

  // Stop the program
  stop(code);
  }


// Quit application [but make sure we call FXPyApp::exit()]
long FXPyApp::onCmdQuit(FXObject*,FXSelector,void*){
  FXPyApp::exit(0);
  return 1;
  }


// Handle message (from another Python object)
long FXPyApp::_handle(FXObject* sender,FXSelector sel,void* ptr){
  return FXApp::handle(sender,sel,ptr);
  }


// Create all application windows (from FOX)
void FXPyApp::create(){
  FXPyCallVoidFunction(this,"create");
  }


// Create all application windows (from Python)
void FXPyApp::_create(){
  FXApp::create();
  }


// Detach all windows (from FOX)
void FXPyApp::detach(){
  FXPyCallVoidFunction(this,"detach");
  }


// Detach all windows (from Python)
void FXPyApp::_detach(){
  FXApp::detach();
  }


// Destroy all windows (from FOX)
void FXPyApp::destroy(){
  FXPyCallVoidFunction(this,"destroy");
  }


// Destroy all windows (from Python)
void FXPyApp::_destroy(){
  FXApp::destroy();
  }


// Default message handler (from FOX)
long FXPyApp::onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return 0;
  }


// Default message handler (from Python)
long FXPyApp::_onDefault(FXObject* sender,FXSelector sel,void* ptr){
  return FXApp::onDefault(sender,sel,ptr);
  }


// This function is called from the Python readline module; it is
// the function assigned to PyOS_InputHook when the member function
// enableEventHook() is called. The function should process one
// event, if one is immediately available (but without blocking).
int FXPyApp::eventHook(){
  FXRawEvent ev;
  if(theApp->getNextEvent(ev,FALSE))
    theApp->dispatchEvent(ev);
  return 0;
  }


// Enable event hook
void FXPyApp::enableEventHook(){
  if(PyOS_InputHook==NULL){
    PyOS_InputHook=eventHook;
    }
  }


// Disable event hook
void FXPyApp::disableEventHook(){
  if(PyOS_InputHook==eventHook){
    PyOS_InputHook=NULL;
    }
  }

