# Generated by Django 4.1 on 2023-02-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0029_remove_register_freelance_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_freelance',
            name='over_view',
            field=models.TextField(default=''),
        ),
    ]
