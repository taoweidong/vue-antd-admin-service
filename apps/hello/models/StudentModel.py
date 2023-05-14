#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from django.db import models


class StudentModel(models.Model):
    # id列，Django框架会默认生成id(自增，主键)，也可以通过AutoField类型自定义主键，不过Django框架默认生成ID列会失效
    # 用户名列，字符串类型，最大长度长度
    id = models.AutoField(primary_key=True, verbose_name="主键ID")
    name = models.CharField(max_length=255, verbose_name="名称")
    role = models.CharField(max_length=50, verbose_name="角色")
    email = models.CharField(max_length=255, verbose_name="email")
    nickname = models.CharField(max_length=255, verbose_name="别名")
    sex = models.CharField(max_length=50, verbose_name="性别")
    age = models.CharField(max_length=50, verbose_name="年龄")
    amount = models.IntegerField(max_length=10, verbose_name="数量")
    updateDate = models.CharField(max_length=255, verbose_name="更新时间")
    createDate = models.CharField(max_length=255, verbose_name="创建时间")

    class Meta:
        db_table = 'tb_student'
