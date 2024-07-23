from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QTextEdit, QDateEdit, QFormLayout, QDialogButtonBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize, Qt, QDate
from datetime import date
from helpers.task_handler import add_task

class AddTaskDialog(QDialog):

    def __init__(self):
        super(AddTaskDialog, self).__init__()

        # Settings for Dialog Frame
        self.setWindowTitle("Add Task")
        self.setFixedSize(600, 300)

        # Layouts
        formLayout = QFormLayout(self)

        # Labels for Form
        nameLabel = QLabel("Name")
        descriptionLabel = QLabel("Description")
        dateLabel = QLabel("End Date")

        # Input fields for form
        self.nameInput = QLineEdit()
        self.descriptionInput = QTextEdit()
        self.dateInput = QDateEdit(QDate.currentDate())

        # Name Input Settings
        self.nameInput.setMaxLength(50)
        self.descriptionInput.setText("")
        self.descriptionInput.textChanged.connect(self.descriptionMaxLength)
        self.dateInput.dateChanged.connect(self.minDate)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttonBox.accepted.connect(self.addTask)
        buttonBox.rejected.connect(self.reject)

        formLayout.addRow(nameLabel, self.nameInput)
        formLayout.addRow(descriptionLabel, self.descriptionInput)
        formLayout.addRow(dateLabel, self.dateInput)
        formLayout.addRow(buttonBox)

    def addTask(self):
        if self.nameInput.text() != "" and self.descriptionInput.toPlainText() != None:
            add_task(self.nameInput.text(), self.descriptionInput.toPlainText(), self.dateInput.date().toString('yyyy-MM-dd'))
            self.accept()
    
    def descriptionMaxLength(self):
        if len(self.descriptionInput.toPlainText()) >= 500:
            self.descriptionInput.setText(self.descriptionInput.toPlainText()[:501])
    
    def minDate(self):
        if self.dateInput.date() < QDate.currentDate():
            self.dateInput.setDate(QDate.currentDate())




