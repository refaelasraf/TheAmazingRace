import runner_module
import racemoudle
import asyncio

first = runner_module.Runner("rabbit", 3, 0)
second = runner_module.Runner("turtle", 4, 0, lambda x: asyncio.sleep(1) if x % 3 == 0 else asyncio.sleep(0));
third = runner_module.Runner("snail", 1, 10)

racemoudle.start_race({first, second, third}, 15)
