/***********************************************************************
 * $Id: FXPy.cpp,v 1.37 2002/02/11 09:58:49 calvin Exp $
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
#include "impl.h"


extern "C" char* SWIG_GetPtr(char*,void**,char*);
extern "C" char* SWIG_GetPtrObj(PyObject*, void**, char*);
extern "C" void SWIG_MakePtr(char*,void*,char*);

extern FXAPI unsigned int fxTraceLevel;

/** Local copy of the current symbol table [as returned by vars()] */
static PyObject *pPyDict = 0;

#ifdef FXPy_WITH_THREADS
extern "C" {
	PyThreadState*	g_FXPyEventThreadState = NULL;
}
#endif

static unsigned int	g_FXPyNestCount = 0;

static PyThreadState* myPyThreadState_Get() {
	PyThreadState* current = PyThreadState_Swap(NULL);
	PyThreadState_Swap(current);
	return current;
}

FXbool FXPyRestoreThread() {
#ifdef FXPy_WITH_THREADS
	g_FXPyNestCount++;
	if (g_FXPyEventThreadState != myPyThreadState_Get()) {
		PyEval_RestoreThread(g_FXPyEventThreadState);
		return TRUE;
	} else
#endif
	return FALSE;
}

void FXPySaveThread(FXbool doSave) {
#ifdef FXPy_WITH_THREADS
	if (doSave) {
		g_FXPyEventThreadState = PyEval_SaveThread();
	}
	g_FXPyNestCount--;
#endif
}

/*
*  Call this function to stop the FOX event loop and stop
*  the program (because an exception of some kind was raised).
*  If "msg" is NULL, assume that Python has already set the
*  error object and data and just quit. If "msg" is not NULL,
*  this indicates some kind of FXPy runtime error (i.e. a
*  bug) and we need to set the error object & string for that.
*/
void raiseException(const char *msg = 0) {
	
	if (msg != 0) {
		fxTraceLevel = 11;
		FXTRACE((10, "raiseException() with msg = \"%s\"\n", msg));
		PyErr_SetString(FXPyApp::errorObject, msg);
	}
	else
		FXTRACE((10, "raiseException(NULL)\n"));
	FXPyApp::pythonExceptionRaised=TRUE;
	FXPyApp::instance()->stop(EXIT_FAILURE);
}


// Store pointer to Python dictionary
PyObject* FXPySetDict(PyObject *, PyObject *args)
{
	FXbool doSave = FXPyRestoreThread();
	if (!PyArg_ParseTuple(args, "O", &pPyDict)) {
		FXPySaveThread(doSave);
		return NULL;
	}
	
	if (!PyDict_Check(pPyDict)) {
		PyErr_SetString(PyExc_TypeError,
			"FXPySetDict must have dictionary object!");
		FXPySaveThread(doSave);
		return NULL;
	}
	Py_INCREF(Py_None);
	FXPySaveThread(doSave);
	return Py_None;
}


// Returns a reference to the dictionary
static FXDict& FXPyGetObjectDict()
{
	static FXDict dict;
	return dict;
}


// Register
void FXPyRegister(PyObject *pPyObject)
{
	Py_INCREF(pPyObject); // FIXME: Artificially increments refcount
	FXObject *pFXObject = 0;
	SWIG_GetPtrObj(pPyObject, (void**) &pFXObject, "_FXObject_p");
	FXString key = FXStringFormat("%p", pFXObject);
	FXbool doSave = FXPyRestoreThread();
	FXPyGetObjectDict().insert(key.text(), pPyObject);
	FXPySaveThread(doSave);
}


// Unregister
void FXPyUnregister(FXObject *pFXObject)
{
	FXString key = FXStringFormat("%p", pFXObject);
	FXbool doSave = FXPyRestoreThread();
	PyObject *pPyObject = (PyObject*) FXPyGetObjectDict().find(key.text());
	if (pPyObject != NULL) {
		FXPyGetObjectDict().remove(key.text());
	}
	FXPySaveThread(doSave);
}


// Given a Python class instance which is a shadow for some
// real C++ object, return the corresponding FXObject pointer.
FXObject *FXPyGetFXObject(PyObject *pPyObject)
{
	FXObject *obj = 0;
 	SWIG_GetPtrObj(pPyObject, (void**) &obj, "_FXObject_p");
 	FXASSERT(obj != 0);
 	return obj;
}


