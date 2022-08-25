import unittest

from necessary.core import necessary


class NecessaryTest(unittest.TestCase):
    def test_import_success(self) -> None:
        if necessary("black"):
            self.assertTrue(True)

        if necessary(("black", "22.6.0")):
            self.assertTrue(True)

        if necessary(["black", "mypy"]):
            self.assertTrue(True)

        if necessary([("black", "22.6.0"), "mypy"]):
            self.assertTrue(True)

        if necessary([("black", "22.6.0"), ("mypy", "0.971")]):
            self.assertTrue(True)

    def test_import_failure(self) -> None:
        with self.assertRaises(ImportError):
            necessary("2222")

        self.assertFalse(necessary("2222", soft=True))

        with self.assertRaises(ImportError):
            necessary(("black", "303030303303"))

        self.assertFalse(necessary(("black", "303030303303"), soft=True))
