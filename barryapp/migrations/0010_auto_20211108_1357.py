# Generated by Django 2.1.5 on 2021-11-08 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0009_auto_20211108_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pics',
            old_name='image',
            new_name='images',
        ),
    ]
