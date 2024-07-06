# Django_REST_API_using_DRF-Django_Rest_Framework

# Cretaing virtual env and installing packages
    -This is one time steup
    1. Python -m venv apiEnv
    2. Set-ExecutionPolicy Unrestricted Scope Process (if problem occurs and cant activate)
    3. apiEnv\Scripts\activate
    4. pip freeze
    5. pip install django
    6. pip install djangorestframework
    7. pip freeze (to see if django installed)

# Creating Project and app, migrate db
    7. django-admin startproject apiProject
    8. django-admin startapp apiApp 
    9. ls (see if there is manage.py in the list)
    10. python manage.py createsuperuser(for admin panel:raijinapi:raijin1234)
    11. python manage.py makemigrations(after model is created for database)
    12. python manage.py migrate(optional)

# Running Application
    13. python manage.py runserver

