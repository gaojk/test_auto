from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from project_app.models import Project
from project_app.forms import ProjectForms


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
    print("请求方法", request.method)
    if request.method == "GET":
        return render(request, 'project.html', {"type": "add"})
    elif request.method == "POST":
        name = request.POST.get("name", "")
        describe = request.POST.get("describe", "")
        status = request.POST.get("status", "")
        if name == "":
            return render(request, "project.html", {"type": "add",
                                                    "name_error": "项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project/")


@login_required
def edit_project(request, pid):
    """
    编辑项目
    :param request:
    :return:
    """
    if request.method == "GET":
        print("要编辑的id", pid)
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectForms(instance=p)
            return render(request, 'project.html', {"type": "edit",
                                                    "project_form": form,
                                                    "id": pid
                                                    })
    if request.method == "POST":
        form = ProjectForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/project/")


@login_required
def delete_project(request, pid):
    """
    删除项目
    :param request:
    :return:
    """
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)
        except Project.DoesNotExist:
            return HttpResponseRedirect("/project/")
        else:
            project.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")


def get_project_list(request):
    """
    接口:获取项目列表
    :param request:
    :return:
    """
    if request.method == "GET":
        projects = Project.objects.all()
        project_list = []

        for pro in projects:
            project_dict = {
                "id": pro.id,
                "name": pro.name
            }
            project_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "请求成功", "data": project_list})  # 返回所有的项目名称
    else:
        return JsonResponse({"status": 10201, "message": "请求方法错误"})
