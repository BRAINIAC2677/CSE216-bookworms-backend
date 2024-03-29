from django.db import models

from reader.models import Reader
from book.models import Book

class Read(models.Model):
    status_choices = (
        ('w', 'Want to Read'),
        ('r', 'Reading'),
        ('c', 'Completed'),
    )
    rsid = models.AutoField(primary_key=True)
    reader = models.OneToOneField(Reader, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=status_choices)

    class Meta:
        db_table = 'read'
        
    def __str__(self):
        return str({
            'rsid': self.rsid,
            'reader': self.reader,
            'book': self.book,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status': self.status,
        })
    