from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import *


def index(request):
    return render(request,'index.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def posts(request):

    context = {'posts':Post.objects.all(),'category':Category.objects.all()}
    return render(request,'blogs.html',context)




