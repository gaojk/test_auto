from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personal.models.module import Module


# 模块管理
@login_required
def module_manage(request):
    """
    模块管理
    :param request:
    :return:
    """
    module_all = Module.objects.all()
    return render(request, 'module.html', {"modules": module_all})