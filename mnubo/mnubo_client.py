
from services import EventServices
from services import OwnerServices
from services import ObjectServices
from api_manager import APIManager

class MnuboClient(object):

    def __init__(self, client_id, client_secret, hostname):
        self.__auth_manager = APIManager(client_id, client_secret, hostname)
        self.owner_services = OwnerServices(self.__auth_manager)
        self.event_services = EventServices(self.__auth_manager)
        self.smart_object_services = ObjectServices(self.__auth_manager)
