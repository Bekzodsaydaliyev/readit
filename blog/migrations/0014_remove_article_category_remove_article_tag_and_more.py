# Generated by Django 4.1.7 on 2023-02-26 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
