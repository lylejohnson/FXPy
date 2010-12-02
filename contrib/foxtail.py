#!/bin/env python
#
# A tail application along the lines of tailtk.py.
# Contributed by John Przybylski (johnp9@bellatlantic.net).
#

from threading import *
from FXPy.fox import *
from Queue import *
import sys,os,time,re

class MyThread(Thread):
    def __init__(self, queue, name='foo'):
        Thread.__init__(self)
        self.name = name
        self.queue = queue
        self.file = open(self.name, 'r')
        return

    def run(self):
        while 1:
            data = self.file.readline()
	    data = re.sub("\n", '', data) 
            self.queue.put(data)
            #time.sleep(.1)
        return

class ListWindow(FXMainWindow):

    ID_TIMEOUT, ID_CHORE = \
      	range(FXMainWindow.ID_LAST, FXMainWindow.ID_LAST+2)

    def __init__(self, app):

        FXMainWindow.__init__(self, app, "List Test", w=600, h=400)

        FXMAPFUNC(self,SEL_CHORE,ListWindow.ID_CHORE,ListWindow.onChore)
        FXMAPFUNC(self,SEL_TIMEOUT,ListWindow.ID_TIMEOUT,ListWindow.onTimeout)

        listframe = FXHorizontalFrame(self, LAYOUT_FILL_X|LAYOUT_FILL_Y|FRAME_THICK|FRAME_RAISED)
        self.simplelist = FXList(listframe, 1, None, 0, LIST_EXTENDEDSELECT|LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.simplelist.appendItem("Start")

        self.queue = Queue(10)
        self.thread = MyThread(self.queue, sys.argv[1])
        self.thread.start()
 
        self.timer = 0
        self.chore = self.getApp().addChore(self,self.ID_CHORE)
        
    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)

    # Do something whenever timer fires
    def onTimeout(self,sender,sel,ptr):
        self.timer = self.getApp().addTimeout(10,self,self.ID_TIMEOUT)

    # Do something whenever a chore message is received
    def onChore(self,sender,sel,ptr):
        try:
            while 1:
              str = self.queue.get(0)
              if len(str)>0:
	          self.simplelist.appendItem(str)
                  if self.simplelist.getNumItems() > 100:
                      self.simplelist.removeItem(0)
	      else:
	          time.sleep(.1)
              break
        except Empty:
            pass
        except:
            import traceback
            traceback.print_exc()
        self.chore = self.getApp().addChore(self,self.ID_CHORE)

def runme():
    import sys
    if len(sys.argv) < 2:
        print "usage: foxtail.py <file>"
        sys.exit(1)
    application = FXApp()
    application.init(sys.argv)
    ListWindow(application)
    application.create()
    application.run()

# Main program starts here
if __name__ == '__main__':
    runme()


