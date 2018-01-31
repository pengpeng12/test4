#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    # hero = HeroInfo.objects.get(pk=2)
    # context = {'hero':hero}

    # list = HeroInfo.objects.filter(hname='ff')
    list = HeroInfo.objects.all()
    context = {'list':list}
    return render(request, 'booktest/index.html',context)

def show(request,text, id):
    context = {'text':text,'id':id}
    return render(request, 'booktest/show.html', context)

#用于练习模板的继承
def index2(request):
    return render(request, 'booktest/indexExtendBase.html')

def user1(request):
    return render(request, 'booktest/user1.html')

def user2(request):
    return render(request, 'booktest/user2.html')