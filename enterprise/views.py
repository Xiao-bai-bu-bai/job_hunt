from django import forms
from django.shortcuts import render, HttpResponse, redirect

from enterprise import models


class EnterpriseModelForm(forms.ModelForm):
    class Meta:
        model = models.Enterprise
        fields = ['name', 'address', 'phone', 'email', 'password', 'limits', 'start_time', 'end_time', 'major']
        # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


def enterprise_list(request):
    """企业列表"""
    enterprise_object = models.Enterprise.objects.all()
    return render(request, "enterprise_list.html", {"enterprise_object": enterprise_object})


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
