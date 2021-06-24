release: python manage.py migrate
release: python manage.py flush
release: python manage.py populate_data 10
web: gunicorn doorstepdelhi.wsgi