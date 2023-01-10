from businessservice import BusinessService


class JMSService(BusinessService):
    def do_processing(self):
        print("Processing task by invoking JMS Service")


if __name__ == "__main__":
    s = JMSService()
    s.do_processing()