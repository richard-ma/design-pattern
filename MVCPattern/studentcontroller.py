from student import Student
from studentview import StudentView


class StudentController:
    def __init__(self, model: "Student", view: "StudentView"):
        self._model = model
        self._view = view

    def set_student_name(self, name: str):
        self._model.set_name(name)

    def get_stduent_name(self):
        return self._model.get_name()

    def set_student_roll_no(self, roll_no: str):
        self._model.set_roll_no(roll_no)

    def get_stduent_roll_no(self):
        return self._model.get_roll_no()

    def update_view(self):
        self._view.print_student_details(
            self._model.get_name(), 
            self._model.get_roll_no()
        )


if __name__ == "__main__":
    def retrieve_student_from_database():
        s = Student()
        s.set_name("Robert")
        s.set_roll_no("10")
        return s

    model = retrieve_student_from_database()
    view = StudentView()
    controller = StudentController(model, view)
    controller.update_view()

    controller.set_student_name("John")
    controller.update_view()