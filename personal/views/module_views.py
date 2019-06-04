from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personal.models.module import Module

@login_required
def module_manage(request):
    """
    管理页面，登录成功默认页面
    """
    return render(request, "module_manage.html")