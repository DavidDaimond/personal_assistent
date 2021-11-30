import datetime
import threading


CHECK_DELTA = datetime.timedelta(minutes=2)
DEFAULT_REPEAT_TIME = datetime.timedelta(minutes=60 * 24 * 365)


class Task:
    def __init__(
            self,
            time, func,
            repetitive=False,
            check_delta=CHECK_DELTA,
            name='NoName',
            repeat_time=DEFAULT_REPEAT_TIME
    ):

        self.time = time
        self.func = func
        self.repetitive = repetitive
        self.repeat_time = repeat_time if repetitive else None
        self.name = name

        self.check_delta = check_delta

        self.active = True

    def __bool__(self):
        delta = abs(datetime.datetime.now() - self.time)
        if self.repetitive:
            delta = delta - self.repeat_time
        return delta < self.check_delta

    def do(self):
        if self and self.active:
            if not self.repetitive:
                self.active = False
            self.func()


class TelegramTask(Task):
    def __init__(
            self,
            time, func,
            user,
            **kwargs
    ):
        super(TelegramTask, self).__init__(time, func, **kwargs)
        self.user = user



class TaskManager:
    def __init__(self, *tasks):
        self.tasks = list(tasks)

    def run(self):
        for task in self.tasks:
            task.do()

    def add(self, task):
        self.tasks.append(task)


class TaskManagerThread(threading.Thread):
    def __init__(self, tm, name=None):
        super().__init__(group=None, name=name)
        self.tm = tm

    def run(self):
        while True:
            self.tm.run()
