#!/bin/sh 
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
PYFILE="$SCRIPTPATH/main.py"

if [ -d "$1" ]; then
  # $1 is a dir
  cd "$1"
  find . -iname '*.epub' -printf "python $PYFILE '%p' > /dev/null 2>&1 &\0" | xargs -L1 -0 -P0 sh -c
  # find . -type f -name '*.epub' -print0 | parallel -j16 -0 python "$PYFILE" {}
else
  python "$PYFILE" "$1" > /dev/null 2>&1 &
fi