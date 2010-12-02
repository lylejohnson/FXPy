#! /usr/bin/env python

from FXPy.fox import *
from math import atan, pi
import os
from threading import Thread
from time import sleep

# How many pixels to move
MOVE = 12

# Directions cat can face
EAST = 1
NORTHEAST = 2
NORTH = 3
NORTHWEST = 4
WEST = 5
SOUTHWEST = 6
SOUTH = 7
SOUTHEAST = 8

# Other states of interest
WAITING, ASLEEP, AWAKENED = 9, 10, 11

# Angular ranges for these directions
compass = [
    (0, 22.5, EAST),
    (337.5, 360, EAST),
    (292.5, 337.5, NORTHEAST),
    (247.5, 292.5, NORTH),
    (202.5, 247.5, NORTHWEST),
    (157.5, 202.5, WEST),
    (112.5, 157.5, SOUTHWEST),
    (67.5, 112.5, SOUTH),
    (22.5, 67.5, SOUTHEAST)
]

# The mouse is a pretty simple class!
class Mouse:
    def __init__(self, canvas):
        self.canvas = canvas

    def getPos(self):
        x, y, buttons = self.canvas.getCursorPosition()
        return x, y

# The cat is much more complex
class Cat(Thread):
    def __init__(self, canvas, mouse):
        Thread.__init__(self)
        self.canvas, self.mouse = canvas, mouse
        self.loadImages(canvas.getApp())
        self.img1, self.img2 = self.images[WAITING]
        self.setSize(40, 40)
        self.setPos(0, 0)
        self.whichImage = 1
        self.setSpeed(40)
        self.setResponseTime(150)
        self.asleep = 0
        self.alive = 1

    def getBoundaries(self):
        xmin    = 0.5*self.getWidth()
        xmax    = self.canvas.getWidth() - 0.5*self.getWidth()
        ymin    = 0.5*self.getHeight()
        ymax    = self.canvas.getHeight() - 0.5*self.getHeight()
        return xmin, xmax, ymin, ymax

    def asCloseAsPossible(self, mouseX, mouseY):
        currX, currY = self.getPos()
        xmin, xmax, ymin, ymax = self.getBoundaries()
        if (currX, currY) == (mouseX, mouseY):
            return 1
        elif mouseX >= xmin and mouseX <= xmax and mouseY >= ymin and mouseY <= ymax:
            return 0
        if mouseY <= currY:     # mouse is above cat
            if mouseX > currX and currX < xmax:
                return 0
            elif mouseX < currX and currX > xmin:
                return 0
            else:
                return 1
        else:                   # mouse is below cat
            if mouseX > currX and currX < xmax:
                return 0
            elif mouseX < currX and currX > xmin:
                return 0
            else:
                return 1

    def run(self):
        "Chase the mouse until we're as close as we can get!"
        self.setPos(0.5*self.canvas.getWidth(), 0.5*self.canvas.getHeight())
        sitsem = 0
        while self.alive:
            sleep(0.001*self.getResponseTime())
            mouseX, mouseY = self.getMousePos()
            if self.asCloseAsPossible(mouseX, mouseY):
                sitsem = sitsem + 1
                if sitsem >= 6:
                    self.sleep()
                else:
                    self.sit()
            else:
                sitsem = 0
                self.chaseMouse()

    def stop(self):
        self.alive = 0

    def loadImages(self, app):
        img = []
        for i in xrange(21):
            filename = os.path.join('icons', 'cat%d.png' % i)
            data = open(filename, 'rb').read()
            img.append(FXPNGIcon(app, data))
            img[i].create()

        self.images = {
            EAST        : (img[0], img[1]),
            NORTHEAST   : (img[2], img[3]),
            NORTH       : (img[4], img[5]),
            NORTHWEST   : (img[6], img[7]),
            WEST        : (img[8], img[9]),
            SOUTHWEST   : (img[10], img[11]),
            SOUTH       : (img[12], img[13]),
            SOUTHEAST   : (img[14], img[15]),
            ASLEEP      : (img[16], img[17]),
            WAITING     : (img[18], img[19]),
            AWAKENED    : (img[20], img[20])
        }

    def setResponseTime(self, responseTime):
        self.responseTime = responseTime

    def getResponseTime(self):
        return self.responseTime

    def getPos(self):
        return self.currX, self.currY

    def setPos(self, x, y):
        xmin, xmax, ymin, ymax = self.getBoundaries()
        self.currX = min(max(x, xmin), xmax)
        self.currY = min(max(y, ymin), ymax)

    def getMousePos(self):
        "Return mouse position in canvas coordinates"
        return self.mouse.getPos()

    def correctTrajectory(self, mouseX, mouseY):
        currX, currY = self.getPos()
        if mouseX == currX:
            mouseX = currX + 0.1
        angle = atan((mouseY-currY)/(mouseX-currX))*180/pi
        if mouseX < currX:
            angle = angle + 180
        elif angle < 0:
            angle = angle + 360
        direction = self.getCompassDirection(angle)
        self.img1, self.img2 = self.images[direction]

    def getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def setSize(self, w, h):
        self.w = max(min(w, 120), 40)
        self.h = max(min(h, 120), 40)

    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = max(min(speed, 120), -120)

    def chaseMouse(self):
        currX, currY = self.getPos()
        mouseX, mouseY = self.getMousePos()
        self.correctTrajectory(mouseX, mouseY)
        if mouseX > currX:
            newX = min(currX + MOVE, mouseX)
        else:
            newX = max(currX - MOVE, mouseX)

        if mouseY > currY:
            newY = min(currY + MOVE, mouseY)
        else:
            newY = max(currY - MOVE, mouseY)

        self.setPos(newX, newY)
        self.repaint()

    def repaint(self):
        self.canvas.update()

    def getCompassDirection(self, angle):
        for d in compass:
            if (angle >= d[0]) and (angle <= d[1]):
                return d[2]

    def isAsleep(self):
        return self.asleep

    def sit(self):
        self.img1, self.img2 = self.images[WAITING]
        self.setResponseTime(800 - 5*self.getSpeed())
        self.repaint()

    def sleep(self):
        if self.asleep == 0:
            self.setResponseTime(1500 - 8*self.getSpeed())
            self.img1, self.img2 = self.images[ASLEEP]
            self.asleep = 1
        self.repaint()

    def wakeUp(self):
        if self.asleep == 1:
            self.setResponseTime(2000 - 10*self.getSpeed())
            self.img1, self.img2 = self.images[AWAKENED]
            self.asleep = 0
            self.repaint()

    def respondToMotion(self):
        if self.isAsleep():
            self.wakeUp()
        else:
            self.setResponseTime(150 - self.getSpeed())

    def draw(self, dc):
        currX, currY = self.getPos()
        x = currX - 0.5*self.getWidth()
        y = currY - 0.5*self.getHeight()
        if self.whichImage == 1:
            dc.drawIcon(self.img1, x, y)
            self.whichImage = 2
        else:
            dc.drawIcon(self.img2, x, y)
            self.whichImage = 1

