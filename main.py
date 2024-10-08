

from genetic_algorithm.population import Population
import genetic_algorithm.config as config

def function(x):
    return 2*x**2-4*x+2

#maximize ustawia czy szukamy maksimum funkcji czy minimum
config.maximize = True
config.population_size = 100
config.bits_per_variable = 10
config.num_variables = 1
population = Population()
population.evaluate_population(function)
for c in population.select_tournament(20):
    print(c.fitness)

