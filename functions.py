from PyQt5.QtWidgets import QListWidgetItem



def generateDeployListItems(ui):
    for i in range(10):
        item = QListWidgetItem("Item %i" % i)
        ui.listWidget_deploys.addItem(item)


