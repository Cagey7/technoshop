# Generated by Django 4.2.6 on 2024-01-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='default',
            field=models.BooleanField(default=False, verbose_name='Адрес по умолчанию'),
        ),
    ]
