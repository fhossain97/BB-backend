# Generated by Django 4.1.5 on 2023-01-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunnybook', '0013_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=''),
        ),
    ]
