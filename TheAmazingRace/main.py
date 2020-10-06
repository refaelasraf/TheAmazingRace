from TheAmazingRace import Runner, RunRace
import TheAmazingRace.Config.runners_config as runners_config


def main():
    runners = [Runner.Runner(runner_config["name"], runner_config["step_per_sec"], runner_config["start_point"],
                             runner_config["do_after_step"]) for runner_config in runners_config.runners]

    race = RunRace.RunRace(runners, 15)
    race.start_race()


if __name__ == "__main__":
    main()
