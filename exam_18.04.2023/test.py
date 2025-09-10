from robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.c = Robot('1010', 'Humanoids', 150, 100)
        self.other = Robot("99", 'Education', 50, 30)

    def test_init(self):
        self.assertEqual('1010', self.c.robot_id)
        self.assertEqual('Humanoids', self.c.category)
        self.assertEqual(150, self.c.available_capacity)
        self.assertEqual(100, self.c.price)
        self.assertEqual([], self.c.hardware_upgrades)
        self.assertEqual([], self.c.software_updates)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'],
                         self.c.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, self.c.PRICE_INCREMENT)

    def test_init_props_a(self):
        with self.assertRaises(Exception) as ex:
            self.c.category = 'Human'
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ex.exception))

    def test_init_props_b(self):
        with self.assertRaises(Exception) as ex:
            self.c.price = -150
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_upgrade(self):
        self.assertEqual([], self.c.hardware_upgrades)
        self.assertEqual(100, self.c.price)
        self.c.hardware_upgrades = ['mouse', "DVD"]
        hardware_component = "DVD"
        component_price = 10
        self.assertEqual(['mouse', "DVD"], self.c.hardware_upgrades)
        self.assertEqual("Robot 1010 was not upgraded.", self.c.upgrade(hardware_component, component_price))
        hardware_component = "cd"
        self.assertEqual('Robot 1010 was upgraded with cd.', self.c.upgrade(hardware_component, component_price))
        self.c.upgrade(hardware_component, component_price)
        self.assertEqual(['mouse', "DVD", "cd"], self.c.hardware_upgrades)
        self.assertEqual(115, self.c.price)

    def test_update(self):
        self.assertEqual([], self.c.software_updates)
        version = 1.236
        needed_capacity = 3
        self.c.available_capacity = 2
        self.assertEqual("Robot 1010 was not updated.", self.c.update(version, needed_capacity))

        needed_capacity = 1
        self.c.software_updates = [1.0, 1.1, 1.236]
        self.assertEqual("Robot 1010 was not updated.", self.c.update(version, needed_capacity))

        needed_capacity = 1
        self.c.software_updates = [1.0, 1.1, 1.15]
        self.assertEqual(f'Robot 1010 was updated to version 1.236.', self.c.update(version, needed_capacity))
        self.assertEqual([1.0, 1.1, 1.15, 1.236], self.c.software_updates)
        self.assertEqual(1, self.c.available_capacity)

    def test_gt(self):
        self.assertEqual('Robot with ID 1010 is more expensive than Robot with ID 99.', self.c.__gt__(self.other))
        self.other.price = 100
        self.assertEqual('Robot with ID 1010 costs equal to Robot with ID 99.',  self.c.__gt__(self.other))
        self.other.price = 300
        self.assertEqual('Robot with ID 1010 is cheaper than Robot with ID 99.',  self.c.__gt__(self.other))


if __name__ == '__main__':
    main()
