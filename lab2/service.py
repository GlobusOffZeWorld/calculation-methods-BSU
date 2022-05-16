from pprint import pprint
import matplotlib.pyplot as plt
from Matrix import Matrix
from SolveMethods import SolveMethods
import time
import math


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