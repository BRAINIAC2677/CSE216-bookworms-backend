from django.db import models


class Event(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = 'event'
    
    def __str__(self):
        return str({
            'eid': self.eid,
            'name': self.name,
            'text': self.text
        })