from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Model
from django.utils.html import format_html
from django.utils.safestring import SafeText

from products.constants import DISPLAY_IMAGE_ADMIN
from products.models import Category, Product, Subcategory


class BaseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'display_image',
    ]
    list_filter = [
        'slug',
    ]
    search_fields = [
        'title',
        'slug',
    ]

    def display_image(self, obj: Model) -> SafeText:
        """Выводит изображение в списке элементов."""
        return format_html(DISPLAY_IMAGE_ADMIN.format(obj.image.url))


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    """Отображение в админ панели категорий."""
    pass


@admin.register(Subcategory)
class SubcategoryAdmin(BaseAdmin):
    """Отображение в админ панели подкатегорий."""

    def get_list_display(self, request: WSGIRequest) -> list[str]:
        """Расширяет поле вывода списка элементов."""
        return self.list_display + ['category']

    def get_list_filter(self, request: WSGIRequest) -> list[str]:
        """Расширяет поле фильтра."""
        return self.list_filter + ['category__slug']


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    """Отображение в админ панели продуктов."""

    def get_list_display(self, request: WSGIRequest) -> list[str]:
        """Расширяет поля вывода списка элементов."""
        return self.list_display + [
            'display_medium_image',
            'display_little_image',
            'price',
            'subcategory',
            ]

    def get_list_filter(self, request: WSGIRequest) -> list[str]:
        """Расширяет поле фильтра."""
        return self.list_filter + ['subcategory__slug']

    def display_medium_image(self, obj: Model) -> SafeText:
        """Выводит среднее изображение в списке элементов."""
        return format_html(DISPLAY_IMAGE_ADMIN.format(obj.medium_image.url))

    def display_little_image(self, obj: Model) -> SafeText:
        """Выводит маленькое изображение в списке элементов."""
        return format_html(DISPLAY_IMAGE_ADMIN.format(obj.little_image.url))
