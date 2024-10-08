

from genetic_algorithm.population import Population
import genetic_algorithm.config as config

def function(x):
    return 2*x**2-4*x+2

#maximize ustawia czy szukamy maksimum funkcji czy minimum
config.maximize = False
config.population_size = 30
config.bits_per_variable = 10
config.num_variables = 1
population = Population()
population.evaluate_population(function)

for idx,c in enumerate(population.select_roulette_wheel(34)):
    print(idx,c.fitness)
