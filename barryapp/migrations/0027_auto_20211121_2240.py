# Generated by Django 2.1.5 on 2021-11-21 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barryapp', '0026_auto_20211121_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='card_type',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='expiry_date',
        ),
    ]
