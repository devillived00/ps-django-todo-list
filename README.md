A little manual:)
1. After cloning this repository create ".env" file with variable SECRET KEY=yousecretkey.
2. Next step is to build our docker-compose with "docker-compose up --build" and after a while you can go to http://localhost:8000 :)
4. You can create superuser now with "python3 manage.py createsuperuser" and login as admin to the application.
5. In /media/imports there is a example template for Employee Import to demonstrate Cekery task working. 
   You can upload it here: http://localhost:8000/import/
6. To see swagger API representation go to http://localhost:8000/docs/
7. Endpoint for all the employees with their tasks set to today: /api/employees/ .

Thank you:)
