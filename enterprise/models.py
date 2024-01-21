from django.db import models
from school.models import Major


class Enterprise(models.Model):
    name = models.CharField(verbose_name='企业名称', max_length=32)
    address = models.CharField(verbose_name='企业地址', max_length=32)
    phone = models.CharField(verbose_name='企业电话', max_length=32)
    email = models.CharField(verbose_name='企业邮箱', max_length=32)
    password = models.CharField(verbose_name='企业密码', max_length=64)
    jianli = models.FileField(verbose_name='简历', upload_to='jianli/', blank=True, null=True)
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
