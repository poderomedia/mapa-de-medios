#!/bin/bash
NAME="mediamapper" # Name of the application
DJANGODIR=%(base_dir)s # Django project directory
SOCKFILE=$DJANGODIR'/gunicorn.sock' # we will communicte using this unix socket

USER=`whoami` #www-data # the user to run as
GROUP=`whoami` #www-data # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn

MAX_REQUESTS=1 # reload the application server for each request
DJANGO_SETTINGS_MODULE=mediamapper.settings # which settings file should Django use
DJANGO_WSGI_MODULE=mediamapper.wsgi # WSGI module name

echo "Starting $NAME as $USER"

# Activate the virtual environment
source $DJANGODIR/env/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn’t exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

echo '*****************************'
# Start your Django Unicorn

# Programs meant to be run under supervisor should not daemonize themselves (do not use –daemon)
exec $DJANGODIR/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
     --name $NAME \
     --workers $NUM_WORKERS \
     --max-requests $MAX_REQUESTS \
     --user $USER --group $GROUP \
     --bind 0.0.0.0:8000 \
     --log-level error \
     --log-file -
