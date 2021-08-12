# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddDeploy.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDeploy(object):
    def setupUi(self, AddDeploy):
        AddDeploy.setObjectName("AddDeploy")
        AddDeploy.resize(1450, 650)
        AddDeploy.setMinimumSize(QtCore.QSize(1450, 650))
        AddDeploy.setMaximumSize(QtCore.QSize(1450, 650))
        AddDeploy.setStyleSheet("background-color:#364052;")
        self.centralwidget = QtWidgets.QWidget(AddDeploy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(" font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(" font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.Btn_SelectSourceFiles = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_SelectSourceFiles.setGeometry(QtCore.QRect(519, 10, 91, 41))
        self.Btn_SelectSourceFiles.setMinimumSize(QtCore.QSize(80, 0))
        self.Btn_SelectSourceFiles.setStyleSheet("QPushButton {\n"
"    border: 0px solid black;\n"
"    border-radius: 6px;\n"
"\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"\n"
"    min-width: 80px;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Btn_SelectSourceFiles.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dist/icons/icons8-add-file-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_SelectSourceFiles.setIcon(icon)
        self.Btn_SelectSourceFiles.setIconSize(QtCore.QSize(36, 36))
        self.Btn_SelectSourceFiles.setObjectName("Btn_SelectSourceFiles")
        self.Btn_SelectDestinationPath = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_SelectDestinationPath.setGeometry(QtCore.QRect(1270, 10, 91, 41))
        self.Btn_SelectDestinationPath.setMinimumSize(QtCore.QSize(80, 0))
        self.Btn_SelectDestinationPath.setStyleSheet("QPushButton {\n"
"    border: 0px solid #0092d1;\n"
"    border-radius: 6px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #f6f7fa, stop: 1 #dadbde);\n"
"    min-width: 80px;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Btn_SelectDestinationPath.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("dist/icons/icons8-folder-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_SelectDestinationPath.setIcon(icon1)
        self.Btn_SelectDestinationPath.setIconSize(QtCore.QSize(36, 36))
        self.Btn_SelectDestinationPath.setObjectName("Btn_SelectDestinationPath")
        self.textEdit_SourceFiles = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_SourceFiles.setGeometry(QtCore.QRect(20, 70, 591, 471))
        self.textEdit_SourceFiles.setStyleSheet("QTextEdit {\n"
"    border: 0px solid #0092d1;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"}")
        self.textEdit_SourceFiles.setObjectName("textEdit_SourceFiles")
        self.Btn_SaveDeploy = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_SaveDeploy.setGeometry(QtCore.QRect(670, 560, 150, 40))
        self.Btn_SaveDeploy.setStyleSheet("QPushButton {\n"
"    border: 1px solid white;\n"
"    border-radius: 8px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #2c509e, stop: 1 #0092d1);\n"
"    min-width: 80px;\n"
"    color:white;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #0092d1, stop: 1 #2c509e);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.Btn_SaveDeploy.setObjectName("Btn_SaveDeploy")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(690, 110, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(" font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_DestPath = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_DestPath.setGeometry(QtCore.QRect(690, 70, 671, 31))
        self.lineEdit_DestPath.setStyleSheet("QLineEdit {\n"
"    border: 0px solid #0092d1;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: #2c509e;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"}")
        self.lineEdit_DestPath.setObjectName("lineEdit_DestPath")
        self.lineEdit_DeployName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_DeployName.setGeometry(QtCore.QRect(690, 140, 671, 31))
        self.lineEdit_DeployName.setStyleSheet("QLineEdit {\n"
"    border: 0px solid #0092d1;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: white;\n"
"    selection-background-color: darkgray;\n"
"    font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"}")
        self.lineEdit_DeployName.setObjectName("lineEdit_DeployName")
        self.label_ErrorSaveDeploy = QtWidgets.QLabel(self.centralwidget)
        self.label_ErrorSaveDeploy.setEnabled(True)
        self.label_ErrorSaveDeploy.setGeometry(QtCore.QRect(30, 550, 631, 51))
        self.label_ErrorSaveDeploy.setStyleSheet(" font-family: \"Lucida Console\", \"Courier New\", monospace;\n"
"font-size: 15px;\n"
"color:#ff8400;")
        self.label_ErrorSaveDeploy.setObjectName("label_ErrorSaveDeploy")
        AddDeploy.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddDeploy)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1450, 22))
        self.menubar.setObjectName("menubar")
        AddDeploy.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddDeploy)
        self.statusbar.setObjectName("statusbar")
        AddDeploy.setStatusBar(self.statusbar)

        self.retranslateUi(AddDeploy)
        QtCore.QMetaObject.connectSlotsByName(AddDeploy)

    def retranslateUi(self, AddDeploy):
        _translate = QtCore.QCoreApplication.translate
        AddDeploy.setWindowTitle(_translate("AddDeploy", "MainWindow"))
        self.label.setText(_translate("AddDeploy", "Source Files:"))
        self.label_2.setText(_translate("AddDeploy", "Destination Path:"))
        self.textEdit_SourceFiles.setPlaceholderText(_translate("AddDeploy", "Source Files"))
        self.Btn_SaveDeploy.setText(_translate("AddDeploy", "Save Deploy"))
        self.label_3.setText(_translate("AddDeploy", "Deploy Name:"))
        self.lineEdit_DestPath.setPlaceholderText(_translate("AddDeploy", "Enter the destination path"))
        self.lineEdit_DeployName.setPlaceholderText(_translate("AddDeploy", "Enter the name with which to save the deploy"))
        self.label_ErrorSaveDeploy.setText(_translate("AddDeploy", "Error while saving the deploy"))
