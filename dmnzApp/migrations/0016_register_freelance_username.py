# Generated by Django 4.1 on 2022-12-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0015_register_freelance_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_freelance',
            name='username',
            field=models.CharField(default='', max_length=255),
        ),
    ]