/*
*  If the input object has a Python shadow class instance
*  counterpart, return a new reference to that instance.
*  Otherwise return NULL.
*/
PyObject *FXPyGetPyObject(const FXObject *pFXObject)
{
	PyObject *pPyObject = NULL;
	FXString key = FXStringFormat("%p", pFXObject);
	FXbool doSave = FXPyRestoreThread();
	pPyObject = (PyObject*) FXPyGetObjectDict().find(key.text());
	Py_XINCREF(pPyObject);
	FXPySaveThread(doSave);
	return pPyObject;
}


/**
 * Convert a C++ class name into its SWIG pointer type representation.
 * For example, a pointer to an object of type FXObject has the SWIG
 * type "_FXObject_p".
 */
FXString FXPyGetSWIGPtrName(const char *s)
{
	FXString classname(s);
	return FXStringFormat("_%s_p", classname.text());
}


/**
 * Given a C++ class name, return the associated Python shadow class name.
 * For the class name "FXWindow" this will return "FX_Window", while for
 * FXPy C++ class names, like "FXPyWindow", this function will return the
 * "FXWindow".
 */
FXString FXPyGetPythonClassName(const FXString& classname)
{
	FXString pythonClassName(classname);
	if (pythonClassName.left(4) == "FXPy")
		pythonClassName = FXString("FX") + pythonClassName.right(pythonClassName.length() - 4);
	else
		pythonClassName = FXString("FX_") + pythonClassName.right(pythonClassName.length() - 2);
	return pythonClassName;
}


/**
 * Return new reference to a Python shadow class instance for
 * this FOX object. If we recognize the input FOX object as one
 * that's already paired with a Python shadow class instance, we
 * return a new reference to that already-existing shadow class
 * instance. Otherwise, we need to construct a new instance of
 * that shadow class on-the-fly.
 *
 * Note that this is highly dependent on SWIG1.1's shadow class
 * implementation. If the passed-in pointer is NULL, or if some
 * error occurs, the error flag is set and the function returns
 * NULL.
 */
PyObject *
FXPyMakeShadowObject(const FXObject* obj)
{
	if (!obj)
		return NULL;

	// First see if it's one we already know about
	PyObject *shadow = FXPyGetPyObject(obj);
	if (shadow)
		return shadow;
	
	/**
	 *  A Python shadow class instance doesn't exist yet for this
	 *  C++ class instance, so we're going to have to instantiate
	 *  one on the fly.
	 */

	// First, determine the SWIG-mangled name for this class
	FXchar *buff;
	FXString swigPtrName = FXPyGetSWIGPtrName(obj->getClassName());
	FXMALLOC(&buff, FXchar, swigPtrName.length()+1);
	strcpy(buff, swigPtrName.text());

	// Next, get the SWIG pointer representation (a string)
	char swigptr[128]; // FIXME
	SWIG_MakePtr(swigptr, (void*) obj, buff);
	FXFREE(&buff);
		
	// Get a pointer to the Python class object
	FXString pythonClassName = FXPyGetPythonClassName(obj->getClassName()) + "Ptr";
	FXMALLOC(&buff, FXchar, pythonClassName.length()+1);
	strcpy(buff, pythonClassName.text());
	FXbool doSave = FXPyRestoreThread();
	PyObject *classobj = PyDict_GetItemString(pPyDict, buff);
	FXFREE(&buff);
	if (!classobj) {
		FXPySaveThread(doSave);
		return NULL;
	}

	// Construct input argument for constructor
	PyObject *args = Py_BuildValue("(s)", swigptr);
	if (!args) {
		FXPySaveThread(doSave);
		return NULL;
	}

	shadow = PyInstance_New(classobj, args, NULL);
	Py_DECREF(args);
	FXPySaveThread(doSave);
	// FXPyRegister(shadow);
	return shadow;
}


// Return the class object for Python class FXEvent
static PyObject* FXPyGetEventClassObject(){
  static PyObject* EventClassObject=0;
  if(EventClassObject==0){
    FXbool doSave=FXPyRestoreThread();
    EventClassObject=PyDict_GetItemString(pPyDict,"FXEventPtr");
    FXPySaveThread(doSave);
    }
  return EventClassObject;
  }

//----------------------------------------------------------------------

static PyObject* to_python(FXint s){
  FXbool doSave=FXPyRestoreThread();
  PyObject* result=Py_BuildValue("i",s);
  FXPySaveThread(doSave);
  return result;
  }

