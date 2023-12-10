from django.db import models
# from django.urls import reverse
from core.models import TimeStampedModel


class PublishedManaget(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Item.Status.IN_STOCK)


class Item(TimeStampedModel):
    class Status(models.IntegerChoices):
        OFF_STOCK = 0, "Нет в наличии"
        IN_STOCK = 1, "В наличии"

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    desc = models.TextField(blank=True)
    price = models.IntegerField(null=False)
    is_published = models.BooleanField(choices=Status.choices, default=Status.IN_STOCK)
    photo = models.ImageField(upload_to="images/%Y/%m/%d", default=None, blank=True, null=True)
    item_category = models.ForeignKey("Category", on_delete=models.PROTECT)
    
    objects = models.Manager()
    published = PublishedManaget()

    def __str__(self):
        return f"Название товара: {self.name}"
    
    # def get_absolute_url(self):
    #     return reverse("products", kwargs={"slug":self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=127, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return f"Категория: {self.name}"