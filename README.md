# eMenu

Siple REST API created to manage restaurant's menus. You can add, update and delete dishes and menus. Email notification with new dishes. Created with Django framework.


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Technologies
* Python version: 3.8.5
* Django version: 3.2.2
* Django REST framework version: 3.12.4
* Docker version: 19.03.8

## Setup
To build backend locally:
```
docker-compose up --build
```

After that, a couple things would happen:
```
- database creation,
- database migrations creation,
- static files collection,
- basic admin account creation,
- primary data initialization,
- tests with coverage report creation,
- Django server creation,
```

To API documentation:
```
http://localhost:8000/swagger/
```

To main API route:
```
http://localhost:8000/api/menus/
```

For home page of app:
```
http://localhost:8000/
```

## Contact
Created by Adam Misiak
