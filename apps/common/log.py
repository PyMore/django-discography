"""
    This a decorator for log request and response services 
"""
from .models import Log


def log(f):
    def acction(model,id,serializer,request,message):
        generateFile(request)
        return f(model,id,serializer,request,message)
    return acction


def generateFile(request):
    f = Log(
        path=request.path,
        headers=request.headers,
        data=request.data,
        body=request.body,
        method=request.method)
    f.save()
