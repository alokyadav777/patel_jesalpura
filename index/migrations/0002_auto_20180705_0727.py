# Generated by Django 2.0.6 on 2018-07-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentclass',
            name='blogId',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='commentclass',
            name='commentId',
            field=models.IntegerField(default=1),
        ),
    ]
