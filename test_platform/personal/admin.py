from django.contrib import admin
from personal.models.project import Project
from personal.models.module import Module


# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time']  # 显示栏
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project']
    search_fields = ['name']  # 搜索栏
    list_filter = ['project']  # 过滤器


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
