from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def index(request):
    """
    登录的首页
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        user = auth.authenticate(username=username, password=password)
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码错误"})
        else:
            auth.login(request, user) #记录用户登录的状态
            return HttpResponseRedirect("/project/")

def logout(request):
    """
    处理用户退出
    """
    auth.logout(request)
    return HttpResponseRedirect("/index/")

@login_required
def project_manage(request):
    """
    管理页面，登录成功默认页面
    """
    return render(request, "project_manage.html")

@login_required
def module_manage(request):
    """
    管理页面，登录成功默认页面
    """
    return render(request, "module_manage.html")