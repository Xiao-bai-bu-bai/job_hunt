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
from django.urls import path
from school import views as school_views
from student import views as student_views
from enterprise import views as enterprise_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", school_views.login, name='login_name'),
    path("home/", school_views.home, name='home_name'),
    path("major/list/", school_views.major_list, name='major_list_name'),
    path("logout/", school_views.logout, name='logout_name'),
    path("major/query/", school_views.major_query, name='major_query_name'),
    path("major/add/", school_views.major_add, name='major_add_name'),
    path("major/edit/", school_views.major_edit, name='major_edit_name'),
    path("major/delete/", school_views.major_delete, name='major_delete_name'),
    # path("add/", school_views.add),
    path("student/logon/", school_views.student_logon, name='student_logon_name'),
    path("enterprise/logon/", school_views.enterprise_logon, name='enterprise_logon_name'),


    path("student/list/", student_views.student_list, name='student_list_name'),
    path("student/query/", student_views.student_query, name='student_query_name'),
    path("student/add/", student_views.student_add, name='student_add_name'),
    path("student/edit/", student_views.student_edit, name='student_edit_name'),
    path("student/delete/", student_views.student_delete, name='student_delete_name'),
    path("student/first/job/fair/", student_views.student_first_job_fair, name='student_first_job_fair_name'),
    path("student/second/job/fair/", student_views.student_second_job_fair, name='student_second_job_fair_name'),
    path("student/third/job/fair/", student_views.student_third_job_fair, name='student_third_job_fair_name'),
    path("student/send/resume/", student_views.student_send_resume, name='student_send_resume_name'),


    path("enterprise/list/", enterprise_views.enterprise_list, name='enterprise_list_name'),
    path("enterprise/query/", enterprise_views.enterprise_query, name='enterprise_query_name'),
    path("enterprise/add/", enterprise_views.enterprise_add, name='enterprise_add_name'),
    path("enterprise/edit/", enterprise_views.enterprise_edit, name='enterprise_edit_name'),
    path("enterprise/delete/", enterprise_views.enterprise_delete, name='enterprise_delete_name'),

]
