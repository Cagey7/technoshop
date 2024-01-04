from django.db import models
from products.models import Item
from users.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField(Item, through="CartItem", related_name="items", verbose_name="Товары")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def item_in_cart(self, item_id):
        return self.cartitem_set.filter(item__id=item_id).exists()

    def __str__(self):
        return f"Пользователь товара: {self.user}"


class CartItem(models.Model):
    quantity = models.IntegerField(null=False, verbose_name="Количество")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Корзина")

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товар корзины"
        unique_together = ["cart", "item"]

    def __str__(self):
        return f"{self.item} пользователя {self.cart.user}"

    def increase_quantity(self, amount=1):
        amount_available = Item.objects.get(id=self.item.pk).quantity
        amount_in_cart = self.quantity + amount
        if amount_in_cart <= amount_available:
            self.quantity += amount
        self.save()

    def decrease_quantity(self, amount=1):
        if self.quantity > amount:
            self.quantity -= amount
            self.save()
