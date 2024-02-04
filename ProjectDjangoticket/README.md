# DjangoStadium

## Description

This is the final project for Software Design lecture, an online ticketshop for a football matches.

## Installation 

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

git clone https://its-git.fh-salzburg.ac.at/fhs48055/ginf-ws21-bence-balogh.git
cd Project DjangoStadium
pip install -r requirements.txt

There are 2 created user with admin rights, an admin with password admin, the basic superuser. As a second there are a "test1" with password "Pword1234" that also a customer and can buy/reserve tickets.

For tests there are the following implemented:

# python manage.py test Customers
# python manage.py test Pages
# python manage.py test Ticketshop

Website can be launched with the command:

python manage.py runserver



## setting up a new Django Project for yourself
python -m venv .
pip install django
django-admin startproject <Projname>
python manage.py startapp <appName>
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# python manage.py createsuperuser --username=admin --email=admin@admin.com
python manage.py runserver