static PyObject* to_python(FXuint s){
  FXbool doSave=FXPyRestoreThread();
  PyObject* result=Py_BuildValue("i",s);
  FXPySaveThread(doSave);
  return result;
  }

static PyObject* to_python(FXuchar c){
  FXbool doSave=FXPyRestoreThread();
  PyObject *result=Py_BuildValue("i",c);
  FXPySaveThread(doSave);
  return result;
  }

static PyObject* to_python(const FXchar *s){
  FXbool doSave=FXPyRestoreThread();
  PyObject* result=Py_BuildValue("s", s);
  FXPySaveThread(doSave);
  return result;
  }

static PyObject* to_python(const FXString& s){
  FXbool doSave=FXPyRestoreThread();
  PyObject* result=Py_BuildValue("s",s.text());
  FXPySaveThread(doSave);
  return result;
  }

static PyObject* to_python(FXObject* ptr){
  FXbool doSave=FXPyRestoreThread();
  PyObject* result;
  if(ptr){
    if(ptr==(FXObject*)-1){
      result=PyLong_FromLong(-1);
      }
    else{
      result=FXPyMakeShadowObject(ptr);
      }
    }
  else{
    result=Py_None;
    Py_INCREF(Py_None);
    }
  FXPySaveThread(doSave);
  return result;
  }


static PyObject* to_python(FXEvent *ptr){
  // Data is pointer to the FXEvent record
  char swigptr[128];
  SWIG_MakePtr(swigptr,ptr,"_FXEvent_p");
  PyObject* eventClass=FXPyGetEventClassObject();
  FXbool doSave=FXPyRestoreThread();
  PyObject* args=Py_BuildValue("(s)", swigptr);
  PyObject* data=PyInstance_New(eventClass, args, NULL);
  Py_DECREF(args);
  FXPySaveThread(doSave);
  return data;
  }

static PyObject* to_python(FXTablePos* ptr){
  FXbool doSave=FXPyRestoreThread();
  Py_INCREF(Py_None);
  FXPySaveThread(doSave);
  return Py_None;
  }

static PyObject* to_python(FXTableRange* ptr){
  FXbool doSave=FXPyRestoreThread();
  Py_INCREF(Py_None);
  FXPySaveThread(doSave);
  return Py_None;
  }


// FIXME
static PyObject* to_python(FXTreeItem** ptr){
  FXbool doSave=FXPyRestoreThread();
  Py_INCREF(Py_None);
  FXPySaveThread(doSave);
  return Py_None;
  }


static PyObject* to_python(PyObject* obj){
  FXbool doSave=FXPyRestoreThread();
  Py_INCREF(obj);
  FXPySaveThread(doSave);
  return obj;
  }


// FIXME
static PyObject* to_python(FXStream& strm){
  return NULL;
  }


// FIXME
static PyObject* to_python(FXuint* array){
  FXbool doSave=FXPyRestoreThread();
  Py_INCREF(Py_None);
  FXPySaveThread(doSave);
  return Py_None;
  }

//----------------------------------------------------------------------

