# Generated by Django 2.1.5 on 2021-11-08 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0011_images2_images3_images4_text3'),
    ]

    operations = [
        migrations.CreateModel(
            name='slide1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('desc', models.CharField(max_length=2000, null=True)),
                ('images', models.ImageField(upload_to='images')),
                ('tag', models.TextField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
