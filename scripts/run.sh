#!/bin/sh

# stop script execution when error
set -e

#apply migrations
python manage.py migrate

# move all static files to STATIC_ROOT folder
python manage.py collectstatic --noinput

# Start wsgi server on port 9000
uwsgi --socket :9000 --workers 4 --master --enable-threads --module  digitaleasyproj.wsgi