from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=True)
    blurb = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

class Comment(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
