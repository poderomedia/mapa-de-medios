# Mapa de medios
Código de Mapa de Medios

## Instalación
--------------

**Nota:** los pasos siguientes son aplicables en Debian. Para otras distros pueden necesitar algunas modificaciones. Se asume que `mysql`, `git` y `python` están instalados, y que tenemos acceso root (o sudo).

### Instalar requerimientos previos
  - Instalar pip, virtualenvwrapper

    Como `root`, para que quede instalado en el sistema:
    ```bash
  apt-get install python-pip python-dev libmysqlclient-dev
  ```

    Como usuario normal, para que `pip` instale en el ambiente del usuario y no del sistema o de `root`:
    ```bash
  pip install virtualenvwrapper
  ```

    Agregar lo siguiente a `~/.bashrc`, preferentemente al final:
    ```bash
  export WORKON_HOME=~/venvs
  source /usr/local/bin/virtualenvwrapper.sh
  ```

    Con esto tendremos instalado `virtualenvwrapper`, paquete que nos otorga los comandos `mkvirtualenv` y `workon` que usaremos más adelante.

    Cuando creemos un entorno virtual con `mkvirtualenv`, dicho entorno se creará en la carpeta `~/venvs`. Esta carpeta puede ser cualquiera otra a gusto.

  - Crear entorno virtual

    Crearemos el entorno virtual `mapa-de-medios` (aunque puede ser cualquier otro nombre a gusto):
    ```bash
  mkvirtualenv mapa-de-medios
  ```

    Con esto aparecerá `(mapa-de-medios)` adelante de nuestro prompt, algo así:
    ```
	(mapa-de-medios) usuario@maquina:~ $
    ```