// Returns message data appropriate for a given sender/type combination
static PyObject *
FXPyGetMessageData(FXObject *sender, FXSelector sel, void *ptr)
{
	FXASSERT(sender != 0);
	FXushort type = SELTYPE(sel);
	if (type == SEL_PAINT ||
	    type == SEL_LEFTBUTTONPRESS ||
	    type == SEL_LEFTBUTTONRELEASE ||
	    type == SEL_MIDDLEBUTTONPRESS ||
	    type == SEL_MIDDLEBUTTONRELEASE ||
	    type == SEL_RIGHTBUTTONPRESS ||
	    type == SEL_RIGHTBUTTONRELEASE ||
	    type == SEL_KEYPRESS ||
	    type == SEL_KEYRELEASE ||
	    type == SEL_MOTION ||
	    type == SEL_BEGINDRAG ||
	    type == SEL_ENDDRAG ||
	    type == SEL_DRAGGED ||
	    type == SEL_ENTER ||
	    type == SEL_LEAVE ||
	    type == SEL_MAP ||
	    type == SEL_UNMAP ||
	    type == SEL_CONFIGURE ||
	    type == SEL_FOCUSIN ||
	    type == SEL_FOCUSOUT ||
	    type == SEL_DND_ENTER ||
	    type == SEL_DND_LEAVE ||
	    type == SEL_DND_MOTION ||
	    type == SEL_DND_DROP ||
	    type == SEL_DND_REQUEST ||
	    type == SEL_SELECTION_LOST ||
	    type == SEL_SELECTION_GAINED ||
	    type == SEL_SELECTION_REQUEST ||
	    type == SEL_CLIPBOARD_LOST ||
	    type == SEL_CLIPBOARD_GAINED ||
	    type == SEL_CLIPBOARD_REQUEST ||
	    type == SEL_UNGRABBED) {
		return to_python((FXEvent*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXArrowButton))) {
		if (type == SEL_CLICKED || type == SEL_COMMAND)
			return to_python((FXuint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXButton))) {
		if (type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_COMMAND)
			return to_python((FXuint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXCheckButton))) {
		if (type == SEL_COMMAND)
			return to_python((FXuchar)((long) ptr));
	}
	else if (sender->isMemberOf(FXMETACLASS(FXColorSelector))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((FXColor) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXColorWell))) {
		if (type == SEL_CHANGED ||
		    type == SEL_COMMAND ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED)
			return to_python((FXColor) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXComboBox))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((const FXchar*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXDial))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXDirBox))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((const FXchar*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXFileList))) {
		if (type == SEL_CHANGED ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXGLViewer))) {
		if (type == SEL_CHANGED ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED)
			return to_python((FXGLObject*) ptr);
		else if (type == SEL_COMMAND) {
			if (SELID(sel) == FXWindow::ID_QUERY_MENU)
				return to_python((FXEvent*) ptr);
			else
				return to_python((FXGLObject*) ptr);
		}
	}
	else if (sender->isMemberOf(FXMETACLASS(FXHeader))) {
		if (type == SEL_COMMAND || type == SEL_CHANGED)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXIconList))) {
		if (type == SEL_CHANGED ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXList))) {
		if (type == SEL_CHANGED ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXMDIChild))) {
		if (type == SEL_SELECTED ||
		    type == SEL_DESELECTED)
			return to_python((FXMDIChild*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXMDIClient))) {
		if (type == SEL_CHANGED)
			return to_python((FXMDIChild*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXRadioButton))) {
		if (type == SEL_COMMAND)
			return to_python((FXuchar)((long) ptr));
	}
	else if (sender->isMemberOf(FXMETACLASS(FXRecentFiles))) {
		if (type == SEL_COMMAND)
			return to_python((const FXchar*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXScrollbar))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXShutter))) {
		if (type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXSlider))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTabBar))) {
		if (type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTabBook))) {
		if (type == SEL_COMMAND)
			return to_python((FXint) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTable))) {
		if (type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_CHANGED ||
		    type == SEL_COMMAND)
			return to_python((FXTablePos*) ptr);
		else if (type == SEL_SELECTED ||
			 type == SEL_DESELECTED ||
			 type == SEL_INSERTED ||
			 type == SEL_DELETED)
			return to_python((FXTableRange*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXText))) {
		if (type == SEL_CHANGED)
			return to_python((FXint) ptr);
		else if (type == SEL_SELECTED ||
				type == SEL_DESELECTED ||
				type == SEL_INSERTED ||
				type == SEL_DELETED) {
			FXint *what = (FXint *) ptr;
			FXbool doSave = FXPyRestoreThread();
			PyObject *tuple = PyTuple_New(2);
			PyTuple_SetItem(tuple, 0, PyInt_FromLong(what[0]));
			PyTuple_SetItem(tuple, 1, PyInt_FromLong(what[1]));
			FXPySaveThread(doSave);
			return tuple;
		}
		else if (type == SEL_REPLACED) {
			FXint *what = (FXint *) ptr;
			FXbool doSave = FXPyRestoreThread();
			PyObject *tuple = PyTuple_New(3);
			PyTuple_SetItem(tuple, 0, PyInt_FromLong(what[0]));
			PyTuple_SetItem(tuple, 1, PyInt_FromLong(what[1]));
			PyTuple_SetItem(tuple, 2, PyInt_FromLong(what[2]));
			FXPySaveThread(doSave);
			return tuple;
		}
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTextField))) {
		if (type == SEL_CHANGED ||
		    type == SEL_COMMAND ||
		    type == SEL_VERIFY)
			return to_python((const FXchar*) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXToggleButton))) {
		if (type == SEL_COMMAND)
			return to_python((FXuchar)((long) ptr));
	}
	else if (sender->isMemberOf(FXMETACLASS(FXToolbarTab))) {
		if (type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_COMMAND)
			return to_python((FXbool)((long) ptr));
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTreeList))) {
		if (type == SEL_COLLAPSED ||
		    type == SEL_EXPANDED ||
		    type == SEL_COMMAND ||
		    type == SEL_CHANGED ||
		    type == SEL_CLICKED ||
		    type == SEL_DOUBLECLICKED ||
		    type == SEL_TRIPLECLICKED ||
		    type == SEL_OPENED ||
		    type == SEL_CLOSED)
			return to_python((FXTreeItem*) ptr);
		else if (type == SEL_SELECTED || type == SEL_DESELECTED)
			return to_python((FXTreeItem**) ptr);
	}
	else if (sender->isMemberOf(FXMETACLASS(FXTreeListBox))) {
		if (type == SEL_CHANGED || type == SEL_COMMAND)
			return to_python((FXTreeItem*) ptr);
	}

	// No match yet so return it as a string
	if (ptr == 0) {
		FXbool doSave = FXPyRestoreThread();
		Py_INCREF(Py_None);
		FXPySaveThread(doSave);
		return Py_None;
	}
	else {
		char s[256];
		sprintf(s, "%p", ptr);
		FXbool doSave = FXPyRestoreThread();
		PyObject *result = PyString_FromString(s);
		FXPySaveThread(doSave);
		return result;
	}
}


