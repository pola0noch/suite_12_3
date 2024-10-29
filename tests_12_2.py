from unittest import TestCase
from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest


class TournamentTest(TestCase):
    is_frozen = True

    def setUp(self):
        self.Usain = Runner("Усэйн", 10)
        self.Andrew = Runner("Андрей", 9)
        self.Nik = Runner("Ник", 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_nik_is_loser1(self):
        tournament = Tournament(90, self.Usain, self.Nik)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.all_results["test_1"] = results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_nik_is_loser2(self):
        tournament = Tournament(90, self.Andrew, self.Nik)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.all_results["test_2"] = results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_nik_is_loser3(self):
        tournament = Tournament(90, self.Usain, self.Andrew, self.Nik)
        results = tournament.start()
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.all_results["test_3"] = results

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_logic_start(self):
        tournament = Tournament(1, self.Usain, self.Andrew, self.Nik)
        results = tournament.start()
        self.assertLess(self.Andrew.speed, self.Usain.speed)
        self.assertGreater(self.Andrew.speed, self.Nik.speed)
        self.assertTrue(results[max(results.keys())] == 'Ник')
        self.all_results["test_4"] = results


if __name__ == '__main__':
    unittest.main()
