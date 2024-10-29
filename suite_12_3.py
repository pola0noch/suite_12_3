# Домашнее задание по теме "Систематизация и пропуск тестов".

import unittest
import tests_12_1
import tests_12_2


rt_ST = unittest.TestSuite()
rt_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
rt_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(rt_ST)