# Generated by Django 4.2.6 on 2024-01-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=123, verbose_name='Итого'),
            preserve_default=False,
        ),
    ]
