# Django项目搭建 

## 查看django安装
- pip show django

## django项目创建
### 创建项目
- django-admin startproject test_platform

### 运行项目
- python manage.py runserver

### 创建应用
- pyhton manage.py startapp personal

### 生成数据库同步文件
- python manage.py makemigrations polls

### 执行数据库同步
- python manage.py migrate

### djang shell 模式
- python manage.py shell

### 创建超级管理账号
- python manage.py createsuperuser

### 运行django单元测试
-  python manage.py test

## django 简单处理流程
1、浏览器URL：http://127.0.0.1:8000/index/

2、urls.py 文件中匹配路径 /index/
```python
path('index/', views.index),
```
3、在 views.py 文件中定义 index() 函数，将 index.html 文件返回给客户端浏览器
```python
def index(request):
    return render(request, "index.html")
```

## 数据库--用户名和密码
使用Django自带的用户表

### 登录admin
地址：http://127.0.0.1:8000/admin

创建超级管理员登录用户名和密码
```python
> python3 manage.py createsuperuser
```
设置用户名和密码：

- 用户名：admin
- 密码：admin123456

## django实现登录功能
在 index.html 页面当中:
```html
<form action="/login_action/" method="get/post">
    <input name="username">
    <input name="password">
</form>
```
- 请求路径 login_action/
- 请求方法：get/post
- input 标签的 name属性是传参的名称

在 views.py 文件中：
```python
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        
        user = auth.authenticate(
            username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 验证登录
            return render(request, "project_manage.html")
        else:
            return render(request, "index.html",
                                    {"error": "用户名或者密码错误"})



@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/index/")
```
- request.POST.get("username", "") 获取POST请求的参数。
- auth.authenticate 判断用户是否存在。
- auth.login(request, user) 保留用户的登录信息。
