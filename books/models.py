from django.db import models
from django.core import validators


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(validators=(validators.MinValueValidator(limit_value=1, message="You cannot be less than 1 age."),))


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
