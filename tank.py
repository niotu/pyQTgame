import math

from PyQt5.QtCore import Qt, QTimer, QObject, QTime
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsEllipseItem

from bullet import Bullet


class Tank(QObject):
    def __init__(self, speed, angle, color, posD, scene, arena):
        super().__init__()
        self.angle = angle
        self.color = color
        self.arena = arena
        self.dif = posD
        self.width = 40
        self.height = 60
        self.scene = scene
        self.speed = speed
        self.tdx = math.sin(math.radians(angle)) * self.speed
        self.tdy = math.cos(math.radians(angle)) * self.speed
        self.bulletList = []
        self.c = 0
        self.shottimer = QTimer(self)
        self.shottimer.timeout.connect(self.moveBullets)
        self.shottimer.start(10)
        self.isReloaded = True
        self.reloadTimer = QTimer(self)
        self.reloadTimer.timeout.connect(self.reloading)
        self.isHitted = False
        self.healthPoints = 3

    def reset(self):
        self.scene.addItem(self.tank)
        self.scene.addItem(self.canon)
        self.scene.addItem(self.baska)
        self.hp1.show()
        self.hp2.show()
        self.hp3.show()
        self.isReloaded = True
        self.angle1 = 0
        self.bulletList = []
        self.tdx = math.sin(math.radians(self.angle)) * self.speed
        self.tdy = math.cos(math.radians(self.angle)) * self.speed
        self.healthPoints = 3

    def isDestroyed(self):
        if self.healthPoints == 0:
            self.hp3.hide()
            return True
        elif self.healthPoints == 1:
            self.hp2.hide()
            return False
        elif self.healthPoints == 2:
            self.hp1.hide()
            return False
        else:
            return False

    def reloading(self):
        self.c += 1
        if self.c % 2 == 0:
            self.isReloaded = True

    def tankCreate(self):
        self.tank: QGraphicsRectItem = self.scene.addRect(-20, -30, 40, 60, pen=Qt.black, brush=self.color)
        self.baska = QGraphicsRectItem(-15, -15, 30, 30, parent=self.tank)
        self.canon = QGraphicsRectItem(-8, -15, 16, -45, parent=self.tank)
        self.hp1 = QGraphicsEllipseItem(8, 32, 4, 4, parent=self.tank)
        self.hp2 = QGraphicsEllipseItem(-2, 32, 4, 4, parent=self.tank)
        self.hp3 = QGraphicsEllipseItem(-12, 32, 4, 4, parent=self.tank)
        self.canon.setBrush(self.color)
        self.canon.setPen(Qt.black)

    def tankLocate(self):
        self.tank.setX(self.dif)
        self.tank.setY(400)
        self.tank.setRotation(0)

    def tankMoving(self, moveDirection):
        self.tank.prepareGeometryChange()
        self.canon.prepareGeometryChange()
        if moveDirection == "up":
            self.tank.setY(self.tank.y() - self.tdy)
            self.tank.setX(self.tank.x() - self.tdx)
            self.moveDown = False
        elif moveDirection == "down":
            self.tank.setY(self.tank.y() + self.tdy)
            self.tank.setX(self.tank.x() + self.tdx)
            self.moveDown = True

    def tankRotation(self, rotateDirection):
        self.tank.prepareGeometryChange()
        self.canon.prepareGeometryChange()
        self.angle1 = 0
        if self.tank.rotation() < 0:
            self.angle1 = -self.tank.rotation()
        elif self.tank.rotation() > 0:
            self.angle1 = -self.tank.rotation()
        self.tdx = math.sin(math.radians(self.angle1)) * self.speed
        self.tdy = math.cos(math.radians(self.angle1)) * self.speed
        if rotateDirection == "right":
            self.angle += 1
            if self.angle > 360:
                self.angle -= 360
        elif rotateDirection == "left":
            self.angle -= 1
            if self.angle < -360:
                self.angle += 360
        self.tank.setRotation(self.angle)

    def tankGunPosition(self):
        x = self.tank.x() - 70 * self.tdx
        y = self.tank.y() - 70 * self.tdy
        return x, y

    def bulletSpawn(self):
        x, y = self.tankGunPosition()
        self.bullet1 = Bullet(speed=2, x=x, y=y,
                              scene=self.scene,
                              dx=self.tdx, dy=self.tdy,
                              arena=self.arena)
        self.reloadTimer.start(500)
        self.bulletList.append(self.bullet1)
        self.isReloaded = False

    def moveBullets(self):
        for bullet1 in self.bulletList:
            bullet1.shooting()
            if bullet1.inScene is False:
                self.bulletList.remove(bullet1)
