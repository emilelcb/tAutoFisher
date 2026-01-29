#!/usr/bin/env bash
mkdir -p logs

printf -v date '%(%Y:%m:%d-%H:%M:%S)T\n' -1

valgrind -s                    \
  --log-file="logs/coredump-${date}.log" \
  --leak-check=full            \
  --show-leak-kinds=all        \
  --track-origins=yes          \
  ./dist/tAutoFisher/tAutoFisher
