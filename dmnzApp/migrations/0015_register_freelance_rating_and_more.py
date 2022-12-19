# Generated by Django 4.1 on 2022-12-15 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dmnzApp', '0014_rename_project_title_register_freelance_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_freelance',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='register_freelance',
            name='w_status',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.CreateModel(
            name='Freelancerworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('fr_file', models.FileField(blank=True, default='', null=True, upload_to='images/')),
                ('fr_status', models.CharField(max_length=40)),
                ('fr_product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dmnzApp.product')),
                ('fr_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('frelancer', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dmnzApp.register_freelance')),
            ],
        ),
    ]