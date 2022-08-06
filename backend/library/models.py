from django.db import models

from django.contrib.auth.models import User

class Library(models.Model):
    lid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library_name = models.CharField(max_length=200, blank=True, null=True)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = 'library'
        
    def __str__(self):
        return {
            'username': self.user.username,
            'library_name': self.library_name,
            'photo_url': self.photo_url,
            'longitude': self.longitude,
            'latitude': self.latitude,
        }
    
