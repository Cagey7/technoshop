from django.db import models
from products.models import Item
from users.models import User


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, through="CartItem")
    total = models.IntegerField(null=True, blank=True)


class CartItem(models.Model):
    quantity = models.IntegerField(null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)