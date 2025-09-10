from restaurant import Restaurant
from unittest import TestCase, main


class TestRestaurant(TestCase):

    def setUp(self):
        self.c = Restaurant('Rest', 5)

    def test_init(self):
        self.assertEqual('Rest', self.c.name)
        self.assertEqual(5, self.c.capacity)
        self.assertEqual([], self.c.waiters)

    def test_init_props_a(self):
        with self.assertRaises(Exception) as ex:
            self.c.name = ' '
        self.assertEqual("Invalid name!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.c.name = ''
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_init_props_b(self):
        with self.assertRaises(Exception) as ex:
            self.c.capacity = -4
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_get_waiters(self):
        self.c.waiters = ['w1', 'w2', 'w3', 'w4']

        self.assertEqual(['w1', 'w2', 'w3', 'w4'], self.c.waiters)
        self.assertEqual(['w1', 'w2', 'w3', 'w4'], self.c.get_waiters())

    def test_get_waiters1(self):
        self.c.waiters = []

        self.assertEqual([], self.c.waiters)
        self.assertEqual([], self.c.get_waiters())

    def test_get_waiters2(self):
        self.c.waiters = [{'name': 'A', 'total_earnings': 3},
                          {'name': 'B', 'total_earnings': 1},
                          {'name': 'C', 'total_earnings': 8}]

        self.assertEqual([{'name': 'A', 'total_earnings': 3}, {'name': 'C', 'total_earnings': 8}], self.c.get_waiters(min_earnings=2))
        self.assertEqual([{'name': 'A', 'total_earnings': 3}, {'name': 'B', 'total_earnings': 1}], self.c.get_waiters(max_earnings=5))

    def test_add_waiters(self):
        self.c.waiters = {'w1': 'A', 'w2': 'B', 'w3': 'C', 'w4': 'D', 'w5': 'E'}
        self.assertEqual("No more places!", self.c.add_waiter('F'))

    def test_add_waiters_a(self):
        waiter_name = 'A'
        w1 = {'name': 'A'}
        self.c.waiters = [w1, 'w2', 'w3']
        self.assertEqual("The waiter A already exists!", self.c.add_waiter(waiter_name))

    def test_add_waiters_new(self):
        waiter_name = 'D'
        new_waiter = {'name': 'D'}
        self.c.waiters = []
        self.assertEqual("The waiter D has been added.", self.c.add_waiter(waiter_name))

    def test_add_waiters_r(self):
        w1 = {'name': 'D'}
        self.c.waiters = [w1]
        waiter_name = 'D'
        self.assertEqual("The waiter D has been removed.", self.c.remove_waiter(waiter_name))

    def test_add_waiters_r1(self):
        w1 = {'name': 'D'}
        self.c.waiters = [w1]
        waiter_name = 'A'
        self.assertEqual("No waiter found with the name A.", self.c.remove_waiter(waiter_name))

    def test_total(self):
        w1 = {'name': 'D'}
        self.c.waiters = [w1]
        self.assertEqual(0, self.c.get_total_earnings())


if __name__ == '__main__':
    main()
