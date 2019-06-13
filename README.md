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
- Model(模型) -- Model
- Template(模板) -- view
- View -- Controller