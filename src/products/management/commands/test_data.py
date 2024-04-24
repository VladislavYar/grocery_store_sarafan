from django.core.management.base import BaseCommand

from products.models import Category, Product, Subcategory


class Command(BaseCommand):

    help = "Создаёт тестовые данные."

    def _create_categories(self):
        """Создаёт категории."""
        categories = []
        for i in range(1, 21):
            categories.append(
                Category(
                    title=f'Категория {i}',
                    slug=f'category-{i}',
                    image='test/test600.png',
                    )
                )
        return Category.objects.bulk_create(categories)

    def _create_subcategories(self, categories):
        """Создаёт подкатегории."""
        subcategories = []
        index = 0
        for category in categories:
            for i in range(1, 6):
                subcategories.append(
                    Subcategory(
                        title=f'Подкатегория {i + index}',
                        slug=f'subcategory-{i + index}',
                        image='test/test600.png',
                        category=category,
                    )
                )
            index += 5
        return Subcategory.objects.bulk_create(subcategories)

    def _create_products(self, subcategories):
        """Создаёт продукты."""
        products = []
        index = 0
        for subcategory in subcategories:
            for i in range(1, 11):
                products.append(
                    Product(
                        title=f'Продукт {i + index}',
                        slug=f'product-{i + index}',
                        price=i,
                        image='test/test600.png',
                        medium_image='test/test300.png',
                        little_image='test/test100.png',
                        subcategory=subcategory,
                    )
                )
            index += 10
        Product.objects.bulk_create(products)

    def handle(self, *args, **options):
        self._create_products(
            self._create_subcategories(
                self._create_categories()
                )
            )
