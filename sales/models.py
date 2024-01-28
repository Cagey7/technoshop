from django.db import models
from core.models import TimeStampedModel
from users.models import User
from products.models import Item
from users.models import Address


class Order(TimeStampedModel):
    class Status(models.IntegerChoices):
        CANCELED = 0, "Отменён"
        CREATED = 1, "Заказ создан"
        DELIVERY = 2, "Передан службе доставки"
        DONE = 3, "Доставлен"
        

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField(Item, through="Purchase", related_name="order_items", verbose_name="Товары")
    order_status = models.IntegerField(choices=Status.choices, default=Status.CREATED, verbose_name="Статус заказа")
    address = models.CharField(max_length=511, verbose_name="Адрес")
    total = models.IntegerField(null=False, verbose_name="Итого")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"

    def get_order_status(self):
        return self.get_order_status_display()

    def formatted_order_date(self):
        months = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 
                  7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
        return f"Заказ от {self.created.day} {months[self.created.month]} {self.created.year}"

    def __str__(self):
        return f"Заказ номер: {self.pk}"


class Purchase(models.Model):
    quantity = models.IntegerField(null=False, verbose_name="Количество")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Товар")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")

    class Meta:
        verbose_name = "Товар заказа"
        verbose_name_plural = "Товар заказа"

    def purchase_total(self):
        return self.item.price * self.quantity
    
    def __str__(self):
        return f"{self.item} пользователя {self.order.user}"
