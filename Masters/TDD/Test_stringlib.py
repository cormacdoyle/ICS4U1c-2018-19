import unittest
import stringlib


class Test_stringlib(unittest.TestCase):

    def test_strLength_general1(self):
        self.assertEqual(4, stringlib.strLength("yeet"))

    def test_strLength_general2(self):
        self.assertEqual(8, stringlib.strLength("bingbing"))

    def test_strLength_corner_emptystring(self):
        self.assertEqual(0, stringlib.strLength(""))

    def test_strLength_corner_emptystring(self):
        self.assertEqual(0, stringlib.strLength(5))
