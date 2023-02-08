from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request):  # 函数视图
    return HttpResponse("Hello world!")
