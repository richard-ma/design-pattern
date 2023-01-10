from businessservice import BusinessService


class EJBService(BusinessService):
    def do_processing(self):
        print("Processing task by invoking EJB Service")


if __name__ == "__main__":
    s = EJBService()
    s.do_processing()