from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen, QFileDialog
from PyQt5.uic.properties import QtGui

from DeployHelper import Ui_DeployHelper
from AddDeploy import Ui_AddDeploy
import sys
import functions

class Main(QMainWindow, Ui_DeployHelper):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)



class Open_AddDeploy(QMainWindow, Ui_AddDeploy):
    def __init__(self):
        super(Open_AddDeploy, self).__init__()
        self.setupUi(self)
        #self.Btn_SelectDestinationPath.clicked.connect(self.close)

        # EVENTO CLICK BOTTONE Btn_SelectSourceFiles
        self.Btn_SelectSourceFiles.clicked.connect(self.openFileExplorer)

    def OPEN(self):
        self.show()

    def openFileExplorer(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        self.textEdit_SourceFiles.setText(fileName)
        print(fileName)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    ShowAddDeploy = Open_AddDeploy()
    main.show()

    #EVENTO CLICK BOTTONE AddDeploy
    main.Btn_AddDeploy.clicked.connect(ShowAddDeploy.OPEN)




    sys.exit(app.exec_())