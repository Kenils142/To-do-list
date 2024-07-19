import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import QSize

fontFamily = "Avenir Next LT Pro"

class MainFrame(QMainWindow):

    def __init__(self):
        super(MainFrame, self).__init__()

        # Doing Setting for MainFrame
        self.setWindowTitle("To Do List")
        self.setFixedWidth(800)
        self.setMinimumHeight(500)

        # Empty widgets for controlling layouts properly for other widgets
        mainWidget = QWidget()
        headerWidget = QWidget()
        tasksWidget = QWidget()

        # Contains all the Layouts
        mainLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()
        tasksLayout = QVBoxLayout()

        # Settings for mainLayout
        mainLayout.setContentsMargins(0,0,0,0)

        # Settings for headerLayout
        headerLayout.setContentsMargins(20,0,20,0)

        # Operations for Header Widget
        headerWidget.setStyleSheet("background-color: #319B05")
        headerWidget.setFixedHeight(75)

        # Header Name Label
        nameLabel = QLabel("To Do List")
        nameLabel.setFont(QFont(fontFamily, 22, QFont.Bold))

        # Add Task Button
        addTaskButton = QPushButton(" + Add Task ")
        addTaskButton.setFixedSize(QSize(150, 50))
        addTaskButton.setFont(QFont(fontFamily, 18))
        addTaskButton.setStyleSheet(''' 
            QPushButton{
                border: 1px outline #297401;
                background-color: #204D00;
                border-radius: 7.5px;    
            }
            QPushButton:pressed{
                border: 1.5px inline #122600;
                background-color: #122600;
                border-radius: 7.5px;
            }
        ''')

        # Adding Widgets to headerLayout
        headerLayout.addWidget(nameLabel)
        headerLayout.addWidget(addTaskButton)

        # Stacking high level widgets and Layouts 
        headerWidget.setLayout(headerLayout)
        tasksWidget.setLayout(tasksLayout)
        mainLayout.addWidget(headerWidget)
        mainLayout.addWidget(tasksWidget)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

app = QApplication([])

window = MainFrame()
window.show()

sys.exit(app.exec())