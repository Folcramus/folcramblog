# Generated by Django 3.1.1 on 2020-10-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_final', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.CharField(blank=True, default=None, max_length=256, null=True),
        ),
    ]
