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


#html转义
def htmlTest(request):
    context={'t1':'<h1>123</h1>'}
    return render(request,'booktest/htmlTest.html',context)

#csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

#验证码
def verifyCode(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    #创建背景色
    bgColor = (random.randrange(50,100),random.randrange(0,50),random.randrange(0,90))
    #规定宽高
    width = 100
    height = 25
    #创建画布
    image = Image.new('RGB',(width,height),bgColor)
    #构造字体对象
    font = ImageFont.truetype('Arial.ttf', 24)
    #创建画笔
    draw = ImageDraw.Draw(image)
    #创建文本内容
    text = '0123ABCD'
    # 逐个绘制字符
    textTemp = ''
    for i in range(4):
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp += textTemp1
        draw.text((i*25,0),
                  textTemp1,
                  (255, 255, 255),
                  font)
    request.session['code'] = textTemp
    #保存到内存流中
    import io
    buf = io.BytesIO()
    image.save(buf,'png')
    #将内存流中的内容输出到客户端
    return HttpResponse(buf.getvalue(), 'image/png')

def verifyTest1(request):
    return render(request, 'booktest/verifyTest1.html')

def verifyTest2(request):
    code1 = request.POST['code1']
    code2 = request.session['code']
    if code1==code2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')