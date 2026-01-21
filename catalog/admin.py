from django.contrib import admin
from .models import Author, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    max_num = 5


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'last_name',
                    'birth_date' )

    search_fields = ('last_name', 'name')
    search_help_text = 'Пошук за ім/ям та прізвищем '
    inlines = (BookInline,)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('author',
                    'genre',
                    'name',
                    'is_available',
                    'book_info')
    list_filter=('author','is_available', 'genre')
    @admin.display(description='Инфо')
    def book_info(self, obj:Book):
        if len(obj.description) > 100:
            return "- Довгий опис"
        return "- Короткий опис"






