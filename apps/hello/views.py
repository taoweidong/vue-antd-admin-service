# Create your views here.
import datetime

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from apps.hello import models


# Create your views here.

def test(request):  # 函数视图
    # 查询所有数据
    print("页面请求进来了，查询数据")
    # data = models.Student.objects.all()
    return HttpResponse("Hello World")


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
    result = {

    }
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})


@require_http_methods(['GET', 'POST'])
def goods(request):
    result = {

    }
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})


@require_http_methods(['GET', 'POST'])
def columns(request):
    result = {

    }
    return JsonResponse({"data": result, "code": 200, "message": "登录成功"})
