from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from personal.models.project import Project


# 项目管理
@login_required
def project_manage(request):
    """
    项目管理
    :param request:
    :return:
    """
    project_all = Project.objects.all()
    return render(request, 'project.html', {"projects": project_all,
                                            "type": "list"
                                            })


@login_required
def add_project(request):
    """
    添加项目
    :param request:
    :return:
    """
    return render(request, 'project.html', {"type": "add"})
