from django.contrib.auth import get_user_model
from django.db.models import F, Sum
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from products.models import Basket, Category, Product, Subcategory

User = get_user_model()


class CategorySubcategoryProductBaseSerializer(
        serializers.ModelSerializer
        ):
    """Базовый сериализатор категорий, подкатегорий и продуктов."""

    class Meta:
        fields = [
            'title',
            'slug',
            'image',
        ]


class SubcategorySerializer(CategorySubcategoryProductBaseSerializer):
    """Сериализатор подкатегорий."""

    class Meta(CategorySubcategoryProductBaseSerializer.Meta):
        model = Subcategory


class CategorySerializer(CategorySubcategoryProductBaseSerializer):
    """Сериализатор категорий."""

    subcategories = SubcategorySerializer(many=True)

    class Meta(CategorySubcategoryProductBaseSerializer.Meta):
        model = Category
        fields = CategorySubcategoryProductBaseSerializer.Meta.fields + [
            'subcategories',
            ]


class ProductSerializer(CategorySubcategoryProductBaseSerializer):
    """Сериализатор продуктов."""

    category = serializers.SlugRelatedField(
        source='subcategory.category',
        slug_field='slug',
        read_only=True,
        )
    subcategory = serializers.SlugRelatedField(
        slug_field='slug',
        read_only=True,
        )
    image = serializers.SerializerMethodField()

    class Meta(CategorySubcategoryProductBaseSerializer.Meta):
        model = Product
        fields = CategorySubcategoryProductBaseSerializer.Meta.fields + [
            'price',
            'category',
            'subcategory',
            ]

    def get_image(self, obj: Product) -> list[str]:
        """Выводит список изображений."""
        full_uri = self.context['request'].build_absolute_uri
        return [
            full_uri(obj.image.url),
            full_uri(obj.medium_image.url),
            full_uri(obj.little_image.url),
            ]


class BasketBaseSerializer(serializers.ModelSerializer):
    """Базовый сериализатор корзины."""

    class Meta:
        model = Basket
        fields = [
            'product',
            'count',
        ]


class BasketListSerializer(BasketBaseSerializer):
    """Сериализатор вывода корзины."""

    product = ProductSerializer()
    total_price_product = serializers.SerializerMethodField()

    class Meta(BasketBaseSerializer.Meta):
        fields = BasketBaseSerializer.Meta.fields + [
            'total_price_product',
        ]

    def get_total_price_product(self, obj):
        """Возвращает цену * количество."""
        return obj.product.price * obj.count


class BasketInfoSerializer(serializers.ModelSerializer):
    """Сериализатор полной информации по корзины."""

    products = BasketListSerializer(source='basket_products', many=True)
    total_count = serializers.SerializerMethodField()
    total_price_products = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'products',
            'total_count',
            'total_price_products',
        ]

    def get_total_count(self, obj):
        """Возвращает общее количество товаров."""
        return obj.basket_products.aggregate(Sum('count'))['count__sum']

    def get_total_price_products(self, obj):
        """Возвращает общую цену товаров."""
        return obj.basket_products.annotate(
            price=F('count') * F('product__price')
            ).aggregate(Sum('price'))['price__sum']


class BasketCreateUpdateSerializer(BasketBaseSerializer):
    """Сериализатор создания/изменения товара из корзины."""

    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field='slug',
        )

    def validate_product(self, value: int) -> int:
        """Валидация поля продукта."""
        method = self.context['request'].method
        product = Basket.objects.filter(
            user=self.context['request'].user,
            product=Product.objects.get(slug=value),
        ).exists()
        if method == 'POST' and product:
            raise serializers.ValidationError(
                _('Такой товар уже присутсвует в корзине')
                )
        elif method != 'POST' and not product:
            raise serializers.ValidationError(
                _('Такой товар отсутсвует в корзине')
                )
        return value


class BasketDestroySerializer(BasketCreateUpdateSerializer):
    """Сериализатор удаления товара из корзины."""

    class Meta(BasketCreateUpdateSerializer.Meta):
        fields = ('product',)
