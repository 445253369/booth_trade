# Generated by Django 2.2.5 on 2021-02-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0003_booth_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='booth',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='update time'),
        ),
        migrations.AlterField(
            model_name='booth',
            name='picture',
            field=models.ImageField(upload_to='boothes'),
        ),
        migrations.AlterField(
            model_name='rent',
            name='status',
            field=models.CharField(choices=[('normal', 'normal'), ('apply to unsubscribe', 'apply to unsubscribe'), ('unsubscribed', 'unsubscribed'), ('delayed', 'delayed')], default='normal', max_length=32, verbose_name='status'),
        ),
    ]