// Check for handle
FXbool FXPyCanHandle(FXObject* self, FXSelector sel)
{
	/*
	fprintf(stderr, "FXPyCanHandle() for %s (%p) and message (%d, %d)\n",
		self->getClassName(), self, SELID(sel), SELTYPE(sel));
	*/
	FXbool result = FALSE;
	PyObject* pPyObject = FXPyGetPyObject(self);
	if (pPyObject) {
		FXbool doSave = FXPyRestoreThread();
		if (PyObject_HasAttrString(pPyObject, "_search")) {
			PyObject *pMethObj = PyObject_CallMethod(pPyObject, "_search",
				"(i)", sel);
			Py_DECREF(pPyObject);
			if (pMethObj) {
				if (pMethObj == Py_None) {
					Py_DECREF(pMethObj);
					result = FALSE;
				}
				else {
					Py_DECREF(pMethObj);
					result = TRUE;
				}
			}
		}
		else {
			Py_DECREF(pPyObject);
			raiseException("object didn't define an _search() method");
		}
		FXPySaveThread(doSave);
	}
	return result;
}


// Handle message
long FXPyHandle(FXObject* self, FXObject* sender, FXSelector sel, void* ptr)
{
	// Get Python object for this C++ object
	PyObject *pPyObject = FXPyGetPyObject(self);
	if (pPyObject) {
		// Switch contexts
		FXbool doSave = FXPyRestoreThread();

		// Call _search() to get the method associated with this selector
		PyObject *pMethObj = PyObject_CallMethod(pPyObject,
			"_search", "(i)", sel);
		if (!pMethObj) {
			Py_DECREF(pPyObject);
			raiseException();
			FXPySaveThread(doSave);
			return 0;
		}
		
		// If _search() returns None then we don't want to handle this one
		if (pMethObj == Py_None) {
			Py_DECREF(Py_None);
			Py_DECREF(pPyObject);
			FXPySaveThread(doSave);
			return 0;
		}
		
		// Make sure it's really a callable object
		if (!PyCallable_Check(pMethObj)) {
			PyErr_SetString(PyExc_TypeError,
				"not a callable object");
			Py_DECREF(pMethObj);
			Py_DECREF(pPyObject);
			raiseException();
			FXPySaveThread(doSave);
			return 0;
		}

		// The sender may or may not have a Python counterpart, depending
		// on whether it was created in Python code or its some kind of
		// object created by FOX itself.
		PyObject *pSender = FXPyGetPyObject(sender);
		if (!pSender)
			pSender = FXPyMakeShadowObject(sender);

		if (pSender) {
			// Convert message data to something usable in Python
			PyObject *data = FXPyGetMessageData(sender, sel, ptr);

			// Call the message handler function (an unbound method)
			PyObject *pResObj = PyObject_CallFunction(pMethObj,
				"OOiO", pPyObject, pSender, sel, data);

			Py_DECREF(data);
			Py_DECREF(pMethObj);
			Py_DECREF(pPyObject);

			// Message handler must return an integer value (or None)
			if (pResObj) {
				if (pResObj == Py_None) {
					Py_DECREF(Py_None);
					FXPySaveThread(doSave);
					return 1;
				}
				else if (PyInt_Check(pResObj)) {
					long nRes = PyInt_AsLong(pResObj);
					Py_DECREF(pResObj);
					FXPySaveThread(doSave);
					return nRes;
				}
				else {
					Py_DECREF(pResObj);
					raiseException("message handler function must return an integer");
					FXPySaveThread(doSave);
					return 1;
				}
			}
			else {
				raiseException();
				FXPySaveThread(doSave);
				return 1;
			}
		}
		else {
			Py_DECREF(pPyObject);
			Py_DECREF(pMethObj);
			raiseException();
			FXPySaveThread(doSave);
			return 0;
		}
	}
	return 1;
}


