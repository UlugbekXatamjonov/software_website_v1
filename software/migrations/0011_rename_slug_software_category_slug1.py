# Generated by Django 4.1 on 2022-09-08 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0010_alter_software_software_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='software_category',
            old_name='slug',
            new_name='slug1',
        ),
    ]