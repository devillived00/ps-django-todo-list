from base.views import EmployeeDetails, EmployeeList, TaskList, TaskDetail, CustomLoginView, TaskDone, TaskDelete, EmployeeViewSet, EmployeeImport
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers
from base.views import export_csv

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('', EmployeeList.as_view(), name='employees'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
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
    path('import/', EmployeeImport.as_view(), name='import')
]
