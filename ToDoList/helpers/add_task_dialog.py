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
        self.setFixedSize(500, 250)
        self.setStyleSheet('''
            QDialog {
                background-color: #150226;
                font-family:"Avenir Next LT Pro"
            }
            
            QLabel{
                color: #FBC5FF;
                font-size: 18px;
                font-weight: bold;
                margin-right: 6px;
            }
                           
            QLineEdit, QTextEdit, QDateEdit{
                background-color: #F198FD;
                color: #150226;
                font-size: 16px;
                font-weight: bold;
            }
                           
            QLineEdit, QTextEdit {
                padding: 2px 4px;
                margin-bottom: 8px;
                border: 0px;
            }

            QDialogButtonBox {
                margin-top: 16px;
            }
                           
            QDialogButtonBox > * {
                background-color: #F198FD;
                color: #150226;
                font-size: 18px;
                font-weight: Bold;
                padding: 4px 8px;
                border-radius: 7.5px
            }        
            
            QDialogButtonBox > *:hover, QDialogButtonBox > *:focus{
                background-color: #E06AF9;
                border: 1px solid #FFF2FF;                       
            }
        ''')

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

        # Input Settings
        self.nameInput.setFocus()
        self.nameInput.setMaxLength(50)
        self.descriptionInput.setText("")
        self.descriptionInput.textChanged.connect(self.descriptionMaxLength)
        self.dateInput.setFixedWidth(150)
        self.dateInput.dateChanged.connect(self.minDate)

        # Button Settings
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




