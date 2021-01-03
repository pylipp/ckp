"""Utility to temporarily Copy Keepass Password to system clipboard."""

import getpass
import sys
import os
import shutil
import time
import argparse

import pykeepass
import pyperclip

DATABASE_FILEPATH = "~/.database.kdbx"


def copy_entry(entry_name, database_filepath=None):
    """Copy the password corresponding to the given entry to the system
    clipboard.
    The user is prompted to give the correct master password to open the
    database file (default is `~/.database.kdbx` which can be overwritten). The
    function raises a SystemExit if the database file is not found.
    The password is then copied to the system clipboard. A progress bar is
    displayed. After ten seconds, the clipboard is cleared.
    """
    while True:
        password = getpass.getpass()
        try:
            database_filepath = database_filepath or DATABASE_FILEPATH
            kp = pykeepass.PyKeePass(
                os.path.expanduser(database_filepath), password=password)
            break
        except FileNotFoundError:
            raise SystemExit("Database file does not exist.")
        except IOError:
            print("Invalid password. Try again.", file=sys.stderr)

    try:
        entry = kp.find_entries_by_title(entry_name, first=True)
        message = "Entry '{}' not found. ".format(entry_name)
    except IndexError:
        entry = None
        message = ""

    if entry is None:
        # print entry titles in database
        print("{}Choose from:".format(message), file=sys.stderr)
        print('\n'.join(("{e.title} ({e.username})".format(e=e) for e in kp.entries)),
            file=sys.stderr)
        raise SystemExit()
    else:
        pyperclip.copy(entry.password)
        print("Password has been copied to clipboard!")

        terminal_width = shutil.get_terminal_size().columns
        time_left = 50  # 50 increments of 0.2s = 10s
        increment = int(terminal_width / time_left)
        residual = terminal_width - time_left * increment
        char = '#'

        try:
            while time_left:
                time.sleep(0.2)
                time_left -= 1
                print(increment * char, end="", flush=True)
            print(residual * char)
        except KeyboardInterrupt:
            pass

        pyperclip.copy("")


def main(args=None):
    """Main entry point of the application."""
    parser = argparse.ArgumentParser(description=globals()["__doc__"])
    parser.add_argument("entry", help="name of the entry to retrieve")
    parser.add_argument("-d", "--database-filepath",
                        help="optional filepath of database. Default: {}".format(
                            DATABASE_FILEPATH))
    args = parser.parse_args(args)

    copy_entry(args.entry, args.database_filepath)
