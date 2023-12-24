from django.db import models
from products.models import Item
from users.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField(Item, through="CartItem", related_name="items", verbose_name="Товары")
    total = models.IntegerField(null=True, blank=True, verbose_name="Итого")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f"Пользователь товара: {self.user}"


class CartItem(models.Model):
    quantity = models.IntegerField(null=False, verbose_name="Количество")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товар корзины"

    def __str__(self):
        return f"{self.item} пользователя {self.cart.user}"
