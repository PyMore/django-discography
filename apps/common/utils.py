import requests


def requestJson(url):
    data = requests.get(url)
    print(data)
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



def serializer_error(self,serializer,data):
    pass