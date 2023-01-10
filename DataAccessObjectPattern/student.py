class Student:
    def __init__(self, name: str, roll_no: int):
        self._roll_no = roll_no
        self._name = name

    def get_roll_no(self):
        return self._roll_no

    def set_roll_no(self, roll_no: str):
        self._roll_no = roll_no

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name


if __name__ == "__main__":
    s = Student()
    s.set_roll_no("33")
    s.set_name("name")
    print(s.get_roll_no())
    print(s.get_name())