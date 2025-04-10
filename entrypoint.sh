#!/bin/sh

# اجرای migrations
python manage.py migrate

# ساخت سوپریوزر فقط اگه وجود نداشته باشه
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser() if not User.objects.filter(username='sajjadhossein').exists() else print('Superuser already exists')" | python manage.py shell

# اجرای سرور با exec
exec gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application