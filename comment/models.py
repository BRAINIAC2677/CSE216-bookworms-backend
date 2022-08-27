from django.db import models


class Comment(models.Model):
    cid = models.AutoField(primary_key=True)
    commented_by = models.ForeignKey('reader.Reader', on_delete=models.CASCADE, related_name='my_comments')
    commented_on = models.ForeignKey('bookreview.BookReview', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    loved_by = models.ManyToManyField('reader.Reader', related_name='loved_comments')

    class Meta:
        db_table = 'comment'
    
    def __str__(self):
        return str({
            'cid': self.cid,
            'commented_by': self.commented_by,
            'commented_on': self.commented_on,
            'content': self.content,    
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'loved_by': self.loved_by
        })