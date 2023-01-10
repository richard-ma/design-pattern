class StudentView:
    def print_student_details(self, student_name: str, student_no: str):
        print("Student:")
        print("name:", student_name)
        print("Roll NO:", student_no)


if __name__ == "__main__":
    sv = StudentView()
    sv.print_student_details("name", "33")