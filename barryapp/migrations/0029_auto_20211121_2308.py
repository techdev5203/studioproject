# Generated by Django 2.1.5 on 2021-11-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0028_auto_20211121_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='Gender',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='payment',
            name='city',
            field=models.CharField(max_length=111, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='state',
            field=models.CharField(max_length=111, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='address',
            field=models.CharField(max_length=2000),
        ),
    ]
