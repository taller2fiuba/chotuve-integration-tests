#!/bin/bash

# Este script permite correr automáticamente las pruebas de aceptación.
# El mismo puede descargar y levantar automáticamente los servicios requeridos
# o utilizar servicios según la URL indicada.
#
# Para correr las pruebas levantando automáticamente todos los servicios:
# ./run-acceptance-tests.sh
# Se clonarán los repositorios, levantaran los servicios mediante docker-compose
# y luego se correrá behave dentro de un contenedor de Docker. Al finalizar se
# limpiaran los archivos temporales dejando el sistema donde se corrió intacto.
# El único rastro que puede quedar son imagenes oficiales de Docker descargadas.

REPO_CHOTUVE_MEDIA="https://github.com/taller2fiuba/chotuve-media-server"
REPO_CHOTUVE_APP="https://github.com/taller2fiuba/chotuve-app-server"
REPO_CHOTUVE_AUTH="https://github.com/taller2fiuba/chotuve-auth-server"

function print_usage() {
    echo "Levanta versiones productivas de los servidores y corre las pruebas de aceptación."
    echo "Uso: $0 [OPCIONES]"
    echo "Opciones:"
    echo '  --chotuve-[app|auth|media]-repo=<directorio>: Ubicación del repositorio para un servidor.'
    echo '      Si no se pasa esta opción para alguno de los servidores, se lo clonará desde su repositorio.'
    echo '  --no-docker-for-behave: Corre behave en la máquina local en lugar de hacerlo dentro de un contenedor de Docker.'
}

# Procesar argumentos
for arg in "$@"
do
case $arg in
    --chotuve-media-repo=*)
        export CHOTUVE_MEDIA_REPO_DIR=$(readlink -f "${arg#*=}")
    shift
    ;;
    --chotuve-app-repo=*)
        export CHOTUVE_APP_REPO_DIR=$(readlink -f "${arg#*=}")
    shift
    ;;
    --chotuve-auth-repo=*)
        export CHOTUVE_AUTH_REPO_DIR=$(readlink -f "${arg#*=}")
    shift
    ;;
    --no-docker-for-behave)
        export NO_DOCKER_FOR_BEHAVE=1
    shift
    ;;
    *)
         print_usage;
         exit 1;
    ;;
esac
done

function get_random_free_port() {
    while :
    do
        PORT="`shuf -i 49152-65535 -n 1`"
        ss -lpn | grep -q ":$PORT " || break
    done
    echo $PORT
}

function wait_server() {
    TIMEOUT=60
    until curl -s -o /dev/null --connect-timeout 1 $1;
    do
        echo "Esperando $TIMEOUT segs para $1."
        sleep 5
        TIMEOUT=$((TIMEOUT-5))
        if ((TIMEOUT < 0)); then
            echo 'Se acabó el tiempo de espera'
            exit 1
        fi
    done;
}

function cleanup() {
    # Limpieza
    if [[ -d $TMPDIR/chotuve-media-server ]]; then
        cd $TMPDIR/chotuve-media-server
        docker-compose down -v --rmi local
    else
        if [[ -d $CHOTUVE_MEDIA_REPO_DIR ]]; then
            cd $CHOTUVE_MEDIA_REPO_DIR
            docker-compose stop
        fi
    fi
    if [[ -d $TMPDIR/chotuve-app-server ]]; then
        cd $TMPDIR/chotuve-app-server
        docker-compose down -v --rmi local
    else
        if [[ -d $CHOTUVE_APP_REPO_DIR ]]; then
            cd $CHOTUVE_APP_REPO_DIR
            docker-compose stop
        fi
    fi
    if [[ -d $TMPDIR/chotuve-auth-server ]]; then
        cd $TMPDIR/chotuve-auth-server
        docker-compose down -v --rmi local
    else
        if [[ -d $CHOTUVE_AUTH_REPO_DIR ]]; then
            cd $CHOTUVE_AUTH_REPO_DIR
            docker-compose stop
        fi
    fi
    cd $TMPDIR/..
    rm -rf $TMPDIR

    if [[ $REMOVE_DOCKER_NETWORK ]]; then
        echo 'Eliminado red de Docker "chotuve"'
        docker network remove chotuve
    fi
}

