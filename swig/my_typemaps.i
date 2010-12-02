/** Tell SWIG to bracket all wrapped functions with Python's thread macros. */
%except(python) {
    FXPy_BEGIN_ALLOW_THREADS
    $function
    FXPy_END_ALLOW_THREADS
}

/*
 * Convert Python strings to input arguments of type FXString.
 * Also accepts "None" as an empty string.
 */
%typemap(python, in) const FXString& {
    if ($source == Py_None)
	$target = new FXString;
    else if (!PyString_Check($source)) {
	PyErr_SetString(PyExc_TypeError, "not a string");
	return NULL;
    }
    else
	$target = new FXString(PyString_AsString($source));
}

/* Clean up */
%typemap(python, freearg) const FXString& {
    delete $source;
}

/* Convert FXString return value to Python string */
%typemap(python, out) FXString {
    $target = PyString_FromString($source->text());
}

/* Clean up */
%typemap(python, ret) FXString {
    delete $source;
}

/* Convert const FXString& return value to Python string */
%typemap(python, out) const FXString& {
    $target = PyString_FromString($source->text());
}

/* Convert a NULL object into a void* */
%typemap(python,in) void* ptr {
    $target = NULL;
    if (PyObject_HasAttrString($source, "this")) {
	PyObject *obj = PyObject_GetAttrString($source, "this");
	char *str = PyString_AsString(obj);
	if (str) {
	    if (!strcmp(str, "NULL"))
		$target = NULL;
	}
	else
	    $target = (void*) $source;
	Py_DECREF(obj);
    }
    else
	$target = (void*) $source;
}

/* Convert Python string into an array of bytes */
%typemap(python, in) void* pix {
  if($source==Py_None){
    $target=NULL;
    }
  else if (PyString_Check($source)){
    int size = PyString_Size($source);
    if(!FXMALLOC(&$target,FXuchar,size)){
      PyErr_SetString(PyExc_MemoryError,"out of memory");
      return NULL;
      }
    FXuchar *bytes=(FXuchar*)$target;
    char *str=PyString_AsString($source);
    for (int i=0; i<size; i++)
      bytes[i]=(FXuchar)str[i];
    }
  else{
    PyErr_SetString(PyExc_TypeError,"expected a string");
    return NULL;
    }
  }

/* Clean up same */
%typemap(python, freearg) void* pix {
  if($source)
    FXFREE(&$source);
  }

/*
 * Convert a list of strings into a const FXchar** array.
 * Used by FXFileSelector::setPatternList() and FXFileDialog::setPatternList().
 */
%typemap(python,in) const FXchar** ptrns {
  if (PyList_Check($source)) {
    int size = PyList_Size($source);
    FXMALLOC(&$target,const FXchar*,size+1);
    for (int i=0; i<size; i++) {
      PyObject *o = PyList_GetItem($source,i);
      if (PyString_Check(o))
	$target[i] = PyString_AsString(PyList_GetItem($source,i));
      else {
	PyErr_SetString(PyExc_TypeError,"list must contain strings");
	FXFREE(&$target);
	return NULL;
	}
      }
    $target[size] = 0;
    }
  else{
    PyErr_SetString(PyExc_TypeError,"not a list");
    return NULL;
    }
}

/* Clean up same */
%typemap(python,freearg) const FXchar** ptrns {
    FXFREE(&$source);
}

/* For functions that return FXObject pointers */
%typemap(python,out) FXObject* OBJECTOUT {
    if ($source) {
	$target = FXPyMakeShadowObject($source);
    } else {
	Py_INCREF(Py_None);
	$target = Py_None;
    }
}

/* Apply this typemap to other types */
%apply FXObject* OBJECTOUT { FXApp* };
%apply FXObject* OBJECTOUT { FXBitmap* };
%apply FXObject* OBJECTOUT { FXButton* };
%apply FXObject* OBJECTOUT { FXComposite* };
%apply FXObject* OBJECTOUT { FXCursor* };
%apply FXObject* OBJECTOUT { FXDragCorner* };
%apply FXObject* OBJECTOUT { FXFont* };
%apply FXObject* OBJECTOUT { FXGLObject* };
%apply FXObject* OBJECTOUT { FXHeader* };
%apply FXObject* OBJECTOUT { FXHeaderItem* };
%apply FXObject* OBJECTOUT { FXIcon* };
%apply FXObject* OBJECTOUT { FXIconItem* };
%apply FXObject* OBJECTOUT { FXImage* };
%apply FXObject* OBJECTOUT { FXMDIChild* };
%apply FXObject* OBJECTOUT { FXOption* };
%apply FXObject* OBJECTOUT { FXPopup* };
%apply FXObject* OBJECTOUT { FXRootWindow* };
%apply FXObject* OBJECTOUT { FXScrollbar* };
%apply FXObject* OBJECTOUT { FXStatusline* };
%apply FXObject* OBJECTOUT { FXTreeItem* };
%apply FXObject* OBJECTOUT { FXVerticalFrame* };
%apply FXObject* OBJECTOUT { FXWindow* };

// For functions which expect FXWindow pointers, accept None
%typemap(python,in) FXWindow* {
    if ($source == Py_None)
	$target = NULL;
    else
	SWIG_GetPtrObj($source, (void**) &$target, "$mangle");
}

// For functions which expect FXIcon pointers, accept None
%typemap(python,in) FXIcon* {
    if ($source == Py_None)
	$target = NULL;
    else
	SWIG_GetPtrObj($source, (void**) &$target, "$mangle");
}

// For functions which expect FXObject pointers, accept None
%typemap(python,in) FXObject* {
    if ($source == Py_None)
	$target = NULL;
    else
	SWIG_GetPtrObj($source, (void**) &$target, "$mangle");
}

// For functions which expect FXTreeItem pointers, accept None
%typemap(python,in) PyObject *treeItem {
    $target = $source;
}

/**
 * Convert a Python File object or integer file descriptor into an
 * platform-specific FXInputHandle for Win32 or Unix.
 */
%typemap(python, in) FXInputHandle {
#ifdef WIN32
    if ($source) {
        if (PyFile_Check($source)) {
            FILE *fp = PyFile_AsFile($source);
            if (fp) {
                int fd = fileno(fp);
                $target = (FXInputHandle) _get_osfhandle(fd);
            }
        } else if (PyInt_Check($source)) {
             int fd = PyInt_AsLong($source);
             $target = (FXInputHandle) _get_osfhandle(fd);
        }
    }
#else
    if ($source) {
        if (PyFile_Check($source)) {
            FILE *fp = PyFile_AsFile($source);
            if (fp != NULL)
                $target = (FXInputHandle) fileno(fp);
        } else if (PyInt_Check($source)) {
             $target = (FXInputHandle) PyInt_AsLong($source);
        }
    }
#endif
}

