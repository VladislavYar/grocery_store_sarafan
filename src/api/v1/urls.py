from django.urls import include, path

from api.v1.views import (BasketCreateUpdateDestroyView, BasketInfoView,
                          BasketСleanView, CategoryView, ProductView)

app_name = 'v1'


urlpatterns = [
    path('basket/', BasketCreateUpdateDestroyView.as_view(), name='basket'),
    path('basket/info/', BasketInfoView.as_view(), name='basket-info'),
    path(
        'basket/clean/', BasketСleanView.as_view(), name='basket-clean'
        ),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('products/', ProductView.as_view(), name='products'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
