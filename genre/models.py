from django.db import models

class Genre(models.Model):
    gid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    class Meta:
        db_table = 'genre'
        
    def __str__(self):
        return self.name
    