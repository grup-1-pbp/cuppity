# Procfile
release: python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --no-input
web: gunicorn mangan_yuk.wsgi:application --bind 0.0.0.0:8000