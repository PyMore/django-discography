from django.db import models

# Create your models here.

class Log(models.Model):
    """ Log Services """
    path  = models.CharField(max_length=200,null=False)
    headers  = models.CharField(max_length=400,null=False)
    data  = models.CharField(max_length=400,null=False)
    body  = models.CharField(max_length=400,null=False)
    method = models.CharField(max_length=100,null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.path

