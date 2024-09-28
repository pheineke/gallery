#!/bin/bash

# Gehe in das Verzeichnis deines Git-Repos
cd /app || exit

# Pull die neuesten Änderungen
git pull

# Starte den Flask-Server neu
touch wsgi.py  # Dies löst einen Reload in Flask aus, wenn du den Debug-Modus verwendest
