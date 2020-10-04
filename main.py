import runner
import racemoudle

first = runner.Runner("bunny", 3)
second = runner.Runner("turtle", 1)

racemoudle.start_race(first, second, 20)
