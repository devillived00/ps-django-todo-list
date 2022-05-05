from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
]