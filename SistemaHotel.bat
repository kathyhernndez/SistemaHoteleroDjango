@echo off
call env/Scripts/activate
start python manage.py runserver
timeout /t 5 /nobreak > NUL
start http://localhost:8000