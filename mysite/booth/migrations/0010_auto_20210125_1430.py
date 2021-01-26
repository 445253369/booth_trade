# Generated by Django 2.2.5 on 2021-01-25 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0009_auto_20210125_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unsubscribe',
            name='booth_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.booth', verbose_name='booth id'),
        ),
        migrations.AlterField(
            model_name='unsubscribe',
            name='status',
            field=models.CharField(choices=[('unsubscribe checking', 'unsubscribe checking'), ('unsubscribe pass', 'unsubscribe pass'), ('unsubscribe refused', 'unsubscribe refused'), ('unsubscribe uncheck', 'unsubscribe uncheck')], default='unsubscribe uncheck', max_length=16, null=True, verbose_name='status'),
        ),
    ]