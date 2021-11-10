#!/usr/bin/env sh

set -o errexit
set -o nounset

# We are using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production",
# fail otherwise, since it may break things:
echo "DJANGO_ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" != 'production' ]; then
  echo 'Error: DJANGO_ENV is not set to "production".'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_ENV

# Collect static
python /code/manage.py collectstatic --noinput

# Start gunicorn:
# Docs: http://docs.gunicorn.org/en/stable/settings.html
/usr/local/bin/gunicorn server.wsgi \
  --workers=4 \
  --max-requests=2000 \
  --max-requests-jitter=400 \
  --bind='0.0.0.0:8000'
