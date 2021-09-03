
if ! nc -z db 5432;
    then
    echo "Database is getting up - please wait"
    sleep 5;
fi;


python manage.py migrate
python manage.py collectstatic --noinput
python manage.py create_admin
python manage.py generate_menus 15
coverage run manage.py test
coverage report -m || true
python manage.py runserver 0.0.0.0:8000