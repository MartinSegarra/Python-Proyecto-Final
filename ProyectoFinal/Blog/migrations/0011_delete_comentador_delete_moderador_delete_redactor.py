# Generated by Django 4.2.5 on 2023-10-21 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_alter_blog_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comentador',
        ),
        migrations.DeleteModel(
            name='Moderador',
        ),
        migrations.DeleteModel(
            name='Redactor',
        ),
    ]