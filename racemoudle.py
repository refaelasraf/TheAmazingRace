import asyncio
from asyncio import CancelledError

import runner


def start_race(runners: set, race_length: int):
    loop = asyncio.get_event_loop()
    for current_runner in runners:
        loop.create_task(__run(current_runner, race_length - current_runner.start_point, loop))
    pending = asyncio.Task.all_tasks()
    try:
        loop.run_until_complete(asyncio.gather(*pending))
    except CancelledError:
        loop.close()
    loop.close()


async def __run(r: runner.Runner, remaining_distance: int, loop: asyncio.AbstractEventLoop):
    if remaining_distance <= 0:
        print("the winner is " + r.name)
        __stop_all_runners()
    await asyncio.sleep(1)
    await __run(r, remaining_distance - r.step_per_sec, loop)


def __stop_all_runners():
    for task in asyncio.Task.all_tasks():
        task.cancel()
