# Generated by Django 4.1.1 on 2022-12-29 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bunnybook', '0011_alter_comment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
    ]