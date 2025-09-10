from tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.c = TennisPlayer("Tom", 25, 100)
        self.other = TennisPlayer("Nole", 35, 500)

    def test_init(self):
        self.assertEqual('Tom', self.c.name)
        self.assertEqual(25, self.c.age)
        self.assertEqual(100, self.c.points)
        self.assertEqual([], self.c.wins)

    def test_init_props_a(self):
        with self.assertRaises(Exception) as ex:
            self.c.name = 'Hi'
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_init_props_b(self):
        with self.assertRaises(Exception) as ex:
            self.c.age = 15
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_c(self):
        self.assertEqual(0, len(self.c.wins))
        tournament_name = "ATP"
        self.c.add_new_win(tournament_name)
        self.assertEqual(f"{tournament_name} has been already added to the list of wins!",
                         self.c.add_new_win(tournament_name))
        self.assertEqual(1, len(self.c.wins))
        self.assertEqual("ATP", self.c.wins[0])

    def test_d(self):
        self.assertEqual(f'{self.other.name} is a top seeded player and he/she is better than {self.c.name}',
                         self.c.__lt__(self.other))

    def test_e(self):
        self.other.points = 20
        self.assertEqual(f'{self.c.name} is a better player than {self.other.name}',
                         self.c.__lt__(self.other))

    def test_string(self):
        self.c.wins = ['ATP', "RG"]
        result = f"Tennis Player: Tom\n" \
               f"Age: 25\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: ATP, RG"
        self.assertEqual(result, str(self.c))


if __name__ == '__main__':
    main()
