# Generated by Django 4.2.6 on 2024-01-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_chapter_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
