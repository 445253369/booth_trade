from django.contrib import admin
from django.db import transaction

from .models import *

admin.site.site_header = 'Farm Booth Booking System'
admin.site.site_title = 'Farm Booth Booking System'


# Register your models here.

@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('status',)
    list_display = ('name', 'description', 'area', 'position', 'price', 'create_at', 'status')


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('booth', 'user', 'create_at', 'deadline', 'status',)


@transaction.atomic
def approve_unsubscribe(modeladmin, request, queryset):
    """
    同意退订
    :param modeladmin:
    :param request:
    :param queryset:
    :return:
    """
    qs = queryset.filter(status='wait to approve')

    for q in qs:
        print(q)
        q.rent.booth.status = 'wait to rent'
        q.rent.booth.save()
        q.rent.status = 'unsubscribed'
        q.rent.save()
    qs.update(status='approve')
    message = 'ok'
    modeladmin.message_user(request, message)


approve_unsubscribe.short_description = 'approve'


@admin.register(Unsubscribe)
class UnsubscribeAdmin(admin.ModelAdmin):
    """
    退订
    """
    actions = [approve_unsubscribe, ]
    list_filter = ('status',)
    list_display = ('rent', 'create_at', 'status', 'update_time', 'is_from_delay')


@admin.register(Delay)
class DelayAdmin(admin.ModelAdmin):
    """
    延期
    """
    list_display = ('rent', 'create_at', 'deadline',)
