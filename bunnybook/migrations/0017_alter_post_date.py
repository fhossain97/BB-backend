# Generated by Django 4.1.5 on 2023-01-26 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bunnybook', '0016_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]