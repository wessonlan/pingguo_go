from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personal.models.project import Project

@login_required
def project_manage(request):
    """
    管理页面，登录成功默认页面
    """
    project_all = Project.objects.all()
    return render(request, "project_manage.html", {"projects": project_all})

@login_required
def add_project(request):
    """
    添加项目
    """
    return render(request, 'add_project.html')