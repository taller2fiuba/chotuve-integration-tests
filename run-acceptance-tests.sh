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
    echo "Corre las pruebas de aceptación."
    echo "Uso: $0 [--chotuve-media-url=<MEDIA URL>] [--chotuve-app-url=<APP URL>] [--chotuve-auth-url=<AUTH URL>]"
    echo "Si se le pasa --chotuve-media-url y/o --chotuve-app-url se utilizarán esas URLs para"
    echo "contactar al servidor de Flask y Node, respectivamente."
    echo "Si no se pasa alguno de esos parámetros el script levantará una imagen"
    echo "productiva del servidor correspondiente mediante docker-compose".
}

# Procesar argumentos
for arg in "$@"
do
case $arg in
    --chotuve-media-url=*)
        export CHOTUVE_MEDIA_URL="${arg#*=}"
    shift
    ;;
    --chotuve-app-url=*)
        export CHOTUVE_APP_URL="${arg#*=}"
    shift
    ;;
    --chotuve-auth-url=*)
        export CHOTUVE_AUTH_URL="${arg#*=}"
    shift
    ;;
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
    export CHOTUVE_MEDIA_URL="http://localhost:$CHOTUVE_MEDIA_PORT"
    echo "Configurando versión productiva de Chotuve Media en $CHOTUVE_MEDIA_URL"
    docker-compose up -d --build
    wait_server $CHOTUVE_MEDIA_URL
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
    export CHOTUVE_APP_URL="http://localhost:$CHOTUVE_APP_PORT"
    echo "Configurando versión productiva de Chotuve App en $CHOTUVE_APP_URL"
    docker-compose up -d --build
    wait_server $CHOTUVE_APP_URL
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
    export CHOTUVE_AUTH_URL="http://localhost:$CHOTUVE_AUTH_PORT"
    echo "Configurando versión productiva de Chotuve Auth en $CHOTUVE_AUTH_URL"
    docker-compose up -d --build
    wait_server $CHOTUVE_AUTH_URL
}

trap cleanup EXIT
set -e

ACCEPTANCE_TESTS_DIR=$(pwd)

# Crear una carpeta temporal
TMPDIR=$(mktemp -d -t ci-XXXXXXXXXX)
cd $TMPDIR

if [[ ! $CHOTUVE_MEDIA_URL ]]; then
    setup_media_server
fi

if [[ ! $CHOTUVE_AUTH_URL ]]; then
    setup_auth_server
fi

if [[ ! $CHOTUVE_APP_URL ]]; then
    setup_app_server
fi

echo 'Corriendo behave...'
docker run -it --network="host" \
    -e CHOTUVE_MEDIA_URL=$CHOTUVE_MEDIA_URL \
    -e CHOTUVE_APP_URL=$CHOTUVE_APP_URL \
    -e CHOTUVE_AUTH_URL=$CHOTUVE_AUTH_URL \
    -v $ACCEPTANCE_TESTS_DIR:/tests \
    -w /tests \
    python:3.8 \
    sh -c 'pip install -r requirements.txt && behave'

# La limpieza se hace automáticamente antes de que termine el proceso de bash
