# Heroes Profile Replay Uploader - Unofficial

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![PyPi](https://img.shields.io/pypi/v/heroes-profile-replay-uploader)](https://pypi.org/project/heroes-profile-replay-uploader/)

A python script that allows a user to upload Heroes of the Storm `.StormReplay`
files to the HeroesProfile.com website.

This tool is not developed or maintained by heroesprofile.com.

## Installation

You can get this script from PyPi:

```bash
pip install heroes-profile-replay-uploader
```

## Usage

Full `--help` message from the tool.

```console
usage: heroes-profile-replay-uploader [-h] [-a ACCOUNTS_DIRECTORY] [-C CATALOGUE] [-c CONFIG] [-q] [-T THREADS] [-t TIMEOUT] [-v] [-V]

A command line uploader for Heroes of the Storm replays to heroesprofile.com

options:
  -h, --help            show this help message and exit
  -a ACCOUNTS_DIRECTORY, --accounts-directory ACCOUNTS_DIRECTORY
                        The 'Accounts' directory for Heroes of the Storm
  -C CATALOGUE, --catalogue CATALOGUE
                        The JSON file of already examined replays (default: $XDG_DATA_HOME/heroes-profile-replay-uploader/catalogue.json)
  -c CONFIG, --config CONFIG
                        The TOML file containing the application config (default: $XDG_CONFIG_HOME/heroes-profile-replay-uploader.toml)
  -q, --quiet           Run with no output (prioritised over --verbose)
  -T THREADS, --threads THREADS
                        The number of uploads to attempt concurrently (default: 1)
  -t TIMEOUT, --timeout TIMEOUT
                        The timeout in seconds (float) for API interactions (default: 10.0)
  -v, --verbose         Enable printing debug messages to stdout
  -V, --version         Print the version of the program and exit
```

Minimal command:

```bash
heroes-profile-replay-uploader --accounts-directory /path/to/the/HotS/Accounts/Dir
```

Note: `--accounts-directory` must point to the "Accounts" directory. Not the
directory of a specific given account.

## Configuration

A TOML configuration can load from
`$XDG_CONFIG_HOME/heroes-profile-replay-uploader.toml` by default.

This file supports every command line argument, except `--help` and `--version`,
under a top level table called `heroes-profile-replay-uploader`:

```toml
[heroes-profile-replay-uploader]
accounts-directory = "/path/to/accounts/directory"
catalogue = "$XDG_DATA_HOME/heroes-profile-replay-uploader/catalogue.json"
config = "$XDG_CONFIG_HOME/heroes-profile-replay-uploader.toml"
quiet = false
threads = 1
timeout = 10.0
verbose = false
```

The tool doesn't create this configuration file.
