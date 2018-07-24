# Generated by Django 2.0.6 on 2018-07-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpsite', '0017_merge_20180703_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapitem',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='mapitem',
            name='media',
            field=models.ManyToManyField(blank=True, through='dpsite.MappedMedia', to='dpsite.Media'),
        ),
        migrations.AlterField(
            model_name='mapitem',
            name='overlay_group',
            field=models.ManyToManyField(blank=True, to='dpsite.OverlayGroup'),
        ),
        migrations.AlterField(
            model_name='mapitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='dpsite.Tag'),
        ),
        migrations.AlterField(
            model_name='media',
            name='file_iframe',
            field=models.CharField(blank=True, help_text='Please paste in an &lt;iframe&gt; to embed external content. Content must begin with &lt;iframe&gt; and end with &lt;/iframe&gt; ', max_length=1000, null=True, verbose_name='File <iframe>'),
        ),
    ]