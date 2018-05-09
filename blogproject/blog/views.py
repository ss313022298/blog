from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse('welcome my blog')
    return render(request, 'index.html', {'title':'你好', 'welcome':'welcome my blog'})