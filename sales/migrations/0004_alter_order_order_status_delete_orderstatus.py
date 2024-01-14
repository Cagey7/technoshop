# Generated by Django 4.2.6 on 2024-01-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Заказ создан'), (2, 'Передан службе доставки'), (3, 'Доставлен')], default=1, verbose_name='Статус заказа'),
        ),
        migrations.DeleteModel(
            name='OrderStatus',
        ),
    ]