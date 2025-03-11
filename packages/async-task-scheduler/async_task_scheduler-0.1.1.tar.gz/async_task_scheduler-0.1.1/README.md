# async_task_scheduler

`async_task_scheduler` is a Python module that allows you to schedule asynchronous tasks using various scheduling strategies such as cron-like schedules, one-time execution, and more.

## Installation

To install the module, simply install it using `pip`:

```sh
pip install async_task_scheduler
```

## Usage

### Creating a Scheduler

First, create an instance of the `Scheduler` class:

```python
from async_task_scheduler import Scheduler

scheduler = Scheduler()
```

### Adding Tasks

You can add tasks to the scheduler using various decorators:

#### Always

Runs the task every minute.

```python
@scheduler.always
async def every_minute():
    print("This will be called every minute")
```

#### Cron

Runs the task based on a cron-like schedule.

```python
@scheduler.cron("*/2 * * * 5")
async def custom_cron_schedule():
    print("This will be called every two minutes on Fridays")
```

#### Hourly

Runs the task at the start of every hour.

```python
@scheduler.hourly
async def every_hour():
    print("This will be called every hour")
```

#### Daily

Runs the task at the start of every day.

```python
@scheduler.daily
async def every_day():
    print("This will be called every day")
```

#### Weekly

Runs the task at the start of every week.

```python
@scheduler.weekly
async def every_week():
    print("This will be called every week")
```

#### Monthly

Runs the task at the start of every month.

```python
@scheduler.monthly
async def every_month():
    print("This will be called every month")
```

#### At Start

Runs the task once when the scheduler starts.

```python
@scheduler.at_start
async def start_task():
    print("This will be called once when the scheduler starts")
```

#### At Specific Time

Runs the task at a specific datetime.

```python
@scheduler.at(datetime(2025, 3, 10, 18, 29))
async def future_task():
    print("This will be called at 6:29 PM on March 10, 2025")
```

### Running the Scheduler

To run the scheduler, await the `run` method or call it using `asyncio.run`:

```python
await scheduler.run()
```

or

```python
import asyncio

asyncio.run(scheduler.run())
```

The scheduler will run indefinitely until the program is stopped.

## Example

See the end of the source file for a complete example.

## License

This project is licensed under the MIT License.
