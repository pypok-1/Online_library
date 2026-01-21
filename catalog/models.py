from django.db import models


class Author(models.Model):
    name = models.CharField( max_length=80)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pages_count = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

