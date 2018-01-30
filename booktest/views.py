from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    hero = HeroInfo.objects.get(pk=2)
    context = {'hero':hero}
    return render(request, 'booktest/index.html',context)