//----------------------------------------------------------------------

// Call a method named "func" of the shadow class "obj".
// The method is assumed to return None.
void FXPyCallVoidFunction(FXObject* obj,char* func){
  // Lookup shadow object pointer
  PyObject *pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    // Call the function
    FXbool doSave=FXPyRestoreThread();
    PyObject *result=PyObject_CallMethod(pPyObject,func,NULL);
    Py_DECREF(pPyObject);
		
    // Function is expected to return None
    if(result){
      if(result==Py_None){
        Py_DECREF(Py_None);
        FXPySaveThread(doSave);
        return;
        }
      else{
        Py_DECREF(result);
        PyErr_SetString(PyExc_TypeError,"Expected function to return None");
        raiseException();
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  }


// Call a method named "func" of the shadow class "obj", passing
// it the shadow class instance for "arg1" as its single argument.
// The method is assumed to return None.
template<class TYPE>
void FXPyCallVoidFunction(const FXObject *obj,char *func,TYPE arg1){
  // Lookup shadow object pointer
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    // Call the function
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject *result=PyObject_CallMethod(pPyObject,func,"(O)",obj1);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
		
    // Function is expected to return None
    if(result){
      if(result==Py_None){
        Py_DECREF(Py_None);
        FXPySaveThread(doSave);
        return;
        }
      else{
        Py_DECREF(result);
        PyErr_SetString(PyExc_TypeError,"Expected function to return None");
        raiseException();
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  }


template<class TYPE1,class TYPE2>
void FXPyCallVoidFunction(FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2){
  // Lookup shadow object pointer
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    // Call the function
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OO)",obj1,obj2);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
		
    // Function is expected to return None
    if(result){
      if(result==Py_None){
        Py_DECREF(Py_None);
        FXPySaveThread(doSave);
        return;
        }
      else{
        Py_DECREF(result);
        PyErr_SetString(PyExc_TypeError,"Expected function to return None");
        raiseException();
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  }


template<class TYPE1,class TYPE2,class TYPE3,class TYPE4>
void FXPyCallVoidFunction(FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2,TYPE3 arg3,TYPE4 arg4){
  // Lookup shadow object pointer
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    // Call the function
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* obj3=to_python(arg3);
    PyObject* obj4=to_python(arg4);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OOOO)",obj1,obj2,obj3,obj4);
    Py_DECREF(obj4);
    Py_DECREF(obj3);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);

    // Function is expected to return None
    if(result){
      if(result==Py_None){
        Py_DECREF(Py_None);
        FXPySaveThread(doSave);
        return;
        }
      else{
        Py_DECREF(result);
        PyErr_SetString(PyExc_TypeError,"Expected function to return None");
        raiseException();
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  }


template<class TYPE1,class TYPE2,class TYPE3,class TYPE4,class TYPE5>
void FXPyCallVoidFunction(FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2,TYPE3 arg3,TYPE4 arg4,TYPE5 arg5){
  // Lookup shadow object pointer
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    // Call the function
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* obj3=to_python(arg3);
    PyObject* obj4=to_python(arg4);
    PyObject* obj5=to_python(arg5);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OOOOO)",obj1,obj2,obj3,obj4,obj5);
    Py_DECREF(obj5);
    Py_DECREF(obj4);
    Py_DECREF(obj3);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);

    // Function is expected to return None
    if(result){
      if(result==Py_None){
        Py_DECREF(Py_None);
        FXPySaveThread(doSave);
        return;
        }
      else{
        Py_DECREF(result);
        PyErr_SetString(PyExc_TypeError,"Expected function to return None");
        raiseException();
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  }


//----------------------------------------------------------------------


// Call a method named "func" of the shadow class "obj".
// The method is assumed to return a boolean value.
FXbool FXPyCallBoolFunction(const FXObject* obj,char* func){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* result=PyObject_CallMethod(pPyObject,func,NULL);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXbool bRes=(FXbool) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return bRes;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return 0 or 1");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return FALSE;
  }


template<class TYPE>
FXbool FXPyCallBoolFunction(const FXObject* obj,char* func,TYPE arg1){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(O)",obj1);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXbool bRes=(FXbool) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return bRes;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return 0 or 1");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return FALSE;
  }


template<class TYPE1,class TYPE2>
FXbool FXPyCallBoolFunction(const FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2){
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OO)",obj1,obj2);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXbool bRes=(FXbool) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return bRes;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return 0 or 1");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return FALSE;
  }


template<class TYPE1,class TYPE2,class TYPE3>
FXbool FXPyCallBoolFunction(const FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2,TYPE3 arg3){
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* obj3=to_python(arg3);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OOO)",obj1,obj2,obj3);
    Py_DECREF(obj3);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXbool bRes=(FXbool) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return bRes;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return 0 or 1");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return FALSE;
  }


template<class TYPE1,class TYPE2,class TYPE3,class TYPE4,class TYPE5>
FXbool FXPyCallBoolFunction(const FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2,TYPE3 arg3,TYPE4 arg4,TYPE5 arg5){
  PyObject* pPyObject=FXPyGetPyObject(obj);

  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* obj3=to_python(arg3);
    PyObject* obj4=to_python(arg4);
    PyObject* obj5=to_python(arg5);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OOOOO)",obj1,obj2,obj3,obj4,obj5);
    Py_DECREF(obj5);
    Py_DECREF(obj4);
    Py_DECREF(obj3);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXbool bRes=(FXbool) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return bRes;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return 0 or 1");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return FALSE;
  }

