# Dost
Dost is a [Discord](https://discord.com) bot for viewing currencies.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

## Prerequisites
Dost requires Python v3.6 or above. To install python3 package write the command below to your terminal.
### Debian Based Distributions
```bash
sudo apt install python3
```
### Arch Based Distributions
```bash
sudo pacman -S python3
```
### Redhat and Fedora Based Distributions
```bash
sudo dnf install python3
```

## Installation
To install dost to your system, you need to enter the commands below to your terminal.
```bash
git clone https://github.com/brngklp/dost ; cd dost ; pip install -r requirements.txt ;
```

## Usage
To use dost, You first need to create a discord bot from [Discord Developer Portal](https://discord.com/developers/applications). After you create the bot, you need to copy the token of your bot and paste it to the token variable at [main.py](https://github.com/brngklp/dost/blob/main/src/main.py). If you're a developer and you want to improve this project, you can copy your server's Id and paste it to the default_enabled_guilds variable at [main.py](https://github.com/brngklp/dost/blob/main/src/main.py). Dost works with Slash commands that you enter in Discord. The available commands are listed in the [Available Commands Section](https://github.com/brngklp/dost/blob/main/README.md#available-commands)

## Available Commands
```
        `help`- Prints the help message.
        `dollar` - Prints out the usd to try currency.
        `dost` - Gives you the choice to select the currency and the base.
```

## Built with
[Hikari](https://github.com/hikari-py/hikari)  
[Hikari Lightbulb](https://github.com/tandemdude/hikari-lightbulb)  
[Coinbase API](https://developers.coinbase.com/api/v2)

## Contributing
To report bugs and suggest new feature use the [issue tracker](https://github.com/brngklp/dost/issues). If you have some code which you would like to be merged, then open a [pull request](https://github.com/brngklp/dost/pulls).

## Authors
Baran Gokalp

## License
This project is licensed under the MPL-2.0 License - see the [LICENSE](https://github.com/brngklp/dost/blob/main/LICENSE) file for details
