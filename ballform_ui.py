# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ballform.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BallForm(object):
    def setupUi(self, BallForm):
        BallForm.setObjectName("BallForm")
        BallForm.resize(924, 572)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BallForm.sizePolicy().hasHeightForWidth())
        BallForm.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(BallForm)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(BallForm)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 204, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(315, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainpic = QtWidgets.QLabel(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(239)
        sizePolicy.setVerticalStretch(51)
        sizePolicy.setHeightForWidth(self.mainpic.sizePolicy().hasHeightForWidth())
        self.mainpic.setSizePolicy(sizePolicy)
        self.mainpic.setMinimumSize(QtCore.QSize(239, 51))
        self.mainpic.setObjectName("mainpic")
        self.verticalLayout.addWidget(self.mainpic)
        self.playButton = QtWidgets.QPushButton(self.page)
        self.playButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(239)
        sizePolicy.setVerticalStretch(51)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(239, 51))
        self.playButton.setText("")
        self.playButton.setAutoDefault(False)
        self.playButton.setObjectName("playButton")
        self.verticalLayout.addWidget(self.playButton)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(314, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 204, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.page_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout.addWidget(self.graphicsView_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reset = QtWidgets.QPushButton(self.page_2)
        self.reset.setObjectName("reset")
        self.verticalLayout_2.addWidget(self.reset)
        self.backButton = QtWidgets.QPushButton(self.page_2)
        self.backButton.setObjectName("backButton")
        self.verticalLayout_2.addWidget(self.backButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        self.retranslateUi(BallForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BallForm)

    def retranslateUi(self, BallForm):
        _translate = QtCore.QCoreApplication.translate
        BallForm.setWindowTitle(_translate("BallForm", "Dialog"))
        self.mainpic.setText(_translate("BallForm", "tanks 3000 by me lmao lol gang shit "))
        self.reset.setText(_translate("BallForm", "reset"))
        self.backButton.setText(_translate("BallForm", "back to menu"))