//----------------------------------------------------------------------

// Call a method named "func" of the shadow class "obj".
// The method is assumed to return an FXint value.
FXint FXPyCallIntFunction(FXObject* obj,char* func){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* result=PyObject_CallMethod(pPyObject,func,NULL);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXint nResult=(FXint) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return nResult;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return an integer");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return -1;
  }


template<class TYPE>
FXint FXPyCallIntFunction(FXObject* obj,char* func,TYPE arg1){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(O)",obj1);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      if(PyInt_Check(result)){
        FXint nResult=(FXint) PyInt_AsLong(result);
        Py_DECREF(result);
        FXPySaveThread(doSave);
        return nResult;
        }
      else{
        Py_DECREF(result);
        raiseException("Expected function to return an integer");
        }
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return -1;
  }

//----------------------------------------------------------------------

FXGLObject* FXPyCallGLObjectFunction(FXObject* obj,char* func){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* result=PyObject_CallMethod(pPyObject,func,NULL);
    Py_DECREF(pPyObject);
    if(result){
      FXGLObject* glObjResult=(FXGLObject*)FXPyGetFXObject(result);
      Py_DECREF(result);
      FXPySaveThread(doSave);
      return glObjResult;
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return NULL;
  }


template<class TYPE>
FXGLObject* FXPyCallGLObjectFunction(FXObject* obj,char* func,TYPE arg1){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(O)",obj1);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      FXGLObject* glObjResult=(FXGLObject*)FXPyGetFXObject(result);
      Py_DECREF(result);
      FXPySaveThread(doSave);
      return glObjResult;
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return NULL;
  }


template<class TYPE1,class TYPE2>
FXGLObject* FXPyCallGLObjectFunction(FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OO)",obj1,obj2);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      FXGLObject* glObjResult=(FXGLObject*)FXPyGetFXObject(result);
      Py_DECREF(result);
      FXPySaveThread(doSave);
      return glObjResult;
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return NULL;
  }

//----------------------------------------------------------------------

