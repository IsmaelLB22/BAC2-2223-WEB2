# Generated by Django 4.1.3 on 2022-11-15 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HELBManager', '0002_member'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='member',
        ),
    ]
