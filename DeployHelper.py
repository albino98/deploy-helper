# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeployHelper.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeployHelper(object):
    def setupUi(self, DeployHelper):
        DeployHelper.setObjectName("DeployHelper")
        DeployHelper.resize(1642, 760)
        DeployHelper.setMinimumSize(QtCore.QSize(1560, 760))
        DeployHelper.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(DeployHelper)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_deploys = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_deploys.setGeometry(QtCore.QRect(10, 50, 256, 591))
        self.listWidget_deploys.setObjectName("listWidget_deploys")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setFamily("LCDMono2")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Btn_AddDeploy = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_AddDeploy.setGeometry(QtCore.QRect(290, 50, 101, 41))
        self.Btn_AddDeploy.setObjectName("Btn_AddDeploy")
        DeployHelper.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeployHelper)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1642, 21))
        self.menubar.setObjectName("menubar")
        DeployHelper.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DeployHelper)
        self.statusbar.setObjectName("statusbar")
        DeployHelper.setStatusBar(self.statusbar)

        self.retranslateUi(DeployHelper)
        QtCore.QMetaObject.connectSlotsByName(DeployHelper)

    def retranslateUi(self, DeployHelper):
        _translate = QtCore.QCoreApplication.translate
        DeployHelper.setWindowTitle(_translate("DeployHelper", "MainWindow"))
        self.label.setText(_translate("DeployHelper", "Your Deploys:"))
        self.Btn_AddDeploy.setText(_translate("DeployHelper", "Add Deploy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeployHelper = QtWidgets.QMainWindow()
    ui = Ui_DeployHelper()
    ui.setupUi(DeployHelper)
    DeployHelper.show()
    sys.exit(app.exec_())