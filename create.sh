#!/bin/bash

echo 1. render.py
[ -d a ] && rm -r a
mkdir a
./render.py

echo 2. gulp build-css
gulp build-css
