# test_auto
Python Django2.0搭建自动化测试平台

## git命令
- git clone http://xxxx 克隆项目
- git status 查看状态
- git add .
- git add xxx.py
- git commit -m "description"
- git push origin master 提交
- git pull origin master 拉取

## 客户端浏览器过程
客户端(浏览器) --> request --> 服务器(Django)

服务器(Django) --> response --> 客户端(浏览器)

# Django
[官方地址](https://www.djangoproject.com)
## django安装
- pip -U django  

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

### test_auto目录文件
- setting 整个项目的配置
- urls 整个项目的路由配置
- wsgi 应该部署

## django基础之MTV模型
Web开发,一般的web框架会遵循MVC模型
- Model(模型)表示应用程序核心(比如数据库记录表)
- View(视图)显示数据(数据记录)
- Controller(控制器)处理输入(写入数据库记录)

MTV
- Model(模型) -- Model, django 封装了ORM，免于直接操作数据库
- Template(模板) -- view, django自带模板语言，可以在HTML中处理数据的展示。
- View -- Controller, 在models和templates之间处理数据

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

## bootstrap使用
[官方地址](https://www.bootcss.com)

[bootstrap表单构造器](https://www.bootcss.com/p/bootstrap-form-builder/)

django-bootstrap3插件
- pip install django-bootstrap3

## 模型ORM
对象关系映射（英语：(Object Relational Mapping，简称ORM，或O/RM，或O/R mapping），是一种程序技术，用于实现面向对象编程语言里不同类型系统的数据之间的转换。从效果上说，它其实是创建了一个可在编程语言里使用的--“虚拟对象数据库”。

ORM 像操作对象一样的操作数据库

django -- ORM -- PyMySQL -- MySQL
```python
from django.db import models


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态：", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.name
```
数据类型查看 C:\Python37\Lib\site-packages\django\db\models\fields\__init__.py
### 参数说明
- max_length 最大长度。
- default 默认值。
- null 针对数据库，null=True 表示该字段允许为空。
- blank 针对表单，blank=True 表示表单该字段可以为空。
- auto_now 每次更新数据，都会获取最新时间更新。
- auto_now_add 当数据被创建时，获取最新时间更新。
- on_delete 指定关联数据， models.CASCADE 表示删除关联数据时，与之关联也删除。

### 数据库表操作：
- 创建
```python
Project.objects.create(name="项目", describe="描述")
```
- 查询
```python
Project.objects.all()
Project.objects.get(pk=1)
Project.objects.filter(status=1)
Project.objects.filter(name__contains='项目')
```
- 更新
```python
g = Project.objects.get(name='xxx测试项目')
g.status=0
g.save()

Project.objects.select_for_update().filter(name__contains='项目').update(describe='') # 批量更新
```
- 删除
```python
Project.objects.get(name='xxx测试项目').delete()
```

### 如何生成数据库的数据表
- python3 manage.py makemigrations
- python3 manage.py migrate

### python如何和mysql交互
python --  PyMySQL(驱动) -- mysql

[PyMySQL Github地址](https://github.com/PyMySQL/PyMySQL) 这种方式的缺点是在编程语言夹杂了大量的SQL语句

## 切换MySQL
[配置mysql参考文档](https://docs.djangoproject.com/en/2.1/ref/databases/)

- 先安装一个MySQL数据库
- 在项目根目录创建一个配置文件my.cnf文件。
```
[client]
host = 127.0.0.1
port = 3306
user = root
password = pyif07
database = test_dev
default-character-set = utf8
```
- settings.py添加配置：
```python
# MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BASE_DIR + '/my.cnf',
        },
    }
}
```
- 安装mysqlclient
```
 pip install mysqlclient
```
- 重新执行数据库迁移和创建超级管理账号
```
python manage.py migrate

python manage.py createsuperuser
```

## 模板

