import unittest
from unittest import mock
import getpass
import time

import pyperclip
import pykeepass

import main


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
        main.copy_entry("Example")

        for call, expected in zip(
                pyperclip.copy.call_args_list, ["Password", ""]):
            self.assertEqual(call[0][0], expected)

    def test_missing_kdbx_file(self):
        with mock.patch("pykeepass.PyKeePass", side_effect=FileNotFoundError):
            self.assertRaises(SystemExit, main.copy_entry, "Entry")


if __name__ == "__main__":
    unittest.main()
