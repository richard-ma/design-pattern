from studentdao import StudentDAO
from student import Student


class StudentDAOImpl(StudentDAO):
    def __init__(self):
        self._students = list()
        s1 = Student("Robert", 0)
        s2 = Student("John", 1)
        self._students.append(s1)
        self._students.append(s2)

    def delete_student(self, student: "Student"):
        for i in range(len(self._students)):
            if self._students[i].get_roll_no() == student.get_roll_no():
                self._students.pop(i) # remove index: i item
                break
        print("Student: Roll No", student.get_roll_no(), "deleted from database.")

    def get_all_students(self):
        return self._students

    def get_student(self, roll_no: int):
        for s in self._students:
            if s.get_roll_no() == roll_no:
                return s
        return None

    def update_student(self, student: "Student"):
        for s in self._students:
            if s.get_roll_no() == student.get_roll_no():
                s.set_name(student.get_name())
                print("Student: Roll No", student.get_roll_no(), "updated in the database.")


if __name__ == "__main__":
    impl = StudentDAOImpl()
    for s in impl.get_all_students():
        print(s.get_name())

    res = impl.get_student(0)
    if res:
        print(res.get_roll_no(), res.get_name())

    new = Student("Hello", 1)
    impl.update_student(new)
    res = impl.get_student(1)
    if res:
        print(res.get_roll_no(), res.get_name())

    impl.delete_student(new)
    res = impl.get_student(1)
    if res:
        print(res.get_roll_no(), res.get_name())
    else:
        print("No such student:", new.get_roll_no())