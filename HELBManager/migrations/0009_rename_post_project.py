# Generated by Django 4.1.3 on 2022-11-28 22:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HELBManager', '0008_rename_task_status_rename_tasks_post_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Project',
        ),
    ]
