# Generated by Django 2.0.6 on 2018-06-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0004_auto_20180628_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='media',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
    ]
