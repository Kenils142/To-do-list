from helpers.form_dialog import FormDialog
from helpers.task_handler import add_task

class AddTaskDialog(FormDialog):

    def __init__(self):
        super().__init__()

        self.buttonBox.accepted.connect(self.addTask)

    def addTask(self):
        name = self.nameInput.text()

        if name != "":
            add_task(
                name, self.descriptionInput.toPlainText(),
                self.endDateInput.date().toString('yyyy-MM-dd')
            )
            self.accept()
