from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json


# Create your views here.
def testcase_manage(request):
    return render(request, "test_case.html", {"type": "debug"})


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


