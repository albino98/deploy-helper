![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

<p align="center">
  <img width="330" alt="splash" src="https://user-images.githubusercontent.com/63566699/129186287-21aba19f-df0a-4b17-a82b-336b3330ef3b.PNG">
</p>

# Deploy-Helper

## Description

**Deploy Helper** is designed to help developers during application releases. Many times to create the release package to be copied to the servers, it is necessary to copy many files (compiled project files such as .dll, etc.) which can be located on various different locations and this can be time consuming.

So, the idea was born to solve this problem, creating a software where you can **extensively configure and save your deployments** (in an xml file) **and execute them at any time with just one click.** For now the software allows the creation, saving and execution of the deploy (copy of the files) but the next functions in addition to the modification and deletion of the deployments will be more advanced such as linking documents to deployments, scheduling of deployments, execution of other custom tasks related to deployment (such as query on the db), etc.

#### Dark Theme:


![image](https://user-images.githubusercontent.com/63566699/129180544-814935b7-572f-4e73-a973-9acbad2b1a6e.png)


![image](https://user-images.githubusercontent.com/63566699/129180604-cb622a07-41e4-4036-834c-dd0d8efb6438.png)


#### Light Theme:


![image](https://user-images.githubusercontent.com/63566699/129180682-04adf6b1-1ddc-42a7-add2-96af3e2f523f.png)


![image](https://user-images.githubusercontent.com/63566699/129180751-1866e58a-891d-474b-9339-e57a8220cd16.png)


### To-Do:


✔️	 Deploy saving

✔️	 Deploy execution

✔️	 Dark and light themes

❌	Functionality to modify the deploy

❌	Functionality to delete the deploy

❌	Progress bar for large files

❌	Linking of documents to deploys

❌	Adding other customs tasks to execute during deployment


## How to Use

If you want to **try the software** and you are using Windows, just download the 'dist' folder and run main.exe.

If you want to **download and modify the project**, fork this repository and follow the instructions below for the configuration.


## Configuration and Requirements

- Python 3.x and pyqt5 are required to run the project.

- To install PyQt5, PyQt5-tools, QtDesigner and PyUIC you can see this tutorial: https://pythonpyqt.com/how-to-install-pyqt5-in-pycharm/

:warning: **Note** that the path of the qt designer can be very different so you will have to be patient to find it. In my case the path was this: C:\Users\*MyUser*\AppData\Roaming\Python\Python39\site-packages\qt5_applications\Qt\designer.exe

## Build (.exe)

To build the project as single .exe file you can use [PyInstaller](http://www.pyinstaller.org/). 

Intall it with: **pip install pyinstaller**
  
To start compiling the project in a single .exe file use the following command: **pyinstaller.exe --onefile --windowed main.py**

:warning: **Note:** If you get the following error: **"C:\Users\username>pyinstaller 'pyinstaller' is not recognized as an internal or external command, operable program or batch file."**:

- Find the path of pyinstaller.exe, in my case it's: **"C:\Users\<user>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts\pyinstaller.exe"** (search it in all disk), copy pyinstaller.exe in the root directory of the project:

![image](https://user-images.githubusercontent.com/63566699/129062713-b24f92bc-5167-4c0e-9f53-3f9774a50064.png)

- Then in the terminal move to the root path of the project ( "C:\Users\<user>\Desktop\DeployHelper" ) and execute command: "**.\pyinstaller.exe --onefile --windowed main.py**". the characters "**.\\**" are used to make trusted the pyinstaller.exe.

Now you should have "build" and "dist" folder. In "dist" folder you have main.exe.

⚠️**Remember** to have in "dist" folder the file "**splash.PNG**" (splash screen image) and file "**Deploys.xml**" with this content:
~~~ xml
<xml>
	<deploys>
	</deploys>
</xml>
~~~

## License 

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


License: [MIT](https://github.com/albino98/deploy-helper/blob/main/LICENSE)
