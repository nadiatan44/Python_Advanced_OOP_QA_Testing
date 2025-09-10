from furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self):
        self.c = Furniture("aaa", 5.55, (3, 5, 7), True)

    def test_init(self):
        self.assertEqual("aaa", self.c.model)
        self.assertEqual(5.55, self.c.price)
        self.assertEqual((3, 5, 7), self.c.dimensions)
        self.assertEqual(True, self.c.in_stock)
        self.assertEqual(None, self.c.weight)

    def test_init_props_m(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = " "
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.",
                         str(ex.exception))

    def test_init_props_m1(self):
        with self.assertRaises(Exception) as ex:
            self.c.model = "jhgfghjnhbgbgbvgfchnjmkmjhgfvbnhnhnhbgvfcdxsdfjknjhvghfuryfuvlunbm"
        self.assertEqual("Model must be a non-empty string with a maximum length of 50 characters.",
                         str(ex.exception))

    def test_init_props_p(self):
        with self.assertRaises(Exception) as ex:
            self.c.price = -5
        self.assertEqual("Price must be a non-negative number.", str(ex.exception))

    def test_init_props_d(self):
        with self.assertRaises(Exception) as ex:
            self.c.dimensions = (3, 5)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

    def test_init_props_d1(self):
        with self.assertRaises(Exception) as ex:
            self.c.dimensions = (3, 5, 3, 7)
        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ex.exception))

    def test_init_props_d2(self):
        with self.assertRaises(Exception) as ex:
            self.c.dimensions = (3, 5, 0)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_init_props_d3(self):
        with self.assertRaises(Exception) as ex:
            self.c.dimensions = (3, 0, 5)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_init_props_d4(self):
        with self.assertRaises(Exception) as ex:
            self.c.dimensions = (0, 5, 8)
        self.assertEqual("Dimensions tuple must contain integers greater than zero.", str(ex.exception))

    def test_init_props_w1(self):
        with self.assertRaises(Exception) as ex:
            self.c.weight = -4
        self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_init_props_w2(self):
        with self.assertRaises(Exception) as ex:
            self.c.weight = "lkj"
            self.assertEqual("Weight must be greater than zero.", str(ex.exception))

    def test_aaa(self):
        result = "Model: aaa is currently in stock."
        self.assertEqual(result, self.c.get_available_status())

    def test_aaa1(self):
        self.c.in_stock = False
        result = "Model: aaa is currently unavailable."
        self.assertEqual(result, self.c.get_available_status())

    def test_get(self):
        height, width, depth = (3, 5, 7)
        self.c.weight = 1
        result = "Model: aaa has the following dimensions: 3mm x 5mm x 7mm and weighs: 1"
        self.assertEqual(result, self.c.get_specifications())

    def test_get1(self):
        height, width, depth = (3, 5, 7)
        result = "Model: aaa has the following dimensions: 3mm x 5mm x 7mm and weighs: N/A"
        self.assertEqual(result, self.c.get_specifications())



if __name__ == '__main__':
    main()
