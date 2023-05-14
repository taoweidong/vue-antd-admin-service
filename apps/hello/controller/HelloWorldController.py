#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from apps.hello import models
from apps.hello.services.HelloWorldService import HelloWorldService


# Create your views here.

def test(request):  # 函数视图
    # 查询所有数据
    print("页面请求进来了，查询数据")
    # data = models.Student.objects.all()
    result = {
        "msg": 'Hello World',
        "message": '恭喜你后台服务接口配置正常，可以访问了~~~~~~~~~~~~~~~~~~~~~~~'
    }
    return JsonResponse({"data": result, "code": 200, "message": "获取数据成功"})


@require_http_methods(['GET', 'POST'])
def welcome(request):  # 函数视图
    # 查询所有数据
    print("页面请求进来了，查询数据")
    result = {
        "timeFix": '@TIMEFIX',
        "message": '@WELCOME'
    }
    return JsonResponse({"data": result, "code": 200, "message": "获取数据成功"})


@require_http_methods(['GET'])
def activity(request):
    result = {

    }
    return JsonResponse({"data": result, "code": 200, "message": "获取数据成功"})


@require_http_methods(['GET', 'POST'])
def auth_login(request):
    """
    管理员用户登录
    :param request: 从前端框架传过来的请求
    :return: 按这种格式返回
    """
    print(request.body)
    result = {
        'id': 1,
        'name': 'name',
        'permissions': [{"id": 'queryForm', "operation": ['add', 'edit']}],
        'roles': [{"id": 'admin', "operation": ['add', 'edit', 'delete']}],
        'user': {
            "name": 'admin',
            'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png',
            "address": '@CITY',
            "position": '@POSITION'
        },
        'lastLoginIp': '27.154.74.117',
        # 设置token过期时间
        'expireAt': datetime.datetime.now() + datetime.timedelta(hours=2),
        # 'expireAt': datetime.datetime.now() + datetime.timedelta(minutes=5),
        'token': 'Authorization:4291d7da9005377ec9aec4a71ea837f'
    }
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})


@require_http_methods(['GET', 'POST'])
def list(request):
    result = [
        {"id": " 10001", " name": " Test1", " nickname": " T1", " role": " Develop", " sex": " 0", " sex2": "1",
         " num1": " 40", " age": " 28", " address": " Shenzhen", " date12": " ", " date13": " "},
        {"id": " 10002", " name": " Test2", " nickname": " T2", " role": " Designer", " sex": " 1", " sex2": "1",
         " num1": " 44", " age": " 22", " address": " Guangzhou", " date12": " ", " date13": " 2020-08-20"},
        {"id": " 10003", " name": " Test3", " nickname": " T3", " role": " Test", " sex": " 0", " sex2": "1",
         " num1": " 200", " age": " 32", " address": " test abc", " date12": " 2020-09-10", " date13": " "},
        {"id": " 10004", " name": " Test4", " nickname": " T4", " role": " Designer", " sex": " 1", " sex2": "1",
         " num1": " 30", " age": " 23", " address": " Shenzhen", " date12": " ", " date13": " 2020-12-04"},
        {"id": " 10005", " name": " Test5", " nickname": " T5", " role": " Develop", " sex": " 0", " sex2": " 1",
         " num1": " 20", " age": " 30", " address": " Shanghai", " date12": " 2020-09-20", " date13": "  "},
        {"id": " 10006", " name": " Test6", " nickname": " T6", " role": " Designer", " sex": " 1", " sex2": "1",
         " num1": " 10", " age": " 21", " address": " Shenzhen", " date12": " ", " date13": "  "},
        {"id": " 10007", " name": " Test7", " nickname": " T7", " role": " Develop", " sex": " 0", " sex2": "1",
         " num1": " 5", " age": " 29", " address": " test abc", " date12": " 2020-01-02", " date13": " 2020-09-20 "},
        {"id": " 10008", " name": " Test8", " nickname": " T8", " role": " PM", " sex": " 1", " sex2": "1",
         " num1": " 2", " age": " 35", " address": " Shenzhen", " date12": " ", " date13": " "}
    ]
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})


@require_http_methods(['GET', 'POST'])
def goods(request):
    page = request.GET.get('currentPage', 1)
    page_size = request.GET.get('pageSize', 10)
    result = HelloWorldService.query_data(page, page_size)
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})


@require_http_methods(['GET', 'POST'])
def columns(request):
    result = {

    }
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})
