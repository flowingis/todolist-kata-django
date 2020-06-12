# todolist_kata_django
**ToDo List Kata - Python Django Application**

Setup iniziale
- Esecuzione prima migrazione db: `python manage.py migrate` 

Creazione di una nuova app
- Creazione app: `python manage.py startapp todo`
- Censire nuova app appena creata in settings.py
- Creazione migration: `python manage.py makemigrations todo`
- Applicazione migration: `python manage.py migrate`

Rest Framework
- Installare il package djangorestframework: `pip install djangorestframework`
- Installare le estensioni django-extensions: `pip install django-extensions`
- Aggiungerea INSTALLED_APPS in settings.py le chiavi:
    - `rest_framework`
    - `django_extensions`
- Vedere tutte le URL esposte: `python manage.py show_urls`

Amministrazione
- Creazione superutente: `python manage.py createsuperuser`
- Accesso area amministrazione: `http://127.0.0.1:8000/admin/` (admin/admin123.)
- Aggiungere la gestione del model da area amministrazione: regustrare il model in `admin.py`

Riferimenti
- https://docs.djangoproject.com/en/3.0/intro/tutorial01/
- https://docs.djangoproject.com/en/3.0/intro/tutorial02/
- https://docs.djangoproject.com/en/3.0/intro/tutorial03/
- https://www.django-rest-framework.org/tutorial/quickstart/
- https://pypi.org/project/django-extensions/
- https://docs.djangoproject.com/en/3.0/topics/testing/