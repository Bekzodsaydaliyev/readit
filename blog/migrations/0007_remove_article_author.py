# Generated by Django 4.1.7 on 2023-02-26 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile_alter_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]
