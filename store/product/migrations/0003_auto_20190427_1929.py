# Generated by Django 2.2 on 2019-04-27 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190427_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.AddField(
            model_name='review',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
