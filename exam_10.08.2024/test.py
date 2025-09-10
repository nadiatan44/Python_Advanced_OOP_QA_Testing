from soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.c = SoccerPlayer("AAAAAA", 20, 35, 'Barcelona')
        self.other = SoccerPlayer("BBBBBB", 30, 50, 'Real Madrid')

    # test __init__
    def test_init(self):
        self.assertEqual('AAAAAA', self.c.name)
        self.assertEqual(20, self.c.age)
        self.assertEqual(35, self.c.goals)
        self.assertEqual('Barcelona', self.c.team)
        self.assertEqual(["Barcelona", "Real Madrid", "Manchester United", "Juventus", "PSG"], self.c._VALID_TEAMS)
        self.assertEqual({}, self.c.achievements)

    def test_init_props_a(self):
        with self.assertRaises(Exception) as ex:
            self.c.name = 'AAA'
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_init_props_b(self):
        with self.assertRaises(Exception) as ex:
            self.c.age = 13
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_init_props_c(self):
        self.c.goals = -13
        self.assertEqual(0, self.c.goals)

    def test_init_props_d(self):
        with self.assertRaises(Exception) as ex:
            self.c.team = "NNN"
        self.assertEqual(f"Team must be one of the following: {', '.join(SoccerPlayer._VALID_TEAMS)}!", str(ex.exception))

    def test_change(self):
        new_team = "OOO"
        self.assertEqual("Invalid team name!", self.c.change_team(new_team))

    def test_change_a(self):
        new_team = "Manchester United"
        self.assertEqual("Team successfully changed!", self.c.change_team(new_team))

    def test_add_new_achievement(self):
        self.c.achievements = {'aaa': 3}
        achievement_name = 'bbb'
        self.assertEqual({'aaa': 3}, self.c.achievements)
        self.assertEqual("bbb has been successfully added to the achievements collection!", self.c.add_new_achievement(achievement_name))
        self.assertEqual({'aaa': 3, 'bbb': 1}, self.c.achievements)

    def test_add_new_achievement_a(self):
        self.c.achievements = {}
        achievement_name = 'bbb'
        self.c.add_new_achievement(achievement_name)
        self.assertEqual(1, self.c.achievements[achievement_name])

    def test_add_new_achievement_b(self):
        self.c.achievements = {'bbb': 2}
        achievement_name = 'bbb'
        self.c.add_new_achievement(achievement_name)
        self.assertEqual(3, self.c.achievements[achievement_name])

    def test_other(self):
        self.assertEqual("BBBBBB is a top goal scorer! S/he scored more than AAAAAA.", self.c.__lt__(self.other))

    def test_other_a(self):
        self.c.goals = 1000
        self.assertEqual("AAAAAA is a better goal scorer than BBBBBB.", self.c.__lt__(self.other))


if __name__ == '__main__':
    main()
