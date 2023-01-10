from frontcontroller import FrontController


if __name__ == "__main__":
    front_controller = FrontController()
    front_controller.dispatch_request('HOME')
    front_controller.dispatch_request('student')