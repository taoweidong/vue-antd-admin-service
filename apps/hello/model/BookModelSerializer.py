# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2023/2/5 21:04
# @Author    :Taoweidong
from rest_framework.serializers import ModelSerializer

from apps.hello.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
