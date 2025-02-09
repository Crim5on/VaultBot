#!/bin/bash

##
# file: setupFedora.sh
#
# date: 2025-01-31
# author: Sandro Schnetzer
# contact: https://www.linkedin.com/in/sandroschnetzer/
#
#
# Installs the Python virtual environment (venv) and sets up dependencies.
#
##


sudo dnf upgrade

sudo dnf install -y python3-virtualenv

# create a new virtual environment:
rm -r ../venv 2> /dev/null
python3 -m venv ../venv

# install the libraries:
../venv/bin/pip3 install python-telegram-bot --upgrade

# make VaultBot executable:
chmod 755 ./VaultBot.py


# clean up
sudo dnf autoremove
sudo dnf clean all