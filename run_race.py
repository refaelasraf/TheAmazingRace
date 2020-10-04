import asyncio
import queue
import runner_class
import os


class RunRace:
    def __init__(self, runners: set, race_length: int):
        self.runners = runners
        self.race_length = race_length
        self.places = queue.Queue(len(runners))

    def start_race(self):
        loop = asyncio.get_event_loop()
        for current_runner in self.runners:
            loop.create_task(
                current_runner.run(self.race_length - current_runner.start_point, self.__print_current_stat,
                                     self.__register_place_of_runner))
        pending = asyncio.Task.all_tasks()
        results = loop.run_until_complete(asyncio.gather(*pending))
        print("the winner is {}".format(self.places.queue.popleft().name))
        loop.close()

    def __print_current_stat(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        for runner in self.runners:
            runner.print(self.race_length)

    def __register_place_of_runner(self, runner: runner_class.Runner):
        self.places.queue.append(runner)
