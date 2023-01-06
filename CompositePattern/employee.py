class Employee:
    def __init__(self, name: str, dept: str, sal: int):
        self._name = name
        self._dept = dept
        self._salary = sal
        self._subordinates = list()

    def add(self, e: "Employee"):
        self._subordinates.append(e)

    def remove(self, e: "Employee"):
        for employee in self._subordinates:
            if employee == e:
                del employee

    def get_subordinates(self):
        return self._subordinates

    def __str__(self):
        return ' '.join([
            "Employee: [ Name:",
            self._name,
            ", dept:",
            self._dept,
            ", salary:",
            str(self._salary),
            "]"
        ])


if __name__ == "__main__":
    CEO = Employee('John', 'CEO', 30000)
    headsales = Employee("Michel", "Head Sales", 20000)
    headmarketing = Employee("Robert", "Head Marketing", 20000)
    clerk1 = Employee("Laura","Marketing", 10000)
    clerk2 = Employee("Bob","Marketing", 10000)
    salesexecutive1 = Employee("Richard","Sales", 10000)
    salesexecutive2 = Employee("Rob","Sales", 10000)

    CEO.add(headsales)
    CEO.add(headmarketing)
 
    headsales.add(salesexecutive1)
    headsales.add(salesexecutive2)
 
    headmarketing.add(clerk1)
    headmarketing.add(clerk2)

    print(CEO)
    for head_employee in CEO.get_subordinates():
        print(head_employee)
        for employee in head_employee.get_subordinates():
            print(employee)