#!/bin/bash



sudo apt install -y python3.12-venv

# create a new virtual environment:
python3.12 -m venv ./env/venv

# install the libraries:
./env/venv/bin/pip3.12 install python-telegram-bot --upgrade
