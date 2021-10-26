# Generated by Django 3.2.8 on 2021-10-26 02:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_librotek_app', '0007_auto_20211025_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Anonymous', max_length=128, null=True, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 842623)),
        ),
        migrations.AlterField(
            model_name='book',
            name='modificationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 842623)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 862627)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='modificationDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 862627)),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastLogin',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 857626), verbose_name='lastLogin'),
        ),
        migrations.AlterField(
            model_name='user',
            name='signUp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 21, 21, 5, 857626), verbose_name='signUp'),
        ),
    ]
