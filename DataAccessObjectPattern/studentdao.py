import abc
from student import Student


class StudentDAO(abc.ABC):
    @abc.abstractmethod
    def get_all_students(self):
        pass

    @abc.abstractmethod
    def get_student(self, roll_no: int):
        pass

    @abc.abstractmethod
    def update_student(self, student: "Student"):
        pass

    @abc.abstractmethod
    def delete_student(self, student: "Student"):
        pass