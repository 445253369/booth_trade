import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .filters import *


# Create your views here.
def index(request):
    """
    首页
    :param request:
    :return:
    """
    latest = Booth.objects.all()[:4]
    return render(request, 'booth/index.html', {'latest': latest})


def detail(request, bid):
    """
    详情
    :param request:
    :return:
    """
    booth = get_object_or_404(Booth, id=bid)
    return render(request, 'booth/detail.html', {'booth': booth})


def search(request):
    """
    检索
    :param request:
    :return:
    """
    # TODO PAGE

    f = BoothFilter(request.GET, queryset=Booth.objects.all())
    return render(request, 'booth/search.html', {'filter': f})


@transaction.atomic
@login_required
def rent(request):
    """
    出租
    :param request:
    :param bid:
    :return:
    """
    bid = request.POST.get('bid')
    booth = get_object_or_404(Booth, id=bid)
    if booth.status == 'rented':
        messages.error(request, 'already rented')
        return redirect('/')
    booth.status = 'rented'
    booth.save()
    rent = Rent(booth=booth, user=request.user)
    rent.deadline = request.POST.get('deadline')
    rent.save()
    messages.success(request, 'You have rented it !')
    return redirect('/')


@transaction.atomic
@login_required
def unsubscribe(request, rid):
    """
    退订
    :param request:
    :return:
    """
    rent = get_object_or_404(Rent, id=rid)
    if rent.deadline < datetime.datetime.now().date():
        messages.error(request, 'your rent is out of time!')
        redirect('/account/center')
    else:
        rent.status = 'apply to unsubscribe'
        rent.save()
        unsub = Unsubscribe(rent=rent)
        _from = request.GET.get('from', '-1')
        if _from == 'delay':
            unsub.is_from_delay = True
        unsub.status = 'wait to approve'
        unsub.save()
        messages.success(request, 'action ok!')
        return redirect('/account/center')


@transaction.atomic
@login_required
def cancel_ubsub(request, cid):
    # TODO 从delay到退订的逻辑
    """
    delay->unsubscribe


    :param request:
    :param cid:
    :return:
    """
    ubsub = get_object_or_404(Unsubscribe, id=cid)

    if ubsub.is_from_delay: # 来自续租
        ubsub.rent.status = 'delayed'
    else:
        ubsub.rent.status = 'normal'

    ubsub.rent.save()
    ubsub.delete()
    messages.success(request, 'cancel ok!')
    return redirect('/account/center/')


@transaction.atomic
@login_required
def delay(request, rid):
    """
    延期
        rent: normal状态下可以
    :param request:
    :param rid:
    :return:
    """
    rent = get_object_or_404(Rent, id=rid)
    if rent.status != 'normal':
        messages.error(request, f'this rent info is {rent.status}, can not delay!')
        return redirect('/account/center/')
    if request.method == 'GET':
        return render(request, 'booth/delay.html', {'rent': rent, 'booth': rent.booth})
    elif request.method == 'POST':
        d = Delay(rent=rent)
        deadline = request.POST.get('deadline')
        # rent信息更新
        rent.status = 'delayed'
        rent.deadline = deadline
        rent.save()
        # # booth信息更新
        # booth = rent.booth
        # booth.deadline = deadline
        # booth.save()
        # delay更新
        d.deadline = deadline
        d.save()
        messages.success(request, 'delay ok!')
        return redirect('/account/center/')
