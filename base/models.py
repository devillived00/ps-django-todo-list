from email.policy import default
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hired_from = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500)
    salary = models.DecimalField(
        max_digits=8, decimal_places=2, null=True, blank=True)

    POSITIONS = [
            ('jp', "Junior Python Developer"),
            ('rp', "Regular Python Developer"),
            ('sp', "Senior Python Developer"),
            ('po', "Project Owner"),
            ('an', "Analyst"),
            ('te', "Tester"),
                ]

    position = models.CharField(max_length=2, choices=POSITIONS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_employees_tasks(self, **kwargs):
        return Task.objects.filter(employee_id=self.id, **kwargs)
    
    def get_completed_tasks_count(self):
        return len(self.get_employees_tasks(state=True))
    
    def get_uncompleted_tasks_count(self):
        return len(self.get_employees_tasks(state=False))
            
class EmployeesImport(models.Model):
    import_file = models.FileField(upload_to="imports")
    uploaded = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}_{self.created}"

class Task(models.Model):
    employee = models.ForeignKey(
        Employee, related_name="tasks", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    state = models.BooleanField(verbose_name="Done" ,default=False)
    deadline = models.DateField(null=True, blank=True)

    CATEGORIES = [
        ('Internal Task', 'IT'),
        ('Helpdesk Task', 'HT'),
        ('Project Task', 'PT')
    ]

    category = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            'state'
        ]
