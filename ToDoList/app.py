import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton)

from Stylesheets.mainframe_styles import header_styles
from CustomWidgets.dialogues import AddTaskDialog
from CustomWidgets.task_widget import TaskWidget
from DataAccess.db_utils import get_tasks



class MainFrame(QMainWindow):
    def __init__(self):
        super(MainFrame, self).__init__()

        # Mainframe Settings
        self.setWindowTitle("To Do List")
        self.setFixedWidth(800)
        self.setMinimumHeight(500)

        # Containers
        mainContainer = QWidget()
        headerContainer = QWidget()
        taskContainer = QWidget()

        # Layouts
        mainContainerLayout = QVBoxLayout()
        headerContainerLayout = QHBoxLayout()
        self.taskContainerLayout = QVBoxLayout()

        # Container settings
        headerContainer.setStyleSheet(header_styles)

        # Layout settings
        mainContainerLayout.setContentsMargins(0, 0, 0, 0)
        headerContainer.setContentsMargins(20, 0, 20, 0)

        # Header Container Contents
        headerLabel = QLabel("To Do List")
        headerLabel.setStyleSheet(header_styles)
        addTaskButton = QPushButton(" + Add Task ")
        addTaskButton.clicked.connect(self.addTaskClicked)
        addTaskButton.setStyleSheet(header_styles)

        # Task Container Contents
        self.refreshTasks()

        # Adding/Setting widgets/layouts into each other
        headerContainerLayout.addWidget(headerLabel)
        headerContainerLayout.addWidget(addTaskButton)
        headerContainer.setLayout(headerContainerLayout)

        taskContainer.setLayout(self.taskContainerLayout)

        mainContainerLayout.addWidget(headerContainer)
        mainContainerLayout.addWidget(taskContainer)
        mainContainer.setLayout(mainContainerLayout)

        self.setCentralWidget(mainContainer)


    def refreshTasks(self):
        # removing old tasks from layout
        for i in reversed(range(self.taskContainerLayout.count())):
            self.taskContainerLayout.itemAt(i).widget().setParent(None)

        tasks = get_tasks()

        for task in tasks:
            taskWidget = TaskWidget(task[0], task[1], task[2], task[3])
            self.taskContainerLayout.addWidget(taskWidget)

            taskWidget.editButton.clicked.connect(self.refreshTasks)
            taskWidget.doneButton.clicked.connect(self.refreshTasks)


    def addTaskClicked(self):
        dialog = AddTaskDialog()
        dialog.exec()

        self.refreshTasks()


app = QApplication()

window = MainFrame()
window.show()

sys.exit(app.exec())
