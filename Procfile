release: python manage.py migrate
web: gunicorn mysite.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
python manage.py migrate