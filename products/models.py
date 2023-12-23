from django.db import models
from django.urls import reverse
from core.models import TimeStampedModel


class PublishedManaget(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Item.Status.IN_STOCK)

class SallingManaget(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published__in=[Item.Status.IN_STOCK, 
                                                               Item.Status.OFF_STOCK])

class Item(TimeStampedModel):
    class Status(models.IntegerChoices):
        OFF_STOCK = 0, "Нет в наличии"
        IN_STOCK = 1, "В наличии"
        NOT_AVALIABLE = 2, "Не продается"

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    desc = models.TextField(blank=True, verbose_name="Описание товара")
    price = models.IntegerField(null=False, verbose_name="Цена")
    amount = models.IntegerField(null=False, verbose_name="Количество")
    is_published = models.IntegerField(choices=Status.choices, default=Status.IN_STOCK, verbose_name="Статус")
    photo = models.ImageField(upload_to="images/items/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")
    item_category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    
    objects = models.Manager()
    published = PublishedManaget()
    salling = SallingManaget()

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("products", kwargs={"slug":self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=127, db_index=True)
    photo = models.ImageField(upload_to="images/categories/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return f"{self.name}"