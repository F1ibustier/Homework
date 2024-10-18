# Методы Юнит-тестирования
# coded by f1ibustier
import unittest
from pprint import pprint


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            all_result = {}
            for key, value in result.items():
                all_result[key] = value.name
            print(all_result)

    def test_run_1(self):
        self.run_1 = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = self.run_1.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.run_2 = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = self.run_2.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.run_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = self.run_3.start()
        last_runner = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
