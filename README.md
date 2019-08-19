[![Build Status](https://travis-ci.org/pylipp/ckp.svg?branch=master)](https://travis-ci.org/pylipp/ckp)

## `ckp`

> Command line utility for Copying Keepass Passwords

## Installation

    pip install git+https://github.com/pylipp/ckp.git#egg=ckp

## Usage

Set up a database at `~/.database.kdbx` and add some entries (or move an existing database). Query an entry from the command line by running

    ckp <entry>

You're prompted for the master password. If correct, and if the specified entry exists, the password is copied to the system clipboard (check the `pyperclip` package for system dependencies). The system clipboard is cleared after ten seconds.

## Testing

    git clone https://github.com/pylipp/ckp
    cd ckp
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -e .
    python test.py

## Releasing

- increase version number in `setup.py`, stage and commit
- run `make release`
