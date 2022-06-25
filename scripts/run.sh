#!/bin/sh

set -e

python manage.py migrate

python manage.py collectstatic --noinput

uwsgi --socket :9000 --workers 4 --master --enable-threads --module  digitaleasyproj.wsgi