from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Модель пользователя."""

    basket = models.ManyToManyField(
        'products.Product', through='products.Basket',
        verbose_name=_('Корзина'),
        help_text=_('Корзина'),
        )

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        db_table_comment = _('Пользователь')

    def __str__(self) -> str:
        return self.username
