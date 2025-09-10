from second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):
    def setUp(self):
        self.c = SecondHandCar("BMW", "combi", 10000, 5000)
        self.other = SecondHandCar("BMW", "combi", 15000, 4000)

    def test_init_model(self):
        self.assertEqual('BMW', self.c.model)

    def test_init_car_type(self):
        self.assertEqual('combi', self.c.car_type)

    def test_init_mileage(self):
        self.assertEqual(10000, self.c.mileage)

    def test_init_prise(self):
        self.assertEqual(5000, self.c.price)

    def test_init_prise_lower_as_one(self):
        with self.assertRaises(Exception) as ex:
            self.c.price = -5
        self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

    def test_init_mileage_under_100(self):
        with self.assertRaises(Exception) as ex:
            self.c.mileage = 5
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ex.exception))

    def test_set_promotional_price_new_higher_than_old_price(self):
        new_price = self.c.price + 100
        with self.assertRaises(Exception) as ex:
            self.c.set_promotional_price(new_price)
        self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

    def test_set_promotional_price_new_lower_than_old_price(self):
        new_price = self.c.price - 1
        self.assertEqual('The promotional price has been successfully set.',
                         self.c.set_promotional_price(new_price))

    # def test_need_repair_repair_price_higher_than_half_price(self):
    def test_need(self):
        repair_price = self.c.price / 2 + 100
        self.assertEqual('Repair is impossible!', self.c.need_repair(repair_price, "asd"))

    # def test_need_repair_repair(self):
    def test(self):
        repair_price = 1
        self.assertEqual(f'Price has been increased due to repair charges.',
                         self.c.need_repair(repair_price, "asd"))
        self.assertEqual(1, len(self.c.repairs))

    # def test_gt_cannot_compare(self):
    def test_g(self):
        self.other.car_type = 'asd'
        self.assertEqual('Cars cannot be compared. Type mismatch!', self.c.__gt__(self.other))

    # def test_gt_compare(self):
    def test_gt(self):
        self.assertEqual(True, self.c.__gt__(self.other))

    def test_str(self):
        self.assertEqual(str(self.c), """Model BMW | Type combi | Milage 10000km
Current price: 5000.00 | Number of Repairs: 0""")

        # self.assertEqual(str(self.c), """Model test model | Type test type | Milage 101km
        # Current price: 2.00 | Number of Repairs: 0""")


if __name__ == '__main__':
    main()

