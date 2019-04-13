from django.db import models

# Create your models here.


class ArtistGroup(models.Model):
    """ Artist Group Model """

    name  = models.CharField(max_length=50,null=False)
    enable = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Album(models.Model):
    """ Artist Group Model """

    name  = models.CharField(max_length=50,null=False)
    artist = models.ForeignKey(ArtistGroup,
        on_delete=models.CASCADE, null=False,
        blank=False, db_column='artist')
    enable = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

