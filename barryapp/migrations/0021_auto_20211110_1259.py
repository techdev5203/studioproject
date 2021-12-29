# Generated by Django 2.1.5 on 2021-11-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0020_header_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='image',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='header',
            name='user',
        ),
        migrations.AlterField(
            model_name='header',
            name='description',
            field=models.CharField(blank=True, default='0.0', max_length=2000),
        ),
        migrations.AlterField(
            model_name='header',
            name='title',
            field=models.TextField(blank=True, default='0.0', max_length=100),
        ),
    ]
