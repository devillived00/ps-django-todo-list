from .models import Employee, Task
from rest_framework import serializers
from datetime import date

class FilteredTasksSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(deadline=date.today())
        return super(FilteredTasksSerializer, self).to_representation(data)

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        list_serializer_class = FilteredTasksSerializer
        model = Task
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'
        