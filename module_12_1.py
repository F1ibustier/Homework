# Простые Юнит-Тесты
# coded by f1ibustier
import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = Runner('Черепаха')
        for walk in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)


    def test_run(self):
        runner2 = Runner('Заяц')
        for run in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)


    def test_challenge(self):
        runner3 = Runner('Лев')
        for run in range(10):
            runner3.run()
        runner4 = Runner('Антилопа')
        for walk in range(10):
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)


if __name__ == '__main__':
    unittest.main()