class NekoWindow(FXMainWindow):
    ID_CANVAS = FXMainWindow.ID_LAST
    ID_TIMER = ID_CANVAS + 1
    ID_SPEED = ID_TIMER + 1
    def __init__(self, app):
        FXMainWindow.__init__(self, app, 'Neko', w=600, h=400)
        FXMAPFUNC(self, SEL_PAINT, self.ID_CANVAS, NekoWindow.onPaint)
        FXMAPFUNC(self, SEL_MOTION, self.ID_CANVAS, NekoWindow.onMotion)
        FXMAPFUNC(self, SEL_DESTROY, 0, NekoWindow.onDestroy)
        FXMAPFUNC(self, SEL_TIMEOUT, self.ID_TIMER, NekoWindow.onTimeout)
        FXMAPFUNC(self, SEL_COMMAND, self.ID_SPEED, NekoWindow.onCmdSpeed)

        controls = FXVerticalFrame(self, LAYOUT_SIDE_RIGHT|LAYOUT_FILL_Y)
        FXLabel(controls, 'Controls', opts=LAYOUT_CENTER_X)
        FXHorizontalSeparator(controls)
        frame = FXHorizontalFrame(controls, LAYOUT_FILL_X)

        FXLabel(frame, 'Cat Speed:')
        spinner = FXSpinner(frame, 6, self, self.ID_SPEED,
            SPIN_NORMAL|FRAME_SUNKEN|FRAME_THICK)
        spinner.setValue(40)
        spinner.setRange(-120, 120)
        spinner.setIncrement(20)

        packer = FXPacker(self,
            FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y,
            pl=0, pr=0, pt=0, pb=0)
        canvas = FXCanvas(packer, self, self.ID_CANVAS,
            LAYOUT_FILL_X|LAYOUT_FILL_Y)
        self.mouse = Mouse(canvas)
        self.cat = Cat(canvas, self.mouse)
        app.addTimeout(10, self, self.ID_TIMER)

    def create(self):
        FXMainWindow.create(self)
        self.show(PLACEMENT_SCREEN)
        self.cat.start()

    def onTimeout(self, sender, sel, ptr):
        self.getApp().flush()
        app.addTimeout(10, self, self.ID_TIMER)

    def onCmdSpeed(self, spinner, sel, ptr):
        self.cat.setSpeed(spinner.getValue())

    def onPaint(self, canvas, sel, ev):
        dc = FXDCWindow(canvas, ev)
        dc.setForeground(canvas.getBackColor())
        dc.fillRectangle(ev.rect.x, ev.rect.y, ev.rect.w, ev.rect.h)
        self.cat.draw(dc)

    def onMotion(self, canvas, sel, ev):
        self.cat.respondToMotion()

    def onDestroy(self, sender, sel, ptr):
        self.cat.stop()
        return FXMainWindow.onDestroy(self, sender, sel, ptr)

if __name__ == '__main__':
    import sys
    app = FXApp('PyNeko', 'Test')
    app.init(sys.argv)
    NekoWindow(app)
    app.create()
    app.run()
