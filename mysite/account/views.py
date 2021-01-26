from django.shortcuts import render,HttpResponse,redirect
from account import forms
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout, hashers
from django.contrib.auth.decorators import login_required
from booth import models
import datetime
from django.utils import timezone
import pytz
from django.db.models import Q
# Create your views here


def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        obj = forms.LoginForm(request.POST)
        if obj.is_valid():
            obj = obj.cleaned_data
            user = authenticate(request, username=obj['username'], password = obj['password'])
            userid = User.objects.filter(username=obj['username']).values()[0]['id']
            if user is not None:
                print(userid)
                login(request, user)
                return redirect('/booth/')
            else:
                return render(request, 'login.html', {'msg':'User name or password is wrong, please try again'})
        else:
            return render(request, 'login.html', {'obj':obj})

def register(request):
    if request.method == 'POST':
        obj = forms.RegisterForm(request.POST)
        if obj.is_valid(): #合法验证
            username = obj.cleaned_data['username']
            password = obj.cleaned_data['password']
            if not User.objects.filter(username=username).exists(): #数据库中没有这个用户名
                new_user = User.objects.create_user(username=username,password=password)
                return redirect('/account/login/')
            else: #数据库中有这个用户名
                user = User.objects.get(username=username)
                if user:
                    return render(request, 'login.html',{'msg':'The user name already exists. Please try to log in or change it!'})
        else:
            return render(request, 'register.html', {'obj':obj})
    else:
        return render(request,'register.html')

@login_required()
def center(request):
    user_id = request.session['_auth_user_id']
    booth_statu = models.booth_status.objects.filter(user_id_id=user_id)
    data = {
        'data':[]
    }
    for row in booth_statu:
        booth_con = models.booth.objects.filter(id=row.booth_id_id).first()
        unsubscribe_con = models.unsubscribe.objects.filter(booth_id=row.booth_id_id)
        rest_time = row.deadline - timezone.now()
        if unsubscribe_con.count() == 0:
            data['data'].append([booth_con.id,booth_con.name,booth_con.price,row.status,row.deadline,rest_time,'uncheck'])
        else:
            print(unsubscribe_con.first().status)
            data['data'].append([booth_con.id, booth_con.name, booth_con.price, row.status, row.deadline, rest_time,unsubscribe_con.first().status])
        # print(data['data'][0])
    # con = Q()
    # con.connector = 'OR'
    # for row in booth_statu:
    #     con.children.append(('id',row.booth_id_id))
    # booth_info = models.booth.objects.filter(con)
    # print(booth_info)
    # data = {
    #     'booth_statu':booth_statu,
    #     'booth_info':booth_info
    # }
    # for row in booth_statu:
    #     print(row.id,row.status,row.type,row.time,row.deadline,row.booth_id_id,row.user_id_id,models.booth.objects.filter(id=row.booth_id_id))
    #     for ele in models.booth.objects.filter(id=row.booth_id_id):
    #         print(ele.id,ele.name,ele.pictrue,ele.description,ele.area,ele.price,ele.position,ele.create_at)
    return render(request, 'center.html',data)

@login_required()
def renewal(request,booth_id):
    deadline = models.booth_status.objects.filter(booth_id_id=booth_id).first().deadline
    if request.method == 'GET':
        return render(request, 'templates/renewal.html',{'booth_id':booth_id,'deadline':deadline})
    else:
        # start_time = datetime.datetime.strptime(request.POST.get('start-time'), '%Y-%m-%dT%H:%M')
        # start_time = start_time.replace(tzinfo=pytz.timezone('UTC'))
        end_time = datetime.datetime.strptime(request.POST.get('end-time'), '%Y-%m-%dT%H:%M')
        end_time = end_time.replace(tzinfo=pytz.timezone('UTC'))
        if end_time < timezone.now() or end_time=='':
            return render(request, 'templates/renewal.html', {'msg':'the time you choose cannot early than now.please rechoose','booth_id':booth_id,'deadline':deadline})
        elif end_time < deadline:
            return render(request, 'templates/renewal.html', {'msg':'the time you choose cannot early than deadline.please rechoose','booth_id':booth_id,'deadline':deadline})
        else:
            models.booth_status.objects.filter(booth_id=booth_id).update(deadline=end_time,time=(end_time-timezone.now()).days)
            return HttpResponse('renewal sucesse!')

@login_required()
def unsubscribe(request,booth_id):
    deadline = models.booth_status.objects.filter(booth_id_id=booth_id).first().deadline
    BoothId = models.booth.objects.filter(id=booth_id).first()
    print(BoothId)
    if request.method == 'GET':
        return render(request, 'templates/unsubscribe.html',{'booth_id':booth_id,'deadline':deadline})
    else:
        unsubscribe_time = datetime.datetime.strptime(request.POST.get('unsubscribe-time'), '%Y-%m-%dT%H:%M')
        unsubscribe_time = unsubscribe_time.replace(tzinfo=pytz.timezone('UTC'))
        if unsubscribe_time > deadline or unsubscribe_time=='':
            return render(request, 'templates/unsubscribe.html',{'booth_id':booth_id,'deadline':deadline,'msg':'you choosed a wrong time.please rechoose'})
        else:
            models.unsubscribe.objects.create(booth_id=BoothId,user_id=request.user,status='checking',unsubscribe_time=unsubscribe_time)
            return HttpResponse('unsubscribe successe.we are checking your application')

@login_required()
def change_password(request):
    if request.method == 'GET':
        return render(request, 'pwdoperate.html')
    else:
        user = request.user
        user_id = request.session['_auth_user_id']
        new_pwd = request.POST.get('password')
        print(user_id,new_pwd)
        if new_pwd == User.objects.filter(id=user_id):
            return render(request,'pwdoperate.html',{'msg':'input-password must diffrent from old'})
        else:
            if 5 < len(new_pwd) < 19:
                user.password = hashers.make_password(new_pwd)
                user.save()
                return redirect('/account/login/')
            else:
                return render(request, 'pwdoperate.html', {'msg': 'input-password must has o length of 6-18'})
@login_required()
def logout(request):
    auth_logout(request)
    return HttpResponse('<script>window.alert("注销成功!");location.href="/"</script>')