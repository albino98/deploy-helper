![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)


# deploy-helper


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

⚠️**Remember** to insert in "dist" folder the file "**splash.PNG**" (splash screen image) and file "**Deploys.xml**" with this content:
~~~ xml
<xml>
	<deploys>
	</deploys>
</xml>
~~~
