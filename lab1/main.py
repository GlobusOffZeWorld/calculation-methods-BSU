import time
import task8

VARIANT_NUMBER = 2**(14 / 4)


def time_to_run(func, *args):
    start_time = time.time()
    x = func(*args)
    return (time.time() - start_time, x)


class MinAvgMax:
    def __init__(self, min, avg, max):
        self.min = min
        self.avg = avg
        self.max = max


def main():
    # task8.task_solution()

    


if __name__ == "__main__":
    main()
