from django.http import HttpResponse
from django.shortcuts import render


def info(request):
    print('请求来了')
    return HttpResponse('hello world')

# Create your views here.
