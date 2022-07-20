# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authored(models.Model):
    book = models.OneToOneField('Book', models.DO_NOTHING, primary_key=True)
    author = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authored'
        unique_together = (('book', 'author'),)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    page_count = models.IntegerField()
    genre = models.TextField()

    class Meta:
        managed = False
        db_table = 'book'


class BookReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    reviewer = models.ForeignKey('Users', models.DO_NOTHING)
    rating = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    love_count = models.IntegerField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookreview'


class Borrow(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    borrower = models.ForeignKey('Users', models.DO_NOTHING)
    library = models.ForeignKey('Library', models.DO_NOTHING)
    checkout_datetime = models.DateTimeField(blank=True, null=True)
    return_datetime = models.DateTimeField()
    fee = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'borrow'


class Follow(models.Model):
    followed_user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    follower_user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'follow'
        unique_together = (('followed_user', 'follower_user'),)


class Friend(models.Model):
    from_friend = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    to_friend = models.ForeignKey('Users', models.DO_NOTHING)
    is_pending = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'friend'
        unique_together = (('from_friend', 'to_friend'),)


class Library(models.Model):
    library_id = models.AutoField(primary_key=True)
    library_name = models.TextField()
    photo_url = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    password = models.TextField()
    longitude = models.TextField(blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'library'


class LibraryStock(models.Model):
    library = models.OneToOneField(Library, models.DO_NOTHING, primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)
    no_of_copies = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'librarystock'
        unique_together = (('library', 'book'),)


class ReadingChallenge(models.Model):
    reading_challenge_id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    finish_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'readingchallenge'


class ReadingChallengeBook(models.Model):
    reading_challenge = models.OneToOneField(ReadingChallenge, models.DO_NOTHING, primary_key=True)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'readingchallengebook'
        unique_together = (('reading_challenge', 'book'),)


class ReadingChallengeCreator(models.Model):
    creator = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)
    reading_challenge = models.ForeignKey(ReadingChallenge, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'readingchallengecreator'
        unique_together = (('creator', 'reading_challenge'),)


class Reads(models.Model):
    book = models.OneToOneField(Book, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    start_datetime = models.DateTimeField(blank=True, null=True)
    finish_datetime = models.DateTimeField(blank=True, null=True)
    read_status = models.TextField()

    class Meta:
        managed = False
        db_table = 'reads'
        unique_together = (('book', 'user'),)

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField()
    full_name = models.TextField(blank=True, null=True)
    photo_url = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True)
    password = models.TextField()
    reading_challenge = models.ForeignKey(
        ReadingChallenge, models.DO_NOTHING, blank=True, null=True)
    user_permissions = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

