# Generated by Django 2.1.5 on 2021-11-08 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion




class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barryapp', '0006_blog2_blog3_photos_pics_text1_text2'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='author',
            field=models.ForeignKey(default='', on_delete=models.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
