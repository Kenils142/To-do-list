from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QDialog, QLabel, QLineEdit, QTextEdit, QDateEdit, QFormLayout, QDialogButtonBox

from helpers.styles import dialog_styles


class FormDialog(QDialog):
    def __init__(self, name="", description="", end_date=QDate.currentDate()):
        super().__init__()

        # Dialog Frame Settings
        self.setWindowTitle("Form Dialog Template")
        self.setFixedSize(500, 250)
        self.setStyleSheet(dialog_styles)

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

        self.descriptionInput.setText("")
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
