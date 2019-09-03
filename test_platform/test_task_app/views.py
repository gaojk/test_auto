import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from project_app.models import Project
from module_app.models import Module
from test_task_app.models import TestTask
from test_case_app.models import TestCase


# Create your views here.

def test_task_manage(request):
    """
    任务管理
    :param request:
    :return:
    """
    task_list = TestTask.objects.all()
    return render(request, "test_task_list.html", {
        "type": "list",
        "tasks": task_list
    })


def test_task_add(request):
    """
    创建任务
    :param request:
    :return:
    """
    return render(request, "test_task_add.html", {"type": "add"})


def test_task_edit(request, tid):
    """
    编辑任务
    :param request:
    :return:
    """
    return render(request, "test_task_edit.html", {"type": "edit"})


def test_task_delete(request, tid):
    """
    删除任务
    :param request:
    :return:
    """
    pass


def save_task(request):
    """
    创建/编辑任务
    """
    if request.method == "POST":
        task_id = request.POST.get("task_id", "")
        name = request.POST.get("name", "")
        desc = request.POST.get("desc", "")
        cases = request.POST.get("cases", "")
        print("name", name, desc)
        print("用例", type(cases), cases)

        if name == "" or cases == "":
            return JsonResponse({"status": 10102, "message": "Parameter is null"})

        if task_id == "0":
            print("创建")
            TestTask.objects.create(name=name, describe=desc, cases=cases)
        else:
            print("编辑")
            task = TestTask.objects.get(id=task_id)
            task.name = name
            task.describe = desc
            task.cases = cases
            task.save()

        return JsonResponse({"status": 10200, "message": "success"})
    else:
        return JsonResponse({"status": 10101, "message": "请求方法错误"})


def get_case_tree(request):
    """
     获得用例树形结构
    """
    if request.method == "GET":
        projects = Project.objects.all()
        data_list = []
        for project in projects:
            project_dict = {
                "name": project.name,
                "isParent": True
            }

            modules = Module.objects.filter(project_id=project.id)
            module_list = []
            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }

                cases = TestCase.objects.filter(module_id=module.id)
                case_list = []
                for case in cases:
                    case_dict = {
                        "name": case.case_name,
                        "isParent": False,
                        "id": case.id,
                    }
                    case_list.append(case_dict)

                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    if request.method == "POST":
        tid = request.POST.get("tid", "")
        print("任务的id", tid)
        if tid == "":
            return JsonResponse({"status": 10200, "message": "任务id不能为空"})

        task = TestTask.objects.get(id=tid)
        casesList = json.loads(task.cases)  # 获取的case的列表
        task_data = {
            "name": task.name,
            "desc": task.describe
        }

        projects = Project.objects.all()
        data_list = []
        for project in projects:
            project_dict = {
                "name": project.name,
                "isParent": True
            }

            # 模块管理
            modules = Module.objects.filter(project_id=project.id)
            module_list = []
            for module in modules:
                module_dict = {
                    "name": module.name,
                    "isParent": True
                }

                cases = TestCase.objects.filter(module_id=module.id)
                case_list = []
                for case in cases:
                    if case.id in casesList:
                        case_dict = {
                            "name": case.case_name,
                            "isParent": False,
                            "id": case.id,
                            "checked": True,  # 选项被选中
                        }
                    else:
                        case_dict = {
                            "name": case.case_name,
                            "isParent": False,
                            "id": case.id,
                            "checked": False,
                        }
                    case_list.append(case_dict)

                module_dict["children"] = case_list
                module_list.append(module_dict)

            project_dict["children"] = module_list
            data_list.append(project_dict)
        task_data["cases"] = data_list
        return JsonResponse({"status": 10200, "message": "success", "data": task_data})
