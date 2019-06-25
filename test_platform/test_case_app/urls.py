from django.urls import path
from test_case_app import views


urlpatterns = [
    # 用例管理
    path('', views.testcase_manage),
    path('debug/', views.debug)
    # path('add_project/', views.add_project),
    # path('delete_project/<int:pid>/', views.delete_project),
    # path('edit_project/<int:pid>/', views.edit_project),

]