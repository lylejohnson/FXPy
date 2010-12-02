/***********************************************************************
 * $Id: FXPyDataTarget.cpp,v 1.7 2002/02/11 09:58:49 calvin Exp $
 ***********************************************************************/

#include "fx.h"
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
#include "fx3d.h"
#include "Python.h"
#include "FXPyApp.h"
#include "FXPy.h"

// Construct using this initial value
FXPyDataTarget::FXPyDataTarget(PyObject* value,FXObject* tgt,FXSelector sel) : FXDataTarget(tgt,sel),intValue(0), doubleValue(0.0) {
  setValue(value);
  }


// Set the value
void FXPyDataTarget::setValue(PyObject* value){
  if(value==Py_None){
    connect();
    }
  else if(PyInt_Check(value)){
    intValue=PyInt_AsLong(value);
    connect(intValue);
    }
  else if(PyFloat_Check(value)){
    doubleValue=PyFloat_AsDouble(value);
    connect(doubleValue);
    }
  else if(PyString_Check(value)){
    stringValue=PyString_AsString(value);
    connect(stringValue);
    }
  else{
    PyErr_SetString(PyExc_TypeError,"can't initialize FXDataTarget with this type.");
    }
  }


// Return the current value
PyObject* FXPyDataTarget::getValue() const {
  switch(type){
    case DT_VOID:
      Py_INCREF(Py_None); return Py_None;
    case DT_CHAR:
      return PyInt_FromLong(*((FXchar*)data));
    case DT_UCHAR:
      return PyInt_FromLong(*((FXuchar*)data));
    case DT_SHORT:
      return PyInt_FromLong(*((FXshort*)data));
    case DT_USHORT:
      return PyInt_FromLong(*((FXushort*)data));
    case DT_INT:
      return PyInt_FromLong(*((FXint*)data));
    case DT_UINT:
      return PyInt_FromLong(*((FXuint*)data));
    case DT_FLOAT:
      return PyFloat_FromDouble(*((FXfloat*)data));
    case DT_DOUBLE:
      return PyFloat_FromDouble(*((FXdouble*)data));
    case DT_STRING:
      return PyString_FromString(((FXString*)data)->text());
    default:
      fxerror("unknown data type in FXPyDataTarget::getValue()");
      return NULL;
    }
  }

