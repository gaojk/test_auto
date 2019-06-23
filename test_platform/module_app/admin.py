from django.contrib import admin
from module_app.models import Module


# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project']
    search_fields = ['name']  # 搜索栏
    list_filter = ['project']  # 过滤器

admin.site.register(Module, ModuleAdmin)
