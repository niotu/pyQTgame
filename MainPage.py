from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QRectF, QObject

from PyQt5 import QtWidgets, uic


class MainPage(QtWidgets.QDialog):
    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('mainPage.ui', self)
