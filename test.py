import unittest
from unittest import mock
import getpass
import time
import os

import pyperclip
import pykeepass

import main

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILEPATH = os.path.join(ROOT_DIR, "database.kdbx")


class CkpTest(unittest.TestCase):

    def setUp(self):
        # Mock input of Master password to avoid prompting
        getpass.getpass = mock.MagicMock(return_value="master")
        # Mock for instant completion of progress bar
        time.sleep = mock.MagicMock()
        # Mock for verifying copying
        pyperclip.copy = mock.MagicMock()

    def test_successful_execution(self):
        """Test prompting, looking up and copying of password as well as
        cleaning up of the system clipboard.
        """
        main.main(["Example", "-d", DATABASE_FILEPATH])

        for call, expected in zip(
                pyperclip.copy.call_args_list, ["Password", ""]):
            self.assertEqual(call[0][0], expected)

    def test_missing_kdbx_file(self):
        self.assertRaises(
            SystemExit, main.main, ["Entry", "-d", "/tmp/random.kdbx"])

    def test_invalid_entry(self):
        self.assertRaises(
            SystemExit, main.main, ["Entry", "-d", DATABASE_FILEPATH])


if __name__ == "__main__":
    unittest.main()
