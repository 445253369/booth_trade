# Generated by Django 2.2.5 on 2021-02-05 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0005_auto_20210203_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='unsubscribe',
            name='is_from_delay',
            field=models.BooleanField(default=False, verbose_name='is from delay'),
        ),
    ]
