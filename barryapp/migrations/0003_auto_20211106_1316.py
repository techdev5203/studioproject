# Generated by Django 2.1.5 on 2021-11-06 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0002_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000, null=True)),
                ('Description', models.CharField(blank=True, max_length=2000, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('title' , models.TextField(max_length=100, blank=True, default='')),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
             
        migrations.AlterField(
            model_name='index',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AddField(
            model_name='header',
            name='title',
            field=models.CharField('barryapp.title'),
        ),
    ]
