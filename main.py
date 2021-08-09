from xml.etree.ElementTree import ElementTree

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen, QFileDialog
from PyQt5.uic.properties import QtGui
from DeployHelper import Ui_DeployHelper
from AddDeploy import Ui_AddDeploy
import sys
from xml.etree import ElementTree as ET


# OPEN THE MAIN WINDOW
class Main(QMainWindow, Ui_DeployHelper):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)



class AddDeployWindow(QMainWindow, Ui_AddDeploy):
    def __init__(self):
        super(AddDeployWindow, self).__init__()
        self.setupUi(self)
        #self.Btn_SelectDestinationPath.clicked.connect(self.close)

        # BUTTON Btn_SelectSourceFiles CLICK EVENT
        self.Btn_SelectSourceFiles.clicked.connect(self.selectSourceFiles)
        # BUTTON Btn_SelectDestinationPath CLICK EVENT
        self.Btn_SelectDestinationPath.clicked.connect(self.selectDestinationPath)
        # BUTTON Btn_SaveDeploy CLICK EVENT
        self.Btn_SaveDeploy.clicked.connect(self.saveDeployAction)
        # SET ERROR LABEL TO HIDDEN
        self.label_ErrorSaveDeploy.hide()


    def OPEN(self):
        self.show()


    # OPEN THE FILE EXPLORER TO SELECT SOURCE FILES
    def selectSourceFiles(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(None, "Select Files", "","All Files (*);;Python Files (*.py)", options=options)
        #self.textEdit_SourceFiles.setText(fileName)
        #print(file_names)
        for file in file_names:
            self.textEdit_SourceFiles.append(file)


    # OPEN THE FILE EXPLORER TO SELECT THE DESTINATION PATH
    def selectDestinationPath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dest_path = str(QFileDialog.getExistingDirectory(self, "Select Directory", "", options=options))
        self.lineEdit_DestPath.setText(dest_path)


    # Btn_SaveDeploy ACTION (SAVE DEPLOY ON XML FILE AND CLOSE AddDeployWindow)
    def saveDeployAction(self):
        try:
            dest_path = self.lineEdit_DestPath.text()
            deploy_name = self.lineEdit_DeployName.text()
            source_files = self.textEdit_SourceFiles.toPlainText()
            source_files_arr = source_files.splitlines()

            # CHECK INSERTED VALUES
            if (not dest_path) or (not deploy_name) or (not source_files_arr):
                self.label_ErrorSaveDeploy.setText('Please fill in all fields')
                self.label_ErrorSaveDeploy.show()
            else:
                self.label_ErrorSaveDeploy.hide()
                saveResult = self.saveDeployOnXml(dest_path, deploy_name, source_files_arr)

                if saveResult == 0:  # ERROR 0: ALREADY EXISTS A DEPLOY NODE WITH THE SAME NAME
                    self.label_ErrorSaveDeploy.setText('Deploy not saved: already exists a deploy with the same name')
                    self.label_ErrorSaveDeploy.show()
                else:
                    self.label_ErrorSaveDeploy.setStyleSheet("""
                                                            font-family: "Lucida Console", "Courier New", monospace;
                                                            font-size: 15px;
                                                            color:green;
                                                            """)
                    self.label_ErrorSaveDeploy.setText('Deploy Saved')
                    self.label_ErrorSaveDeploy.show()

        except Exception as error:
            print(str(error))

    def saveDeployOnXml(self, dest_path, deploy_name, source_files_arr):
        try:
            # COLLECT ALL DEPLOYS ELEMENT OF XML
            tree = ElementTree()
            root = tree.parse("Deploys.xml")

            # CHECK IF ESISTE A DEPLOY NODE WITH SAME NAME
            check_exists = root.find('.//deploy[@name="'+ deploy_name + '"]')
            if check_exists != None:
                return 0

            # CREATE NEW DEPLOY ELEMENT OF XML
            deploys_node = root.find('.//deploys')
            new_deploy_node = ET.SubElement(deploys_node, 'deploy')
            new_deploy_node.text = 'New Data'
            new_deploy_node.set('name', deploy_name)

            prova = [elem.tag for elem in deploys_node.iter() if elem is not deploys_node]
            for pr in prova:
                print(str(pr))

            tree = ET.ElementTree(root)
            tree.write("Deploys.xml")


        except Exception as error:
            print("Error: " + str(error))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    ShowAddDeploy = AddDeployWindow()
    main.show()

    #BUTTON AddDeploy CLICK EVENT
    main.Btn_AddDeploy.clicked.connect(ShowAddDeploy.OPEN)




    sys.exit(app.exec_())