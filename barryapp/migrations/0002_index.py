# Generated by Django 2.1.5 on 2021-11-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='docs')),
            ],
        ),
    ]