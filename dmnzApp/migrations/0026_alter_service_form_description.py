# Generated by Django 4.1 on 2023-01-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0025_freelancerworks_fr_desecr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_form',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
