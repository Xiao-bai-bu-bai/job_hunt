from django.db import models
from school.models import Major


class Student(models.Model):
    Student_ID = models.IntegerField(verbose_name='学号', primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别',
                                 choices=[(1, '男'), (2, '女')],
                                 default=1)
    jianli = models.FileField(verbose_name='简历', upload_to='media/', blank=True, null=True)
    major = models.ForeignKey(
        verbose_name='专业',
        to='school.Major',
        on_delete=models.SET_NULL,
        null=True,  # 允许外键字段为空
        default=1  # 设置默认值为 None
    )
    limits = models.IntegerField(verbose_name='权限',
                                 choices=[(0, '学生'), (1, '管理员'), (2, '企业')],
                                 default=0,
                                 )


