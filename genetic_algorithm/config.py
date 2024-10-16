#config.py
import math
import numpy as np
maximize = False
population_size = 100
num_variables = 3
bits_per_variable = 10
min_value = -600
max_value = 600
precision = 1e-8
generations_num = 1000
elitary_percent = 0.01
crossover_chance = 0.8
def solve_for_bits_per_var(var=bits_per_variable):
    return math.ceil(math.log2((max_value-min_value)/precision+1))
def f(*args):
    n = len(args)
    sum_term = sum((x**2) / 4000 for x in args)
    product_term = np.prod([np.cos(x / np.sqrt(i + 1)) for i, x in enumerate(args)])
    return sum_term - product_term + 1