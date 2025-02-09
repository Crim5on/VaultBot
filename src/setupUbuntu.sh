#!/bin/bash

##
# file: setupUbuntu.sh
#
# date: 2025-02-03
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
rm -r ../venv 2> /dev/null
python3 -m venv ../venv

# install the libraries:
../venv/bin/pip3 install python-telegram-bot --upgrade

# make VaultBot executable:
chmod 755 ./VaultBot.py


# clean up
sudo apt autoremove 
sudo apt autoclean 