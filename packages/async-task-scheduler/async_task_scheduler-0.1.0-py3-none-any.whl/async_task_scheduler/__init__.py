import asyncio
from datetime import datetime
from typing import Awaitable, Callable, List, Any, Iterable, TypeAlias

__all__ = [
    "Task",
    "CronTask",
    "OnceTask",
    "OnceAtTask",
    "Scheduler",
]

DecoratedAsync: TypeAlias = Callable[[], Awaitable]


class Task:
    def __init__(
        self,
        func: Callable[[], Awaitable],
        args: Iterable[Any] = [],
        kwargs: dict[str, Any] = {},
        loop: asyncio.AbstractEventLoop | None = None,
    ):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.loop = loop

    async def run(self) -> None:
        coro = self.func(*self.args, **self.kwargs)
        assert asyncio.iscoroutine(coro), "Task function must be a coroutine"
        self.get_loop().create_task(coro)

    def needs_run(self) -> bool:
        return True

    def get_loop(self) -> asyncio.AbstractEventLoop:
        return self.loop or asyncio.get_event_loop()


class CronTask(Task):
    def __init__(
        self, *args, schedule: str | tuple[Callable[[int], bool], ...], **kwargs
    ):
        super().__init__(*args, **kwargs)
        if isinstance(schedule, tuple):
            self.minute, self.hour, self.day, self.month, self.weekday = schedule
        else:
            self.minute, self.hour, self.day, self.month, self.weekday = (
                self.parse_schedule(schedule)
            )

    def parse_schedule(self, schedule: str) -> tuple[Callable[[int], bool], ...]:
        minute, hour, day, month, weekday = schedule.split(" ")
        return (
            self.get_condition(minute),
            self.get_condition(hour),
            self.get_condition(day),
            self.get_condition(month),
            self.get_condition(weekday),
        )

    def get_condition(self, spec: str) -> Callable[[int], bool]:
        if spec == "*":
            return lambda x: True
        if "/" in spec:
            value, step = spec.split("/")
            value = 0 if value == "*" else int(value)
            step = int(step)
            return lambda x: x % step == value
        if "-" in spec:
            start, end = spec.split("-")
            start = int(start)
            end = int(end)
            return lambda x: start <= x <= end
        if "," in spec:
            values = map(int, spec.split(","))
            return lambda x: x in values
        return lambda x: x == int(spec)

    def needs_run(self) -> bool:
        now = datetime.now()
        minute, hour, day, month, weekday = map(
            int, now.strftime("%M %H %d %m %w").split()
        )
        return all(
            [
                self.minute(minute),
                self.hour(hour),
                self.day(day),
                self.month(month),
                self.weekday(weekday),
            ]
        )


class OnceTask(Task):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ran = False

    def needs_run(self) -> bool:
        if self.ran:
            return False
        return True

    async def run(self) -> None:
        self.ran = True
        await super().run()


class OnceAtTask(Task):
    def __init__(self, *args, at: datetime, **kwargs):
        super().__init__(*args, **kwargs)
        self.at = at
        self.ran = False

    def needs_run(self) -> bool:
        return datetime.now() >= self.at and not self.ran

    async def run(self) -> None:
        self.ran = True
        await super().run()


class Scheduler:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def always(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(Task(func))
        return func

    def cron(self, schedule: str) -> Callable[[DecoratedAsync], DecoratedAsync]:
        def decorator(func: DecoratedAsync) -> DecoratedAsync:
            self.tasks.append(CronTask(func, schedule=schedule))
            return func

        return decorator

    def hourly(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(
            CronTask(
                func,
                schedule=(
                    lambda x: x == 0,
                    lambda x: True,
                    lambda x: True,
                    lambda x: True,
                    lambda x: True,
                ),
            )
        )
        return func

    def daily(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(
            CronTask(
                func,
                schedule=(
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: True,
                    lambda x: True,
                    lambda x: True,
                ),
            )
        )
        return func

    def weekly(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(
            CronTask(
                func,
                schedule=(
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: True,
                    lambda x: True,
                ),
            )
        )
        return func

    def monthly(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(
            CronTask(
                func,
                schedule=(
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: x == 0,
                    lambda x: True,
                ),
            )
        )
        return func

    def at_start(self, func: DecoratedAsync) -> DecoratedAsync:
        self.add_task(OnceTask(func))
        return func

    def at(self, at: datetime) -> Callable[[DecoratedAsync], DecoratedAsync]:
        def decorator(func: DecoratedAsync) -> DecoratedAsync:
            self.add_task(OnceAtTask(func, at=at))
            return func

        return decorator

    async def run(self) -> None:
        while True:
            await asyncio.sleep(60 - datetime.now().second)
            for task in self.tasks:
                if task.needs_run():
                    await task.run()


if __name__ == "__main__":
    scheduler = Scheduler()

    @scheduler.at_start
    async def long_task():
        print("Long task starting")
        await asyncio.sleep(5)
        print("Long task done")

    @scheduler.cron("*/2 * * * *")
    async def two_minutes():
        print("Every 2 minutes")

    @scheduler.cron("30 */12 * * 4")
    async def twice_thursdays():
        print("12:30 AM and 12:30 PM on Thursdays")

    @scheduler.cron("0-5 * * * *")
    async def first_five_minutes():
        print("First five minutes of every hour")

    @scheduler.cron("22 18 10 3 *")
    async def this_codes_anniversary():
        print("6:22 PM on March 10th")

    @scheduler.always
    async def print_time_every_minute():
        print("Cron time:", datetime.now().strftime("%M %H %d %m %w"))

    @scheduler.hourly
    async def hourly_task():
        print("It is now", datetime.now().strftime("%H:%M"))

    @scheduler.daily
    async def daily_task():
        print("Good morning!")

    @scheduler.weekly
    async def weekly_task():
        print("This is a weekly task!")

    @scheduler.monthly
    async def monthly_task():
        print("Welcome to", datetime.now().strftime("%B"))

    @scheduler.at(datetime(2025, 3, 10, 18, 29))
    async def future_task():
        print("This is a task for a specific time.")

    print("Scheduler is starting")
    asyncio.run(scheduler.run())
