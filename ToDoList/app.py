import sys
from datetime import datetime
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QVBoxLayout, QHBoxLayout, QScrollArea,
                               QLabel, QPushButton)

from Stylesheets.mainframe_styles import title_bar_styles
from CustomWidgets.dialogues import AddTaskDialog
from CustomWidgets.task_widget import TaskWidget
from DataAccess.db_utils import get_tasks


def parse_date(date_str):
    dateObj = datetime.strptime(date_str, '%Y-%m-%d')
    return dateObj.date()


class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()

        # Frame Settings
        self.setWindowTitle('ToDo List')
        self.setFixedWidth(800)
        self.setMinimumHeight(500)

        # Containers
        appContainer = QWidget()

        titleBarContainer = QWidget()
        titleBarContainer.setFixedHeight(75)
        titleBarContainer.setStyleSheet(title_bar_styles)

        tasksScrollAreaContainer = QScrollArea()
        tasksScrollAreaContainer.setWidgetResizable(True)
        tasksScrollAreaContainer.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        tasksScrollAreaContainer.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        tasksContainer = QWidget()

        # Layouts
        appContainerLayout = QVBoxLayout()
        appContainerLayout.setContentsMargins(0, 0, 0, 0)
        appContainerLayout.setSpacing(0)

        titleContainerLayout = QHBoxLayout()
        titleContainerLayout.setContentsMargins(20, 0, 20, 0)

        self.tasksContainerLayout = QVBoxLayout()
        self.tasksContainerLayout.setContentsMargins(20, 20, 20, 20)
        self.tasksContainerLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Title Contents
        title = QLabel("To Do List")

        addTaskButton = QPushButton(" + Add Task ")
        addTaskButton.clicked.connect(self.addTaskClicked)

        # Adding tasks to tasksContainer
        self.refreshTasksContainer()

        # Setting Widget/Layout Hierarchy
        titleContainerLayout.addWidget(title)
        titleContainerLayout.addWidget(addTaskButton)

        titleBarContainer.setLayout(titleContainerLayout)

        tasksContainer.setLayout(self.tasksContainerLayout)

        tasksScrollAreaContainer.setWidget(tasksContainer)

        appContainerLayout.addWidget(titleBarContainer)
        appContainerLayout.addWidget(tasksScrollAreaContainer)

        appContainer.setLayout(appContainerLayout)

        self.setCentralWidget(appContainer)

    def addTaskClicked(self):
        dialog = AddTaskDialog()
        dialog.exec()

        self.refreshTasksContainer()

    def refreshTasksContainer(self):
        # removing old tasks from layout
        for i in reversed(range(self.tasksContainerLayout.count())):
            self.tasksContainerLayout.itemAt(i).widget().setParent(None)

        tasks = get_tasks()

        sorted_tasks = sorted(tasks, key=lambda x: parse_date(x[-1]))

        for task in sorted_tasks:
            taskWidget = TaskWidget(task[0], task[1], task[2], task[3])
            self.tasksContainerLayout.addWidget(taskWidget)

            taskWidget.editButton.clicked.connect(self.refreshTasksContainer)
            taskWidget.doneButton.clicked.connect(self.refreshTasksContainer)


app = QApplication()

window = MainFrame()
window.show()

sys.exit(app.exec())
