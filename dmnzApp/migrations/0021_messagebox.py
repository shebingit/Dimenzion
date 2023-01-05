# Generated by Django 4.1 on 2023-01-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0020_freelancerworks_fr_categori_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messagebox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phno', models.CharField(default='', max_length=100)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('messag', models.TextField()),
                ('files', models.FileField(upload_to='files')),
            ],
        ),
    ]
