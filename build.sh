#!/usr/bin/env bash
set -euo pipefail

INSTALL="poetry run pyinstaller tAutoFisher/__main__.py -y -n tAutoFisher"
if [[ $(uname) == "Linux" ]] && command -v nix &>/dev/null; then
  nix develop .#default -i \
    --command bash -c "$INSTALL"
else
  $INSTALL
fi
