from django.contrib.gis.db.models.functions import IsValid

from apps.api.serializers import *
from apps.api_v2serializers import *

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
            api = Apiv1()
            self.__data = api.get_serializer_class(type)
            return self.__data

        elif version == 'v2':
            api = Apiv2()
            self.__data =  api.get_serializer_class(type)        
            return self.__data
        else:
            """ Error vesion :( """
            return None

    
    def is_valid(self):
        """
            Validate Succes get Class Versicion APi
        """
        if self.__data is not None:
            return False
        else:
            return True

