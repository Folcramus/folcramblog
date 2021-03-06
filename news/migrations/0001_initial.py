# Generated by Django 3.1.1 on 2020-10-14 10:18

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default=None, max_length=260, unique=True)),
                ('name', models.CharField(blank=True, default=None, max_length=260)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=260)),
                ('author', models.CharField(blank=True, default=None, max_length=64)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, null=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True, default=None)),
                ('image', models.ImageField(upload_to='media/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата добавления')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.news', verbose_name='Новость')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
