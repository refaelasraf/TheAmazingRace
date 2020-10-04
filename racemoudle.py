import asyncio

import runner


def start_race(first: runner.Runner, second: runner.Runner):
    loop = asyncio.get_event_loop()
    loop.create_task(__run(first, 20, loop))
    loop.create_task(__run(second, 20, loop))
    loop.run_forever()
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
