# Project Description
This project is a simple To Do application which will take the tasks and save them into our server database.

## Programming languages
In this project we used [Kotlin language](https://developer.android.com/kotlin) for developing the android application and [Django Rest framework](https://www.django-rest-framework.org/) to develope  the back-end Api.

<br>

# Requirement
You will need to :<br>
  download [android studio](https://developer.android.com/studio) and sync the dependencys in gradle.build file.<br>
  download [Python](https://www.python.org/downloads/) and add it to your Path in your environment variables.<br>
  download Django framework: you can use the command<br>
```
pip install django
pip install djangorestframework
```
  

# Cloning this project
To clone this project you will need to add Secret key and Database to the 'settings.py' file

## Generating a secret key
To generate a scerete key run this commands, and make sure that you are in your project directory 'ToDoApp\myBackEnd':

```
py manage.py shell
from django.core.management.utils import get_random_secret_key 
get_random_secret_key()  
```

Then you can add the generated secret key in your settings.py file:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}
SECRET_KEY = 'GENERATED_SECRET_KEY'
