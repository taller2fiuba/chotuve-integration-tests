#!/bin/bash


export CHOTUVE_APP_URL=http://localhost:28080
export CHOTUVE_AUTH_URL=http://localhost:26080
export CHOTUVE_MEDIA_URL=http://localhost:27080

ACCEPTANCE_TESTS_DIR=$(readlink -f $(dirname $0))

cd $ACCEPTANCE_TESTS_DIR
exec behave $@
