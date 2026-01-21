from django.contrib import admin
from .models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    max_num = 5


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'birth_date' )
    search_fields = ('last_name', 'first_name')
    search_help_text = 'Пошук за ім/ям та прізвищем '

