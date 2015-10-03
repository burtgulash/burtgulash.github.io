#!/bin/bash

echo install npm
sudo apt-get install npm

# http://stackoverflow.com/questions/26320901/cannot-install-nodejs-usr-bin-env-node-no-such-file-or-directory
sudo ln -s /usr/bin/nodejs /usr/bin/node

echo install gulp
sudo npm install -g gulp

echo install gulp + plugins
sudo npm install --save-dev gulp
sudo npm install --save-dev gulp-rename
sudo npm install --save-dev gulp-concat
sudo npm install --save-dev gulp-sass
sudo npm install --save-dev gulp-sourcemaps
