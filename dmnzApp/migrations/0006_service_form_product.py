# Generated by Django 4.0.4 on 2022-12-07 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0005_service_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_form',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dmnzApp.product'),
        ),
    ]
