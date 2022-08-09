from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QRectF, QObject
from PyQt5.QtGui import QPainter, QPixmap, QPalette
from PyQt5.QtWidgets import QDialog, QGraphicsScene, QMessageBox, QGraphicsLineItem, QGraphicsItem, QGraphicsRectItem, \
    QGraphicsPixmapItem
from ballform_ui import Ui_BallForm
from tank import Tank


class BallForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_BallForm()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.page.setStyleSheet("background-image : url(background.jpg)")
        self.ui.playButton.setStyleSheet("background-image : url(playbutton.png)")
        self.ui.mainpic.setStyleSheet("background-image : url(mainpicback.png)")
        self.ui.playButton.clicked.connect(self.play)
        self.ui.backButton.clicked.connect(self.backToMenu)
        self.scene = KeyMoving(self)
        self.rus = QPixmap("russia.png")
        self.usa = QPixmap("usa.png")
        self.ui.reset.clicked.connect(self.reset)
        self.ui.graphicsView_2.setScene(self.scene)
        self.ui.graphicsView_2.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.scene.keyPressed.connect(self.onKeyPressed)
        self.scene.keyRelease.connect(self.onKeyRelease)
        self.sea = QRectF(0, 0, 1200, 600)
        self.scene.addRect(self.sea, pen=Qt.black, brush=Qt.blue)
        self.arena = self.scene.addRect(50, 50, 1100, 500, pen=Qt.black, brush=Qt.yellow)
        self.tank1 = Tank(speed=1, angle=1, color=Qt.green, posD=1080, scene=self.scene, arena=self.sea)
        self.tank2 = Tank(speed=1, angle=1, color=Qt.red, posD=120, scene=self.scene, arena=self.sea)
        self.lineList = [QGraphicsLineItem(50, 50, 1150, 50),
                         QGraphicsLineItem(1150, 50, 1150, 550),
                         QGraphicsLineItem(1150, 550, 50, 550),
                         QGraphicsLineItem(50, 550, 50, 50)]
        for i in self.lineList:
            self.scene.addItem(i)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.moving)
        self.moveUp = False
        self.moveDown = False
        self.turnRight = False
        self.turnLeft = False
        self.moveUp2 = False
        self.moveDown2 = False
        self.turnRight2 = False
        self.turnLeft2 = False
        self.shot = False
        self.shot2 = False
        self.tank1.tankCreate()
        self.tank1.tankLocate()
        self.tank2.tankCreate()
        self.tank2.tankLocate()
        self.grEagle = Eagle(scene=self.scene, pic=self.rus, pos=[1120, 80])
        self.grEagle.create()
        self.grEagle.eagle.setPos(920, 280)
        self.grEagleBody = self.scene.addRect(918, 278, 64, 64)
        self.redEagle = Eagle(scene=self.scene, pic=self.usa, pos=[1120, 80])
        self.redEagle.create()
        self.redEagle.eagle.setPos(200, 320)
        self.redEagleBody = self.scene.addRect(198, 318, 64, 64)
        self.wallList = [Wall(50, 50, 100, 100),
                         Wall(170, 500, 50, 50),
                         Wall(250, 180, 120, 120),
                         Wall(300, 300, 20, 100),
                         Wall(280, 400, 60, 60),
                         Wall(550, 300, 80, 80),
                         Wall(800, 480, 70, 70),
                         Wall(850, 350, 70, 70),
                         Wall(820, 200, 70, 70),
                         Wall(860, 200, 20, 150),
                         Wall(950, 50, 100, 100)]
        for i in self.wallList:
            self.scene.addItem(i.wall1)
        self.timer.start(10)
        self.physTimer = QTimer(self)
        self.physTimer.timeout.connect(self.checkCollides)
        self.physTimer.start(10)

    def play(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def backToMenu(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def checkCollides(self):
        allBullets = []
        allBullets.extend(self.tank1.bulletList)
        allBullets.extend(self.tank2.bulletList)
        if self.tank2.tank.collidesWithItem(self.tank1.tank, Qt.IntersectsItemBoundingRect):
            self.moveUp = False
            self.moveUp2 = False
        for line in self.lineList:
            if line.collidesWithItem(self.tank1.tank):
                if self.tank1.moveDown is True:
                    self.moveDown = False
                elif self.tank1.moveDown is False:
                    self.moveUp = False
            if line.collidesWithItem(self.tank2.tank):
                if self.tank2.moveDown is True:
                    self.moveDown2 = False
                elif self.tank2.moveDown is False:
                    self.moveUp2 = False
        for wall in self.wallList:
            if wall.wall1.collidesWithItem(self.tank1.tank):
                if self.tank1.moveDown is False:
                    self.moveUp = False
                elif self.tank1.moveDown is True:
                    self.moveDown = False
            if wall.wall1.collidesWithItem(self.tank2.tank):
                if self.tank2.moveDown is False:
                    self.moveUp2 = False
                elif self.tank2.moveDown is True:
                    self.moveDown2 = False
            for bullet in allBullets:
                if wall.wall1.collidesWithItem(bullet.bullet):
                    bullet.bullet.setPos(-1, -1)
        for bullet in allBullets:
            if self.tank2.tank.collidesWithItem(bullet.bullet, Qt.IntersectsItemBoundingRect):
                self.shot = False
                allBullets.remove(bullet)
                bullet.bullet.setPos(-1, -1)
                self.tank2.healthPoints -= 1
                if self.tank2.isDestroyed():
                    self.scene.removeItem(self.tank2.tank)
                    self.scene.removeItem(self.tank2.baska)
                    self.scene.removeItem(self.tank2.canon)
                    self.moveUp2 = False
                    self.moveDown2 = False
                    self.turnRight2 = False
                    self.turnLeft2 = False
                    QMessageBox.information(self, "победа", "победил зеленый")
            if self.tank1.tank.collidesWithItem(bullet.bullet, Qt.IntersectsItemBoundingRect):
                self.shot = False
                bullet.bullet.setPos(-1, -1)
                self.tank1.healthPoints -= 1
                if self.tank1.isDestroyed():
                    self.scene.removeItem(self.tank1.tank)
                    self.scene.removeItem(self.tank1.baska)
                    self.scene.removeItem(self.tank1.canon)
                    self.moveUp = False
                    self.moveDown = False
                    self.turnRight = False
                    self.turnLeft = False
                    QMessageBox.information(self, "победа", "победил красный")

    def reset(self):
        if self.tank1.isDestroyed():
            self.tank1.reset()
        elif self.tank2.isDestroyed():
            self.tank2.reset()
        self.tank1.tankLocate()
        self.tank2.tankLocate()

    def onKeyPressed(self, code):
        if code == Qt.Key_I:
            self.moveUp = True
        elif code == Qt.Key_K:
            self.moveDown = True
        elif code == Qt.Key_L:
            self.turnRight = True
        elif code == Qt.Key_J:
            self.turnLeft = True
        elif code == Qt.Key_W:
            self.moveUp2 = True
        elif code == Qt.Key_S:
            self.moveDown2 = True
        elif code == Qt.Key_D:
            self.turnRight2 = True
        elif code == Qt.Key_A:
            self.turnLeft2 = True
        elif code == Qt.Key_N:
            self.shot = True
        elif code == Qt.Key_C:
            self.shot2 = True

    def onKeyRelease(self, code):
        if code == Qt.Key_I:
            self.moveUp = False
        elif code == Qt.Key_K:
            self.moveDown = False
        elif code == Qt.Key_L:
            self.turnRight = False
        elif code == Qt.Key_J:
            self.turnLeft = False
        elif code == Qt.Key_W:
            self.moveUp2 = False
        elif code == Qt.Key_S:
            self.moveDown2 = False
        elif code == Qt.Key_D:
            self.turnRight2 = False
        elif code == Qt.Key_A:
            self.turnLeft2 = False
        elif code == Qt.Key_N:
            self.shot = False
        elif code == Qt.Key_C:
            self.shot2 = False

    def moving(self):
        if self.moveUp is True:
            self.tank1.tankMoving("up")
        elif self.moveDown is True:
            self.tank1.tankMoving("down")
        if self.turnRight is True:
            self.tank1.tankRotation("right")
        elif self.turnLeft is True:
            self.tank1.tankRotation("left")
        if self.moveUp2 is True:
            self.tank2.tankMoving("up")
        elif self.moveDown2 is True:
            self.tank2.tankMoving("down")
        if self.turnRight2 is True:
            self.tank2.tankRotation("right")
        elif self.turnLeft2 is True:
            self.tank2.tankRotation("left")
        if self.shot is True:
            if self.tank1.isReloaded:
                self.tank1.bulletSpawn()
        if self.shot2 is True:
            if self.tank2.isReloaded:
                self.tank2.bulletSpawn()


class KeyMoving(QGraphicsScene):
    keyPressed = pyqtSignal(int)
    keyRelease = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.isAutoRepeat():
            return
        self.keyPressed.emit(event.key())

    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None:
        super().keyReleaseEvent(event)
        if event.isAutoRepeat():
            return
        self.keyRelease.emit(event.key())


class Wall(QObject):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        x1 = x1
        x2 = x2
        y1 = y1
        y2 = y2
        self.wall1 = QGraphicsRectItem(x1, y1, x2, y2)
        self.wall1.setBrush(Qt.black)


class Eagle(QObject):
    def __init__(self, scene, pic, pos):
        super().__init__()
        self.health_points = 10
        self.scene = scene
        self.pos = pos
        self.pic = pic

    def create(self):
        self.eagle = QGraphicsPixmapItem(self.pic)
        self.scene.addItem(self.eagle)

    def isDestroyed(self):
        pass