from studentview import StudentView
from homeview import HomeView


class Dispatcher:
    def __init__(self):
        self._student_view = StudentView()
        self._home_view = HomeView()

    def dispatch(self, request: str):
        request = request.lower()

        if request == "student":
            self._student_view.show()
        else:
            self._home_view.show()