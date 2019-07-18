import time


def cronize_function(duration, cycle, fn, *args):
    while duration > 0:
        yield fn(*args)
        duration -= cycle
        if duration < cycle:
            break
        time.sleep(cycle)
