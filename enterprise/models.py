from django.db import models
from school.models import Major
from student.models import Student


class Enterprise(models.Model):
    name = models.CharField(verbose_name='企业名称', max_length=32)
    address = models.CharField(verbose_name='企业地址', max_length=32)
    phone = models.CharField(verbose_name='企业电话', max_length=32)
    email = models.CharField(verbose_name='企业邮箱', max_length=32)
    password = models.CharField(verbose_name='企业密码', max_length=64)
    limits = models.IntegerField(verbose_name='权限',
                                 choices=[(0, '学生'), (1, '管理员'), (2, '企业'), (3, '学校')],
                                 default=2,
                                 )
    start_time = models.DateTimeField(verbose_name='开始时间', null=True, blank=True)
    end_time = models.DateTimeField(verbose_name='结束时间', null=True, blank=True)
    major = models.ForeignKey(
        verbose_name='专业',
        to='school.Major',
        on_delete=models.SET_NULL,
        null=True,  # 允许外键字段为空
        default=1  # 设置默认值为 None
    )

    def __str__(self):
        return self.name


# 创建中间表连接Student表与enterorise表，如果通过则为1，否则为2，未被查看为0
class StudentEnterprise(models.Model):
    """学生企业表"""
    student = models.ForeignKey(
        verbose_name='学生',
        to='student.Student',
        on_delete=models.CASCADE,
        null=True,  # 允许外键字段为空
        default=1  # 设置默认值为 None
    )
    enterprise = models.ForeignKey(
        verbose_name='企业',
        to='Enterprise',
        on_delete=models.CASCADE,
        null=True,  # 允许外键字段为空
        default=1  # 设置默认值为 None
    )
    status = models.IntegerField(verbose_name='状态',
                                 choices=[(0, '未查看'), (1, '通过'), (2, '未通过')],
                                 default=0,
                                 )

    def __str__(self):
        return self.student.name + self.enterprise.name
