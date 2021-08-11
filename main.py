import time
from xml.etree.ElementTree import ElementTree

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen, QFileDialog, QListWidgetItem, QListWidget
from DeployHelper import Ui_DeployHelper
from AddDeploy import Ui_AddDeploy
import sys
from xml.etree import ElementTree as ET
import functions

# OPEN THE MAIN WINDOW
class Main(QMainWindow, Ui_DeployHelper):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.populateDeploysList(False)
        self.groupBox.hide()

        # POPULATE AND SHOW GROUPBOX WITH DEPLOY INFO WHEN A DEPLOY ITEM IS SELECTED
        self.listWidget_Deploys.itemClicked.connect(self.populateAndShowGroupBox)

        # BUTTON Btn_StartDeploy ACTION
        self.Btn_StartDeploy.clicked.connect(self.runDeploy)

        # HIDE label_ResultDeploy
        self.label_ResultDeploy.hide()

    # MAIN WINDOW close event. NOT RENAME (OVERRIDE)
    def closeEvent(self, event):
        can_exit = True
        if can_exit:
            self.lineEdit_DeployName.clear()
            self.lineEdit_DestPath.clear()
            self.textEdit_SourceFiles.clear()
            self.label_ResultDeploy.hide()
            self.groupBox.hide()
            event.accept()  # let the window close
        else:
            event.ignore()

    def populateDeploysList(self, updateList):
        if updateList:
            self.listWidget_Deploys.clear()
        # COLLECT ALL DEPLOYS NODES OF XML
        tree = ElementTree()
        root = tree.parse("Deploys.xml")
        # GET ALL NODE 'DEPLOY' OF XML
        allDeploys = root.findall('.//deploy')
        for node in allDeploys:
            deploy_name = node.get('name')
            newQListItem = QListWidgetItem()
            newQListItem.setText(deploy_name)
            self.listWidget_Deploys.addItem(newQListItem)

    def populateAndShowGroupBox(self):
        # GET THE NAME OF SELECTED DEPLOY
        selected_deploy = self.listWidget_Deploys.selectedItems()[0].text()
        # GET THE DEPLOY INFO
        deploy_info = self.getDeployInfoByName(selected_deploy)
        #print(str(deploy_info))

        # CLEAR GROUPBOX FIELDS
        self.lineEdit_DeployName.clear()
        self.textEdit_SourceFiles.clear()
        self.lineEdit_DestPath.clear()

        # POPULATE GROUP BOX FILEDS WITH DATA OF SELECTED DEPLOY
        self.lineEdit_DeployName.setText(deploy_info['name'])
        for source_file in deploy_info['source_files']:
            self.textEdit_SourceFiles.append(source_file)
        self.lineEdit_DestPath.setText(deploy_info['destination_path'])

        # SHOW GROUP BOX
        self.groupBox.show()

    def getDeployInfoByName(self, deploy_name):
        try:
            deploy_info = {"name": "", "source_files": [], "destination_path": "", 'name': deploy_name}
            # COLLECT ALL DEPLOYS NODES OF XML
            tree = ElementTree()
            root = tree.parse("Deploys.xml")

            # GET THE DEPLOY NODE BY NAME
            deploy_node = root.find('.//deploy[@name="' + deploy_name + '"]')
            if deploy_node is not None:
                source_files_nodes = deploy_node.findall('.//sourceFilePath')
                for source in source_files_nodes:
                    deploy_info['source_files'].append(source.text)

                destination_path_node = deploy_node.find('.//destinationPath')
                if destination_path_node is not None:
                    deploy_info['destination_path'] = destination_path_node.text

        except Exception as error:
            print(str(error))

        return deploy_info

    def runDeploy(self):
        #GET SELECTED DEPLOY
        selected_deploy = self.listWidget_Deploys.selectedItems()[0].text()
        deploy_info = self.getDeployInfoByName(selected_deploy)
        # RUN COPY FILES
        result = functions.copyFilesToDir(deploy_info['source_files'], deploy_info['destination_path'])
        self.showDeployResultMessage(result)

    def showDeployResultMessage(self, result):
        if result['error'] is True:
            # message for dark theme
            if self.Btn_ChangeTheme.text() == 'Light':
                self.label_ResultDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:#ff5900;
                                                        """)
            # message for light theme
            else:
                self.label_ResultDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:red;
                                                        """)
        else:
            # message for dark theme
            if self.Btn_ChangeTheme.text() == 'Light':
                self.label_ResultDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:#00ff00;
                                                        """)
            #message for light theme
            else:
                self.label_ResultDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:green;
                                                        """)
        self.label_ResultDeploy.setText(result['message'])
        self.label_ResultDeploy.show()

    def changeTheme(self):
        # SWITCH FROM DARK TO LIGHT
        if self.Btn_ChangeTheme.text() == 'Light':
            #region SWITCH MAIN WINDOW TO LIGHT
            self.label.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:black;
            ''')
            self.label_2.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:black;
            ''')
            self.label_3.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:black;
            ''')
            self.label_4.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:black;
            ''')
            self.listWidget_Deploys.setStyleSheet('''
                QListWidget {
                    border: 2px solid #0092d1;
                    /*border: 2px solid white;*/
                    border-radius: 5px;
                    padding: 0 8px;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                QListWidget::item:selected {
                    border : 0px solid black;
                    background : #0092d1;
                    /*background : #9ca2ad;*/
                    border-radius: 1px;
                    color:white;
                    font-family: "Lucida Console", "Courier New",monospace;
                }
                QListWidget::item {
                    border : 0px solid black;
                    font-family: "Lucida Console", "Courier New",monospace;
                    color:black;
                }
            ''')
            self.groupBox.setStyleSheet('''
                QGroupBox {
                    border: 2px solid #0092d1;
                    /*border: 2px solid white;*/
                    border-radius: 5px;
                    padding: 0 8px;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                    color:black;
                    font-size: 15px;
                }
            ''')
            self.lineEdit_DeployName.setStyleSheet('''
                border: 1px solid #0092d1;
                border-radius: 5px;
                padding: 0 8px;
                background: white;
                selection-background-color: darkgray;
                font-family: "Lucida Console", "Courier New", monospace;
                font-size: 14px;
            ''')
            self.textEdit_SourceFiles.setStyleSheet('''
                QTextEdit {
                    border: 1px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                    font-size: 14px;
                }
            ''')
            self.lineEdit_DestPath.setStyleSheet('''
                QLineEdit {
                    border: 1px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: #2c509e;
                    font-family: "Lucida Console", "Courier New", monospace;
                    font-size: 14px;
                }
            ''')
            self.setStyleSheet('')
            self.Btn_ChangeTheme.setText('Dark')
            #endregion
            #region SWITCH AddDeploy WINDOW TO LIGHT

            #endregion
        # SWITCH FROM LIGHT TO DARK
        else:
            #region SWITCH MAIN WINDOW TO DARK
            self.setStyleSheet('background-color:#364052;')
            self.label.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:white;
            ''')
            self.label_2.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:white;
            ''')
            self.label_3.setStyleSheet('''
                            font-family: "Lucida Console", "Courier New", monospace;
                            color:white;
                        ''')
            self.label_4.setStyleSheet('''
                            font-family: "Lucida Console", "Courier New", monospace;
                            color:white;
                        ''')
            self.listWidget_Deploys.setStyleSheet('''
                QListWidget {
                    /*border: 2px solid #0092d1;*/
                    border: 2px solid white;
                    border-radius: 5px;
                    padding: 0 8px;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                 QListWidget::item:selected {
                    border : 0px solid black;
                    background : #0092d1;
                    border-radius: 1px;
                    /*background : #9ca2ad;*/
                    color:white;
                    font-family: "Lucida Console", "Courier New",monospace;
                    }
                 QListWidget::item {
                    border : 0px solid black;
                    font-family: "Lucida Console", "Courier New",monospace;
                    color:white;
                }
            ''')
            self.lineEdit_DeployName.setStyleSheet('''
                /*border: 1px solid #0092d1;*/
                border: 0px solid #0092d1;
                border-radius: 5px;
                padding: 0 8px;
                background: white;
                selection-background-color: darkgray;
                font-family: "Lucida Console", "Courier New", monospace;
                font-size: 14px;
            ''')
            self.textEdit_SourceFiles.setStyleSheet('''
                QTextEdit {
                    /* border: 1px solid #0092d1;*/
                    border: 0px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                    font-size: 14px;
                }
            ''')
            self.lineEdit_DestPath.setStyleSheet('''
                QLineEdit {
                    /*border: 1px solid #0092d1;*/
                    border: 0px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: #2c509e;
                    font-family: "Lucida Console", "Courier New", monospace;
                    font-size: 14px;
                }
            ''')
            self.groupBox.setStyleSheet('''
                QGroupBox {
                    /* border: 2px solid #0092d1;*/
                    border: 2px solid white;
                    border-radius: 5px;
                    padding: 0 8px;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                    color:white;
                    font-size: 15px;
                }
            ''')
            self.Btn_ChangeTheme.setText('Light')
            # endregion


