# Generated by Django 4.1 on 2023-01-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0023_messagebox_mg_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_form',
            name='req_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
