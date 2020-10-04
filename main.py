import runner_class
import run_race
import asyncio

first = runner_class.Runner("rabbit", 3, 0)
second = runner_class.Runner("turtle", 4, 0, lambda r: asyncio.sleep(1) if r.step % 3 == 0 else asyncio.sleep(0))
third = runner_class.Runner("snail", 1, 10)

race = run_race.RunRace({first, second, third}, 15)
race.start_race()
