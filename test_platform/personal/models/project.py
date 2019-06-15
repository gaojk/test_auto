from django.db import models


# Create your models here.
# MTV -- M

class Project(models.Model):
    """
    项目表

    操作数据表: 进入django shell (python manage.py shell)
    > from personal.models import Project
    > Project.objects.create(name="test project",describe="this is test project") # 插入数据
    > p = Project.objects.get(id=1) # 查询数据
    > print(p)
    """
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    status = models.BooleanField("状态：", default=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)

    def __str__(self):
        return self.name
