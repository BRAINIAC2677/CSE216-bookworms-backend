from django.db import models

from library.models import Library
from book.models import Book

class LibraryStock(models.Model):
    lsid = models.AutoField(primary_key=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    borrow_fee_per_day = models.IntegerField(default=0)

    class Meta:
        db_table = 'library_stock'
        
    def __str__(self):
        return str({
            'library': self.library.library_name,
            'book': self.book.title,
            'quantity': self.quantity,
            'borrow_fee_per_day': self.borrow_fee_per_day,
        })
    
