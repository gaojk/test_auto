from django.urls import path
from test_case_app import views


urlpatterns = [
    # 用例管理
    path('', views.testcase_manage),
    path('add_case/', views.testcase_add),
    path('edit_case/<int:cid>/', views.testcase_edit),
    path('delete_case/<int:cid>/', views.testcase_delete),
    path('debug/', views.testcase_debug),
    path('assert/', views.testcase_assert),
    path('save_case/', views.testcase_save_case),

    # 接口
    path('get_case_info/', views.testcase_get_case_info),

]