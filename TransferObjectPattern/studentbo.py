from studentvo import StudentVO


class StudentBO:
    def __init__(self):
        self._students = list()
        s1 = StudentVO("Robert", 0)
        s2 = StudentVO("John", 1)
        self._students.append(s1)
        self._students.append(s2)

    def delete_student(self, student: "StudentVO"):
        for i in range(len(self._students)):
            if self._students[i].get_roll_no() == student.get_roll_no():
                self._students.pop(i)
                print("Student: Roll No", student.get_roll_no(), "deleted from database")
    
    def get_all_students(self):
        return self._students

    def get_student(self, roll_no: int):
        for s in self._students:
            if s.get_roll_no() == roll_no:
                return s

        return None

    def update_student(self, student: "StudentVO"):
        for s in self._students:
            if s.get_roll_no() == student.get_roll_no():
                s.set_name(student.get_name())
                print("Student: Roll No", student.get_roll_no(), "updated in the database")