# Generated by Django 2.1.5 on 2021-11-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0004_auto_20211106_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]