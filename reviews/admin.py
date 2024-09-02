from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, Reviewed


# Customises how the Book model appears and behaves in the admin interface
@admin.register(Book)
class ReviewAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'status')
    search_fields = ['title', 'blurb', 'author']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('blurb',)


admin.site.register(Reviewed)
