# Generated by Django 2.2 on 2019-04-28 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190427_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='colors',
            new_name='color',
        ),
    ]
