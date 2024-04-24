from django.db.models.query import QuerySet
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from api.v1.paginations import CategoryPagination, ProductPagination
from api.v1.serializers import (BasketCreateUpdateSerializer,
                                BasketDestroySerializer, BasketInfoSerializer,
                                CategorySerializer, ProductSerializer)
from products.models import Basket, Category, Product
from users.models import User
from utils.decorators import change_serializer_class


class CategoryView(ListAPIView):
    """View вывода списка категорий."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination


class ProductView(ListAPIView):
    """View вывода списка продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination


class BasketInfoView(RetrieveAPIView):
    """View вывода полной информации по корзине."""

    permission_classes = (IsAuthenticated,)
    serializer_class = BasketInfoSerializer

    def get_object(self) -> User:
        """Отдаёт объект пользователя."""
        return self.request.user


class BasketСleanView(DestroyAPIView):
    """View очистки корзины."""

    queryset = Basket.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> QuerySet[Basket]:
        """Отдаёт товары в корзине пользователя."""
        return self.queryset.filter(user=self.request.user)


class BasketCreateUpdateDestroyView(
    CreateAPIView, DestroyAPIView, UpdateAPIView
):
    """View создание, удаление, изменения товара в корзине."""

    permission_classes = (IsAuthenticated,)
    serializer_class = BasketCreateUpdateSerializer

    def _validate_data_serializer(self) -> None:
        """Валидирует данные."""
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

    def get_serializer_class(self) -> ModelSerializer:
        """Возврщает сериализатор в зависимости от метода."""
        if self.request.method == 'DELETE':
            return BasketDestroySerializer
        return BasketCreateUpdateSerializer

    def get_object(self) -> Basket:
        """Отдаёт товар для изменения/удаления."""
        self._validate_data_serializer()
        product = self.request.data['product']
        return Basket.objects.get(
            user=self.request.user,
            product=Product.objects.get(slug=product),
        )

    def perform_create(self, serializer: BasketCreateUpdateSerializer) -> None:
        """Сохранение продукта в корзину."""
        serializer.save(user=self.request.user)

    @change_serializer_class
    def create(self, request: Request) -> Response:
        """Переназначает сериализатор для вывода."""
        return super().create(request)

    @change_serializer_class
    def update(self, request: Request, *args, **kwargs) -> Response:
        """Переназначает сериализатор для вывода."""
        return super().update(request, *args, **kwargs)
