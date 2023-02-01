import unittest

from necessary.core import necessary


class TestParsing(unittest.TestCase):
    def test_parse(self):
        self.assertTrue(necessary("pytest>=3.0.0", soft=True))
        self.assertTrue(necessary("pytest>=3.0.0,>4.5", soft=True))
        self.assertFalse(necessary("pytest<=3.0.0", soft=True))
        self.assertFalse(necessary("pytest<3.0.0,>2", soft=True))

        with self.assertRaises(ImportError):
            necessary(("pytest", "3000"))
