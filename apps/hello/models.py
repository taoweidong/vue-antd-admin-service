from django.db import models


class Student(models.Model):
    # id列，Django框架会默认生成id(自增，主键)，也可以通过AutoField类型自定义主键，不过Django框架默认生成ID列会失效
    # 用户名列，字符串类型，最大长度长度
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'tb_student'
