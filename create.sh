#!/bin/bash

# 1. render templates from markdowned articles
./render.py

# 2. preprocess scss styles. Copy over library css
mkdir -p css
sass --scss _styles/style.scss > css/style.css
cp _includes/*.css css
