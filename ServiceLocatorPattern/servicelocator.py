from cache import Cache
from initialcontext import InitialContext


class ServiceLocator:
    cache = Cache()

    @staticmethod
    def get_service(jndi_name: str):
        service = ServiceLocator.cache.get_service(jndi_name)
        if service is not None:
            return service
        
        context = InitialContext()
        service1 = context.lookup(jndi_name)
        ServiceLocator.cache.add_service(service1)
        return service1