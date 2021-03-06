# Generated by Django 3.2.9 on 2021-12-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0036_delete_beginnerpay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applynow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phonenumber', models.CharField(max_length=12)),
                ('age', models.TextField()),
                ('portfoliolink', models.TextField()),
                ('experience', models.TextField()),
                ('images', models.ImageField(upload_to='')),
                ('date', models.DateField()),
            ],
        ),
    ]
