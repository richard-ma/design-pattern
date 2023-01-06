class Person:
    def __init__(self, name: str, gender: str, marital_statue: str):
        self._name = name
        self._gender = gender
        self._marital_status = marital_statue

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_marital_status(self):
        return self._marital_status


if __name__ == "__main__":
    person = Person("John", "Male", "Married")
    print(person.get_name())
    print(person.get_gender())
    print(person.get_marital_status())