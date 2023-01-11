from studentbo import StudentBO


if __name__ == "__main__":
    student_business_object = StudentBO()

    for s in student_business_object.get_all_students():
        print("Student: [ Roll No:", s.get_roll_no(), ", Name:", s.get_name(), "]")

    s = student_business_object.get_all_students()[0]
    s.set_name("Micheal")
    student_business_object.update_student(s)

    s = student_business_object.get_all_students()[0]
    print("Student: [ Roll No:", s.get_roll_no(), ", Name:", s.get_name(), "]")