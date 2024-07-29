from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton)
from PySide6.QtCore import QDate, Qt

from Stylesheets.tasks_styles import header_styles, body_styles
from CustomWidgets.dialogues import EditTaskDialog
from DataAccess.db_utils import del_task


class TaskWidget(QWidget):

    def __init__(self, id, name, description, end_date):
        super().__init__()

        self.id = id
        self.name = name
        self.description = description
        self.end_date = end_date

        # Containers
        self.headerContainer = QWidget()
        self.headerContainer.setStyleSheet(header_styles(False))
        self.bodyContainer = QWidget()

        # Layouts
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)

        headerLayout = QHBoxLayout()
        bodyLayout = QHBoxLayout()

        contentLayout = QVBoxLayout()
        contentLayout.setSpacing(15)
        buttonLayout = QVBoxLayout()
        buttonLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)
        buttonLayout.setSpacing(15)

        # Labels
        nameLabel = QLabel(name)

        descriptionLabel = QLabel(description.strip())
        descriptionLabel.setWordWrap(True)

        dateLabel = QLabel(f"<b>End Date:</b> {end_date}")

        # Widget settings
        self.bodyContainer.hide()

        # Buttons
        self.moreInfoButton = QPushButton("More")

        self.editButton = QPushButton("Edit")
        self.doneButton = QPushButton("Done")

        # Button settings
        self.moreInfoButton.setCheckable(True)
        self.moreInfoButton.clicked.connect(self.moreInfoClicked)
        self.moreInfoButton.setFixedWidth(60)

        self.editButton.clicked.connect(self.editButtonClicked)
        self.editButton.setFixedWidth(60)

        self.doneButton.clicked.connect(self.doneButtonClicked)
        self.doneButton.setFixedWidth(60)

        # Adding widgets and layouts to respective layouts/Widgets
        headerLayout.addWidget(nameLabel)
        headerLayout.addWidget(self.moreInfoButton)
        self.headerContainer.setLayout(headerLayout)

        contentLayout.addWidget(descriptionLabel)
        contentLayout.addWidget(dateLabel)

        buttonLayout.addWidget(self.editButton)
        buttonLayout.addWidget(self.doneButton)

        bodyLayout.addLayout(contentLayout)
        bodyLayout.addLayout(buttonLayout)

        self.bodyContainer.setLayout(bodyLayout)

        mainLayout.addWidget(self.headerContainer)
        mainLayout.addWidget(self.bodyContainer)

        self.setLayout(mainLayout)


    def moreInfoClicked(self, isChecked):
        if isChecked:
            self.headerContainer.setStyleSheet(header_styles(isChecked))
            self.bodyContainer.setStyleSheet(body_styles)
            self.moreInfoButton.setText("Less")
            self.bodyContainer.show()
        else:
            self.headerContainer.setStyleSheet(header_styles(isChecked))
            self.moreInfoButton.setText("More")
            self.bodyContainer.hide()


    def editButtonClicked(self):
        # converting end_date to QDate and checking if >= Current Date
        end_date = QDate.fromString(self.end_date, "yyyy-MM-dd")
        end_date = end_date if end_date >= QDate.currentDate() \
            else QDate.currentDate()

        dialog = EditTaskDialog(self.id, self.name, self.description,
                                end_date)
        dialog.exec()

    def doneButtonClicked(self):
        del_task(self.id)
