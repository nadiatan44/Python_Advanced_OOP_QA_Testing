from climbing_robot import ClimbingRobot
from unittest import TestCase, main


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.c = ClimbingRobot("Mountain", 'part_a', 20, 40)
        self.sw = {'name': 'A', 'capacity_consumption': 3, 'memory_consumption': 3}

    def test_init(self):
        self.assertEqual('Mountain', self.c.category)
        self.assertEqual('part_a', self.c.part_type)
        self.assertEqual(20, self.c.capacity)
        self.assertEqual(40, self.c.memory)
        self.assertEqual(['Mountain', 'Alpine', 'Indoor', 'Bouldering'], self.c.ALLOWED_CATEGORIES)
        self.assertEqual(self.c.installed_software, [])

    def test_init_props_a(self):
        all_cat = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        with self.assertRaises(Exception) as ex:
            self.c.category = 'bbb'
        self.assertEqual(f"Category should be one of {all_cat}", str(ex.exception))
        self.assertEqual(self.c.category, 'Alpine')

    def test_a(self):
        self.c.installed_software = [self.sw]
        self.assertEqual(3, self.c.get_used_capacity())
        sw2 = {'name': 'Software1', 'capacity_consumption': 1, 'memory_consumption': 1}
        self.c.installed_software = [self.sw, sw2]
        self.assertEqual(4, self.c.get_used_capacity())


    def test_b(self):
        self.c.installed_software = [self.sw]
        self.assertEqual(17, self.c.get_available_capacity())

    def test_c(self):
        self.c.installed_software = [self.sw]
        self.assertEqual(3, self.c.get_used_memory())

    def test_d(self):
        self.c.installed_software = [self.sw]
        self.assertEqual(37, self.c.get_available_memory())

    def test_install(self):
        software = self.sw
        self.assertEqual("Software 'A' successfully installed on Mountain part.", self.c.install_software(software))

    def test_install_a(self):
        software = self.sw
        software['capacity_consumption'] = 100
        self.assertEqual("Software 'A' cannot be installed on Mountain part.", self.c.install_software(software))

    def test_install_b(self):
        software = self.sw
        software['memory_consumption'] = 100
        self.assertEqual("Software 'A' cannot be installed on Mountain part.", self.c.install_software(software))


if __name__ == '__main__':
    main()
