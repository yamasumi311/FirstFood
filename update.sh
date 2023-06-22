#/usr/bin/env bash
set -o nounset
set -o errexit
set -o pipefail

git pull
sudo systemctl restart firstfood
