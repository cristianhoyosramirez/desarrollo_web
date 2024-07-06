from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)
    
class Author(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    birth_date=models.CharField(null=True,blank=True)
    nationality=models.CharField(max_length=255,null=True,blank=True)
    
class Book(models.Model):
    title=models.CharField(max_length=255)
    description=models.TimeField(blank=True)
    publication_date=models.DateField()
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
    
class BookAuthor(models.Model):
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
