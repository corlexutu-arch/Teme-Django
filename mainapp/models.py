from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=20, default='Uncategorized')
    description = models.TextField()
    release_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'movie'

class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.TextField()
    category = models.CharField(max_length=20, default='Uncategorized')
    release_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'book'