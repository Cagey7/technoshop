# Generated by Django 4.2.6 on 2024-01-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_chapter_category_category_chapter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(default='slug', max_length=255, unique=True),
        ),
    ]
