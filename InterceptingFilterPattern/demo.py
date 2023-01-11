from filtermanager import FilterManager
from target import Target
from client import Client
from authenticationfilter import AuthenticationFilter
from debugfilter import DebugFilter


if __name__ == "__main__":
    filter_manager = FilterManager(Target())
    filter_manager.set_filter(AuthenticationFilter())
    filter_manager.set_filter(DebugFilter())

    c = Client()
    c.set_fitler_manager(filter_manager)
    c.send_request("HOME")