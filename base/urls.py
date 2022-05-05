from base.views import EmployeeDetails, EmployeeList, TaskList, TaskDetail, TaskDone, TaskDelete, EmployeeViewSet
from django.views.generic import TemplateView
from django.urls import path, include
from rest_framework import routers
from base.views import export_csv

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', EmployeeList.as_view(), name='employees'),
    path('employee/<int:pk>', EmployeeDetails.as_view(), name='employee'),
    path('employee/tasks-list/<int:pk>/', TaskList.as_view(), name='employee-task-list'),
    path('task-detail/<int:pk>', TaskDetail.as_view(), name="task-detail"),
    path('employee/tasks-list/<str:id>/task-done/', TaskDone.as_view(), name='task-done'),
    path('employee/tasks-list/<str:id>/task-delete/', TaskDelete.as_view(), name='task-done'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('export/<str:id>/', export_csv, name='export'),
    path('docs/', TemplateView.as_view(
        template_name='base/swagger.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]
