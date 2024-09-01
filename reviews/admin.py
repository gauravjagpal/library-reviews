from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book, Reviewed


@admin.register(Book)
class ReviewAdmin(SummernoteModelAdmin):


    list_display = ('title', 'author', 'status')
    search_fields = ['title', 'blurb', 'author']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('blurb',)

# Register your models here.
admin.site.register(Reviewed)
