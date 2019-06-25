from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests, json


# Create your views here.
def testcase_manage(request):
    return render(request, "test_case.html", {"type": "debug"})


def debug(request):
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")

        json_header = header.repalce("\'", "\"")
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数错误"})

        json_par = parameter.replace("\'", "\"")
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数错误"})

        if method == "get":
            if header == "":
                r = requests.get(url, params=payload)
            else:
                r = requests.get(url, params=payload, headers=header)

        if method == "post":
            if type_ == "from":
                r = requests.post(url, data=payload)
            if type_ == "json":
                r = requests.post(url, json=payload)
        return JsonResponse({"result": r.text})
    else:
        return JsonResponse({"result": "请求方法错误"})

