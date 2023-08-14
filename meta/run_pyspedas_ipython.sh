#!/usr/bin/env bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

SPEDAS_DATA_DIR=$SCRIPT_DIR/../tmp ipython "$@"
