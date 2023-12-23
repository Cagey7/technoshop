# Generated by Django 4.2.6 on 2023-12-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='amount',
            field=models.IntegerField(default=10, verbose_name='Количество'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.IntegerField(choices=[(0, 'Нет в наличии'), (1, 'В наличии'), (2, 'Не продается')], default=1, verbose_name='Статус'),
        ),
    ]
