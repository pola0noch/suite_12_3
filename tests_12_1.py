import unittest
from unittest import TestCase
from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_w = Runner("Test walk")
        for i in range(10):
            test_w.walk()
        self.assertEqual(test_w.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_r = Runner("Test run")
        for i in range(10):
            test_r.run()
        self.assertEqual(test_r.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_1 = Runner("runner1")
        test_2 = Runner("runner2")
        for i in range(10):
            test_1.walk()
            test_2.run()
        self.assertNotEqual(test_1.distance, test_2.distance)

if __name__ == '__main__':
    unittest.main()





