from django import forms
from django.shortcuts import render, HttpResponse, redirect

from student import models


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


def student_list(request):
    """学生列表"""
    students_object = models.Student.objects.all()
    return render(request, "student_list.html", {"students_object": students_object})


def student_query(request):
    """学生姓名查询"""
    query = request.GET.get('qn')
    students_object = models.Student.objects.all()
    if query:
        students_object = models.Student.objects.filter(
            name__icontains=query
        )
    return render(request, "student_list.html", {"students_object": students_object})


def student_add(request):
    """添加学生"""
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, "student_form.html", {"form": form})
    if request.method == "POST":
        form = StudentModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "student_form.html", {"form": form})
        form.save()
        return redirect("/student/list/")


def student_edit(request):
    """编辑学生"""
    aid = request.GET.get('aid')
    student_object = models.Student.objects.filter(Student_ID=aid).first()
    if request.method == "GET":
        form = StudentModelForm(instance=student_object)
        return render(request, "student_form.html", {"form": form})
    if request.method == "POST":
        form = StudentModelForm(data=request.POST, instance=student_object)
        if not form.is_valid():
            return render(request, "student_form.html", {"form": form})
        form.save()
        return redirect("/student/list/")


def student_delete(request):
    """删除学生"""
    aid = request.GET.get("aid")
    models.Student.objects.filter(Student_ID=aid).delete()
    return redirect("/student/list/")