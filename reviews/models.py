from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Model designed to represent a book with essential information
# Such as title, author, a blurb, a URL to buy the book
class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    blurb = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    buy_here = models.URLField(max_length=128, blank=False)


# Model designed to store and manange reviews of books
# Each review is linked to a specific book with an approval status
class Reviewed(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="book_details"
        )
    body = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review {self.body} by {self.author}"
