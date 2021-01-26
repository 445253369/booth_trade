from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class booth(models.Model):
    name = models.CharField(max_length=32,verbose_name='BoothName')
    pictrue = models.ImageField(upload_to = 'static/img/')
    description = models.TextField(verbose_name='about booth')
    area = models.FloatField(verbose_name='area')
    price = models.FloatField(verbose_name='price')
    position = models.CharField(max_length=64,verbose_name='position')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='online time')
    class Meta:
        verbose_name = 'booth'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)
    def __str__(self):
        return str(self.name)



class booth_status(models.Model):

    # def type(self,time,id):
    #     now = datetime.datetime.now()
    #     if time <= now:
    #         type = 'renting'
    #     else:
    #         if delay_booth.objects.filter

    type_choice = (
        ('rented','rented'),
        ('renting','renting'),
        ('delay','delay')
    )
    status_choices = (
        ('checking','checking'),
        ('pass','pass'),
        ('refused','refused'),
        ('uncheck','uncheck')
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user id',null=True)
    booth_id = models.ForeignKey(booth, on_delete=models.CASCADE, verbose_name='booth id',null=True)
    status = models.CharField(max_length=12, verbose_name='status',choices=status_choices,default='uncheck',null=True)
    type = models.CharField(max_length=12,verbose_name='type',choices=type_choice,default='renting',null=True)
    time = models.IntegerField(verbose_name='length of lease',null=True)
    deadline = models.DateTimeField(verbose_name='deadline',null=True)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = verbose_name
        ordering = ('type', '-deadline')

    @property
    def is_deadline(self):
        now = timezone.now()
        if self.deadline < now:
            return False
        else:
            print(self.deadline,now)
            print(self.booth_id)
            return True

    def __str__(self):
        return str(self.booth_id) + '-' + self.type

# class delay_booth(models.Model):
#     rent_id = models.ForeignKey(booth_status,on_delete=models.CASCADE,verbose_name='rent id')
#     time = models.DateTimeField(auto_now_add=True,verbose_name='restart time')
#     deadline = models.DateTimeField(verbose_name='deadline')
#     class Meta:
#         verbose_name = 'delay booth'
#         verbose_name_plural = verbose_name
#         ordering = ('-deadline',)
#     def __str__(self):
#         return self.rent_id

class unsubscribe(models.Model):
    status_choices = (
        ('checking', 'checking'),
        ('pass', 'pass'),
        ('refused', 'refused'),
        ('uncheck', 'uncheck')
    )
    booth_id = models.ForeignKey(booth, on_delete=models.CASCADE, verbose_name='booth id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user id',null=True)
    status_id = models.ForeignKey(booth_status, on_delete=models.CASCADE, verbose_name='booth id',null=True)
    status = models.CharField(max_length=28, verbose_name='status',choices=status_choices,default='uncheck',null=True)
    unsubscribe_time = models.DateTimeField(verbose_name='unsubscribe_time',null=True)
    class Meta:
        verbose_name = 'unsubscribe_booth'
        ordering = ('-unsubscribe_time',)
    def __str__(self):
        return 'booth_id' + '==>' + str(self.booth_id)
