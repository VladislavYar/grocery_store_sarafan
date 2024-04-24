from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

from products.constants import (BIG_IMAGE, FORMAT_IMAGE, LEN_NAME,
                                LITTLE_IMAGE, MEDIUM_IMAGE, MIN_COUNT_PRODUCT,
                                MIN_PRICE)

User = get_user_model()


class BaseModel(models.Model):
    """Базовая модель."""

    title = models.CharField(
        max_length=LEN_NAME,
        verbose_name=_('Название'),
        help_text=_('Название'),
        db_comment=_('Название'),
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=_('Slug-имя'),
        help_text=_('Slug-имя'),
        db_comment=_('Slug-имя'),
    )
    image = ResizedImageField(
        size=BIG_IMAGE,
        force_format=FORMAT_IMAGE,
        upload_to='images/',
        verbose_name=_('Изображение'),
        help_text=_('Изображение'),
        db_comment=_('Изображение'),
    )

    class Meta:
        ordering = ('title',)
        abstract = True

    def __str__(self) -> str:
        return self.slug


class Category(BaseModel):
    """Модель категории."""

    class Meta(BaseModel.Meta):
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        db_table_comment = _('Категории')


class Subcategory(BaseModel):
    """Модель подкатегории."""

    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        verbose_name=_('Категория'),
        help_text=_('Категория'),
        db_comment=_('Категория'),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _('Подкатегория')
        verbose_name_plural = _('Подкатегории')
        db_table_comment = _('Подкатегория')


class Product(BaseModel):
    """Модель продукта."""

    medium_image = ResizedImageField(
        size=MEDIUM_IMAGE,
        force_format=FORMAT_IMAGE,
        upload_to='images/',
        verbose_name=_('Среднее изображение'),
        help_text=_('Среднее изображение'),
        db_comment=_('Среднее изображение'),
    )

    little_image = ResizedImageField(
        size=LITTLE_IMAGE,
        force_format=FORMAT_IMAGE,
        upload_to='images/',
        verbose_name=_('Маленькое изображение'),
        help_text=_('Маленькое изображение'),
        db_comment=_('Маленькое изображение'),
    )

    price = models.PositiveIntegerField(
        verbose_name=_('Цена'),
        help_text=_('Цена'),
        db_comment=_('Цена продукта'),
        validators=(MinValueValidator(MIN_PRICE),)
    )

    subcategory = models.ForeignKey(
        to=Subcategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Подкатегория продукта'),
        help_text=_('Подкатегория продукта'),
        db_comment=_('Подкатегория продукта'),
    )

    class Meta(BaseModel.Meta):
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
        db_table_comment = _('Продукт')


class Basket(models.Model):
    """Модель корзины."""

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='basket_products',
        verbose_name=_('Пользователь'),
        help_text=_('Пользователь'),
        db_comment=_('Пользователь'),
    )
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='baskets',
        verbose_name=_('Продукт'),
        help_text=_('Продукт'),
        db_comment=_('Продукт'),
    )
    count = models.PositiveIntegerField(
        verbose_name=_('Количество продукта'),
        help_text=_('Количество продукта'),
        db_comment=_('Количество продукта'),
        validators=(MinValueValidator(MIN_COUNT_PRODUCT),)
    )

    class Meta:
        verbose_name = _('Корзина')
        verbose_name_plural = _('Корзины')
        db_table_comment = _('Корзина')
        unique_together = (
                ('user', 'product',),
            )

    def __str__(self) -> str:
        return f'{self.user} - {self.product} - {self.count}'
