#/bin/sh

python manage.py migrate --no-input
python manage.py create_data
python manage.py runserver 0.0.0.0:8000