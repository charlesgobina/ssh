from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple",spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_valid_integer_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_integer_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1.5")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple",spreadsheet.evaluate("A1"))

    def test_evaluate_valid_another_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Pneumonoultramicroscopicsilicovolcanioconosis'")
        self.assertEqual('Pneumonoultramicroscopicsilicovolcanioconosis',spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_another_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=Apple")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_valid_reference_to_a_cell(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "1")
        self.assertEqual(1,spreadsheet.evaluate("A1"))

    def test_evaluate_non_valid_reference_to_a_cell(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "1.5")
        self.assertEqual('#Error',spreadsheet.evaluate("A1"))

    def test_evaluate_circular_reference_to_a_cell(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular",spreadsheet.evaluate("A1"))

    def test_evaluate_addition_operation(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1+3")
        self.assertEqual(4,spreadsheet.evaluate("A1"))

    def test_evaluate_multiplication_operation(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1*3")
        self.assertEqual(3,spreadsheet.evaluate("A1"))



