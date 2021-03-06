import asyncio
from asyncio import CancelledError

import runner_module


def start_race(runners: set, race_length: int):
    loop = asyncio.get_event_loop()
    for current_runner in runners:
        loop.create_task(__take_a_step(current_runner, race_length - current_runner.start_point, loop))
    pending = asyncio.Task.all_tasks()
    try:
        loop.run_until_complete(asyncio.gather(*pending))
    except CancelledError:
        loop.close()
    loop.close()


async def __take_a_step(runner: runner_module.Runner, remaining_distance: int, loop: asyncio.AbstractEventLoop,
                        step_number: int = 0):
    if remaining_distance <= 0:
        print("the winner is " + runner.name)
        await __stop_all_runners()

    await asyncio.sleep(1 / runner.step_per_sec)
    runner.step += 1
    if step_number > 0 and runner.do_after_step != None:
        await runner.do_after_step(step_number)
    await __take_a_step(runner, remaining_distance - 1, loop, step_number + 1)


async def __stop_all_runners():
    await asyncio.sleep(0)
    for task in asyncio.Task.all_tasks():
        task.cancel()
