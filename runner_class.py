import asyncio


class Runner:
    def __init__(self, name, step_per_sec, start_point, do_after_step=None):
        self.name = name
        self.step_per_sec = step_per_sec
        self.start_point = start_point
        self.do_after_step = do_after_step
        self.step = 0

    async def run(self, remaining_distance: int, step_callback, finish_callback):
        if remaining_distance == 0:
            finish_callback(self)
            return self

        await asyncio.sleep(1 / self.step_per_sec)
        self.step += 1
        step_callback()
        if self.do_after_step is not None:
            await self.do_after_step(self)
        await self.run(remaining_distance - 1, step_callback, finish_callback)

    def print(self, race_length: int):
        done_steps = self.step + self.start_point
        step_to_do = race_length - done_steps
        output = ""
        for i in range(done_steps):
            output += "  X  "

        output += self.name

        for i in range(step_to_do):
            output += "  -  "

        print(output)
