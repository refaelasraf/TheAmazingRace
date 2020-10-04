import runner
import racemoudle

first = runner.Runner("bunny", 3, 0)
second = runner.Runner("turtle", 2, 6)

racemoudle.start_race({first, second}, 16)
