#!/bin/bash

##
# file: setupUbuntu.sh
#
# date: 2025-01-26
# author: Sandro Schnetzer
# contact: https://www.linkedin.com/in/sandroschnetzer/
#
#
# Installs the Python virtual environment (venv) and sets up dependencies.
#
##


sudo apt update && sudo apt upgrade

sudo apt install -y python3-venv

# create a new virtual environment:
python3 -m venv ../venv

# install the libraries:
../venv/bin/pip3 install python-telegram-bot --upgrade

# make VaultBot executable:
chmod 755 ./VaultBot.py


# clean up
apt autoremove