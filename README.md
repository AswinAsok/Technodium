<div align = "center">
  <h1>Technodium</h1>
My aim is to create an event website for my imaginary institution with different events and registration forms. 
</div>

<hr>

## Day 2 - Setting Up, Models, admin-panel and Shell

### Creating virtual environment 
```python
pip install virtualenv
py -m venv env
.\env\Scripts\activate #Activating the virtual Environment
```

### Installing django 
```python
pip install django
django-admin startproject Technodium
cd Technodium
```

### Starting app 
```python
django-admin startapp Events
```
- After creating the app add the class name to the 'settings.py' inside the 'Technodium' folder so that django can identify it as a app.

### Creating Models
- Create the models with the required informations for the app, for a event it requires name, registration fees, description etc.., then use these commands to create the database.
```python
python manage.py makemigrations 
python manage.py migrate
```

### Admin-panel
- Django has default admin-panel therefore no need to code it form the start. In order to use it we need to create a superuser, after creating the admin that password can be used to access the admin panels.
```python
python manage.py createsuperuser
```

### Shell
```python
python manage.py shell
from Events.models import Event
e = Event(event_name = "Java Coding", event_description = "Learn Java", registration_fees = "125")
e.save()
Event.objects.all()
Event.objects.filter(event_name = "Java Coding")
```
- Managers are accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations. Therefore e(instance of model class) cannot be used only Event(Model class name) can used.

## Day 3 - Views, Models, Urls, and Loading Data from Database.

<img  height="50%" width="50%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D31.png">
<img height="50%" width="50%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D32.png">

## Day 4 -  Admin Panel Customisations and Introduction to Static Files

<img  height="50%" width="50%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D41.png">
<img height="50%" width="50%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D42.png">

## Day 5 -  Django Forms and Static Files


<img  height="80%" width="80%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D51.png">
<img height="80%" width="80%" src = "https://github.com/AswinAsok/Technodium/blob/master/Images%20Progress/D52.png">