### Clonar el proyecto

  Basta con ir a una carpeta donde tengamos nuestros proyectos, y hacemos:

  * SSH:
  ```
  git clone git@github.com:poderomedia/mapa-de-medios.git
  ```

  * HTTPS (Para acceso público (sin llave SSH):
  ```
  git clone https://github.com/poderomedia/mapa-de-medios.git
```

### Instalar requerimientos

  Ahora es turno de instalar los paquetes necesarios en nuestro entorno virtual, en el cual echaremos a correr este proyecto:
  ```
  cd mapa-de-medios # carpeta del proyecto recién clonado
  pip install -r requirements.txt
  ```

### Configuración local del proyecto (local settings)

  Es necesario crear un archivo que tenga los datos necesarios para que el proyecto funcione localmente. Esto también aplica para cuando estemos instalando el proyecto en un servidor, ya que "localmente" se referirá a ese servidor, y no a la máquina que estemos usando para desarrollar.

  Agregar al archivo `mediamapper/local_settings.py`:
  ```python
  SECRET_KEY = 'algún string largo y único'

  DEBUG = True  # cambiar a False si es entorno de producción
  TEMPLATE_DEBUG = DEBUG

  # Definir ALLOWED_HOSTS si DEBUG es False
  ALLOWED_HOSTS = []

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'nombre_de_la_bd',
          'USER': 'usuario',  # cambiar según configuración local
          'PASSWORD': 'password',  # cambiar según config. local
      }
  }
  ```

En `mediamapper/local_settings.py` se pueden agregar todas las configuraciones que aplicarán al entorno local en el cual se está instalando el proyecto. Cualquier configuración añadida sobreescribirá lo definido en `mediamapper/settings.py`

#### Configurar base de datos

En MySQL debemos crear la base de datos, y configurar los permisos correspondientes.

En la consola MySQL podemos hacer lo siguiente:

```sql
create database nombre_de_la_bd;
grant all privileges on nombre_de_la_bd.* to usuario@localhost identified by 'password';
```

#### Configurar superuser

Para acceder a la zona de administración del proyecto, debemos crear un superuser:

```
python manager.py createsuperuser
```

Nos pedirá
  - Nombre de usuario: poner `admin` (o alguno a gusto, **ojo: será un usuario administrador**)
  - Email: dejar en blanco o poner una dirección de correo electrónico válida
  - Contraseña: poner alguna, no se permite dejar en blanco.

### Probar ambiente de desarrollo/prueba

Hasta aquí, ya tenemos lo suficiente y necesario para echar a andar el proyecto.

Podemos ejecutar lo siguiente para hacerlo:

```
python manage.py runserver
```

Esto echa a andar el servidor de desarrollo de Django, para poder ver nuestro proyecto localmente. Dicho servidor corre en [127.0.0.1:8000](http://127.0.0.1:8000)

Las rutas disponibles son:
  - [Admin (http://127.0.0.1:8000/admin)](http://127.0.0.1:8000/admin)
  - [Home (http://127.0.0.1:8000/home)](http://127.0.0.1:8000/home)
  - [Api (http://127.0.0.1:8000/api)](http://127.0.0.1:8000/api)

### Configurar Nginx

Instalar nginx:

```
apt-get install nginx
```

#### Configurar virtualhost

Crear un archivo en `/etc/nginx/sites-available/mi-virtualhost` con el siguiente contenido:

```nginx
server {
    listen       80;
    server_name  dominio.com; ## reemplazar con el que se usará

    location / {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header Host $http_host;
		proxy_redirect off;
        proxy_pass http://127.0.0.1:8000;
	}

    location /static/ {
        # autoindex on;
        alias /ruta/a/proyecto/clonado/mapa-de-medios/static/;
	}

    location /media/ {
        alias /ruta/a/proyecto/clonado/mapa-de-medios/media/;
    }
}
```

Activar el virtualhost:

```
ln -s /etc/nginx/sites-available/mi-virtualhost /etc/nginx/sites-enabled
```

Reiniciar nginx:

```service restart nginx ```

### Configurar Supervisor

Instalar supervisor:

```
apt-get install supervisor
```

Crear el archivo `gunicorn.sh` en la carpeta raíz del proycto:

```bash
#!/bin/bash
NAME="mediamapper" # Name of the application
DJANGODIR=/ruta/al/proyecto/mapa-de-medios # Django project directory
SOCKFILE=$DJANGODIR'/gunicorn.sock' # we will communicte using this unix socket

USER=`whoami` #www-data # the user to run as
GROUP=`whoami` #www-data # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn

MAX_REQUESTS=1 # reload the application server for each request
DJANGO_SETTINGS_MODULE=mediamapper.settings # which settings file should Django use
DJANGO_WSGI_MODULE=mediamapper.wsgi # WSGI module name

echo "Starting $NAME as $USER"

# Activate the virtual environment
source /ruta/al/directorio/de/virtualenvs/mapa-de-medios/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn’t exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

echo '*****************************'
# Start your Django Unicorn

# Programs meant to be run under supervisor should not daemonize themselves (do not use –daemon)
exec /ruta/al/directorio/de/virtualenvs/mapa-de-medios/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
     --name $NAME \
     --workers $NUM_WORKERS \
     --max-requests $MAX_REQUESTS \
     --user $USER --group $GROUP \
     --bind 0.0.0.0:8000 \
     --log-level error \
     --log-file -

```

Crear `/etc/supervisor/conf.d/mapa-de-medios.conf`:

```
[program:mapa-de-medios]
directory=/ruta/al/proyecto/mapa-de-medios
command=/ruta/al/proyecto/mapa-de-medios/gunicorn.sh
autostart=true
autorestart=true
user=admin
stdout_logfile = /var/log/supervisor/%(program_name)s.log
stderr_logfile = /var/log/supervisor/%(program_name)s-error.log
```

Ejecutar como root lo siguiente, para agregar nuevo proceso a supervisor:

```
supervisorctl reread
supervisorctl update
supervisorctl restart mapa-de-medios
```

Con esto podremos ir a http://dominio.com (dominio puesto en el virtualhost de nginx), y ver el proyecto listo para usarse.
