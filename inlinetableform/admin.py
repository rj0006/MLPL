from django.contrib import admin
from .models import Author, BookDetail

# Register your models here.
class BookDetailInline(admin.StackedInline):  # Inline for BookDetail
    model = BookDetail
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookDetailInline]  # Add BookDetail as inline in Author admin
    list_display = ('name', 'first_name', 'age')  # Display these fields in the Author list

class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'publish_date', 'price')  # Display these fields in the BookDetail list

admin.site.register(Author, AuthorAdmin)  # Register Author model with its admin class
admin.site.register(BookDetail, BookDetailAdmin)  # Register BookDetail model with its admin class