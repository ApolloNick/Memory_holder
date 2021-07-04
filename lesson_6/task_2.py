import time
import datetime


def count_down(func):
    def wrapper(*args, **kwargs):
        count = 3
        while count > 0:
            time.sleep(1)
            print(count)
            count -= 1
        result = func(*args, **kwargs)
    return wrapper


@count_down
def what_time_is_now():
    time_for_task = datetime.datetime.now()
    current_time = time_for_task.strftime("%I:%M:%S %p")
    print(current_time)
    return current_time


what_time_is_now()

