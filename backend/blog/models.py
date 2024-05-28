from django.db import models
from django.utils import timezone

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title_punjabi = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200, default="english")
    content = models.TextField()
    book_punjabi = models.CharField(max_length=100,default="ਅਖਬਾਰ ਦੇ ਲੇਖ")
    book_english = models.CharField(max_length=100,default="book")
    author = models.CharField(max_length=100,default="ਦੇਵਿੰਦਰ ਦੀਦਾਰ")
    year = models.IntegerField(default=timezone.now().year)

    def __str__(self):
        return self.title_punjabi
    
class Story(models.Model):
    id = models.AutoField(primary_key=True)
    title_punjabi = models.CharField(max_length=200)
    title_english = models.CharField(max_length=200, default="english")
    content = models.TextField()
    author = models.CharField(max_length=100,default="ਦੇਵਿੰਦਰ ਦੀਦਾਰ")
    year = models.IntegerField(default=timezone.now().year)

    def __str__(self):
        return self.title_punjabi

class Prose(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return str(self.id)
