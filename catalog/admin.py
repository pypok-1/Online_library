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
                    'birth_date')
    list_display_links = ('last_name', 'name')
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
    list_filter = ('author', 'genre')
    search_fields = ('name', 'genre')
    search_help_text = 'Пошук за назвою книги або жанром'

    fieldsets = (
        ('Основна інфа', {
            'fields': ('name', 'author', 'genre')
        }),
        ('Додатково', {
            'fields': ('description', 'pages_count', 'is_available', 'created_at'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Инфо')
    def book_info(self, obj: Book):
        if len(obj.description) > 100:
            return '> Довгий опис'
        return '> Короткий опис'

    actions = ['make_available', 'make_unavailable']

    @admin.action(description='(В наявності)')
    def make_available(self, request, queryset):
        updated = queryset.update(is_available=True)
        self.message_user(request, f'Оновлено {updated}')

    @admin.action(description='(Немає в наявності)')
    def make_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f'Оновлено {updated}')
