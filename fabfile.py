# -*- coding: utf-8 -*-

import datetime
import locale
import os
import time

from fabric.api import *
from fabric.contrib import files, django

# importo los settings del proyecto
django.project('mediamapper')
from mediamapper import settings as project_settings


#locale.setlocale(locale.LC_ALL, 'es_CL.utf8')
local_path = os.path.dirname(os.path.abspath(__file__))

env.use_ssh_config = True


def hello():
    print("Hello world!")


def restart_nginx(host, base_dir="/home/admin/html",
                  port=8000, user='admin'):
    ctx = {
        'base_dir': base_dir,
        'port': port,
        'host': host
    }
    with settings(host_string=host, user=user):
        nginx_conf = '/etc/nginx/sites-available/%s' % host
        nginx_template = 'fabric_templates/nginx_template'
        files.upload_template(nginx_template, nginx_conf,
                              context=ctx, mode=0755, use_jinja=False,
                              use_sudo=True)

        sudo("cat %s" % nginx_conf)
        sudo("rm -rf /etc/nginx/sites-enabled/%s" % host)
        sudo("ln -s %s /etc/nginx/sites-enabled/" % nginx_conf)
        sudo("service nginx restart")


def restart_supervisor(host, user='admin'):
    with settings(host_string=host, user=user):
        run("sudo service supervisor restart")


def restart_gunicorn(host, user='admin', base_dir='/home/admin/html/'):
    ctx = {
        'base_dir': base_dir + 'current'
    }
    with settings(host_string=host, user=user):
        gunicorn_script = os.path.join(base_dir, 'current/gunicorn.sh')
        gunicorn_source_file = 'fabric_templates/gunicorn_template.sh'
        files.upload_template(gunicorn_source_file, gunicorn_script,
                              context=ctx, mode=0755, use_jinja=False)
        run("cat %s" % gunicorn_script)

        supervisor_conf = '/etc/supervisor/conf.d/mapa-de-medios.conf'
        supervisor_source_file = 'fabric_templates/supervisor_template.conf'
        files.upload_template(supervisor_source_file, supervisor_conf,
                              context=ctx, mode=0755, use_jinja=False,
                              use_sudo=True)
        sudo("cat %s" % supervisor_conf)

        sudo("supervisorctl reread")
        sudo("supervisorctl update")
        sudo("supervisorctl restart mapa-de-medios")


def deploy(host, branch, user='admin', base_dir='/home/admin/html/'):
    """
    Esto hace el deploy de la aplicación.

    Se deben hacer los siguientes pasos:

    1. Clonar el proyecto en una carpeta con el timestamp
    2. Crear enlace simbólico a la carpeta con el timestamp
    3. En la carpeta nueva configurar local_settings.py (copiar anterior)
    4. Configurar base de datos
      4.1. Respaldar base de datos (mysqldump)
      4.2. Sincronizar (syncdb) o ejecutar migraciones (migrate)
    5. Instalar requirements, Collect static, migrate, syncdb
    6. Reiniciar gunicorn
    """
    db = db_credentials()

    print "Pull in host: %s, branch: %s, at %s" % (host, branch, base_dir)
    with settings(host_string=host, user=user):
        if not files.exists(base_dir):
            run("mkdir -p %s" % base_dir)
        with cd(base_dir):
            run("rm -rf mapa-de-medios")

            # # paso 1
            timestamp = int(time.time())
            st_datetime = datetime.datetime.fromtimestamp(timestamp)
            st = st_datetime.strftime("%Y-%m-%d_%H-%M-%S")
            st_version = "version-%s" % st

            # se obtiene versión anterior para recuperar local settings
            print "Se obtiene última versión en %s " % base_dir
            last_version = 'ninguna'
            output = run('ls %s' % base_dir)
            files_ = output.split()
            if len(files_) > 0:
                last_version = files_[-1]
            print "Última versión: %s" % last_version

            run("git clone -q -b %s --single-branch " % branch +
                "https://github.com/poderomedia/mapa-de-medios.git" +
                " %s" % st_version)
            # # fin paso 1

            # # paso 2
            # se borra enlace actual
            run("rm -rf current")
            # y creamos el que bajamos de nuevo
            run("ln -s %s current" % st_version)
            # # fin paso 2

            # entro a la carpeta current para trabajar ahí ahora
            with cd('current'):
                run("pwd;ls -al ../current")

                # # paso 3
                local_settings = "mediamapper/local_settings.py"
                last_local_settings = os.path.join(
                    base_dir,
                    last_version,
                    local_settings
                )
                if files.exists(last_local_settings):
                    print "Se restaura archivo de configuración local" + \
                        " anterior."
                    run("cat %s" % last_local_settings)
                    run("cp ../%s/%s %s" % (last_version, local_settings,
                                            local_settings))
                else:
                    # setear db_name con --set db_name="dbname"
                    ctx = {
                        'db_name': db['name'],
                        'db_user': db['user'],
                        'db_password': db['password'],
                        'secret_key': 'mi súper secreta llave'
                    }
                    print ctx
                    print "Se crea archivo nuevo de configuración local."
                    print "CONFIGURAR USUARIO, CONTRASEÑA, "
                    local_settings_template = 'fabric_templates' +\
                                              '/local_settings.py'
                    files.upload_template(local_settings_template,
                                          local_settings,
                                          context=ctx, mode=0755,
                                          use_jinja=False)
                    run("cat %s" % local_settings)
                # # fin paso 3

                # sigo acá después del local settings
                # # paso 4, base de datos
                dump_db()

                # # paso 5, collect static
                # si no existe el virtualenv lo creo
                if not files.exists('./env'):
                    run('virtualenv env')

                # ya creado el virtualenv lo activo
                with prefix('source ./env/bin/activate'):
                    run('pip install -r requirements.txt')
                    run('./manage.py collectstatic --noinput')
                    run('./manage.py migrate')
                    run('./manage.py syncdb')

        # se reinicia gunicorn
        restart_gunicorn(host, user)


def deploy_staging():
    host = 'staging.poderopedia.org'
    branch = 'staging'
    deploy(host, branch)


def deploy_dev():
    host = 'dev.poderopedia.org'
    branch = 'dev'
    deploy(host, branch)


def deploy_production():
    host = 'www.poderopedia.org'
    branch = 'master'
    deploy(host, branch)


def deploy_prod():
    deploy_production()


def db_credentials():
    '''
    Obtiene las credenciales desde settings.py
    '''
    db = {
        'name': project_settings.DATABASES['default']['NAME'],
        'user': project_settings.DATABASES['default']['USER'],
        'password': project_settings.DATABASES['default']['PASSWORD'],
    }
    return db


def dump_db():
    db = db_credentials()
    timestamp = int(time.time())
    st_datetime = datetime.datetime.fromtimestamp(timestamp)
    st = st_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    print "Usando los siguientes datos:"
    print "Nombre de la base de datos: %s" % db['name']
    print "Nombre de usuario de la base de datos: %s" % db['user']
    print "Password de la base de datos: %s" % db['password']
    run('mysqldump -u %s -p"%s" %s > /tmp/db_backup-%s.sql' % (
        db['user'],
        db['password'],
        db['name'],
        st))
