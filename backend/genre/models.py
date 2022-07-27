from django.db import models

# Create your models here.

class Genre(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name