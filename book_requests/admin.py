from django.contrib import admin
from .models import Request
from django_summernote.admin import SummernoteModelAdmin


# Customises how CollaborareRequest looks in the admin interface
@admin.register(Request)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'what_book_would_you_like_to_request',)
