# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatclient.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 232)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(10, 10, 113, 20))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(180, 10, 113, 20))
        self.passwordEdit.setObjectName("passwordEdit")
        self.inputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEdit.setGeometry(QtCore.QRect(10, 190, 231, 20))
        self.inputEdit.setObjectName("inputEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(250, 190, 41, 23))
        self.sendButton.setObjectName("sendButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 281, 141))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChatClient"))
        self.usernameEdit.setPlaceholderText(_translate("MainWindow", "Username"))
        self.passwordEdit.setPlaceholderText(_translate("MainWindow", "Password"))
        self.inputEdit.setPlaceholderText(_translate("MainWindow", "Text here..."))
        self.sendButton.setText(_translate("MainWindow", "Send"))
