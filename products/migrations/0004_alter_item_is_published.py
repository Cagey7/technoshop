# Generated by Django 4.2.6 on 2024-01-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_amount_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.IntegerField(choices=[(0, 'Нет в наличии'), (1, 'В наличии')], default=1, verbose_name='Статус'),
        ),
    ]
