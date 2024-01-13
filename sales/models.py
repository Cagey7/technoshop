from django.db import models
from core.models import TimeStampedModel
from users.models import User
from products.models import Item
from users.models import Address


class Order(TimeStampedModel):
    class Status(models.IntegerChoices):
        CREATED = 1, "Заказ создан"
        DELIVERY = 2, "Передан службе доставки"
        DONE = 3, "Доставлен"

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField(Item, through="Purchase", related_name="order_items", verbose_name="Товары")
    order_status = models.IntegerField(choices=Status.choices, default=Status.CREATED, verbose_name="Статус заказа")
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, verbose_name="Адрес")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"

    def __str__(self):
        return f"Заказ номер: {self.pk}"


class Purchase(models.Model):
    quantity = models.IntegerField(null=False, verbose_name="Количество")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    class Meta:
        verbose_name = "Товар заказа"
        verbose_name_plural = "Товар заказа"

    def __str__(self):
        return f"{self.item} пользователя {self.order.user}"
