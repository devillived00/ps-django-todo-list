from .models import Employee, Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'
        