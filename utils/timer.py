import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        ts = time.perf_counter()
        result = func(*args, **kwargs)
        te = time.perf_counter()
        elapsed_time = te - ts
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return result
    return wrapper_timer
