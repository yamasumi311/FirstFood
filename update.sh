#/usr/bin/env bash
set -o nounset
set -o errexit
set -o pipefail

git reset --hard
git pull
sudo systemctl restart firstfood
