# Generated by Django 3.2.9 on 2021-12-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0040_auto_20211204_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applynow',
            name='age',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='applynow',
            name='experience',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='applynow',
            name='images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
