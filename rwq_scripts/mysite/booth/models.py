import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Booth(models.Model):
    """
    摊位表
    """
    name = models.CharField(max_length=32, verbose_name='name')
    picture = models.ImageField(upload_to='boothes')
    description = models.TextField(verbose_name='detail')
    area = models.FloatField(verbose_name='area')
    price = models.FloatField(verbose_name='price')
    position = models.CharField(max_length=64, verbose_name='position')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='online time')

    # 当前摊位信息的状态
    # TODO status 未出租|已出租
    STATUS_CHOICES = (
        ('wait to rent', 'wait to rent'),
        ('rented', 'rented'),
    )
    status = models.CharField(max_length=32, verbose_name='status', choices=STATUS_CHOICES, default='wait to rent')
    update_time = models.DateTimeField(verbose_name='update time', auto_now=True)  # 更新时间

    class Meta:
        verbose_name = 'booth'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return str(self.name)


class Rent(models.Model):
    """
    租赁
    """
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE, verbose_name='Booth')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Booth')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='rent time')
    deadline = models.DateField(verbose_name='deadline')
    STATUS_CHOICES = (
        ('normal', 'normal'),
        ('apply to unsubscribe', 'apply to unsubscribe'),
        ('unsubscribed', 'unsubscribed'),
        ('delayed', 'delayed'),
    )
    status = models.CharField(max_length=32, verbose_name='status', choices=STATUS_CHOICES, default='normal')  # 退订的时候需要管理员去审核

    @property
    def is_deadline(self):
        """
        是否在截止日期
        :return:
        """
        return datetime.datetime.now().date() >= self.deadline

    @property
    def current_status(self):
        """
        当前的状态
        1. 租赁中
        2. 已申请提起退租
        3. 退租成功
        4. 继续延期
        :return:
        """
        pass
        # TODO

    class Meta:
        verbose_name = 'rent'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return f'{self.booth.name} - {self.user.username} - {self.create_at}'


class Unsubscribe(models.Model):
    """
    退订信息表
    """
    rent = models.OneToOneField(Rent, on_delete=models.CASCADE, verbose_name='rent info')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='rent time')
    STATUS_CHOICES = (
        ('wait to approve', 'wait to approve'),
        ('approve', 'approve'),
    )
    status = models.CharField(max_length=32, verbose_name='status', choices=STATUS_CHOICES)  # 退订的时候需要管理员去审核
    update_time = models.DateTimeField(verbose_name='update time', auto_now=True)  # 更新时间
    is_from_delay = models.BooleanField(verbose_name='is from delay', default=False) # 是否来自延期
    class Meta:
        verbose_name = 'subscribe'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return str(self.rent)


class Delay(models.Model):
    """
    延期|续租
    """
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, verbose_name='rent info')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='create time')
    deadline = models.DateField(verbose_name='deadline') # 延期时间

    class Meta:
        verbose_name = 'delay'
        verbose_name_plural = verbose_name
        ordering = ('-create_at',)

    def __str__(self):
        return str(self.rent)

