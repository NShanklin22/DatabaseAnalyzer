
# importing libraries
import random

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtGui import *
from PyQt5 import QtTest
from PyQt5.QtCore import *
from verifyNames import *
from screeninfo import get_monitors
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from loadDatabaseNames import *
from loadApprovedNames import *
import pandas as pd
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

import time

current_file_path = os.getcwd()
path_to_exports = os.path.join(current_file_path, "exports")

screen = get_monitors()[0]

# Define the x and y size of the screen
sizeX = int(screen.width / 1.5)
sizeY = int(screen.height / 1.5)

# Deine the location of the window so that it is at the center of the screen
locX = int(sizeX / 2)
locY = int(sizeY / 2)

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
        ## Setting up the menubar ####
        ##############################


        ##############################
        ## Setting up the layout #####
        ##############################

        # Create a vertical layout
        mainLayout = QVBoxLayout()
        layout01 = QVBoxLayout()
        layout02 = QHBoxLayout()

        # Add the menu to the main layout

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
        # Label 09
        self.Label09 = QLabel("", my_frame01)
        self.Label09.move(0,LabelSeparation * 9)
        self.Label09.resize(sizeX, int(FontSize * 3))
        self.Label09.setFont(QFont('Helveitca', 28))

        # Add the progress bar
        self.progress_bar = QProgressBar(self)

        # Add the labels to the first layout
        layout01.addWidget(my_frame01)
        layout01.addWidget(self.progress_bar)

        # Add the two buttons to the second layout
        load_database_button = QPushButton("Load Database", clicked = self.getfile)
        results_button = QPushButton("View Results", clicked = self.GotoChartWindow)
        analyze_database_button = QPushButton("Analyze Database", clicked = self.checkFileName)

        layout02.addWidget(load_database_button)
        layout02.addWidget(results_button)
        layout02.addWidget(analyze_database_button)

        # Add layout01 and layout02 to mainLayout
        mainLayout.addLayout(layout01)
        mainLayout.addLayout(layout02)

        self.setLayout(mainLayout)

        self.show()

    # Function to open file dialog so user can select a file
    def getfile(self):
        self.clearStatusText()
        fname,type = QFileDialog.getOpenFileName(self, 'Open file',
                                            '{}'.format(path_to_exports), "xml files (*.xml)")
        if(fname == ""):
            return
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
            QtTest.QTest.qWait(random.randint(5, 50)*100)
            self.loadDatabaseNames(databaseFile)

    def loadDatabaseNames(self, databaseFile):
        randomDur = random.randint(20,50)

        self.Label04.setText("Loading object names from database...")
        databaseNames = loadDatabaseNames(databaseFile)
        print(databaseNames)
        self.progress_bar.setValue(randomDur/2)
        QtTest.QTest.qWait(randomDur * 10)
        self.loadApprovedNames(databaseNames)

    def loadApprovedNames(self, databaseNames):
        current_progress = self.progress_bar.value()
        randomDur = current_progress + random.randint(15,30)
        print(randomDur)
        self.Label05.setText("Importing list of approved names...")
        # Load the approved names
        approvedNames = loadApprovedNames()
        self.progress_bar.setValue(randomDur)
        QtTest.QTest.qWait(randomDur * 10)
        self.getDatabaseGrade(databaseNames,approvedNames)

    def getDatabaseGrade(self,databaseNames, approvedNames):
        self.Label06.setText("Cross-referencing database names with approved names...")
        self.progress_bar.setValue(75)
        QtTest.QTest.qWait(random.randint(5, 15) * 100)
        self.Grade,totalIncorrect,totalCorrect = analyzeDatabase(databaseNames, approvedNames)
        self.progressAnimation()
        self.Label07.setText("Analysis Complete - Sending data to database")
        QtTest.QTest.qWait(500)
        self.Label08.setText("Total Correct Names: {} Total Incorrect Names: {}".format(totalCorrect,totalIncorrect))
        self.Label09.setText("Total SEBA+ Name Score: {}%".format(self.Grade))
        self.fname = ""

    # Function to display the progress animation once the database has been analyzed
    def progressAnimation(self):
        print("Nate!")
        # setting for loop to set value of progress bar
        for i in range(25):
            # slowing down the loop
            time.sleep(0.10)
            # setting value to progress bar
            self.progress_bar.setValue(i + 76)

    # Clear the status window when called
    def clearStatusText(self):
        self.Label02.setText("")
        self.Label03.setText("")
        self.Label04.setText("")
        self.Label05.setText("")
        self.Label06.setText("")
        self.Label07.setText("")
        self.Label08.setText("")

    def open_new_window(self):
        # create the new window
        print("Here")
        self.new_window = QWidget()
        self.new_window.setWindowTitle("New Window")
        self.new_window.setGeometry(200, 200, 400, 300)
        print("Here")
        # create the layout for the new window
        new_layout = QVBoxLayout()
        label = QLabel("This is the new window!")
        new_layout.addWidget(label)
        print("Here")
        #set the l`ayout for the new window
        # new_widget = QWidget()
        # new_widget.setLayout(new_layout)
        # self.new_window.setCentralWidget(new_widget)
        print("Here")
        #show the new window
        self.new_window.show()

    def GotoChartWindow(self):
        widget.setCurrentIndex(1)  # Swap to Window2

class ChartWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Define the layout objects for the chart window
        mainLayout = QVBoxLayout()
        layout01 = QVBoxLayout()
        layout02 = QHBoxLayout()

        # Define the matplotlib chart
        self.canvas = FigureCanvas(Figure(figsize=(2, 1)))
        fig = self.canvas.figure
        self.createBarChart(fig)
        self.canvas.draw()

        # Create the button to go back
        self.button = QPushButton("Go Back")
        self.button.clicked.connect(self.GoBack)

        self.refresh = QPushButton("Refresh Chart")
        self.refresh.clicked.connect(self.update_chart)

        # Add the widget to the defined layout
        layout01.addWidget(self.canvas)
        layout02.addWidget(self.button)
        layout02.addWidget(self.refresh)
        mainLayout.addLayout(layout01)
        mainLayout.addLayout(layout02)
        self.setLayout(mainLayout)

    def createBarChart(self,fig):
        file = "data\incorrectNames.csv"
        df = pd.read_csv(file, header=None)# Get the top 10 items by value
        incorrectNamesData = df.value_counts().nlargest(10)
        labels = [x[0] for x in incorrectNamesData.index]
        fig.subplots_adjust(bottom=0.15)

        self.ax = fig.add_subplot(111)
        self.bars = self.ax.bar(labels,incorrectNamesData)
        self.ax.set_title("Most Common Incorrect Names", fontsize = 18)
        self.ax.set_xticklabels(labels, rotation = 25)
        self.ax.set_xlabel("Incorrect Name", fontsize = 18)
        self.ax.set_ylabel("# of Occurrences", fontsize = 18)


    def update_chart(self):
        file = "data\incorrectNames.csv"
        df = pd.read_csv(file, header=None)# Get the top 10 items by value
        new_y = df.value_counts().nlargest(10)
        new_labels = [x[0] for x in new_y.index]
        print("Nate")
        print(self.bars)
        for i, rect in enumerate(self.bars):
            rect.set_height(new_y[i])

        ax = self.bars[0].axes
        ax.set_xticklabels(new_labels, rotation=25)
        ax.set_ylim(0, new_y.max() + new_y.max()/10)
        self.canvas.draw()

    def GoBack(self):
        widget.setCurrentIndex(0)

app = QApplication([])
widget = QtWidgets.QStackedWidget()
mainWindow = MainWindow()
chartWindow = ChartWindow()
widget.addWidget(mainWindow)
widget.addWidget(chartWindow)
widget.setFixedHeight(sizeY)
widget.setFixedWidth(sizeX)
widget.setWindowTitle("SEBA+ Database Analyzer")
widget.show()

# Run the app
app.exec_()