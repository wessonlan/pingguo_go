from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from personal.models.project import Project

@login_required
def project_manage(request):
    """
    管理页面，登录成功默认页面
    """
    project_all = Project.objects.all()
    return render(request, "project_manage.html", {"projects": project_all,
                                                   "type": "list"})

@login_required
def add_project(request):
    """
    添加项目
    """
    if request.method == 'GET':
        return render(request, 'project_manage.html', {"type": "add"})
    elif request.method == 'POST':
        name = request.POST.get('name', '')
        describe = request.POST.get('describe', '')
        status = request.POST.get('status', '')
        if name == '':
            return render(request, 'project_manage.html',{"type": "add",
                                                          "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project/")