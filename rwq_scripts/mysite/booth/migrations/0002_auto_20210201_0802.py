# Generated by Django 2.2.5 on 2021-02-01 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='rent time')),
                ('deadline', models.DateField(verbose_name='deadline')),
                ('status', models.CharField(choices=[('wait to approve', 'wait to approve'), ('approve', 'approve'), ('disapprove', 'disapprove')], max_length=32, verbose_name='status')),
            ],
            options={
                'verbose_name': 'rent',
                'verbose_name_plural': 'rent',
                'ordering': ('-create_at',),
            },
        ),
        migrations.AlterField(
            model_name='booth',
            name='name',
            field=models.CharField(max_length=32, verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Unsubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='rent time')),
                ('status', models.CharField(choices=[('wait to approve', 'wait to approve'), ('approve', 'approve')], max_length=32, verbose_name='status')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('rent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booth.Rent', verbose_name='rent info')),
            ],
            options={
                'verbose_name': 'subscribe',
                'verbose_name_plural': 'subscribe',
                'ordering': ('-create_at',),
            },
        ),
        migrations.AddField(
            model_name='rent',
            name='booth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.Booth', verbose_name='Booth'),
        ),
        migrations.AddField(
            model_name='rent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Booth'),
        ),
        migrations.CreateModel(
            name='Delay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('deadline', models.DateField(verbose_name='deadline')),
                ('rent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booth.Rent', verbose_name='rent info')),
            ],
            options={
                'verbose_name': 'delay',
                'verbose_name_plural': 'delay',
                'ordering': ('-create_at',),
            },
        ),
    ]
