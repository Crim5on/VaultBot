# VaultBot

Hi, I'm VaultBot, your insanity avoidance companion!

Simple chatbot to enhance our flatshare's Telegram chat. Bot listens to certain keywords and replies with the according answer specified in a custom dictionary.  

## Setup

This project is designed to run on Debian and Red Hat based Linux distributions (e.g. Ubuntu & Fedora). To get started, execute the setup script ```setupUbuntu.sh``` or ```setupFedora.sh```. This will install all dependencies and set up a Python virtual environment (venv). Note that the path to the environment's Python interpreter must be specified in the shebang line of the Python script that uses it. Don't forget to edit the config file ```config.json``` to point to your local token file. Don't check in your token file!

```bash
# go to source folder:
cd ./src

# make setup script executable:
chmod 755 setupUbuntu.sh    # or setupFedora.sh

# execute setup script:
./setupUbuntu.sh            # or setupFedora.sh

# run VaulBot:
./VaultBot.py
```

## Configuration

Specify the path to your token and dictionary in the config file (under```./src/config.json```). The dictionary is what makes VaultBot seem "socially intelligent". Think of a list of keywords and replies - be creative!

```json
{
    "tokenfile" : "/path/to/mytoken.token"
}
```

## Actionshots

<p align="middle">
  <img src="./img/screenshotChat2.png" width="230" hspace="20" />
  <img src="./img/screenshotChat1.png" width="230" hspace="20" />
  <img src="./img/screenshotChat3.png" width="230" hspace="20" />
</p>
