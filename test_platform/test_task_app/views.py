from django.shortcuts import render


# Create your views here.

def test_task_manage(request):
    """
    任务管理
    :param request:
    :return:
    """
    return render(request, "test_task_list.html", {"type": "list"})


def test_task_add(request):
    """
    创建任务
    :param request:
    :return:
    """
    return render(request, "test_task_add.html", {"type": "add"})


def test_task_edit(request):
    """
    编辑任务
    :param request:
    :return:
    """
    return render(request, "test_task_edit.html", {"type": "edit"})


def test_task_delete(request):
    """
    删除任务
    :param request:
    :return:
    """
    pass
