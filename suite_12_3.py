# Систематизация и пропуск тестов
# coded by f1ibustier
import unittest
import tests_12_3

test_suite_12_3 = unittest.TestSuite()
test_suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
test_suite_12_3.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(test_suite_12_3)
