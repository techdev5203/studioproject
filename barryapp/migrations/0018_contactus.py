# Generated by Django 2.1.5 on 2021-11-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0017_delete_slide2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
