# Generated by Django 4.2.6 on 2024-02-01 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
    ]
