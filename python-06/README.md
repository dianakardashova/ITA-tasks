Task description.
There is a decorator which measures execution time of decorated function

import functools
import time

def timer(func):
    """Prints the runtime of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer
The current implementation will measure execution time only if a decorated function doesn't raise
an error. But the current execution time won't be shown if some error will occur.

So, you need to update existing code in order to make it showing execution time regardless of
errors in decorated function. And if an error happens, it has to be raised.