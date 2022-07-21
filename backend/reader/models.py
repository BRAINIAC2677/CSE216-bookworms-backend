from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo_url = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'reader'