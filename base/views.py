from django.http import HttpResponse
from django.shortcuts import render, redirect
from base.forms import EmployeeForm, TaskForm
from base.models import Task, Employee
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework import viewsets
from .serializer import EmployeeSerializer
from datetime import date
import csv

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetails(DetailView):
    model = Employee
    template_name = "base/employee_detail.html"
    context_object_name = "employee"
    success_url = reverse_lazy('employees')


class TaskList(View):

    def get(self, request, pk):
        form = TaskForm()
        employee = Employee.objects.get(pk=pk)
        employees = employee.get_employees_tasks()
        state = None
        dates = ["start_date", "end_date"]
        
        if 'state' in request.GET:
            if request.GET["state"] != "null":
                if request.GET["state"] == "Done":
                    state = True
                    employees = employee.get_employees_tasks(state=state)
                elif request.GET["state"] == "Undone":
                    state = False
                    employees = employee.get_employees_tasks(state=state)
            elif request.GET["state"] == "null":
                employees = employee.get_employees_tasks()

        if all(key in request.GET for key in dates):
            print(request)
            if state in [True, False]:
                print(state)
                employees = employee.get_employees_tasks(deadline__range=[str(
                    request.GET["start_date"]), str(request.GET["end_date"])], state=state)
            elif state == None:
                employees = employee.get_employees_tasks(
                    deadline__range=[request.GET["start_date"], request.GET["end_date"]])
        else:
            employees = employee.get_employees_tasks()

        return render(request, 'base/tasks_list.html', context={'form': form, 'employee': employee, 'TaskList': employees, 'pk': pk})

    def post(self, request, pk):
        form = TaskForm(request.POST or None)
        print(request.POST)
        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)

        return render(request, 'base/tasks_list.html', context={'form': form})


class TaskDetail(DetailView):
    model = Task
    template_name = "base/task_detail.html"
    context_object_name = "Task"


class EmployeeList(View):

    def get(self, request):
        form = EmployeeForm()
        employees = Employee.objects.all()

        return render(request, 'base/employee_list.html', context={'form': form, 'employees': employees})

    def post(self, request):
        form = EmployeeForm(request.POST)
        print(request.POST)
        if request.is_ajax():
            if form.is_valid():
                new_employee = form.save()
                return JsonResponse({'employee': model_to_dict(new_employee)}, status=200)
        else:
            return render(request, 'base/employee_list.html', context={'form': form})


class TaskDone(View):

    def get(self,  request):
        return render(request, 'base/tasks_list.html')

    def post(self, request, id):
        if request.is_ajax():
            if request.POST['done'] == "true":
                task = Task.objects.get(id=id)
                task.state = True
                task.save()
                return JsonResponse({'task': model_to_dict(task)}, status=200)
        return render(request, 'base/tasks_list.html')


class TaskDelete(View):

    def post(self, request, id):
        if request.is_ajax():
            if request.POST['del'] == "true":
                task = Task.objects.get(id=id)
                task.delete()
                return JsonResponse({'result': 'ok'}, status=200)
        return render(request, 'base/tasks_list.html')

def export_csv(request, id):
    employee = Employee.objects.get(pk=id)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={employee.first_name}_{employee.last_name}_tasklist.csv'
    writer = csv.writer(response)
    writer.writerow(["Title", "Description", "State", "Deadline", "Category"])
    tasks = employee.get_employees_tasks(deadline=date.today())
    for task in tasks:
        writer.writerow([task.title, task.description, task.state, task.deadline, task.category])
    print("exported")
    return response
    
   