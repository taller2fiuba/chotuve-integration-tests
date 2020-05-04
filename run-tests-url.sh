#!/bin/bash

function print_usage() {
    echo "Corre las pruebas de aceptación sin levantar ningún servidor."
    echo "Uso: $0 [OPCIONES]"
    echo "Opciones:"
    echo '  --chotuve-[app|auth|media]-url=<URL>: Requerido. URL de cada servidor.'
    echo '  --no-docker-for-behave: Corre behave en la máquina local en lugar de hacerlo dentro de un contenedor de Docker.'
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

if [[ ! $CHOTUVE_MEDIA_URL ]]; then
    echo 'La URL para Chotuve Media es un parámetro requerido.'
    exit 1
fi

if [[ ! $CHOTUVE_AUTH_URL ]]; then
    echo 'La URL para Chotuve Auth es un parámetro requerido.'
    exit 1
fi

if [[ ! $CHOTUVE_APP_URL ]]; then
    echo 'La URL para Chotuve App es un parámetro requerido.'
    exit 1
fi

set -e

ACCEPTANCE_TESTS_DIR=$(readlink -f $(dirname $0))

echo 'Corriendo behave...'
if [[ ! $NO_DOCKER_FOR_BEHAVE ]]; then
    docker run -it --network="host" \
        -e CHOTUVE_MEDIA_URL=$CHOTUVE_MEDIA_URL \
        -e CHOTUVE_APP_URL=$CHOTUVE_APP_URL \
        -e CHOTUVE_AUTH_URL=$CHOTUVE_AUTH_URL \
        -v $ACCEPTANCE_TESTS_DIR:/tests \
        -w /tests \
        python:3.8 \
        sh -c 'pip install -r requirements.txt && behave'
else
    cd $ACCEPTANCE_TESTS_DIR
    behave
fi
# La limpieza se hace automáticamente antes de que termine el proceso de bash
