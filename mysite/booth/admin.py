from django.contrib import admin
from booth.models import booth,booth_status,unsubscribe
# Register your models here.

class booth_status_admin(admin.ModelAdmin):
    list_display = ('booth_id', 'user_id', 'status',)
    list_editable = ('status',)

class unsubscribe_admin(admin.ModelAdmin):
    list_display=('booth_id','status',)
    list_editable = ('status',)

admin.site.register(booth)
admin.site.register(booth_status,booth_status_admin)
admin.site.register(unsubscribe,unsubscribe_admin)

