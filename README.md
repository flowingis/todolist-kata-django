# todolist_kata_django
**ToDo List Kata - Python Django Application**

Setup iniziale
- Esecuzione prima migrazione db: `python manage.py migrate` 

Creazione di una nuova app
- Creazione app: `python manage.py startapp todo`
- Censire nuova app appena creata in settings.py
- Creazione migration: `python manage.py makemigrations todo`
- Creazione sql migration: `python manage.py sqlmigrate todo 0001`
- Applicazione migration: `python manage.py migrate`

Amministrazione
- Creazione superutente: `python manage.py createsuperuser`
- Accesso area amministrazione: `http://127.0.0.1:8000/admin/` (admin/admin123.)
- Aggiungere la gestione del model da area amministrazione: regustrare il model in `admin.py`

Riferimenti
- https://docs.djangoproject.com/en/1.8/intro/tutorial01/
- https://docs.djangoproject.com/en/1.8/intro/tutorial02/
- https://docs.djangoproject.com/en/1.8/intro/tutorial03/