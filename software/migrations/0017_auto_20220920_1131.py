# Generated by Django 3.1.1 on 2022-09-20 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0016_comment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_at',
        ),
    ]