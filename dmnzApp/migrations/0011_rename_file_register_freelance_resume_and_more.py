# Generated by Django 4.0.4 on 2022-12-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmnzApp', '0010_alter_service_form_service_freelancer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_freelance',
            old_name='file',
            new_name='Resume',
        ),
        migrations.RenameField(
            model_name='register_freelance',
            old_name='education',
            new_name='qualification',
        ),
        migrations.RemoveField(
            model_name='register_freelance',
            name='end',
        ),
        migrations.RemoveField(
            model_name='register_freelance',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='register_freelance',
            name='start',
        ),
        migrations.RemoveField(
            model_name='register_freelance',
            name='startdate',
        ),
        migrations.AddField(
            model_name='register_freelance',
            name='work_2',
            field=models.FileField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='register_freelance',
            name='work_3',
            field=models.FileField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
