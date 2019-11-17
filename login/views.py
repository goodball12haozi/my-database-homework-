from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from login.models import User
from login.models import Student
from login.models import Grade
from django.http import HttpResponse
from login.forms import UserForm
from login.forms import RegisterForm


def adminuserlist(request):
    users = User.objects.all()
    return render(request, 'adminuserlist.html', {'users': users})


def adminstudentlist(request):
    students = Student.objects.all()
    return render(request, 'adminstudentlist.html', {'students': students})


def admingradelist(request):
    grades = Grade.objects.all()
    return render(request, 'admingradelist.html', {'grades': grades})


def generaluserlist(request):
    users = User.objects.all()
    return render(request, 'generaluserlist.html', {'users': users})


def generalstudentlist(request):
    students = Student.objects.all()
    return render(request, 'generalstudentlist.html', {'students': students})


def generalgradelist(request):
    grades = Grade.objects.all()
    return render(request, 'generalgradelist.html', {'grades': grades})


def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = '请检查填写的内容'
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if password == user.password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    if user.permission == 'administrator':
                        return redirect('/adminuserlist/')
                    else:
                        return redirect('/generaluserlist/')
                else:
                    message = '密码不正确'
            except:
                message = username
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def logout(request):
    request.session.flush()
    return redirect("/login/")


def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def adduser(request):
    if request.method == "POST":
        User.objects.create(name=request.POST['name'], password=request.POST['password'], email=request.POST['email'], sex=request.POST['sex'], permission=request.POST['permission'])
        return redirect('/adminuserlist/')
    else:
        return render(request, 'adduser.html')


def addstudent(request):
    if request.method == "POST":
        Student.objects.create(name=request.POST['name'], grade=request.POST['grade'], studentid=request.POST['studentid'], college=request.POST['college'], profession=request.POST['profession'])
        return redirect('/adminstudentlist/')
    else:
        return render(request, 'addstudent.html')


def addgrade(request):
    if request.method == "POST":
        Grade.objects.create(name=request.POST['name'], studentid=request.POST['studentid'], Chinese=request.POST['Chinese'], Mathematics=request.POST['Mathematics'], English=request.POST['English'], Physical=request.POST['Physical'], Chemistry=request.POST['Chemistry'], PE=request.POST['PE'])
        return redirect('/admingradelist/')
    else:
        return render(request, 'addgrade.html')


def deleteuser(request):
    if request.method == "POST":
        ID=request.POST['id']
        User.objects.filter(id=ID).delete()
        return redirect('/adminuserlist/')
    else:
        return render(request, 'deleteuser.html')


def deletestudent(request):
    if request.method == "POST":
        studentID = request.POST['studentid']
        Student.objects.filter(studentid=studentID).delete()
        return redirect('/adminstudentlist/')
    else:
        return render(request, 'deletestudent.html')


def deletegrade(request):
    if request.method == "POST":
        studentID = request.POST['studentid']
        Grade.objects.filter(studentid=studentID).delete()
        return redirect('/admingradelist/')
    else:
        return render(request, 'deletegrade.html')


def updateuser(request):
    if request.method == "POST":
        ID=request.POST['id']
        User.objects.filter(id=ID).update(name=request.POST['name'])
        User.objects.filter(id=ID).update(email=request.POST['email'])
        User.objects.filter(id=ID).update(sex=request.POST['sex'])
        User.objects.filter(id=ID).update(permission=request.POST['permission'])
        return redirect('/adminuserlist/')
    else:
        return render(request, 'updateuser.html')


def updatestudent(request):
    if request.method == "POST":
        ID=request.POST['id']
        Student.objects.filter(id=ID).update(name=request.POST['name'])
        Student.objects.filter(id=ID).update(grade=request.POST['grade'])
        Student.objects.filter(id=ID).update(college=request.POST['college'])
        Student.objects.filter(id=ID).update(profession=request.POST['profession'])
        return redirect('/adminstudentlist/')
    else:
        return render(request, 'updatestudent.html')


def updategrade(request):
    if request.method == "POST":
        ID=request.POST['id']
        Grade.objects.filter(id=ID).update(name=request.POST['name'])
        Grade.objects.filter(id=ID).update(Chinese=request.POST['Chinese'])
        Grade.objects.filter(id=ID).update(Mathematics=request.POST['Mathematics'])
        Grade.objects.filter(id=ID).update(English=request.POST['English'])
        Grade.objects.filter(id=ID).update(Physical=request.POST['Physical'])
        Grade.objects.filter(id=ID).update(Chemistry=request.POST['Chemistry'])
        Grade.objects.filter(id=ID).update(PE=request.POST['PE'])
        return redirect('/admingradelist/')
    else:
        return render(request, 'updategrade.html')