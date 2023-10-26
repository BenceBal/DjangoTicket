# virtual environment -> easy
python -m venv .
pip install django
django-admin startproject <Projname>
python manage.py startapp <appName>
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

admin/admin
