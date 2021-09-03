# eMenu

Simple REST API created to manage restaurant's menus. It allows to add, update and delete dishes and menus, as well as to send email notifications with new dishes. Created with Django framework.


## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## Technologies
* Python version: 3.8.5
* Django version: 3.2.4
* Django REST framework version: 3.12.4
* Docker version: 19.03.8

## Setup
To build backend locally:
```
docker-compose up --build
```

After that, a couple things will be either created or initialized:
```
- database,
- database migrations,
- static files,
- basic admin account,
- primary data,
- tests with coverage report,
- Django server,
```

API documentation:
```
http://localhost:8000/swagger/
```

Main API route:
```
http://localhost:8000/api/menus/
```

Default admin account:
```
username: admin
email: admin@admin.com
password: Temp1234
```

## Contact
Created by Adam Misiak
