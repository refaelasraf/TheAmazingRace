from __future__ import annotations

import asyncio
from typing import TypeVar
from . import UNDONE_STEP_CHAR
from . import DONE_STEP_CHAR
self_type = TypeVar('T', bound='Runner')


class Runner:

    def __init__(self, name, step_per_sec, start_point, do_after_step=None):
        self.name = name
        self.step_per_sec = step_per_sec
        self.start_point = start_point
        self.do_after_step = do_after_step
        self.step = 0

    async def run(self, remaining_distance: int, step_callback, finish_callback) -> self_type:
        if remaining_distance == 0:
            finish_callback(self)
            return self

        await asyncio.sleep(1 / self.step_per_sec)
        self.step += 1
        step_callback()
        if self.do_after_step:
            await self.do_after_step(self)
        await self.run(remaining_distance - 1, step_callback, finish_callback)

    def show_runner_stats(self, race_length: int):
        done_steps = self.step + self.start_point
        step_to_do = race_length - done_steps
        runner_race_string = ""
        for step in range(done_steps):
            runner_race_string += DONE_STEP_CHAR

        runner_race_string += self.name

        for step in range(step_to_do):
            runner_race_string += UNDONE_STEP_CHAR

        print(runner_race_string)
