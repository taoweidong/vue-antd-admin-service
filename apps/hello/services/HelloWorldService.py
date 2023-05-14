#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.core import serializers
from django.core.paginator import Paginator
from django.forms import model_to_dict

from apps.hello.models.StudentModel import StudentModel


class HelloWorldService(object):

    def __init__(self):
        pass

    @classmethod
    def query_data(cls, page, page_size):
        data = StudentModel.objects.all().order_by('id')
        page_data = Paginator(data, page_size)  # 进行分页
        result_data = page_data.page(page)  # 返回对应页码
        # article_list.num_pages 总页码数，article_list.page_range 下标从 1 开始的页数范围迭代器，article_list.count表示所有页面的对象总数
        result_list = []
        for i in result_data:
            result_list.append(model_to_dict(i))

        result = {
            "record": result_list,
            "total": data.count()
        }

        return result
