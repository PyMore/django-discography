from rest_framework.response import Response as DRFResponse
from rest_framework.status import is_client_error
from rest_framework import  status as statusCode

class Response(DRFResponse):
    """Response"""

    def __init__(self, *args, **kwargs):
        self.__get_error(kwargs)
        super(self.__class__, self).__init__(*args, **kwargs)

    def __get_error(self, kwargs):
        if not is_client_error(kwargs['status']):
            items = kwargs.get('data', {})
            status = kwargs.get('status', '')
            
            kwargs['data'] = {
                'code': status,
                'msj': items,
                'extra': 'success'
            }
        
        else:
            items = kwargs.get('data', {}).items()
            print(statusCode)
            for k, v in items:
                kwargs['data'] = {
                    'code': int(v[1]) if len(v) == 2
                        else statusCode.HTTP_400_BAD_REQUEST,
                    'msj': "Error",    
                    'extra': k, 
                }
        
        