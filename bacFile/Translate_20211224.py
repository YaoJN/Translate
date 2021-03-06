# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_Translate(object):
    def setupUi(self, Translate):
        Translate.setObjectName("Translate")
        Translate.resize(1109, 828)
        self.groupBox = QtWidgets.QGroupBox(Translate)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 1091, 231))
        self.groupBox.setObjectName("groupBox")
        self.originalBox = QtWidgets.QComboBox(self.groupBox)
        self.originalBox.setGeometry(QtCore.QRect(50, 10, 101, 31))
        self.originalBox.setObjectName("originalBox")
        self.originalText = QtWidgets.QTextEdit(self.groupBox)
        self.originalText.setGeometry(QtCore.QRect(20, 50, 1051, 171))
        self.originalText.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.originalText.setObjectName("originalText")
        self.groupBox_2 = QtWidgets.QGroupBox(Translate)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 270, 531, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.translationText = QtWidgets.QTextEdit(self.groupBox_2)
        self.translationText.setGeometry(QtCore.QRect(20, 50, 491, 171))
        self.translationText.setObjectName("translationText")
        self.translationBox = QtWidgets.QComboBox(self.groupBox_2)
        self.translationBox.setGeometry(QtCore.QRect(90, 10, 101, 31))
        self.translationBox.setObjectName("translationBox")
        self.groupBox_3 = QtWidgets.QGroupBox(Translate)
        self.groupBox_3.setGeometry(QtCore.QRect(570, 270, 531, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.transToOriginalText = QtWidgets.QTextEdit(self.groupBox_3)
        self.transToOriginalText.setGeometry(QtCore.QRect(20, 50, 491, 171))
        self.transToOriginalText.setObjectName("transToOriginalText")
        self.groupBox_4 = QtWidgets.QGroupBox(Translate)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 530, 531, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.translationText_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.translationText_2.setGeometry(QtCore.QRect(20, 50, 491, 171))
        self.translationText_2.setObjectName("translationText_2")
        self.translationBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.translationBox_2.setGeometry(QtCore.QRect(90, 10, 101, 31))
        self.translationBox_2.setObjectName("translationBox_2")
        self.groupBox_5 = QtWidgets.QGroupBox(Translate)
        self.groupBox_5.setGeometry(QtCore.QRect(570, 530, 531, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.transToOriginalText_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.transToOriginalText_2.setGeometry(QtCore.QRect(20, 50, 491, 171))
        self.transToOriginalText_2.setObjectName("transToOriginalText_2")
        self.queryBtn = QtWidgets.QPushButton(self.groupBox)
        self.queryBtn.setGeometry(QtCore.QRect(200, 10, 93, 28))
        self.queryBtn.setObjectName("queryBtn")
        self.queryBtnJToC = QtWidgets.QPushButton(self.groupBox)
        self.queryBtnJToC.setGeometry(QtCore.QRect(310, 10, 93, 28))
        self.queryBtnJToC.setObjectName("queryBtnJToC")
        self.small = QtWidgets.QPushButton(self.groupBox)
        self.small.setGeometry(QtCore.QRect(640, 10, 93, 28))
        self.small.setObjectName("small")
        self.clear = QtWidgets.QPushButton(self.groupBox)
        self.clear.setGeometry(QtCore.QRect(530, 10, 93, 28))
        self.clear.setObjectName("clear")
        self.queryBtnCTOJ = QtWidgets.QPushButton(self.groupBox)
        self.queryBtnCTOJ.setGeometry(QtCore.QRect(420, 10, 93, 28))
        self.queryBtnCTOJ.setObjectName("queryBtnCTOJ")

        self.originalBox.addItem("")
        self.originalBox.addItem("")
        self.originalBox.addItem("")
        self.translationBox.addItem("")
        self.translationBox.addItem("")
        self.translationBox.addItem("")
        self.translationBox_2.addItem("")
        self.translationBox_2.addItem("")
        self.translationBox_2.addItem("")

        self.originalText.setFont(QFont("Arial", 10))
        self.transToOriginalText.setFont(QFont("Arial", 10))
        self.transToOriginalText_2.setFont(QFont("Arial", 10))
        self.translationText.setFont(QFont("Arial", 10))
        self.translationText_2.setFont(QFont("Arial", 10))
        self.retranslateUi(Translate)
        self.queryBtn.clicked.connect(Translate.queryText)
        self.clear.clicked.connect(Translate.clearText)
        self.small.clicked.connect(Translate.small)
        self.queryBtnCTOJ.clicked.connect(Translate.queryBtnCTOJ)
        self.queryBtnJToC.clicked.connect(Translate.queryBtnJTOC)
        QtCore.QMetaObject.connectSlotsByName(Translate)

    def retranslateUi(self, Translate):
        _translate = QtCore.QCoreApplication.translate
        Translate.setWindowTitle(_translate("Translate", "Dialog"))
        self.groupBox_2.setTitle(_translate("Translate", "BdiDu??????"))
        self.groupBox_3.setTitle(_translate("Translate", "BaiDu????????????"))
        self.groupBox_4.setTitle(_translate("Translate", "Google??????"))
        self.groupBox_5.setTitle(_translate("Translate", "Google????????????"))
        self.groupBox.setTitle(_translate("Translate", "??????"))
        self.queryBtn.setText(_translate("Translate", "??????"))
        self.queryBtn.setShortcut(_translate("Translate", "Ctrl+Return"))
        self.queryBtnJToC.setText(_translate("Translate", "??????"))
        self.queryBtnJToC.setShortcut(_translate("Translate", "Ctrl+1"))
        self.minBtn.setText(_translate("Translate", "?????????"))
        self.minBtn.setShortcut(_translate("Translate", "Ctrl+4"))
        self.clearBtn.setText(_translate("Translate", "?????????"))
        self.clearBtn.setShortcut(_translate("Translate", "Ctrl+3"))
        self.queryBtnCTOJ.setText(_translate("Translate", "??????"))
        self.queryBtnCTOJ.setShortcut(_translate("Translate", "Ctrl+2"))
        self.originalBox.setItemText(0, _translate("Translate", "?????????"))
        self.originalBox.setItemText(1, _translate("Translate", "?????????"))
        self.originalBox.setItemText(2, _translate("Translate", "??????"))
        self.translationBox.setItemText(0, _translate("Translate", "?????????"))
        self.translationBox.setItemText(1, _translate("Translate", "?????????"))
        self.translationBox.setItemText(2, _translate("Translate", "??????"))
        self.translationBox_2.setItemText(0, _translate("Translate", "?????????"))
        self.translationBox_2.setItemText(1, _translate("Dialog", "?????????"))
        self.translationBox_2.setItemText(2, _translate("Dialog", "??????"))
