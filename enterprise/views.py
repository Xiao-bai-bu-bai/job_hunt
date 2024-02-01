from django import forms
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from enterprise import models
from student.views import get_paginated_data


class EnterpriseModelForm(forms.ModelForm):
    class Meta:
        model = models.Enterprise
        fields = ['name', 'address', 'phone', 'email', 'password', 'limits', 'start_time', 'end_time']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


def enterprise_list(request):
    """企业列表"""
    enterprise_object = models.Enterprise.objects.all()
    cons = get_paginated_data(request, enterprise_object, 7)
    return render(request, "enterprise_list.html", locals())


def enterprise_query(request):
    """企业名称查询"""
    query = request.GET.get('qn')
    enterprise_object = models.Enterprise.objects.all()
    if query:
        enterprise_object = models.Enterprise.objects.filter(
            name__icontains=query
        )
    return render(request, "enterprise_list.html", {"enterprise_object": enterprise_object})


def enterprise_add(request):
    """添加企业"""
    if request.method == "GET":
        form = EnterpriseModelForm()
        return render(request, "enterprise_form.html", {"form": form})
    if request.method == "POST":
        form = EnterpriseModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "enterprise_form.html", {"form": form})
        form.save()
        return redirect("/enterprise/list/")
    return render(request, "enterprise_form.html")


def enterprise_edit(request):
    """编辑企业"""
    aid = request.GET.get('aid')
    enterprise_object = models.Enterprise.objects.filter(id=aid).first()
    if request.method == "GET":
        form = EnterpriseModelForm(instance=enterprise_object)
        return render(request, "enterprise_form.html", {"form": form})
    if request.method == "POST":
        form = EnterpriseModelForm(data=request.POST, instance=enterprise_object)
        if not form.is_valid():
            return render(request, "enterprise_form.html", {"form": form})
        form.save()
        return redirect("/enterprise/list/")
    return render(request, "enterprise_form.html")


def enterprise_delete(request):
    """删除企业"""
    aid = request.GET.get("aid")
    models.Enterprise.objects.filter(id=aid).delete()
    return redirect("/enterprise/list/")


def enterprise_check_resume(request):
    """企业查看简历列表"""
    # 获取登录的企业id
    enterprise_id = request.info_dict['enterprise_id']
    student_enterprise_object0 = models.StudentEnterprise.objects.filter(enterprise_id=enterprise_id, status=0).all()
    cons = get_paginated_data(request, student_enterprise_object0, 7)

    return render(request, "enterprise_check_resume.html", locals())


def enterprise_resume_pass(request):
    """简历通过"""
    aid = request.GET.get("aid")
    models.StudentEnterprise.objects.filter(id=aid).update(status=1)
    return redirect(reverse("enterprise_check_resume_name"))


def enterprise_resume_not_pass(request):
    """简历不通过"""
    aid = request.GET.get("aid")
    models.StudentEnterprise.objects.filter(id=aid).update(status=2)
    return redirect(reverse("enterprise_check_resume_name"))


def enterprise_resume_pass_list(request):
    """查看通过的简历列表"""
    enterprise_id = request.info_dict['enterprise_id']
    student_enterprise_object1 = models.StudentEnterprise.objects.filter(enterprise_id=enterprise_id, status=1).all()
    cons = get_paginated_data(request, student_enterprise_object1, 7)

    return render(request, "enterprise_resume_pass.html", locals())


def enterprise_resume_not_pass_list(request):
    """查看未通过的简历列表"""
    enterprise_id = request.info_dict['enterprise_id']
    student_enterprise_object2 = models.StudentEnterprise.objects.filter(enterprise_id=enterprise_id, status=2).all()
    cons = get_paginated_data(request, student_enterprise_object2, 7)

    return render(request, "enterprise_resume_not_pass.html", locals())