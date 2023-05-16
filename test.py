from whiteboard import solution
from unittest import TestCase, main


class TestWhiteboard(TestCase):

    def test_1(self):
        self.assertEqual(solution("helloWorld"), "hello World")

    def test_2(self):
        self.assertEqual(solution("identifier"), "identifier")

    def test_3(self):
        self.assertEqual(solution("camelCasing"), "camel Casing")

    def test_4(self):
        self.assertEqual(solution("uncamelThisCamel"),
                         "uncamel This Camel")

    def test_5(self):
        self.assertEqual(solution(""), "")


if __name__ == "__main__":
    main()