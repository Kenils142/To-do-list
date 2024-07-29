from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import (QDialog, QLabel, QLineEdit,
                               QTextEdit, QDateEdit, QFormLayout,
                               QDialogButtonBox)

from Stylesheets.dialog_styles import style
from DataAccess.db_utils import add_task, edit_task


class FormDialog(QDialog):
    def __init__(self, name="", description="", end_date=QDate.currentDate()):
        super().__init__()

        # Dialog Frame Settings
        self.setWindowTitle("Form Dialog Template")
        self.setFixedSize(500, 250)
        self.setStyleSheet(style)

        # Layouts
        layout = QFormLayout(self)

        # Labels
        nameLabel = QLabel("Name")
        descriptionLabel = QLabel("Description")
        endDateLabel = QLabel("End Date")

        # Input fields
        self.nameInput = QLineEdit(name)
        self.descriptionInput = QTextEdit(description)
        self.endDateInput = QDateEdit(end_date)

        # Input field settings
        self.nameInput.setFocus()
        self.nameInput.setMaxLength(50)

        self.descriptionInput.textChanged.connect(self.descriptionMaxLength)

        self.endDateInput.dateChanged.connect(self.minEndDate)

        # Button Settings
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self
        )

        self.buttonBox.rejected.connect(self.reject)

        # Adding Widgets to Layout
        layout.addRow(nameLabel, self.nameInput)
        layout.addRow(descriptionLabel, self.descriptionInput)
        layout.addRow(endDateLabel, self.endDateInput)
        layout.addRow(self.buttonBox)

        self.setLayout(layout)

    def descriptionMaxLength(self):
        description = self.descriptionInput.toPlainText()

        if len(description) > 500:
            description = description[0:501]
            self.descriptionInput.setText(description)

    def minEndDate(self):
        if self.endDateInput.date() < QDate.currentDate():
            self.endDateInput.setDate(QDate.currentDate())


class AddTaskDialog(FormDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add Task")
        self.buttonBox.accepted.connect(self.addTask)

    def addTask(self):
        name = self.nameInput.text()

        if name != "":
            add_task(
                name, self.descriptionInput.toPlainText(),
                self.endDateInput.date().toString('yyyy-MM-dd')
            )
            self.accept()


class EditTaskDialog(FormDialog):
    def __init__(self, id, name, description, end_date):
        self.id = id
        super().__init__(name, description, end_date)

        self.setWindowTitle("Edit Task")

        self.buttonBox.accepted.connect(self.editTask)

    def editTask(self):
        name = self.nameInput.text()
        if name != "":
            edit_task(
                self.id, name, self.descriptionInput.toPlainText(),
                self.endDateInput.date().toString('yyyy-MM-dd')
            )
            self.accept()
