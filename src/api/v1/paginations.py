from rest_framework.pagination import PageNumberPagination

from api.v1.constants import CATEGORY_PAGE_SIZE, PRODUCT_PAGE_SIZE


class CategoryPagination(PageNumberPagination):
    """Пагинация категорий."""

    page_size = CATEGORY_PAGE_SIZE


class ProductPagination(PageNumberPagination):
    """Пагинация продуктов."""

    page_size = PRODUCT_PAGE_SIZE
