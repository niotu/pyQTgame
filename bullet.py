from PyQt5.QtCore import QObject, QTimer, QRectF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsScene


class Bullet(QObject):
    def __init__(self, speed, x, y, scene, dx, dy, arena):
        super().__init__()
        self.inScene = True
        self.bulletSpeed = speed
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.arena: QRectF = arena
        self.scene: QGraphicsScene = scene
        self.bullet: QGraphicsEllipseItem = QGraphicsEllipseItem(0, 0, 6, 6)
        self.scene.addItem(self.bullet)
        self.bullet.setPos(self.x, self.y)

    def shooting(self):
        if self.arena.contains(self.bullet.pos()):
            self.inScene = True
            self.bullet.setX(self.bullet.x() - self.dx * 2)
            self.bullet.setY(self.bullet.y() - self.dy * 2)
        else:
            self.inScene = False
            self.scene.removeItem(self.bullet)
