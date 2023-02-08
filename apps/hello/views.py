from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from apps.hello import models


# Create your views here.

def test(request):  # 函数视图
    # 查询所有数据
    data = models.Student.objects.all()
    return HttpResponse(data)
