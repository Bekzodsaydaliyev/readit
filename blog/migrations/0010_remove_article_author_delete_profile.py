# Generated by Django 4.1.7 on 2023-02-26 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
