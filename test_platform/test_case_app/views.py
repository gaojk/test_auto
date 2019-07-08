from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import requests, json
from test_case_app.models import TestCase
from module_app.models import Module
from project_app.models import Project


# Create your views here.
def testcase_manage(request):
    """
    用例列表主页/用例列表
    :param request:
    :return:
    """
    case_list = TestCase.objects.all()
    # 将数据做分页处理，每一页显示 3 条
    p = Paginator(case_list, 1)
    # 通过请求得到要第几页的数据
    page = request.GET.get('page')
    try:
        cases = p.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        cases = p.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        cases = p.page(p.num_pages)

    return render(request, "test_case_list.html", {"type": "list",
                                                   "cases": cases
                                                   })


def testcase_add(request):
    """
    添加测试用例
    :param request:
    :return:
    """
    return render(request, "test_case_add.html")


def testcase_edit(request, cid):
    """
    编辑测试用例
    :param request:
    :return:
    """
    return render(request, "test_case_edit.html")


def testcase_delete(request, cid):
    """
    删除测试用例
    :param request:
    :return:
    """
    case = TestCase.objects.get(id=cid)
    case.delete()
    return HttpResponseRedirect("/testcase/")


def testcase_debug(request):
    """
    测试用例调试
    :param request:
    :return:
    """
    if request.method == "POST":
        url = request.POST.get("url", "")  # URL
        method = request.POST.get("method", "")  # 方法
        header = request.POST.get("header", "")  # header
        par_type = request.POST.get("type", "")  # 参数类型
        par_body = request.POST.get("parameter", "")  # 参数

        if header == "":
            header = "{}"

        try:
            header = json.loads(header.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})

        if par_body == "":
            par_body = "{}"

        try:
            payload = json.loads(par_body.replace("\'", "\""))
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})

        result_text = None
        if method == "get":
            r = requests.get(url, params=payload, headers=header)
            result_text = r.text

        if method == "post":
            if par_type == "form":
                r = requests.post(url, data=payload, headers=header)
                result_text = r.text

            if par_type == "json":
                r = requests.post(url, json=payload, headers=header)
                result_text = r.text

        return JsonResponse({"result": result_text})
    else:
        return JsonResponse({"result": "请求方法错误"})


def testcase_assert(request):
    """
    测试用例的断言
    """
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        if assert_type == "contains":
            assert_list = assert_text.split(">>")
            for assert_value in assert_list:
                if assert_value not in result_text:
                    return JsonResponse({"result": "断言失败"})
                else:
                    return JsonResponse({"result": "断言成功"})

        elif assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})

    else:
        return JsonResponse({"result": "请求方法错误"})


def testcase_save_case(request):
    """
    用例创建/编辑保存

    :param request:
    :return:
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        parameter_type = request.POST.get("par_type", "")
        parameter_body = request.POST.get("par_body", "")
        assert_type = request.POST.get("ass_type", "")
        assert_text = request.POST.get("ass_text", "")
        module_id = request.POST.get("mid", "")
        name = request.POST.get("name", "")
        cid = request.POST.get("cid", "")

        print("url", url)
        print("method", method)
        print("header", header)
        print("parameter_type", parameter_type)
        print("parameter_body", parameter_body)
        print("assert_type", assert_type)
        print("assert_text", assert_text)
        print("module_id", module_id)
        print("name", name)
        print("cid", cid)
        if name == "":
            return JsonResponse({"status": 10101, "message": "用例名称不能为空"})

        if module_id == "":
            return JsonResponse({"status": 10103, "message": "所属的模块不能为空"})

        if assert_type == "" or assert_text == "":
            return JsonResponse({"status": 10102, "message": "断言的类型或文本不能为空"})

        # 1:GET, 2: POST, 3:DELETE, 4:PUT
        if method == "get":
            method_number = 1
        elif method == "post":
            method_number = 2
        elif method == "delete":
            method_number = 3
        elif method == "put":
            method_number = 4
        else:
            return JsonResponse({"status": 10104, "message": "未知的请求方法"})

        if parameter_type == "form":
            parameter_number = 1
        elif parameter_type == "json":
            parameter_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的参数类型"})

        if assert_type == "contains":
            assert_number = 1
        elif assert_type == "mathches":
            assert_number = 2
        else:
            return JsonResponse({"status": 10104, "message": "未知的断言类型"})

        if cid == "":
            TestCase.objects.create(case_name=name, module_id=module_id,
                                    url=url, method=method_number, header=header,
                                    parameter_type=parameter_number, parameter_body=parameter_body,
                                    assert_type=assert_number, assert_text=assert_text)
        else:
            case = TestCase.objects.get(id=cid)
            case.name = name
            case.module_id = module_id
            case.url = url
            case.method = method_number
            case.header = header
            case.parameter_type = parameter_number
            case.parameter_body = parameter_body
            case.assert_type = assert_number
            case.assert_text = assert_text
            case.save()

        return JsonResponse({"status": 10200, "message": "创建成功！"})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def testcase_get_case_info(request):
    """
    获取接口数据
    :param request:
    :return:
    """
    if request.method == "POST":
        cid = request.POST.get("cid", "")
        case = TestCase.objects.get(id=cid)
        module = Module.objects.get(id=case.module.id)
        project_id = module.project.id

        case_dict = {
            "id": case.id,
            "url": case.url,
            "name": case.case_name,
            "method": case.method,
            "header": case.header,
            "parameter_type": case.parameter_type,
            "parameter_body": case.parameter_body,
            "assert_type": case.assert_type,
            "assert_text": case.assert_text,
            "module_id": case.module.id,
            "project_id": project_id,
        }
        return JsonResponse({"status": 10200, "message": "请求成功", "data": case_dict})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})


def get_select_data(request):
    """
    获取 "项目>模块" 列表
    :param request:
    :return: 项目接口列表
    """
    if request.method == "GET":
        project_list = Project.objects.all()
        data_list = []
        for project in project_list:
            project_dict = {
                "id": project.id,
                "name": project.name
            }

            module_list = Module.objects.filter(project_id=project.id)
            module_name = []
            for module in module_list:
                module_name.append({
                    "id": module.id,
                    "name": module.name,
                })

            project_dict["moduleList"] = module_name
            data_list.append(project_dict)

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

    else:
        return JsonResponse({"status": 10100, "message": "请求方法错误"})
