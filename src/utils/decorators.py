from functools import wraps

from api.v1.serializers import BasketListSerializer
from products.models import Basket, Product


def change_serializer_class(func):
    """Изменяет serializer для возвращаемых данных."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        request = args[0].request
        obj = Basket.objects.get(
            product=Product.objects.get(
                slug=response.data['product']
            ),
            user=request.user,
            )
        instance_serializer = BasketListSerializer(
            obj,
            context={'request': request},
            )
        response.data = instance_serializer.data
        return response
    return wrapper
