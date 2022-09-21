# Generated by Django 4.1 on 2022-08-26 10:00

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=15, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', verbose_name='Slug')),
                ('created_year', models.DateField(verbose_name='Yaratilgan vaqti')),
                ('genre', models.CharField(max_length=30, verbose_name='Janri')),
                ('creator', models.CharField(max_length=70, verbose_name='Yaratuvchi')),
                ('interface_lang', models.CharField(blank=True, max_length=100, null=True, verbose_name="O'yin tili")),
                ('voice_lang', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ovoz tili')),
                ('system', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sistema')),
                ('processor', models.CharField(blank=True, max_length=70, null=True, verbose_name='Protsesor')),
                ('ram', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tezkor hotira')),
                ('video_card', models.CharField(blank=True, max_length=50, null=True, verbose_name='Video karta')),
                ('hard_disk', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qattiq disk')),
                ('system_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sistema 2')),
                ('processor_2', models.CharField(blank=True, max_length=70, null=True, verbose_name='Protsesor 2')),
                ('ram_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tezkor hotira 2')),
                ('video_card_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Video karta 2')),
                ('hard_disk_2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Qattiq disk 2')),
                ('trailer', models.FileField(blank=True, null=True, upload_to='videos/game_trailer/%Y/%m/%d/', verbose_name='Trailer videosi')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='photos/game_photo/%Y/%m/%d/', verbose_name='Skrinshot')),
                ('size', models.CharField(max_length=50, verbose_name='Hajmi')),
                ('file_64x', models.FileField(blank=True, null=True, upload_to='files/game/64x/%Y/%m/%d/', verbose_name="O'yin fayli(64x)")),
                ('file_32x', models.FileField(blank=True, null=True, upload_to='files/game/32x/%Y/%m/%d/', verbose_name="O'yin fayli(32x)")),
                ('about', models.TextField(verbose_name="O'yin haqida")),
                ('installation', models.CharField(blank=True, max_length=150, null=True, verbose_name="O'rnatish")),
                ('website', models.CharField(blank=True, max_length=200, null=True, verbose_name='Websayt')),
                ('game_type', models.CharField(choices=[('offline', 'Offline'), ('online', 'Online')], max_length=20, verbose_name="O'yin turi")),
                ('version', models.CharField(max_length=20, verbose_name='Versia')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=20, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan vaqti')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.category', verbose_name='Kategoriya')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=15, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nomi')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('creator', models.CharField(max_length=200, verbose_name='Yaratuvchi')),
                ('version', models.CharField(blank=True, max_length=50, null=True, verbose_name='Versia')),
                ('requarment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsia qilingan sistema')),
                ('size', models.CharField(max_length=50, verbose_name='Hajmi')),
                ('about', models.TextField(verbose_name='Ilova haqida')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='photos/software_photo/%Y/%m/%d/', verbose_name='Skrinshot')),
                ('file_64x', models.FileField(blank=True, null=True, upload_to='files/software/64x/%Y/%m/%d/', verbose_name='Ilova fayli(64x)')),
                ('file_32x', models.FileField(blank=True, null=True, upload_to='files/software/32x/%Y/%m/%d/', verbose_name='Ilova fayli(32x)')),
                ('status', models.CharField(choices=[('active', 'Active'), ('deactive', 'Deactive')], default='active', max_length=20, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Yaratilgan vaqti')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.category', verbose_name='Kategorya')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.platform', verbose_name='Platforma')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='SoftwarePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='photos/software_photo/%Y/%m/%d/', verbose_name='Skrinshot')),
                ('software', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='software.software', verbose_name='Dastur')),
            ],
        ),
        migrations.CreateModel(
            name='GamePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='photos/game_photo/%Y/%m/%d/', verbose_name='Skrinshot')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='software.game', verbose_name="O'yin")),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.platform', verbose_name='Platforma'),
        ),
        migrations.AddField(
            model_name='game',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
