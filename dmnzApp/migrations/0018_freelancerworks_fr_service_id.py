# Generated by Django 4.1 on 2022-12-20 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0017_freelancerworks_submitte_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancerworks',
            name='fr_service_id',
            field=models.IntegerField(default='0'),
        ),
    ]
