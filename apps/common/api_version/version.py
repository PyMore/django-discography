from apps.api.serializers import *
from apps.api_v2.serializers import *

from .api_v1 import Apiv1
from .api_v2 import Apiv2


class FactoryVersion:
    """ Factorry Vesion Api control """
    
    def __init__(self,version,type):

        self.__data = None

        """
             get Class Versicion APi
        """

        if version == 'v1':
            """
                Here call api v2 class to get_serializer_class 
            """
            api = Apiv1()
            self.__data = api.get_serializer_class(type)            
        elif version == 'v2':
            """
                Here call api v2 class to get_serializer_class 
            """
            self.__data = None
        else:
            """ Error vesion :( """
            self.__data = None


    
    def is_valid(self):
        """
            Validate Succes get Class Versicion APi
        """

        if self.__data:
            return True
        else:
            return False


    @property
    def data(self):
        """
            Get data object serializer 
        """
        return self.__data
