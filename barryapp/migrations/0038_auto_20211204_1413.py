# Generated by Django 3.2.9 on 2021-12-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0037_applynow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applynow',
            old_name='phonenumber',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='applynow',
            name='email',
            field=models.EmailField(max_length=122),
        ),
        migrations.AlterField(
            model_name='applynow',
            name='portfoliolink',
            field=models.CharField(max_length=122),
        ),
    ]