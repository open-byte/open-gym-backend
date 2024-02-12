#!/bin/bash
username=admin
password=cambiame

echo "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.filter(username='admin').delete(); User.objects.create_superuser(\"$username\", 'admin@example.com', \"$password\")" | python manage.py shell

echo "username: admin"
echo "password: cambiame"
