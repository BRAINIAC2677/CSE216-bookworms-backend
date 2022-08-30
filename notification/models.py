from django.db import models

class Notification(models.Model):
    nid = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_to = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notification_to_me')
    notification_from = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='notification_from_me')
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
    content_id = models.BigIntegerField() 

    class Meta:
        db_table = 'notification'

    def __str__(self):
        return str({
            'nid': self.nid,
            'created_at': self.created_at,
            'notification_to': self.notification_to,
            'notification_from': self.notification_from,
            'event': self.event,
            'content_id': self.content_id,
        })