from django.db import models


class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name='管理员', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别',
                                 choices=[(1, '男'), (2, '女')],
                                 default=1)
    limits = models.IntegerField(verbose_name='权限',
                                 choices=[(0, '学生'), (1, '管理员'), (2, '企业'), (3, '学校')],
                                 default=1,
                                 )


class Major(models.Model):
    """专业表"""
    name = models.CharField(verbose_name='专业名称', max_length=32, unique=False)

    def __str__(self):
        return self.name


class School(models.Model):
    """学校表"""
    name = models.CharField(verbose_name='学校名称', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64, default='123')
    address = models.CharField(verbose_name='学校地址', max_length=32)
    limits = models.IntegerField(verbose_name='权限',
                                 choices=[(0, '学生'), (1, '管理员'), (2, '企业'), (3, '学校')],
                                 default=3,
                                 )

    def __str__(self):
        return self.name


class SchoolMajor(models.Model):
    """学校专业表"""
    school = models.ForeignKey(verbose_name='学校',
                               to='School',
                               on_delete=models.CASCADE,
                               default=1  # 设置默认值为 None
                               )
    major = models.ForeignKey(verbose_name='专业',
                              to='Major',
                              on_delete=models.CASCADE,
                              default=1  # 设置默认值为 None
                              )

    def __str__(self):
        return self.school.name + self.major.name


class SchoolEnterprise(models.Model):
    """学校企业表"""
    school = models.ForeignKey(verbose_name='学校',
                               to='School',
                               on_delete=models.CASCADE,
                               null=True,  # 允许外键字段为空
                               default=1  # 设置默认值为 None
                               )
    enterprise = models.ForeignKey(verbose_name='企业',
                                   to='enterprise.Enterprise',
                                   on_delete=models.CASCADE,
                                   null=True,  # 允许外键字段为空
                                   default=1  # 设置默认值为 None
                                   )

    def __str__(self):
        return self.school.name + self.enterprise.name
