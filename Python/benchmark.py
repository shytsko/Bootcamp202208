import time


def TimeBenchmark(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        return_value = func(*args, **kwargs)
        end = time.perf_counter_ns()
        print(
            f'[*] Время выполнения {func.__name__}: {(end-start)/1000000} мс')
        return return_value
    return wrapper
