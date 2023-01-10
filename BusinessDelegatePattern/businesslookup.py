from ejbservice import EJBService
from jmsservice import JMSService


class BusinessLookUp:
    def get_business_service(self, service_type: str):
        service_type = service_type.lower()

        if service_type == 'ejb':
            return EJBService()
        else:
            return JMSService()


if __name__ == "__main__":
    lookup = BusinessLookUp()
    service = lookup.get_business_service('ejb')
    service.do_processing()
    service = lookup.get_business_service('jms')
    service.do_processing()
    service = lookup.get_business_service('other')
    service.do_processing()