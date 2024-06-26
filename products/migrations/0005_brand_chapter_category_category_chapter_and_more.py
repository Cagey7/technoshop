# Generated by Django 4.2.6 on 2024-01-14 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_item_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=127)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='images/brands/%Y/%m/%d', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Бренды',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=127)),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to='images/chapters/%Y/%m/%d', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Разделы',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='category_chapter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.chapter', verbose_name='Раздел'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.brand', verbose_name='Бренд'),
        ),
    ]