class AddDeployWindow(QMainWindow, Ui_AddDeploy):
    def __init__(self):
        super(AddDeployWindow, self).__init__()
        self.setupUi(self)

        # BUTTON Btn_SelectSourceFiles CLICK EVENT
        self.Btn_SelectSourceFiles.clicked.connect(self.selectSourceFiles)
        # BUTTON Btn_SelectDestinationPath CLICK EVENT
        self.Btn_SelectDestinationPath.clicked.connect(self.selectDestinationPath)
        # BUTTON Btn_SaveDeploy CLICK EVENT
        self.Btn_SaveDeploy.clicked.connect(self.saveDeployAction)
        # SET ERROR LABEL TO HIDDEN
        self.label_ErrorSaveDeploy.hide()


    def OPEN(self):
        if main.Btn_ChangeTheme.text() == 'Dark':
            #region SET LIGHT THEME TO AddDeploy WINDW
            self.label.setStyleSheet('font-family: "Lucida Console", "Courier New", monospace;')
            self.label_2.setStyleSheet('font-family: "Lucida Console", "Courier New", monospace;')
            self.label_3.setStyleSheet('font-family: "Lucida Console", "Courier New", monospace;')
            self.Btn_SelectSourceFiles.setStyleSheet('''
                QPushButton {
                    border: 1px solid #0092d1;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                    min-width: 80px;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                
                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                
                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }
                
                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }
            ''')
            self.Btn_SelectDestinationPath.setStyleSheet('''
                QPushButton {
                    border: 1px solid #0092d1;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                    min-width: 80px;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                
                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                
                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }
                
                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }
            ''')
            self.textEdit_SourceFiles.setStyleSheet('''
                QTextEdit {
                    border: 1px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.lineEdit_DestPath.setStyleSheet('''
                QLineEdit {
                    border: 1px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: #2c509e;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.lineEdit_DeployName.setStyleSheet('''
                QLineEdit {
                    border: 1px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.setStyleSheet('')
            #endregion
        else:
            # region SET DARK THEME TO AddDeploy WINDOW
            self.label.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:white;
            ''')
            self.label_2.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:white;
            ''')
            self.label_3.setStyleSheet('''
                font-family: "Lucida Console", "Courier New", monospace;
                color:white;
            ''')
            self.Btn_SelectSourceFiles.setStyleSheet('''
                QPushButton {
                    border: 0px solid #0092d1;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                    min-width: 80px;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                
                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                
                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }
                
                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }
            ''')
            self.Btn_SelectDestinationPath.setStyleSheet('''
                QPushButton {
                    border: 0px solid #0092d1;
                    border-radius: 6px;
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #f6f7fa, stop: 1 #dadbde);
                    min-width: 80px;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
                
                QPushButton:pressed {
                    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                      stop: 0 #dadbde, stop: 1 #f6f7fa);
                }
                
                QPushButton:flat {
                    border: none; /* no border for a flat push button */
                }
                
                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }
            ''')
            self.textEdit_SourceFiles.setStyleSheet('''
                QTextEdit {
                    border: 0px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: darkgray;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.lineEdit_DestPath.setStyleSheet('''
                QLineEdit {
                    border: 0px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: #2c509e;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.lineEdit_DeployName.setStyleSheet('''
                QLineEdit {
                    border: 0px solid #0092d1;
                    border-radius: 5px;
                    padding: 0 8px;
                    background: white;
                    selection-background-color: #2c509e;
                    font-family: "Lucida Console", "Courier New", monospace;
                }
            ''')
            self.setStyleSheet('background-color:#364052;')
            #endregion
        main.close()
        self.show()

    # AddDploy Close event. NOT RENAME (OVERRIDE)
    def closeEvent(self, event):
        can_exit = True
        if can_exit:
            self.textEdit_SourceFiles.clear()
            self.lineEdit_DestPath.clear()
            self.lineEdit_DeployName.clear()
            self.label_ErrorSaveDeploy.hide()
            main.populateDeploysList(True)
            main.show()
            event.accept()  # let the window close
        else:
            event.ignore()

    # OPEN THE FILE EXPLORER TO SELECT SOURCE FILES
    def selectSourceFiles(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(None, "Select Files", "", "All Files (*);;Python Files (*.py)",
                                                     options=options)
        # self.textEdit_SourceFiles.setText(fileName)
        # print(file_names)
        for file in file_names:
            self.textEdit_SourceFiles.append(file)

    # OPEN THE FILE EXPLORER TO SELECT THE DESTINATION PATH
    def selectDestinationPath(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
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
                self.showErrorMessage(True, 'Please fill in all fields')
            else:
                self.label_ErrorSaveDeploy.hide()
                saveResult = self.saveDeployOnXml(dest_path, deploy_name, source_files_arr)

                if saveResult == 0:  # ERROR 0: ALREADY EXISTS A DEPLOY NODE WITH THE SAME NAME
                    self.showErrorMessage(True, 'Deploy not saved: already exists a deploy with the same name')
                else:
                    self.showErrorMessage(False, 'Deploy Saved')

        except Exception as error:
            print(str(error))

    def showErrorMessage(self, error, message):
        if error:
            # message for dark theme
            if main.Btn_ChangeTheme.text() == 'Light':
                self.label_ErrorSaveDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:#ff5900;
                                                        """)
            # message for light theme
            else:
                self.label_ErrorSaveDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:red;
                                                        """)
        else:
            # message for dark theme
            if main.Btn_ChangeTheme.text() == 'Light':
                self.label_ErrorSaveDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:#00ff00;
                                                           """)
            # message for light theme
            else:
                self.label_ErrorSaveDeploy.setStyleSheet("""
                                                        font-family: "Lucida Console", "Courier New", monospace;
                                                        font-size: 15px;
                                                        color:green;
                                                           """)
        self.label_ErrorSaveDeploy.setText(message)
        self.label_ErrorSaveDeploy.show()

    def saveDeployOnXml(self, dest_path, deploy_name, source_files_arr):
        try:
            # COLLECT ALL DEPLOYS ELEMENT OF XML
            tree = ElementTree()
            root = tree.parse("Deploys.xml")

            # CHECK IF EXISTS A DEPLOY NODE WITH SAME NAME
            check_exists = root.find('.//deploy[@name="' + deploy_name + '"]')
            if check_exists != None:
                return 0

            # CREATE NEW DEPLOY ELEMENT OF XML
            deploys_node = root.find('.//deploys')  # FIND THE NODE NAMED 'deploys'
            new_deploy_node = ET.SubElement(deploys_node, 'deploy')
            new_deploy_node.set('name', deploy_name)

            '''
            prova = [elem.tag for elem in deploys_node.iter() if elem is not deploys_node]
            for pr in prova:
                print(str(pr))
            '''
            # ADD SOURCE PATH FILES SUB-NODES TO THE NEW DEPLOY NODE
            for path in source_files_arr:
                path_node = ET.SubElement(new_deploy_node, 'sourceFilePath')
                path_node.text = path

            # ADD DESTINATION PATH SUB-NODE TO THE NEW DEPLOY NODE
            destPath_node = ET.SubElement(new_deploy_node, 'destinationPath')
            destPath_node.text = dest_path



            # SAVE XML
            tree = ET.ElementTree(root)
            tree.write("Deploys.xml")


        except Exception as error:
            print("Error: " + str(error))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # start splash screen
    pixmap = QPixmap("splash.png")
    splash = QSplashScreen(pixmap)
    splash.show()
    # end splash screen

    main = Main()
    ShowAddDeploy = AddDeployWindow()  #prepare main window

    time.sleep(5)  # wait 5 seconds before close splash screen
    splash.close()
    main.show()

    # BUTTON AddDeploy CLICK EVENT
    main.Btn_AddDeploy.clicked.connect(ShowAddDeploy.OPEN)
    # BUTTON Btn_ChangeTheme CLICK EVENT
    main.Btn_ChangeTheme.clicked.connect(main.changeTheme)
    #print(PyQt5.QtWidgets.QStyleFactory.keys())
    app.setStyle('Fusion')
    sys.exit(app.exec_())
