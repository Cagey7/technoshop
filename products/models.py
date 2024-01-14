from django.db import models
from django.urls import reverse
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

    name = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    desc = models.TextField(blank=True, verbose_name="Описание товара")
    item_brand = models.ForeignKey("Brand", on_delete=models.PROTECT, null=True, verbose_name="Бренд")
    price = models.IntegerField(null=False, verbose_name="Цена")
    quantity = models.IntegerField(null=False, verbose_name="Количество")
    is_published = models.IntegerField(choices=Status.choices, default=Status.IN_STOCK, verbose_name="Статус")
    photo = models.ImageField(upload_to="images/items/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")
    item_category = models.ForeignKey("Category", on_delete=models.PROTECT, verbose_name="Категория")
    
    objects = models.Manager()
    published = PublishedManaget()

    def __str__(self):
        return f"{self.name}"
    
    def is_in_cart(self, user):
        from cart.models import Cart
        cart = Cart.objects.get(user=user)
        return cart.items.filter(pk=self.pk).exists()

    def decrease_quantity(self, num):
        self.quantity -= num
        if self.quantity <= 0:
            self.is_published = self.Status.OFF_STOCK
        self.save()

    def get_absolute_url(self):
        return reverse("products", kwargs={"slug":self.slug})


class Category(models.Model):
    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=127, db_index=True)
    photo = models.ImageField(upload_to="images/categories/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    category_chapter = models.ForeignKey("Chapter", on_delete=models.PROTECT, null=True, verbose_name="Раздел")

    def __str__(self):
        return f"{self.name}"


class Chapter(models.Model):
    class Meta:
        verbose_name = "Разделы"
        verbose_name_plural = "Разделы"
    
    name = models.CharField(max_length=127, db_index=True)
    photo = models.ImageField(upload_to="images/chapters/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")
    
    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    class Meta:
        verbose_name = "Бренды"
        verbose_name_plural = "Бренды"

    name = models.CharField(max_length=127, db_index=True)
    photo = models.ImageField(upload_to="images/brands/%Y/%m/%d", default=None, blank=True, null=True, verbose_name="Изображение")

    def __str__(self):
        return f"{self.name}"
