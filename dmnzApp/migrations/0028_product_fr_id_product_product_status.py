# Generated by Django 4.1 on 2023-01-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0027_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fr_id',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.IntegerField(default='0'),
        ),
    ]
