# Generated by Django 4.1.2 on 2022-12-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HELBManager', '0016_alter_task_assignedmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tasks',
            field=models.TextField(default='Task Title;UserAssigned'),
        ),
    ]
