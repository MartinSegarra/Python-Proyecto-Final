# Generated by Django 4.2.5 on 2023-10-19 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_blog_author_alter_blog_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
