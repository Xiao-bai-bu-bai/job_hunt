import os
from django import forms
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect

from student import models
from enterprise.models import Enterprise
from student.models import Student


class StudentModelForm(forms.ModelForm):
    """学生表单"""

    class Meta:
        model = models.Student
        fields = ['Student_ID', 'name', 'password', 'age', 'gender', 'major', 'school', 'limits']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class EnterpriseResumeModelForm(forms.ModelForm):
    """投简历"""

    class Meta:
        model = models.Student
        fields = ['jianli']

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


def student_first_job_fair(request):
    """第一次招聘会的企业"""
    first_job_fair_object = Enterprise.objects.filter(start_time__gte="2023-07-01 00:00:00.000000",
                                                      end_time__lte="2023-11-02 00:00:00.000000")
    return render(request, "first_job_fair.html", {"first_job_fair_object": first_job_fair_object})


def student_second_job_fair(request):
    """第二次招聘会的企业"""
    second_job_fair_object = Enterprise.objects.filter(start_time__gte="2023-07-01 00:00:00.000000",
                                                       end_time__lte="2024-03-02 00:00:00.000000")
    return render(request, "second_job_fair.html", {"second_job_fair_object": second_job_fair_object})


def student_third_job_fair(request):
    """第三次招聘会的企业"""
    third_job_fair_object = Enterprise.objects.filter(start_time__gte="2023-07-01 00:00:00.000000",
                                                      end_time__lte="2024-07-02 00:00:00.000000")
    return render(request, "third_job_fair.html", {"third_job_fair_object": third_job_fair_object})


def student_upload_resume(request):
    """上传简历"""
    if request.method == "GET":
        form = EnterpriseResumeModelForm()
        return render(request, "send_resume.html", {"form": form})
    if request.method == "POST":
        rec_file = request.FILES.get('jianli')
        if not rec_file:
            return HttpResponse("请选择文件")

        file_path = os.path.join(settings.MEDIA_ROOT, "jianli", rec_file.name)
        with open(file_path, "wb") as f:
            for i in rec_file.chunks():  # 生成器chunks()方法是对文件进行分块读取，防止文件过大导致内存溢出
                f.write(i)

        # 上传的简历存储到Student表当前用户的jianli中
        student_id = request.info_dict['student_id']
        student_object = Student.objects.filter(Student_ID=student_id).first()
        student_object.jianli = rec_file
        student_object.save()

        return redirect("/student/list/")


# 查看简历
def student_check_resume(request):
    """查看简历"""
    student_id = request.info_dict['student_id']
    student_object = Student.objects.filter(Student_ID=student_id).first()
    file_path = student_object.jianli
    return render(request, "student_check_resume.html", {"file_path": file_path})


# 投递简历，把本人的简历复制一份，存储到以企业名称命名的文件夹中
def student_send_resume(request):
    """投递简历"""
    student_id = request.info_dict['student_id']
    student_object = Student.objects.filter(Student_ID=student_id).first()
    file_path = student_object.jianli
    aid = request.GET.get('aid')
    enterprise_object = Enterprise.objects.filter(id=aid).first()
    enterprise_name = enterprise_object.name
    print(enterprise_name)
    # 复制本人的简历文件到以企业名称命名的文件夹中
    new_file_path = os.path.join(settings.MEDIA_ROOT, enterprise_name, file_path.name).replace("\\", "/")
    with open(new_file_path, "wb") as f:
        for i in file_path.chunks():
            f.write(i)
    return HttpResponse("投递成功！")
