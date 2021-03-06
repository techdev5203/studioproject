# Generated by Django 3.2.9 on 2021-12-04 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0041_auto_20211204_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('text', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='applynow',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applynow',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
