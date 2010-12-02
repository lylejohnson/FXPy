import os, re, string, tempfile
# renaming does not work over device boundaries
tempfile.tempdir = os.getcwd()

def findClassDefinition(lines, classname):
    expr1 = re.compile('^class ' + classname + '\(')
    expr2 = re.compile('^class ' + classname + ' :')
    for lineIndex in range(len(lines)):
        if expr1.match(lines[lineIndex]) or expr2.match(lines[lineIndex]):
            return lineIndex
    return -1

def findFuncBounds(lines, classname, funcname):
    startIndex, stopIndex = -1, -1
    classStartIndex = findClassDefinition(lines, classname)
    if classStartIndex == -1:
        return startIndex, stopIndex
    expr1 = re.compile('^ *def ' + funcname + '\(')
    expr2 = re.compile('^ *def ')	# new function definition
    expr3 = re.compile('^ *$')		# blank line
    for lineIndex in range(classStartIndex+1, len(lines)):
        line = lines[lineIndex]
        if startIndex < 0:
            if expr1.match(line):
                startIndex = lineIndex
        else:
            if expr2.match(line) or expr3.match(line):
                stopIndex = lineIndex 
                break
    return startIndex, stopIndex

def substituteFuncText(lines, classname, funcname, text):
    textlines = string.split(text, '\r')
    startIndex, stopIndex = findFuncBounds(lines, classname, funcname)
    return lines[:startIndex] + textlines + lines[stopIndex:]

def substituteConstructor(filename, classname, text):
    substituteFunc(filename, classname, '__init__', text)

def substituteFunc(filename, classname, funcname, text):
    lines = substituteFuncText(open(filename, 'r').readlines(),
                               classname, funcname, text)
    tmpfile = tempfile.mktemp()
    open(tmpfile, 'w').writelines(lines)
    bakfilename = filename + '.bak'
    if os.path.exists(bakfilename):
        os.remove(bakfilename)
    os.rename(filename, bakfilename)
    os.rename(tmpfile, filename)

