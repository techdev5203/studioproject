# Generated by Django 2.1.5 on 2021-11-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0018_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='address',
            field=models.TextField(max_length=200),
        ),
    ]
