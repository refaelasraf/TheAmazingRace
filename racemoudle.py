import asyncio
from asyncio import CancelledError

import runner


def start_race(first: runner.Runner, second: runner.Runner, race_length: int):
    loop = asyncio.get_event_loop()
    loop.create_task(__run(first, race_length, loop))
    loop.create_task(__run(second, race_length, loop))
    pending = asyncio.Task.all_tasks()
    try:
        loop.run_until_complete(asyncio.gather(*pending))
    except CancelledError:
        loop.close()
    loop.close()


async def __run(r: runner.Runner, race_length: int, loop: asyncio.AbstractEventLoop):
    if race_length <= 0:
        print("the winner is " + r.name)
        __stop_all_runners()
    await asyncio.sleep(1)
    await __run(r, race_length - r.step_per_sec, loop)


def __stop_all_runners():
    for task in asyncio.Task.all_tasks():
        task.cancel()
