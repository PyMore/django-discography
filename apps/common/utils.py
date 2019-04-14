import requests
from rest_framework import generics, status

#from apps.common.api_version.version import FactoryVersion

from .api_version.api_name import SerializersListApv1
from .log import log
from .response import Response


def requestJson(url):
    data = requests.get(url)
    if data.status_code == requests.codes.ok:
        return data._content
    else:
        return {
            'error': 'error conection'
        }


def get_object_or_none(model, *args, **kwargs):
    """Get object or none"""
    try:
        obj = model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        obj = None
    return obj


def api_version(vesion,serializer,serializerDefautl):
    if self.request.version == 'v1':
        pass


@log
def serializer_data(model,id,serializer,request,message):
    data = get_object_or_none(model,pk=id)

    """
    Here api version logical 
    version = FactoryVersion(request.version,'').is_valid()
    if verion.is_valid():
        pass
    else:
        pass
    """

    if not data:
        return Response (data=message,
            status=status.HTTP_400_BAD_REQUEST)

    serializer = serializer(data,
        context={'request':request}, many=False)
    return Response(data=serializer.data, status=status.HTTP_200_OK)



def serializer_data_create(model,id,serializer,isPartial,request,message):
    """ Serializer Data Create """

    data = get_object_or_none(model, pk=id)


    """
    Here api version logical 
    version = FactoryVersion(request.version,'').is_valid()
    if verion.is_valid():
        pass
    else:
        pass
    """

    
    if not data:
        return Response (data=message,
            status=status.HTTP_400_BAD_REQUEST)

    serializer = serializer(data,
        data=request.data,
        partial=isPartial
    )
    
    if not serializer.is_valid():
        return Response(data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(data='update', status=status.HTTP_200_OK)    