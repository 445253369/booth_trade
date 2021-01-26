from django.shortcuts import render, HttpResponse,redirect
from booth import models
from django.contrib.auth.decorators import login_required
from account import forms
from django.contrib.auth.models import User
from .utils import *
import datetime,pytz
from django.utils import timezone
# Create your views here.

def main(request):
    data = models.booth.objects.all().values()
    print(data)
    return render(request, 'main.html',{
        'data':data
    })

@login_required()
def booth(request):
    user_id = request.session['_auth_user_id']
    user_info = User.objects.filter(id=user_id).values()[0]
    booth_info = models.booth.objects.all()
    data = {
        'data':[],
        'user_info':user_info
    }
    for row in booth_info:
        if models.booth_status.objects.filter(booth_id_id=row.id).count() == 0 or models.booth_status.objects.filter(booth_id_id=row.id).first().is_deadline:
            try:
                type = row.booth_status_set.filter(booth_id_id=row.id).values()[0]['type']
                status = row.booth_status_set.filter(booth_id_id=row.id).values()[0]['status']
            except:
                type = 'renting'
                status = 'uncheck'
            try:
                deadline = row.booth_status_set.filter(booth_id_id=row.id).values()[0]['deadline'].date()
            except:
                deadline = datetime.datetime.now()
            if status == 'uncheck':
                data['data'].append([row.id,row.name,row.pictrue,row.description,row.area,row.price,row.position,type])
        else:
            models.booth_status.objects.filter(booth_id_id=row.id).update(type='renting',status='uncheck')
            data['data'].append([row.id, row.name, row.pictrue, row.description, row.area, row.price, row.position, type])
    page_count = len(data['data'])
    current_page_num = request.GET.get("page")
    pagination = Pagination(current_page_num, page_count, request, per_page_num=15)
    data['data'] = data['data'][pagination.start:pagination.end]
    data["pagination"]= pagination
    return render(request, 'booth.html',data)

@login_required()
def Renting(request,booth_id):
    user_id = request.session['_auth_user_id']
    user_info = User.objects.filter(id=user_id).values()[0]
    BoothId = models.booth.objects.filter(id=booth_id).first()
    user = User.objects.filter(id=user_id).first()
    if request.method == 'GET':
        return render(request, 'renting.html',{'booth_id':booth_id})
    else:
        start_time = datetime.datetime.strptime(request.POST.get('start-time'), '%Y-%m-%dT%H:%M')
        start_time = start_time.replace(tzinfo=pytz.timezone('UTC'))
        end_time = datetime.datetime.strptime(request.POST.get('end-time'), '%Y-%m-%dT%H:%M')
        end_time = end_time.replace(tzinfo=pytz.timezone('UTC'))
        if start_time < timezone.now() or end_time < timezone.now() or end_time < start_time or start_time=='' or end_time=='':
            return render(request, 'renting.html', {'msg':'the time you choose cannot early than now.please rechoose'})
        else:
            models.booth_status.objects.create(user_id_id=user.id,booth_id_id=BoothId.id,status='checking',type='rented',time=(end_time - start_time).days,deadline=end_time)
            return HttpResponse('You have submitted your application, please wait for the administrator to review')

def retrival(request):
    return render(request, 'retrival.html')