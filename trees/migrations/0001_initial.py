# Generated by Django 3.1.3 on 2022-05-08 17:31

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import trees.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Família',
                'verbose_name_plural': 'Famílias',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Espécie',
                'verbose_name_plural': 'Espécies',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('address', models.TextField(max_length=200, verbose_name='Descrição')),
                ('image1', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('image2', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('image3', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Praça',
                'verbose_name_plural': 'Praças',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('image1', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('image2', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('image3', models.ImageField(blank=True, upload_to=trees.models.get_file_path, verbose_name='imagem')),
                ('description', models.TextField(blank=True)),
                ('is_display', models.BooleanField(default=True)),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family', to='trees.square')),
                ('specie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specie', to='trees.specie')),
                ('square', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trees', to='trees.square')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
