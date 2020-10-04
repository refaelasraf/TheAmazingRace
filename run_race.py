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
            loop.create_task(self.__run(current_runner, self.race_length - current_runner.start_point, loop))
        pending = asyncio.Task.all_tasks()
        results = loop.run_until_complete(asyncio.gather(*pending))
        print("the winner is {}".format(self.places.queue.popleft().name))
        loop.close()

    async def __run(self, runner: runner_class.Runner, remaining_distance: int, loop: asyncio.AbstractEventLoop):
        if remaining_distance == 0:
            self.places.queue.append(runner)
            return runner

        await asyncio.sleep(1 / runner.step_per_sec)
        runner.step += 1
        self.__print_current_stat()
        if runner.do_after_step is not None:
            await runner.do_after_step(runner)
        await self.__run(runner, remaining_distance - 1, loop)

    def __print_current_stat(self):
        os.system("cls")
        for runner in self.runners:
            self.__print_runner(runner)

    def __print_runner(self, runner: runner_class.Runner):
        done_steps = runner.step + runner.start_point
        step_to_do = self.race_length - done_steps
        output = ""
        for i in range(done_steps):
            output += "  X  "

        output += runner.name

        for i in range(step_to_do):
            output += "  -  "

        print(output)
