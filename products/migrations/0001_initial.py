# Generated by Django 4.2.6 on 2023-12-06 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=127)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('desc', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(choices=[(0, 'В наличии'), (1, 'Нет в наличии')], default=1)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='images/%Y/%m/%d')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
