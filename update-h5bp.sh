#!/bin/bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
TARGET=${DIR}/files/h5bp-server-configs-nginx.tar.gz

prepare() {
    rm --recursive --force ${DIR}/files/h5bp
    cleanup
}

cleanup() {
    rm --recursive --force ${DIR}/files/h5bp-server-configs*
}

download_latest() {
    local filename=$1

    cleanup
    local latest_url=$( curl --silent https://api.github.com/repos/h5bp/server-configs-nginx/releases/latest | grep tarball_url | cut -d : -f 2,3 | tr -d '", ' )
    curl --silent --output ${filename} --location $latest_url

    tar --extract --gzip --directory $( dirname $filename ) --file $filename

    H5BP_DIR=$( ls -d $( dirname $filename )/h5bp-server-configs*/)
    H5BP_DIR=${H5BP_DIR%/}
}

prepare
download_latest $TARGET

cp --recursive $H5BP_DIR/h5bp ${DIR}/files/h5bp
cp $H5BP_DIR/mime.types ${DIR}/files/mime.types

cleanup
