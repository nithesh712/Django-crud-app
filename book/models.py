from django.db import models

# Create your models here.


class BooksModel(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    read_by = models.CharField(max_length=30)
