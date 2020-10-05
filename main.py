import Runner
import RunRace
import Config.runners_config as runners_config


def main():
    runners = []
    for runner_config in runners_config.runners:
        name = runner_config.get("name")
        step_per_sec = runner_config.get("step_per_sec")
        start_point = runner_config.get("start_point")
        do_after_step = runner_config.get("do_after_step")
        runners.append(Runner.Runner(name, step_per_sec, start_point, do_after_step))

    race = RunRace.RunRace(runners, 15)
    race.start_race()


if __name__ == "__main__":
    main()
