from django.db import models


class Admin(models.Model):
    username = models.CharField(verbose_name='管理员', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别',
                                 choices=[(1, '男'), (2, '女')],
                                 default=1)
    limits = models.IntegerField(verbose_name='权限',
                                 choices=[(0, '学生'), (1, '管理员'), (2, '企业')],
                                 default=1,
                                 )


class Major(models.Model):
    name = models.CharField(verbose_name='专业名称', max_length=32)

    def __str__(self):
        return self.name





