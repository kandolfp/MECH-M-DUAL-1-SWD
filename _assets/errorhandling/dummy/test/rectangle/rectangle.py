import unittest
from src.rectangle import Rectangle


class TestGetAreaRectangle(unittest.TestCase):
    def test_area_correct(self):
        rectangle = Rectangle(2, 3)
        self.assertEqual(rectangle.get_area(), 6, "incorrect area")

    def test_area_incorrect(self):
        rectangle = Rectangle(2, 3)
        self.assertNotEqual(rectangle.get_area(), 5, "correct area")

    def test_set_width(self):
        rectangle = Rectangle(1, 1)
        rectangle.set_width(0.7)
        self.assertEqual(rectangle.get_area(), 0.7, "set_width not working")

    def test_set_height(self):
        rectangle = Rectangle(1, 1)
        rectangle.set_width(0.7)
        self.assertEqual(rectangle.get_area(), 0.7, "set_width not working")
    
    def test_deliberate_error(self):
        rectangle = Rectangle(1, 1)
        self.assertEqual(rectangle.get_area(), 2, "deliberate error")
