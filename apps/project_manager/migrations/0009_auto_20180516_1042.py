# Generated by Django 2.0.2 on 2018-05-16 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_manager', '0008_incepmakeexectask_sqlsha1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incepmakeexectask',
            old_name='task_id',
            new_name='celery_task_id',
        ),
    ]
