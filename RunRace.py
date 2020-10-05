import asyncio
from typing import List
import os
import Config.config as config

import Runner


class RunRace:
    WIN_MESSAGE_FORMAT = config.run_race_constant.get("win_message_format")

    def __init__(self, runners: List[Runner.Runner], race_length: int):
        self.runners = runners
        self.race_length = race_length
        self.places = []

    def start_race(self):
        loop = asyncio.get_event_loop()
        for current_runner in self.runners:
            loop.create_task(
                current_runner.run(self.race_length - current_runner.start_point, self.__print_current_stat,
                                   self.__register_place_of_runner))
        pending = asyncio.Task.all_tasks()
        loop.run_until_complete(asyncio.gather(*pending))
        print(self.WIN_MESSAGE_FORMAT.format(self.places.pop(0).name))
        loop.close()

    def __print_current_stat(self):
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        for runner in self.runners:
            runner.show_runner_stats(self.race_length)

    def __register_place_of_runner(self, runner: Runner.Runner):
        self.places.append(runner)
