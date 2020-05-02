# Pruebas de aceptación

Este script permite correr automáticamente las pruebas de aceptación. El mismo puede 
descargar y levantar automáticamente los servicios requeridos o utilizar servicios 
según la URL indicada.

## Requerimientos:
- Docker
- Docker Compose

## Cómo correr las pruebas

### Para correr las pruebas levantando automáticamente todos los servicios:

```bash
$ ./run-acceptance-tests.sh
```

El script clonará los repositorios, levantará los servicios mediante `docker-compose`
y luego se correrá behave dentro de un contenedor de Docker. Al finalizar se limpiaran 
los archivos temporales dejando el sistema donde se corrió intacto.
El único rastro que puede quedar son imagenes oficiales de Docker descargadas.

### Para correrlo utilizando un Chotuve App en una URL específica:

```bash
$ ./run-acceptance-tests.sh --chotuve-app-url=http://localhost:27080
```

En este caso sólo se clonarán y levantarán los servicios Auth y Media. Las pruebas
se correrán en un contenedor de Docker utilizando la URL indicada.

### Para correrlo sin levantar ningún servicio extra:

```bash
$ ./run-acceptance-tests.sh --chotuve-app-url=http://localhost:27080 \
                            --chotuve-media-url=http://localhost:5000 \
                            --chotuve-auth-url=http://localhost:5001
```

En este caso no se clonará ningún repositorio, las pruebas se correrán dentro 
de Docker realizando solicitudes a dichas URL.

### Para correrlo desde un repositorio ya clonado

```bash
$ ./run-acceptance-tests.sh --chotuve-app-repo=./chotuve-app-server
```

En este caso no se clonará el repo del App server, pero sí se levantarán las versiones 
productivas del Media y Auth server. En este caso no se realizará limpieza de 
la ejecución. El contenedor se detendrá mediante `docker-compose stop`.


Todos los parámetros `--<chotuve-app|chotuve-media|chotuve-auth>-*` tienen su 
versión para las otras variantes.
