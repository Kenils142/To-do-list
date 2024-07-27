from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
from helpers.task_handler import del_task


class TaskWidget(QWidget):

    def __init__(self, id, name, description, end_date):
        super().__init__()

        self.id = id
        self.name = name
        self.description = description
        self.end_date = end_date

        # Widgets
        self.bodyWidget = QWidget()

        # Layouts
        mainLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()
        bodyLayout = QHBoxLayout()
        contentLayout = QVBoxLayout()
        buttonLayout = QVBoxLayout()

        # Labels
        nameLabel = QLabel(name)
        descriptionLabel = QLabel(f"Description: {description}")
        dateLabel = QLabel(f"End Date: {end_date}")

        # Widget settings
        self.bodyWidget.hide()

        # Buttons
        self.moreInfoButton = QPushButton("More")
        editButton = QPushButton("Edit")
        doneButton = QPushButton("Done")

        # Button settings
        self.moreInfoButton.setCheckable(True)
        self.moreInfoButton.clicked.connect(self.moreInfoClicked)
        editButton.clicked.connect(self.editButtonClicked)
        doneButton.clicked.connect(self.doneButtonClicked)

        # Adding widgets and layouts to respective layouts/Widgets
        headerLayout.addWidget(nameLabel)
        headerLayout.addWidget(self.moreInfoButton)
        contentLayout.addWidget(descriptionLabel)
        contentLayout.addWidget(dateLabel)
        buttonLayout.addWidget(editButton)
        buttonLayout.addWidget(doneButton)
        bodyLayout.addLayout(contentLayout)
        bodyLayout.addLayout(buttonLayout)
        self.bodyWidget.setLayout(bodyLayout)
        mainLayout.addLayout(headerLayout)
        mainLayout.addWidget(self.bodyWidget)
        self.setLayout(mainLayout)

    def moreInfoClicked(self, isChecked):
        if isChecked:
            self.moreInfoButton.setText("Less")
            self.bodyWidget.show()
        else:
            self.moreInfoButton.setText("More")
            self.bodyWidget.hide()

    def editButtonClicked(self):
        pass

    def doneButtonClicked(self):
        print(self.id, type(self.id))
        del_task(self.id)
        self.hide()
