# Generated by Django 2.2.5 on 2019-09-27 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0024_media_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='featured',
        ),
        migrations.AddField(
            model_name='mapitem',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]