// FIXME
template<class TYPE1,class TYPE2,class TYPE3,class TYPE4>
FXGLObject** FXPyCallGLObjectListFunction(FXObject* obj,char* func,TYPE1 arg1,TYPE2 arg2,TYPE3 arg3,TYPE4 arg4){
  PyObject* pPyObject=FXPyGetPyObject(obj);
  if(pPyObject){
    FXbool doSave=FXPyRestoreThread();
    PyObject* obj1=to_python(arg1);
    PyObject* obj2=to_python(arg2);
    PyObject* obj3=to_python(arg3);
    PyObject* obj4=to_python(arg4);
    PyObject* result=PyObject_CallMethod(pPyObject,func,"(OOOO)",obj1,obj2,obj3,obj4);
    Py_DECREF(obj4);
    Py_DECREF(obj3);
    Py_DECREF(obj2);
    Py_DECREF(obj1);
    Py_DECREF(pPyObject);
    if(result){
      FXGLObject** glObjResult=NULL;
      Py_DECREF(result);
      FXPySaveThread(doSave);
      return glObjResult;
      }
    else{
      raiseException();
      }
    FXPySaveThread(doSave);
    }
  return NULL;
  }

//----------------------------------------------------------------------

// long FXObject::onDefault(FXObject* sender,FXSelector sel,void* ptr)
static long
_onDefault(FXObject* fxObj,FXObject* sender,FXSelector sel,void* ptr) {
	PyObject *pyObj = FXPyGetPyObject(fxObj);
	if (pyObj != NULL) {
		PyObject *arg0 = FXPyMakeShadowObject(sender);
		if (arg0 == NULL) {
			FXbool doSave = FXPyRestoreThread();
			Py_DECREF(pyObj);
			FXPySaveThread(doSave);
			raiseException();
			return 0;
		}
		FXbool doSave = FXPyRestoreThread();
		PyObject *result = PyObject_CallMethod(pyObj, "onDefault", "(Oii)", arg0, sel, 0);
		Py_DECREF(arg0);
		Py_DECREF(pyObj);
		if (result != NULL) {
			if (PyInt_Check(result)) {
				long longResult = PyInt_AsLong(result);
				Py_DECREF(result);
				FXPySaveThread(doSave);
				return longResult;
			}
			else {
				Py_DECREF(result);
				raiseException("onDefault() should return an integer");
			}
			Py_DECREF(result);
		}
		else {
			raiseException();
		}
		FXPySaveThread(doSave);
	}
	return 0;
}


template <class ItemType, class ListType>
FXint _getWidth(const ItemType *self, const ListType *list)
{
	PyObject *obj = FXPyGetPyObject(self);
	if (obj) {
		PyObject *arg1 = FXPyMakeShadowObject(list);
		if (!arg1) {
			FXbool doSave = FXPyRestoreThread();
			Py_DECREF(obj);
			FXPySaveThread(doSave);
			raiseException();
			return -1;
		}
		FXbool doSave = FXPyRestoreThread();
		PyObject *result = PyObject_CallMethod(obj, "getWidth", "(O)", arg1);
		Py_DECREF(arg1);
		Py_DECREF(obj);
		if (result) {
			if (PyInt_Check(result)) {
				FXint w = PyInt_AsLong(result);
				Py_DECREF(result);
				FXPySaveThread(doSave);
				return w;
			}
			else {
				Py_DECREF(result);
				raiseException("getWidth() should return an integer");
				FXPySaveThread(doSave);
				return -1;
			}
		}
		else {
			raiseException();
			FXPySaveThread(doSave);
		}
	}
	return -1;
}

template <class ItemType, class ListType>
FXint _getHeight(const ItemType *self, const ListType *list)
{
	PyObject *obj = FXPyGetPyObject(self);
	if (obj) {
		PyObject *arg1 = FXPyMakeShadowObject(list);
		if (!arg1) {
			FXbool doSave = FXPyRestoreThread();
			Py_DECREF(obj);
			FXPySaveThread(doSave);
			raiseException();
			return -1;
		}
		FXbool doSave = FXPyRestoreThread();
		PyObject *result = PyObject_CallMethod(obj,
			"getHeight", "(O)", arg1);
		Py_DECREF(arg1);
		Py_DECREF(obj);
		if (result) {
			if (PyInt_Check(result)) {
				FXint h = PyInt_AsLong(result);
				Py_DECREF(result);
				FXPySaveThread(doSave);
				return h;
			}
			else {
				Py_DECREF(result);
				raiseException("getHeight() should return an integer");
				FXPySaveThread(doSave);
				return -1;
			}
		}
		else {
			raiseException();
			FXPySaveThread(doSave);
		}
	}
	return -1;
}


#include "virtuals.cpp"
