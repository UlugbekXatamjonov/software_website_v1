# Generated by Django 4.1 on 2022-09-08 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0004_alter_gamephoto_options_gamephoto_created_at'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Game_Category',
        ),
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='game_category',
            options={'ordering': ('-created_at',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='software',
            options={'ordering': ('-created_at',)},
        ),
    ]
