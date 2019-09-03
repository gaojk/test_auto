from django.urls import path
from test_task_app import views

urlpatterns = [
    # 任务管理
    path('', views.test_task_manage),
    path('add_task/', views.test_task_add),
    path('edit_task/<int:tid>/', views.test_task_edit),
    path('delete_task/<int:tid>/', views.test_task_delete),
    path('save_task/', views.save_task),

    # 接口
    path('get_case_tree/', views.get_case_tree),
]
