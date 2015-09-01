#!/bin/bash

echo 1. render templates from markdowned articles
[ -d articles ] && rm -r articles
mkdir articles
./render.py

echo 2. preprocess scss styles. Copy over library css
mkdir -p css
sass --scss _styles/style.scss > css/style.css
