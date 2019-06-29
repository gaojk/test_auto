# 模型ORM
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