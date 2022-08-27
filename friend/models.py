from django.db import models

from reader.models import Reader 

class Friend(models.Model):
    fid = models.AutoField(primary_key=True)
    friendship_from = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='friendship_from_me')
    friendship_to = models.ForeignKey(Reader, on_delete=models.CASCADE, related_name='friendship_to_me')
    created_at = models.DateTimeField(auto_now_add=True)
    is_pending = models.BooleanField(default=True)

    class Meta:
        db_table = 'friend'
        
    def __str__(self):
        return str({
            'fid': self.fid,
            'friendship_from': self.friendship_from,
            'friendship_to': self.friendship_to,
            'created_at': self.created_at,
            'is_pending': self.is_pending,
        })
    
