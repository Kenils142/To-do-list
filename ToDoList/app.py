import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize
from helpers.task_handler import get_tasks
from helpers.add_task_dialog import AddTaskDialog
from helpers.task_widget import TaskWidget

fontFamily = "Avenir Next LT Pro"

class MainFrame(QMainWindow):

    def __init__(self):
        super(MainFrame, self).__init__()

        # Settings for MainFrame
        self.setWindowTitle("To Do List")
        self.setFixedWidth(800)
        self.setMinimumHeight(500)

        # Empty widgets for controlling layout
        mainWidget = QWidget()
        headerWidget = QWidget()
        taskContainer = QWidget()

        # Layouts
        mainLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()
        self.tasksLayout = QVBoxLayout()

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
                border:0;
                background-color: #204D00;
                border-radius: 7.5px;    
            }
            
            QPushButton:hover{
                background-color: #122600;
                border-radius: 7.5px;
            }
        ''')
        addTaskButton.clicked.connect(self.add_task_clicked)

        # Displaying tasks
        self.refresh()

        # Adding Widgets to headerLayout
        headerLayout.addWidget(nameLabel)
        headerLayout.addWidget(addTaskButton)

        # Stacking high level widgets and Layouts 
        headerWidget.setLayout(headerLayout)
        taskContainer.setLayout(self.tasksLayout)
        mainLayout.addWidget(headerWidget)
        mainLayout.addWidget(taskContainer)
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)


    def refresh(self):
        for i in reversed(range(self.tasksLayout.count())):
            self.tasksLayout.itemAt(i).widget().setParent(None)
        tasks = get_tasks()
        for task in tasks:
            print(task)
            task_widget = TaskWidget(task[0], task[1], task[2], task[3])
            self.tasksLayout.addWidget(task_widget)


    def add_task_clicked(self):
        dlg = AddTaskDialog()
        dlg.exec()
        self.refresh()

app = QApplication([])

window = MainFrame()
window.show()

sys.exit(app.exec())