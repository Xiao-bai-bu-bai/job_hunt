from django import forms
from django.shortcuts import render, HttpResponse, redirect

from school import models
from student.models import Student
from enterprise.models import Enterprise
from school.models import Major as SM
from school.models import SchoolMajor as M


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': "form-control", "placeholder": '输入用户名'})
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '输入密码'}, render_value=True)
    )


class StudentModelForm(forms.ModelForm):
    """学生注册表单"""

    class Meta:
        model = Student
        fields = ['Student_ID', 'password', 'name', 'age', 'gender', 'major']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class EnterpriseModelForm(forms.ModelForm):
    """企业注册表单"""

    class Meta:
        model = Enterprise
        fields = ['name', 'password', 'address', 'phone', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class SchoolMajorModelForm(forms.ModelForm):
    """专业表单"""

    class Meta:
        model = models.Major
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class MajorModelForm(forms.ModelForm):
    """学校专业表单"""

    class Meta:
        model = models.SchoolMajor
        fields = ['school', 'major']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class SchoolModelForm(forms.ModelForm):
    """学校表单"""

    class Meta:
        model = models.School
        fields = ['name', 'address', 'limits', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class SchoolStudentModelForm(forms.ModelForm):
    """学校学生表单"""

    class Meta:
        model = Student
        fields = ['name', 'password', 'age', 'gender', 'major']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


class SchoolEnterpriseModelForm(forms.ModelForm):
    """学校企业表单"""

    class Meta:
        model = models.SchoolEnterprise
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 自定义操作，找到所有的字段
        for name, field_object in self.fields.items():
            field_object.widget.attrs = {"class": 'form-control'}


def login(request):
    """用户登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    form = LoginForm(data=request.POST)
    if request.method == "POST":
        if not form.is_valid():
            return render(request, "login.html", {'form': form})

    user = form.cleaned_data['username']
    pwd = form.cleaned_data['password']
    admin_object = models.Admin.objects.filter(username=user, password=pwd).first()
    student_object = Student.objects.filter(name=user, password=pwd).first()
    enterprise_object = Enterprise.objects.filter(name=user, password=pwd).first()
    school_object = models.School.objects.filter(name=user, password=pwd).first()

    user_info = {}  # 定义一个空字典，用于存储用户信息

    if admin_object:
        user_info = {'name': admin_object.username, 'limits': admin_object.limits}
    elif student_object:
        user_info = {'name': student_object.name, 'limits': student_object.limits,
                     "student_id": student_object.Student_ID, 'school': student_object.school.name}  # 外键不可以直接序列化因此要加.name
    elif enterprise_object:
        user_info = {'name': enterprise_object.name, 'limits': enterprise_object.limits,
                     'enterprise_id': enterprise_object.id}
    elif school_object:
        user_info = {'name': school_object.name, 'limits': school_object.limits}

    if user_info:
        request.session['info'] = user_info
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/home/")
    else:
        return render(request, 'login.html', {"form": form, 'error': "用户名或密码错误"})


def home(request):
    """首页"""
    return render(request, "home.html")


from django.urls import reverse


def logout(request):
    """退出登录"""
    if 'info' in request.session:
        del request.session['info']
    return redirect(reverse('login_name'))


def major_list(request):
    """专业列表"""
    major_objects = M.objects.all()
    # major_objects = Major.objects.filter(school__name=request.session['info']['name'])
    return render(request, "major_list.html", {"major_objects": major_objects})


def school_major_list(request):
    """学校专业列表"""
    # school_major_objects = SchoolMajor.objects.filter(school__name=request.session['info']['name'])
    school_major_objects = SM.objects.all()
    return render(request, "school_major_list.html", {"school_major_objects": school_major_objects})


def major_query(request):
    """专业名称查询"""
    query = request.GET.get('qn')
    major_objects = M.objects.all()
    if query:
        major_objects = M.objects.filter(
            major__name__icontains=query
        )
    return render(request, "major_list.html", {"major_objects": major_objects})


def school_major_query(request):
    """学校专业名称查询"""
    query = request.GET.get('qn')
    school_major_objects = SM.objects.filter(school__name=request.session['info']['name'])
    if query:
        school_major_objects = SM.objects.filter(
            major__name__icontains=query
        )
    return render(request, "school_major_list.html", {"school_major_objects": school_major_objects})


def major_add(request):
    """添加专业"""
    if request.method == "GET":
        form = MajorModelForm()
        return render(request, "major_form.html", {"form": form})
    if request.method == "POST":
        form = MajorModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "major_form.html", {"form": form})
        form.save()
        return redirect("/major/list/")
    return render(request, "major_form.html")


def school_major_add(request):
    """学校添加专业"""
    if request.method == "GET":
        form = SchoolMajorModelForm()
        return render(request, "major_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolMajorModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "major_form.html", {"form": form})
        form.save()
        return redirect("/school/major/list/")


def major_edit(request):
    """编辑专业"""
    aid = request.GET.get('aid')
    major_object = M.objects.filter(id=aid).first()
    if request.method == "GET":
        form = MajorModelForm(instance=major_object)
        return render(request, "major_form.html", {"form": form})
    if request.method == "POST":
        form = MajorModelForm(data=request.POST, instance=major_object)
        if not form.is_valid():
            return render(request, "major_form.html", {"form": form})
        form.save()
        return redirect("/major/list/")
    return render(request, "major_form.html")


def school_major_edit(request):
    """学校编辑专业"""
    aid = request.GET.get('aid')
    major_object = SM.objects.filter(id=aid).first()
    if request.method == "GET":
        form = SchoolMajorModelForm(instance=major_object)
        return render(request, "major_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolMajorModelForm(data=request.POST, instance=major_object)
        if not form.is_valid():
            return render(request, "major_form.html", {"form": form})
        form.save()
        return redirect("/school/major/list/")
    return render(request, "major_form.html")


def major_delete(request):
    """删除专业"""
    aid = request.GET.get("aid")
    models.Major.objects.filter(id=aid).delete()
    return redirect("/major/list/")


def student_logon(request):
    """学生注册"""
    if request.method == "GET":
        form = StudentModelForm()
        return render(request, "student_logon.html", {"form": form})
    if request.method == "POST":
        form = StudentModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "student_logon.html", {"form": form})
        form.save()
        return redirect("/login/")


def enterprise_logon(request):
    """企业注册"""
    if request.method == "GET":
        form = EnterpriseModelForm()
        return render(request, "enterprise_logon.html", {"form": form})
    if request.method == "POST":
        form = EnterpriseModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "enterprise_logon.html", {"form": form})
        form.save()
        return redirect("/login/")


def school_list(request):
    """学校列表"""
    school_objects = models.School.objects.all()
    return render(request, "school_list.html", {"school_objects": school_objects})


def school_query(request):
    """学校名称查询"""
    query = request.GET.get('qn')
    school_objects = models.School.objects.all()
    if query:
        school_objects = models.School.objects.filter(
            name__icontains=query
        )
    return render(request, "school_list.html", {"school_objects": school_objects})


def school_add(request):
    """添加学校"""
    if request.method == "GET":
        form = SchoolModelForm()
        return render(request, "school_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "school_form.html", {"form": form})
        form.save()
        return redirect("/school/list/")
    return render(request, "school_form.html")


def school_edit(request):
    """编辑学校"""
    aid = request.GET.get('aid')
    school_object = models.School.objects.filter(id=aid).first()
    if request.method == "GET":
        form = SchoolModelForm(instance=school_object)
        return render(request, "school_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolModelForm(data=request.POST, instance=school_object)
        if not form.is_valid():
            return render(request, "school_form.html", {"form": form})
        form.save()
        return redirect("/school/list/")
    return render(request, "school_form.html")


def school_delete(request):
    """删除学校"""
    aid = request.GET.get("aid")
    models.School.objects.filter(id=aid).delete()
    return redirect("/school/list/")


def school_student_list(request):
    """学校学生列表"""
    student_objects = Student.objects.filter(school__name=request.session['info']['name'])
    return render(request, "school_student_list.html", {"student_objects": student_objects})


def school_student_add(request):
    """学校添加学生"""
    if request.method == "GET":
        form = SchoolStudentModelForm()
        return render(request, "student_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolStudentModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "student_form.html", {"form": form})
        form.save()
        return redirect("/student/list/")


def school_student_edit(request):
    """学校编辑学生"""
    aid = request.GET.get('aid')
    student_object = Student.objects.filter(Student_ID=aid).first()
    if request.method == "GET":
        form = SchoolStudentModelForm(instance=student_object)
        return render(request, "student_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolStudentModelForm(data=request.POST, instance=student_object)
        if not form.is_valid():
            return render(request, "student_form.html", {"form": form})
        form.save()
        return redirect(reverse('student_list_name'))


def school_enterprise_list(request):
    """学校企业列表"""
    # 判断当前用户是学校用户还是管理员用户
    if request.session['info']['limits'] == 3:
        enterprise_objects = models.SchoolEnterprise.objects.filter(school__name=request.session['info']['name'])
        return render(request, "school_enterprise_list.html", {"enterprise_objects": enterprise_objects})
    else:
        enterprise_objects = models.SchoolEnterprise.objects.all()
        return render(request, "admin_school_enterprise_list.html", {"enterprise_objects": enterprise_objects})


def school_enterprise_add(request):
    """学校添加企业"""
    if request.method == "GET":
        form = SchoolEnterpriseModelForm()
        return render(request, "enterprise_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolEnterpriseModelForm(data=request.POST)
        if not form.is_valid():
            return render(request, "enterprise_form.html", {"form": form})
        form.save()
        return redirect(reverse('school_enterprise_list_name'))


def school_enterprise_edit(request):
    """学校编辑企业"""
    aid = request.GET.get('aid')
    enterprise_object = models.SchoolEnterprise.objects.filter(id=aid).first()
    if request.method == "GET":
        form = SchoolEnterpriseModelForm(instance=enterprise_object)
        return render(request, "enterprise_form.html", {"form": form})
    if request.method == "POST":
        form = SchoolEnterpriseModelForm(data=request.POST, instance=enterprise_object)
        if not form.is_valid():
            return render(request, "enterprise_form.html", {"form": form})
        form.save()
        return redirect(reverse('school_enterprise_list_name'))


def school_enterprise_query(request):
    """学校企业名称查询"""
    query = request.GET.get('qn')
    query2 = request.GET.get('qn2')
    # 判断当前用户是学校用户还是管理员用户
    if request.session['info']['limits'] == 3:
        enterprise_objects = models.SchoolEnterprise.objects.filter(school__name=request.session['info']['name'])
        if query:
            enterprise_objects = enterprise_objects.filter(
                enterprise__name__icontains=query
            )
        return render(request, "school_enterprise_list.html", {"enterprise_objects": enterprise_objects})

    else:
        enterprise_objects = models.SchoolEnterprise.objects.all()
        if query or query2:
            enterprise_objects = enterprise_objects.filter(
                enterprise__name__icontains=query,
                school__name__icontains=query2
            )
        return render(request, "admin_school_enterprise_list.html", {"enterprise_objects": enterprise_objects})


def school_enterprise_delete(request):
    """删除学校企业"""
    aid = request.GET.get("aid")
    models.SchoolEnterprise.objects.filter(id=aid).delete()
    return redirect(reverse('school_enterprise_list_name'))