function setup_media_server() {
    if [[ ! $CHOTUVE_MEDIA_REPO_DIR ]]; then
        echo 'Obteniendo versión productiva de Chotuve Media'
        cd $TMPDIR
        git clone $REPO_CHOTUVE_MEDIA
        export CHOTUVE_MEDIA_REPO_DIR=$TMPDIR/chotuve-media-server
    fi
    cd $CHOTUVE_MEDIA_REPO_DIR
    export CHOTUVE_MEDIA_PORT=$(get_random_free_port)
    export CHOTUVE_MEDIA="http://localhost:$CHOTUVE_MEDIA_PORT"
    echo "Configurando versión productiva de Chotuve Media en $CHOTUVE_MEDIA"
    docker-compose up -d --build
    wait_server $CHOTUVE_MEDIA
}

function setup_app_server() {
    if [[ ! $CHOTUVE_APP_REPO_DIR ]]; then
        echo 'Obteniendo versión productiva de Chotuve App'
        cd $TMPDIR
        git clone $REPO_CHOTUVE_APP
        export CHOTUVE_APP_REPO_DIR=$TMPDIR/chotuve-app-server
    fi
    cd $CHOTUVE_APP_REPO_DIR
    export CHOTUVE_APP_PORT=$(get_random_free_port)
    export CHOTUVE_APP="http://localhost:$CHOTUVE_APP_PORT"
    echo "Configurando versión productiva de Chotuve App en $CHOTUVE_APP"
    docker-compose up -d --build
    wait_server $CHOTUVE_APP
}

function setup_auth_server() {
    if [[ ! $CHOTUVE_AUTH_REPO_DIR ]]; then
        echo 'Obteniendo versión productiva de Chotuve Auth'
        cd $TMPDIR
        git clone $REPO_CHOTUVE_AUTH
        export CHOTUVE_AUTH_REPO_DIR=$TMPDIR/chotuve-auth-server
    fi
    cd $CHOTUVE_AUTH_REPO_DIR
    export CHOTUVE_AUTH_PORT=$(get_random_free_port)
    export CHOTUVE_AUTH="http://localhost:$CHOTUVE_AUTH_PORT"
    echo "Configurando versión productiva de Chotuve Auth en $CHOTUVE_AUTH"
    docker-compose up -d --build
    wait_server $CHOTUVE_AUTH
}

trap cleanup EXIT
set -e

ACCEPTANCE_TESTS_DIR=$(readlink -f $(dirname $0))

# Crear una carpeta temporal
TMPDIR=$(mktemp -d -t ci-XXXXXXXXXX)
cd $TMPDIR

if [[ ! $(docker network ls -f name=chotuve$ -q) ]]; then
    echo 'Creando red "chotuve"'
    docker network create -d bridge chotuve
    export REMOVE_DOCKER_NETWORK=1
fi

setup_media_server
setup_auth_server
setup_app_server

echo 'Corriendo behave...'
if [[ ! $NO_DOCKER_FOR_BEHAVE ]]; then
    docker run -it --network="host" \
        -e CHOTUVE_MEDIA_URL=$CHOTUVE_MEDIA \
        -e CHOTUVE_APP_URL=$CHOTUVE_APP \
        -e CHOTUVE_AUTH_URL=$CHOTUVE_AUTH \
        -v $ACCEPTANCE_TESTS_DIR:/tests \
        -w /tests \
        python:3.8 \
        sh -c 'pip install -r requirements.txt && behave'
else
    cd $ACCEPTANCE_TESTS_DIR
    CHOTUVE_MEDIA_URL=$CHOTUVE_MEDIA CHOTUVE_APP_URL=$CHOTUVE_APP CHOTUVE_AUTH_URL=$CHOTUVE_AUTH behave
fi
# La limpieza se hace automáticamente antes de que termine el proceso de bash
