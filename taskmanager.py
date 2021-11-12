import datetime
import threading


CHECK_DELTA = datetime.timedelta(minutes=2)


class Task:
    def __init__(
            self,
            user, time, func,
            repetitive=False,
            check_delta=CHECK_DELTA,
            name='NoName'
    ):
        self.user = user
        self.time = time
        self.func = func
        self.repetitive = repetitive
        self.name = name

        self.check_delta = check_delta

    def __bool__(self):
        delta = datetime.datetime.now() - self.time
        if self.repetitive:
            delta = delta - datetime.timedelta(days=delta.days)
        return delta < self.check_delta


class TaskManager:
    def __init__(self, *tasks):
        self.tasks = list(tasks)

    def run(self):
        for task in self.tasks:
            task.func() if task else None

    def add(self, task):
        self.tasks.append(task)


class TaskManagerThread(threading.Thread):
    def __init__(self, tm):
        super().__init__(group=None)
        self.tm = tm

    def run(self):
        while True:
            tm.run()