FXSplitter__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.CreateSplitter1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.CreateSplitter2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FX4Splitter__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.Create4Splitter1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.Create4Splitter2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXMenubar__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(menusc.CreateFloatingMenubar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(menusc.CreateNonFloatingMenubar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXFont__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(miscc.CreateFont1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(miscc.CreateFont2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass

        try:
            self.this = apply(miscc.CreateFont3,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXRecentFiles__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(miscc.CreateRecentFiles1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(miscc.CreateRecentFiles2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXToolbar__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(controlsc.CreateFloatingToolbar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(controlsc.CreateNonFloatingToolbar,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXDCWindow__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(containersc.CreateDCWindow,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(containersc.CreateClippedDCWindow,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

text2 = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(dialogsc.CreateOwnedDialogBox,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(dialogsc.CreateFreeDialogBox,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

text3 = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(graphicsc.CreateStockCursor,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(graphicsc.CreateCursorFromMask,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXGLContext__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLContext1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLContext2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXGLCanvas__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLCanvas1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLCanvas2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

FXGLViewer__init__ = """    def __init__(self,*_args,**_kwargs):
        try:
            self.this = apply(fox3dc.CreateGLViewer1,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
            return
        except:
            pass

        try:
            self.this = apply(fox3dc.CreateGLViewer2,_args,_kwargs)
            self.thisown = 1
            FXPyRegister(self)
        except:
            pass
"""

text4 = """    def addItemFirst(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemFirst,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemFirst2,(self,) + _args, _kwargs)
            return val
"""

text5 = """    def addItemLast(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemLast,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemLast2,(self,) + _args, _kwargs)
            return val
"""

text6 = """    def addItemBefore(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemBefore,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemBefore2,(self,) + _args, _kwargs)
            return val
"""

text7 = """    def addItemAfter(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeList_addItemAfter,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeList_addItemAfter2,(self,) + _args, _kwargs)
            return val
"""

text8 = """    def addItemFirst(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemFirst,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemFirst2,(self,) + _args, _kwargs)
            return val
"""

text9 = """    def addItemLast(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemLast,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemLast2,(self,) + _args, _kwargs)
            return val
"""

text10 = """    def addItemBefore(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemBefore,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemBefore2,(self,) + _args, _kwargs)
            return val
"""

text11 = """    def addItemAfter(self, *_args, **_kwargs):
        try:
            val = apply(treelistc.FX_TreeListBox_addItemAfter,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(treelistc.FX_TreeListBox_addItemAfter2,(self,) + _args, _kwargs)
            return val
"""

FXList_appendItem = """    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_appendItemStr,(self,) + _args, _kwargs)
            return val
"""

FXList_prependItem = """    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_prependItemStr,(self,) + _args, _kwargs)
            return val
"""

FXList_insertItem = """    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_insertItemStr,(self,) + _args, _kwargs)
            return val
"""

FXList_replaceItem = """    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_List_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_List_replaceItemStr,(self,) + _args, _kwargs)
            return val
"""

FXIconList_appendItem = """    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_appendItemStr,(self,) + _args, _kwargs)
            return val
"""

FXIconList_prependItem = """    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_prependItemStr,(self,) + _args, _kwargs)
            return val
"""

FXIconList_insertItem = """    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_insertItemStr,(self,) + _args, _kwargs)
            return val
"""

FXIconList_replaceItem = """    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(iconlistc.FX_IconList_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(iconlistc.FX_IconList_replaceItemStr,(self,) + _args, _kwargs)
            return val
"""

FXHeader_appendItem = """    def appendItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_appendItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_appendItem2,(self,) + _args, _kwargs)
            return val
"""

FXHeader_prependItem = """    def prependItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_prependItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_prependItem2,(self,) + _args, _kwargs)
            return val
"""

FXHeader_insertItem = """    def insertItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_insertItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_insertItem2,(self,) + _args, _kwargs)
            return val
"""

FXHeader_replaceItem = """    def replaceItem(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FX_Header_replaceItem,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FX_Header_replaceItem2,(self,) + _args, _kwargs)
            return val
"""

FXApp_stopModal = """    def stopModal(self, *_args, **_kwargs):
        try:
            val = apply(miscc.FX_App_stopModal,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(miscc.FX_App_stopModal2,(self,) + _args, _kwargs)
            return val
"""

FXDC_setStipple = """    def setStipple(self, *_args, **_kwargs):
        try:
            val = apply(containersc.FX_DC_setStipple,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(containersc.FX_DC_setStipple2,(self,) + _args, _kwargs)
            return val
"""

FXFileList_showHiddenFiles = """    def showHiddenFiles(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FX_FileList_showHiddenFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FX_FileList_showHiddenFiles2,(self,) + _args, _kwargs)
            return val
"""

FXFileList_showOnlyDirectories = """    def showOnlyDirectories(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FX_FileList_showOnlyDirectories,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FX_FileList_showOnlyDirectories2,(self,) + _args, _kwargs)
            return val
"""

FXDirList_showHiddenFiles = """    def showHiddenFiles(self, *_args, **_kwargs):
        try:
            val = apply(dirlistc.FX_DirList_showHiddenFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dirlistc.FX_DirList_showHiddenFiles2,(self,) + _args, _kwargs)
            return val
"""

FXDirList_showFiles = """    def showFiles(self, *_args, **_kwargs):
        try:
            val = apply(dirlistc.FX_DirList_showFiles,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dirlistc.FX_DirList_showFiles2,(self,) + _args, _kwargs)
            return val
"""

FXWindow_update = """    def update(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_Window_update,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_Window_update2,(self,) + _args, _kwargs)
            return val
"""

FXWindow_repaint = """    def repaint(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_Window_repaint,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_Window_repaint2,(self,) + _args, _kwargs)
            return val
"""

FXTopWindow_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FX_TopWindow_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FX_TopWindow_show2,(self,) + _args, _kwargs)
            return val
"""

FXToolbarShell_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(controlsc.FXToolbarShell_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(controlsc.FXToolbarShell_show2,(self,) + _args, _kwargs)
            return val
"""

FXMainWindow_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(windowsc.FXMainWindow_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(windowsc.FXMainWindow_show2,(self,) + _args, _kwargs)
            return val
"""

FXDialogBox_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXDialogBox_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXDialogBox_show2,(self,) + _args, _kwargs)
            return val
"""

FXSearchDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXSearchDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXSearchDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXReplaceDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXReplaceDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXReplaceDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXPrintDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXPrintDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXPrintDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXMessageBox_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXMessageBox_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXMessageBox_show2,(self,) + _args, _kwargs)
            return val
"""

FXInputDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXInputDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXInputDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXFontDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXFontDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXFontDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXFileDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXFileDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXFileDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXDirDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXDirDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXDirDialog_show2,(self,) + _args, _kwargs)
            return val
"""

FXColorDialog_show = """    def show(self, *_args, **_kwargs):
        try:
            val = apply(dialogsc.FXColorDialog_show,(self,) + _args, _kwargs)
            return val
        except:
            val = apply(dialogsc.FXColorDialog_show2,(self,) + _args, _kwargs)
            return val
"""



if __name__ == '__main__':
    substituteConstructor('containers.py', 'FX4Splitter', FX4Splitter__init__)
    substituteConstructor('containers.py', 'FXSplitter', FXSplitter__init__)
    substituteConstructor('containers.py', 'FXDCWindow', FXDCWindow__init__)
    substituteConstructor('controls.py', 'FXToolbar', FXToolbar__init__)
    substituteConstructor('dialogs.py', 'FXDialogBox', text2)
    substituteConstructor('fox3d.py', 'FXGLContext', FXGLContext__init__)
    substituteConstructor('fox3d.py', 'FXGLCanvas', FXGLCanvas__init__)
    substituteConstructor('fox3d.py', 'FXGLViewer', FXGLViewer__init__)
    substituteConstructor('graphics.py', 'FXCursor', text3)
    substituteConstructor('menus.py', 'FXMenubar', FXMenubar__init__)
    substituteConstructor('misc.py', 'FXFont', FXFont__init__)
    substituteConstructor('misc.py', 'FXRecentFiles', FXRecentFiles__init__)

    substituteFunc('misc.py', 'FX_AppPtr', 'stopModal', FXApp_stopModal)

    substituteFunc('containers.py', 'FX_DCPtr', 'setStipple', FXDC_setStipple)

    substituteFunc('dialogs.py', 'FX_FileListPtr', 'showHiddenFiles',
        FXFileList_showHiddenFiles)
    substituteFunc('dialogs.py', 'FX_FileListPtr', 'showOnlyDirectories',
        FXFileList_showOnlyDirectories)

    substituteFunc('dirlist.py', 'FX_DirListPtr', 'showFiles',
        FXDirList_showFiles)
    substituteFunc('dirlist.py', 'FX_DirListPtr', 'showHiddenFiles',
        FXDirList_showHiddenFiles)

    substituteFunc('treelist.py', 'FX_TreeListPtr', 'addItemFirst', text4)
    substituteFunc('treelist.py', 'FX_TreeListPtr', 'addItemLast', text5)
    substituteFunc('treelist.py', 'FX_TreeListPtr', 'addItemBefore', text6)
    substituteFunc('treelist.py', 'FX_TreeListPtr', 'addItemAfter', text7)

    substituteFunc('treelist.py', 'FX_TreeListBoxPtr', 'addItemFirst', text8)
    substituteFunc('treelist.py', 'FX_TreeListBoxPtr', 'addItemLast', text9)
    substituteFunc('treelist.py', 'FX_TreeListBoxPtr', 'addItemBefore', text10)
    substituteFunc('treelist.py', 'FX_TreeListBoxPtr', 'addItemAfter', text11)

    substituteFunc('controls.py', 'FX_ListPtr', 'appendItem', FXList_appendItem)
    substituteFunc('controls.py', 'FX_ListPtr', 'prependItem', FXList_prependItem)
    substituteFunc('controls.py', 'FX_ListPtr', 'insertItem', FXList_insertItem)
    substituteFunc('controls.py', 'FX_ListPtr', 'replaceItem',
        FXList_replaceItem)

    substituteFunc('iconlist.py', 'FX_IconListPtr', 'appendItem',
        FXIconList_appendItem)
    substituteFunc('iconlist.py', 'FX_IconListPtr', 'prependItem',
        FXIconList_prependItem)
    substituteFunc('iconlist.py', 'FX_IconListPtr', 'insertItem',
        FXIconList_insertItem)
    substituteFunc('iconlist.py', 'FX_IconListPtr', 'replaceItem',
        FXIconList_replaceItem)

    substituteFunc('controls.py', 'FX_HeaderPtr', 'appendItem',
        FXHeader_appendItem)
    substituteFunc('controls.py', 'FX_HeaderPtr', 'prependItem',
        FXHeader_prependItem)
    substituteFunc('controls.py', 'FX_HeaderPtr', 'insertItem',
        FXHeader_insertItem)
    substituteFunc('controls.py', 'FX_HeaderPtr', 'replaceItem',
        FXHeader_replaceItem)

    substituteFunc('windows.py', 'FX_WindowPtr', 'update',
        FXWindow_update)
    substituteFunc('windows.py', 'FX_WindowPtr', 'repaint',
        FXWindow_repaint)

    substituteFunc('windows.py', 'FX_TopWindowPtr', 'show',
        FXTopWindow_show)
    substituteFunc('windows.py', 'FXTopWindowPtr', 'show',
        FXTopWindow_show)
    substituteFunc('windows.py', 'FXMainWindowPtr', 'show',
        FXMainWindow_show)
    substituteFunc('controls.py', 'FXToolbarShellPtr', 'show',
        FXToolbarShell_show)
    substituteFunc('dialogs.py', 'FXDialogBoxPtr', 'show',
        FXDialogBox_show)
    substituteFunc('dialogs.py', 'FXSearchDialogPtr', 'show',
        FXSearchDialog_show)
    substituteFunc('dialogs.py', 'FXReplaceDialogPtr', 'show',
        FXReplaceDialog_show)
    substituteFunc('dialogs.py', 'FXPrintDialogPtr', 'show',
        FXPrintDialog_show)
    substituteFunc('dialogs.py', 'FXMessageBoxPtr', 'show',
        FXMessageBox_show)
    substituteFunc('dialogs.py', 'FXInputDialogPtr', 'show',
        FXInputDialog_show)
    substituteFunc('dialogs.py', 'FXFontDialogPtr', 'show',
        FXFontDialog_show)
    substituteFunc('dialogs.py', 'FXFileDialogPtr', 'show',
        FXFileDialog_show)
    substituteFunc('dialogs.py', 'FXDirDialogPtr', 'show',
        FXDirDialog_show)
    substituteFunc('dialogs.py', 'FXColorDialogPtr', 'show',
        FXColorDialog_show)
