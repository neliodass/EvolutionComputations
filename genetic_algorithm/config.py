#config.py
import math
import numpy as np

def rosenbrock(x):
    X = np.array(x) 
    return sum([100 * (X[i+1] - X[i]**2)**2 + (X[i] - 1)**2 for i in range(len(X) - 1)])
def rastrigin(x):
 
    N = len(x)  
    A = 10
    return A * N + sum((xi**2 - A * np.cos(2 * np.pi * xi)) for xi in x)

f = rastrigin
num_variables = 5
min_value = -5
max_value = 10
maximize = False


precision = 1e-8
population_size = 100
generations_num = 5000
bits_per_variable = 10

#best - 1
#wheel - 2
#tournament - 3
selection_method = 1
tournament_size = 10
selection_percentage = 0.5
# one point - 1
# multi point - 2
# uniform - 3
# discrete - 4
crossover_method= 1
crossover_chance = 0.8
crossover_param = 0.5

# bitflip - 1
# edge - 2
mutation_method =1
mutation_chance = 0.4
mutation_param = 0.5

inversion_chance = 0.5
inversion_param = 0.5

elitary_num = 2
ui_enabled = False


results = None
def solve_for_bits_per_var(var=bits_per_variable):
    return math.ceil(math.log2((max_value-min_value)/precision+1))


