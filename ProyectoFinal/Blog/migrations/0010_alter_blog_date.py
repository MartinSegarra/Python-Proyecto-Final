# Generated by Django 4.2.5 on 2023-10-21 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0009_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
