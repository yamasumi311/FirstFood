#/usr/bin/env bash
set -o nounset
set -o errexit
set -o pipefail

git pull
service firstfood restart
