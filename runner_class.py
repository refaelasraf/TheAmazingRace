class Runner:
    def __init__(self, name, step_per_sec, start_point, do_after_step=None):
        self.name = name
        self.step_per_sec = step_per_sec
        self.start_point = start_point
        self.do_after_step = do_after_step
        self.step = 0
