# Generated by Django 4.2.5 on 2023-10-19 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
