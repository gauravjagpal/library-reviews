from django.db import models

class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    what_book_would_you_like_to_request = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.what_book_would_you_like_to_request