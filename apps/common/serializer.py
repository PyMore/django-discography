from rest_framework import serializers

class ApiVersionSerializer(serializers.ModelSerializer):
    """
        This mixin only get the name serializer for api version
    """

    def __init__(self, *args, **kwargs):
        self._name = None
        super(serializers.ModelSerializer,self).__init__(*args, **kwargs)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value