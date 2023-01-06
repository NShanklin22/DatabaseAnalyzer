
# importing libraries
import random

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtTest
from PyQt5.QtCore import *
from verifyNames import *
from screeninfo import get_monitors
from loadDatabaseNames import *
from loadApprovedNames import *

import time

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.fname = ""
        self.Grade = 0

        ##############################
        ### Seting up the window #####
        ##############################
        # Determine the size of the PC window
        screen = get_monitors()[0]

        # Define the x and y size of the screen
        sizeX = int(screen.width/2)
        sizeY = int(screen.height/2)

        # Deine the location of the window so that it is at the center of the screen
        locX = int(sizeX/2)
        locY = int(sizeY/2)

        # Define the geometry of the window
        self.setGeometry(locX,locY,sizeX,sizeY)

        # Add a title
        self.setWindowTitle("SEBA+ Database Analyzer")

        ##############################
        ## Setting up the layout #####
        ##############################

        # Create a vertical layout
        mainLayout = QVBoxLayout()
        layout01 = QVBoxLayout()
        layout02 = QHBoxLayout()

        # Frame for app updates)
        my_frame01 = QFrame()
        my_frame01.setFrameShape(QFrame.StyledPanel)

        # FontSize stores the default font size for the window
        FontSize = 18
        LabelSeparation = int(FontSize * 2.0)

        # Label 01 uses QLabel and applies it to frame 01, the text can then be updated later
        self.Label01 = QLabel("Click Load Database and select an AS-P xml export", my_frame01)
        self.Label01.move(0,0)
        self.Label01.resize(sizeX,int(FontSize *2.0))
        self.Label01.setFont(QFont('Helveitca', 18))
        # Label 02
        self.Label02 = QLabel("", my_frame01)
        self.Label02.move(0,LabelSeparation)
        self.Label02.setFont(QFont('Helveitca', 18))
        self.Label02.resize(sizeX,int(FontSize *2.0))
        # Label 03
        self.Label03 = QLabel("", my_frame01)
        self.Label03.move(0,LabelSeparation * 2)
        self.Label03.resize(sizeX, int(FontSize * 2.0))
        self.Label03.setFont(QFont('Helveitca', 18))
        # Label 04
        self.Label04 = QLabel("", my_frame01)
        self.Label04.move(0,LabelSeparation * 3)
        self.Label04.resize(sizeX, int(FontSize * 2.0))
        self.Label04.setFont(QFont('Helveitca', 18))
        # Label 05
        self.Label05 = QLabel("", my_frame01)
        self.Label05.move(0,LabelSeparation * 4)
        self.Label05.resize(sizeX, int(FontSize * 2.0))
        self.Label05.setFont(QFont('Helveitca', 18))
        # Label 06
        self.Label06 = QLabel("", my_frame01)
        self.Label06.move(0,LabelSeparation * 5)
        self.Label06.resize(sizeX, int(FontSize * 2.0))
        self.Label06.setFont(QFont('Helveitca', 18))
        # Label 07
        self.Label07 = QLabel("", my_frame01)
        self.Label07.move(0,LabelSeparation * 6)
        self.Label07.resize(sizeX, int(FontSize * 2.0))
        self.Label07.setFont(QFont('Helveitca', 18))
        # Label 08
        self.Label08 = QLabel("", my_frame01)
        self.Label08.move(0,LabelSeparation * 8)
        self.Label08.resize(sizeX, int(FontSize * 3))
        self.Label08.setFont(QFont('Helveitca', 28))


        # Create a text box to add to frame01
        my_frame02 = QFrame()
        my_frame02.setFrameShape(QFrame.StyledPanel)

        # Add the progress bar
        self.progress_bar = QProgressBar(self)

        # Add the labels to the first layout
        layout01.addWidget(my_frame01)
        layout01.addWidget(self.progress_bar)


        # Add the two buttons to the second layout
        my_button01 = QPushButton("Load Database", clicked = self.getfile)
        my_button02 = QPushButton("Analyze Database", clicked = self.checkFileName)

        layout02.addWidget(my_button01)
        layout02.addWidget(my_button02)


        # Add layout01 and layout02 to mainLayout
        mainLayout.addLayout(layout01)
        mainLayout.addLayout(layout02)

        self.setLayout(mainLayout)

        self.show()

    # Function to open file dialog so user can select a file
    def getfile(self):
        fname,type = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "xml files (*.xml)")
        self.Label02.setText("File {} selected".format(fname))
        self.Label03.setText("")
        self.fname = fname

    def checkFileName(self):
        databaseFile = self.fname
        if(databaseFile == ""):
            self.Label03.setText("Error: Please select a file")
        else:
            self.Label03.setText("Process starting...")
            self.progress_bar.setValue(10)
            QtTest.QTest.qWait(random.randint(5, 15)*100)
            self.loadNames(databaseFile)

    def loadNames(self,databaseFile):
        self.Label04.setText("Loading object names from database...")
        databaseNames = loadDatabaseNames(databaseFile)
        self.progress_bar.setValue(25)
        QtTest.QTest.qWait(random.randint(5, 15) * 100)
        self.loadApprovedNames(databaseNames)

    def loadApprovedNames(self, databaseNames):
        self.Label05.setText("Importing list of approved names...")
        # Load the approved names
        approvedNames = loadApprovedNames()
        self.progress_bar.setValue(40)
        QtTest.QTest.qWait(random.randint(5, 15) * 100)
        self.getDatabaseGrade(databaseNames,approvedNames)

    def getDatabaseGrade(self,databaseNames, approvedNames):
        self.Label06.setText("Cross-referencing database names with approved names...")
        self.progress_bar.setValue(75)
        QtTest.QTest.qWait(random.randint(5, 15) * 100)
        self.Grade = analyzeDatabase(databaseNames, approvedNames)
        self.progressAnimation()
        self.Label07.setText("Analysis Complete")
        QtTest.QTest.qWait(500)
        self.Label08.setText("Total SEBA+ Name Score: {}%".format(self.Grade))

    # Function to display the progress animation once the database has been analyzed
    def progressAnimation(self):
        print("Nate!")
        # setting for loop to set value of progress bar
        for i in range(25):
            # slowing down the loop
            time.sleep(0.10)
            # setting value to progress bar
            self.progress_bar.setValue(i + 76)

app = QApplication([])
mw = MainWindow()

# Run the app
app.exec_()