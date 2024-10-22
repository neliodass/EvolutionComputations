#config.py
import math
import numpy as np
maximize = False
population_size = 30
num_variables = 3
bits_per_variable = 10
min_value = -5.12
max_value = 5.12
precision = 1e-6
generations_num = 100
elitary_percent = 0.01
crossover_chance = 0.8
mutation_chance = 0.1

def solve_for_bits_per_var(var=bits_per_variable):
    return math.ceil(math.log2((max_value-min_value)/precision+1))


def rastrigin(*args):
    N = len(args)  # liczba elementów w *args
    A = 10
    return A * N + sum((xi**2 - A * np.cos(2 * np.pi * xi)) for xi in args)
f = rastrigin