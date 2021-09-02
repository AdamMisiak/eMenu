python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createadmin
python manage.py generate_menus 15
python manage.py test
coverage report -m
python manage.py runserver 0.0.0.0:8000