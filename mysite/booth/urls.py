from django.urls import path
from booth import views

app_name='booth_view'

urlpatterns = [
    path('',views.booth,name='BoothRenting'),
    path('renting/<int:booth_id>',views.Renting,name="RentingId"),
    path('retrival/',views.retrival,name='retrival')
]