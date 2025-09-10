from cat import Cat

import unittest


class TestCat(unittest.TestCase):
    def setUp(self):
        self.c = Cat('Lady')

    def test_init(self):
        self.assertEqual("Lady", self.c.name)
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

    def test_eat_cat_already_fed_raise(self):
        self.c.fed = True
        self.assertTrue(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

        with self.assertRaises(Exception) as ex:
            self.c.eat()

        self.assertTrue(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)
        self.assertEqual('Already fed.', str(ex.exception))

    def test_eat(self):
        self.assertFalse(self.c.fed)
        self.assertFalse(self.c.sleepy)
        self.assertEqual(0, self.c.size)

        self.c.eat()

        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(1, self.c.size)

        self.c.fed = False
        self.c.eat()

        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(2, self.c.size)

    def test_cat_cannot_sleep_if_not_fed(self):
        self.c.sleepy = True
        self.assertFalse(self.c.fed)
        self.assertTrue(self.c.sleepy)

        with self.assertRaises(Exception) as ex:
            self.c.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
        self.assertFalse(self.c.fed)
        self.assertTrue(self.c.sleepy)

    def test_cat_sleeps(self):
        self.c.eat()
        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)

        self.c.sleep()

        self.assertTrue(self.c.fed)
        self.assertFalse(self.c.sleepy)


if __name__ == '__main__':
    unittest.main()
