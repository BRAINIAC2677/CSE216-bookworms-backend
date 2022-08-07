from django.db import models

from book.models import Book
from library.models import Library
from reader.models import Reader

class BookBorrow(models.Model):
    bbid = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_from = models.ForeignKey(Library, on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(Reader, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(blank=True, null=True)
    fee = models.FloatField()

    class Meta:
        db_table = 'book_borrow'
        
    def __str__(self):
        return {
            'book': self.book.title,
            'borrowed_from': self.borrowed_from.library_name,
            'borrowed_by': self.borrowed_by.user.username,
            'borrowed_date': self.borrowed_date,
            'returned_date': self.returned_date,
            'fee': self.fee,
        }
    

