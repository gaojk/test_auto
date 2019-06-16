from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth  # 认证模块


# Create your views here.
# MVT -- V
# 客户端(浏览器) --> request 服务器(django)
# 客户端(浏览器) Response <-- 服务器(django)

def say_hello(request):  # 入参名随意, 但常规叫request 表示从客户端接收到的参数
    name = request.GET.get("name", "")  # GET Http请求方式 get是获取 name是key,需指定value,如果value为空则为""
    if name == "":
        return HttpResponse("请求输入?name=name")
    return render(request, "index.html", {"name": name})


def index(request):
    """
    登录的首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        print(user_name)
        print(pass_word)

        if user_name == "" or pass_word == "":
            return render(request, "index.html", {"error": "用户名或密码为空!"})

        user = auth.authenticate(username=user_name, password=pass_word)
        print("user -->", user)
        """
        if user_name == "admin" and pass_word == "123123":
            return HttpResponse("登录成功!")
        else:
            return render(request, "index.html", {"error": "用户名或密码为错误!"})
        """
        if user is None:
            return render(request, "index.html", {"error": "用户名或密码为错误!"})
        else:
            auth.login(request, user)  # 记录用户登录的状态
            return HttpResponseRedirect('/project/')  # 重定向


# 处理用户的退出
def logout(request):
    auth.logout(request)  # Django自带的退出,可清除session
    return HttpResponseRedirect('/index/')
