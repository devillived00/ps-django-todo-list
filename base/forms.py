from django import forms
from base.models import Employee, Task, EmployeesImport


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'salary',
            'position', 'last_name',
            'hired_from', 'birth_date',
            'bio',
        ]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['employee', 'title', 'description',
                  'deadline', 'category']
        
class EmployeeImportForm(forms.ModelForm):
    
    class Meta:
        model = EmployeesImport
        fields = ['import_file']