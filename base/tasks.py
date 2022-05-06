from celery import shared_task
from .models import Employee, EmployeesImport
import csv


@shared_task(bind=True)
def create_employee(self):
    obj = EmployeesImport.objects.get(uploaded=False)
    with open(obj.import_file.path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                row = list(row)
                Employee.objects.create(
                    first_name = row[0],
                    last_name = row[1], 
                    hired_from = row[2],
                    birth_date = row[3],
                    bio = row[4],
                    salary = row[5],
                    position = row[6],
                )
        obj.uploaded = True
        obj.save()
    return "Done"
