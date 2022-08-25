import unittest

from necessary.core import necessary


class NecessaryWithTest(unittest.TestCase):
    def test_with_necessary(self) -> None:
        with necessary("black") as import_successful:
            self.assertTrue(True)
            self.assertTrue(import_successful)

        with self.assertRaises(ImportError):
            with necessary("blackz"):
                pass

        with necessary("blackz", soft=True) as import_unsuccessful:
            self.assertFalse(import_unsuccessful)
