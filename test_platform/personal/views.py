from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# MVT -- V
# 客户端(浏览器) --> request 服务器(django)
# 客户端(浏览器) Response <-- 服务器(django)

def say_hello(request):  # 入参名随意, 但常规叫request 表示从客户端接收到的参数
    name = request.GET.get("name", "")  # GET Http请求方式 get是获取 name是key,需指定value,如果value为空则为""
    if name == "":
        return HttpResponse("请求输入?name=name")
    return render(request, "index.html")
