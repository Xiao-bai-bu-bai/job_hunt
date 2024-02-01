"""job_hunt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from job_hunt import settings
from school import views as school_views
from student import views as student_views
from enterprise import views as enterprise_views

urlpatterns = [
    # 配置上传文件的访问处理函数
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    path("admin/", admin.site.urls),
    path("login/", school_views.login, name='login_name'),  # 登录
    path("home/", school_views.home, name='home_name'),  # 首页
    path("major/list/", school_views.major_list, name='major_list_name'),  # 专业列表
    path("logout/", school_views.logout, name='logout_name'),  # 退出登录
    path("major/query/", school_views.major_query, name='major_query_name'),  # 专业名称查询
    path("major/add/", school_views.major_add, name='major_add_name'),  # 添加专业
    path("major/edit/", school_views.major_edit, name='major_edit_name'),  # 编辑专业
    path("major/delete/", school_views.major_delete, name='major_delete_name'),  # 删除专业
    path("student/logon/", school_views.student_logon, name='student_logon_name'),  # 学生注册
    path("enterprise/logon/", school_views.enterprise_logon, name='enterprise_logon_name'),  # 企业注册
    path("school/list/", school_views.school_list, name='school_list_name'),  # 学校列表
    path("school/add/", school_views.school_add, name='school_add_name'),  # 添加学校
    path("school/edit/", school_views.school_edit, name='school_edit_name'),  # 编辑学校
    path("school/delete/", school_views.school_delete, name='school_delete_name'),  # 删除学校
    path("school/query/", school_views.school_query, name='school_query_name'),  # 学校名称查询
    path("school/student/list/", school_views.school_student_list, name='school_student_list_name'),  # 学校学生列表
    path("school/student/add/", school_views.school_student_add, name='school_student_add_name'),  # 学校学生添加
    path("school/student/edit/", school_views.school_student_edit, name='school_student_edit_name'),  # 学校学生编辑
    path("school/major/list/", school_views.school_major_list, name='school_major_list_name'),  # 学校专业列表
    path("school/major/add/", school_views.school_major_add, name='school_major_add_name'),  # 学校专业添加
    path("school/major/edit/", school_views.school_major_edit, name='school_major_edit_name'),  # 学校专业编辑
    path("school/major/query/", school_views.school_major_query, name='school_major_query_name'),  # 学校专业名称查询

    # 学校企业列表
    path("school/enterprise/list/", school_views.school_enterprise_list, name='school_enterprise_list_name'),  # 学校企业列表
    path("school/enterprise/add/", school_views.school_enterprise_add, name='school_enterprise_add_name'),  # 学校企业添加
    path("school/enterprise/edit/", school_views.school_enterprise_edit, name='school_enterprise_edit_name'),  # 学校企业编辑
    path("school/enterprise/query/", school_views.school_enterprise_query, name='school_enterprise_query_name'),
    # 学校企业名称查询
    path("school/enterprise/delete/", school_views.school_enterprise_delete, name='school_enterprise_delete_name'),
    # 学校企业删除
    # path("admin/school/enterprise/list/", school_views.admin_school_enterprise_list, name='admin_school_enterprise_list_name'),  # 管理员学校企业列表

    path("student/list/", student_views.student_list, name='student_list_name'),  # 学生列表
    path("student/query/", student_views.student_query, name='student_query_name'),  # 学生名称查询
    path("student/add/", student_views.student_add, name='student_add_name'),  # 添加学生
    path("student/edit/", student_views.student_edit, name='student_edit_name'),  # 编辑学生
    path("student/delete/", student_views.student_delete, name='student_delete_name'),  # 删除学生
    path("student/first/job/fair/", student_views.student_first_job_fair, name='student_first_job_fair_name'),  # 第一次招聘会
    path("student/second/job/fair/", student_views.student_second_job_fair, name='student_second_job_fair_name'),
    # 第二次招聘会
    path("student/third/job/fair/", student_views.student_third_job_fair, name='student_third_job_fair_name'),  # 第三次招聘会
    # path("student/send/resume/", student_views.student_send_resume, name='student_send_resume_name'),  # 学生投递简历
    path("student/upload/resume/", student_views.student_upload_resume, name='student_upload_resume_name'),  # 学生上传简历
    path("student/check/resume", student_views.student_check_resume, name='student_check_resume_name'),  # 学生查看简历
    path("student/send/resume/", student_views.student_send_resume, name='student_send_resume_name'),  # 学生投递简历

    path("enterprise/list/", enterprise_views.enterprise_list, name='enterprise_list_name'),  # 企业列表
    path("enterprise/query/", enterprise_views.enterprise_query, name='enterprise_query_name'),  # 企业名称查询
    path("enterprise/add/", enterprise_views.enterprise_add, name='enterprise_add_name'),  # 添加企业
    path("enterprise/edit/", enterprise_views.enterprise_edit, name='enterprise_edit_name'),  # 编辑企业
    path("enterprise/delete/", enterprise_views.enterprise_delete, name='enterprise_delete_name'),  # 删除企业
    path("enterprise/check/resume/", enterprise_views.enterprise_check_resume, name='enterprise_check_resume_name'),  # 企业查看简历
    path("enterprise/resume/pass/", enterprise_views.enterprise_resume_pass, name='enterprise_resume_pass_name'),  # 简历通过
    path("enterprise/resume/not/pass/", enterprise_views.enterprise_resume_not_pass, name='enterprise_resume_not_pass_name'),  # 简历未通过
    path("enterprise/resume/pass/list/", enterprise_views.enterprise_resume_pass_list, name='enterprise_resume_pass_list_name'),  # 查看通过的简历
    path("enterprise/resume/not/pass/list/", enterprise_views.enterprise_resume_not_pass_list, name='enterprise_resume_not_pass_list_name'),  # 查看未通过的简历

]