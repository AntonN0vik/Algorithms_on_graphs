import time


def runtime_benchmark(func, *args, repeats=10):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = sum(times) / repeats
    std_dev = (sum((t - avg_time) ** 2 for t in times) / (
                repeats - 1)) ** 0.5 if repeats > 1 else 0
    return avg_time, std_dev
