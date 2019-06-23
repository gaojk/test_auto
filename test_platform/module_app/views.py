from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from module_app.models import Module
from module_app.forms import ModuleForms


# 模块管理
@login_required
def module_manage(request):
    """
    模块管理
    :param request:
    :return:
    """
    if request.method == "GET":
        module_all = Module.objects.all()
        return render(request, 'module.html', {"modules": module_all,
                                               "type": "list"
                                               })


@login_required
def add_module(request):
    """
    添加模块
    :param request:
    :return:
    """
    if request.method == "GET":
        module_form = ModuleForms()
        return render(request, 'module.html', {"type": "add",
                                               "module_form": module_form
                                               })
    elif request.method == "POST":
        # name = request.POST.get("name", "")
        # describe = request.POST.get("describe", "")
        # if name == "":
        #     return render(request, "module.html", {"type": "add",
        #                                            "name_error": "模块名称不能为空"})
        # Module.objects.create(name=name, describe=describe)
        module_form = ModuleForms(request.POST)
        if module_form.is_valid():
            name = module_form.cleaned_data['name']
            describe = module_form.cleaned_data['describe']
            project = module_form.cleaned_data['project']

            Module.objects.create(project=project, name=name, describe=describe)
            return HttpResponseRedirect("/module/")


@login_required
def edit_module(request, mid):
    """
    编辑项目
    :param request:
    :return:
    """
    if request.method == "GET":
        if mid:
            p = Module.objects.get(id=mid)
            form = ModuleForms(instance=p)
            return render(request, 'module.html', {"type": "edit",
                                                   "module_form": form,
                                                   "id": mid
                                                   })
    if request.method == "POST":
        form = ModuleForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']

            m = Module.objects.get(id=mid)
            m.name = name
            m.describe = describe
            m.project = project
            m.save()
        return HttpResponseRedirect("/module/")


@login_required
def delete_module(request, mid):
    """
    删除项目
    :param request:
    :return:
    """
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)
        except Module.DoesNotExist:
            return HttpResponseRedirect("/module/")
        else:
            module.delete()
        return HttpResponseRedirect("/module/")
    else:
        return HttpResponseRedirect("/module/")
