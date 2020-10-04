import runner
import asyncio
import time


def start_race(first: runner.Runner, second: runner.Runner):
    loop = asyncio.get_event_loop()
    loop.create_task(__run(first, 20, loop))
    loop.create_task(__run(second, 20, loop))
    loop.run_forever()
    loop.close()


async def __run(r: runner.Runner, race_length: int, loop: asyncio.AbstractEventLoop, counter: int = 0):
    if race_length <= 0:
        print("the winner is " + r.name + "   time : " + str(counter))
        loop.stop()
    await asyncio.sleep(1)
    await __run(r, race_length - r.step_per_sec, loop, counter + 1)
