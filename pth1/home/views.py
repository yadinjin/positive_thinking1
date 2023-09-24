from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    # print(dir(request))
    # return HttpResponse("Привет мир!!!")
    return render(request, 'base.html')


def test(request):
    return HttpResponse("<h1>Тестовая страница</h1>")
