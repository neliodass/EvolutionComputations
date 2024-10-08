

from genetic_algorithm.population import Population
import genetic_algorithm.config as config
from genetic_algorithm.selections import *

def function(x,y):
    return 2*x**2-4*x+2 +y**3

#maximize ustawia czy szukamy maksimum funkcji czy minimum
config.maximize = True
config.population_size = 1000
config.bits_per_variable = 10
config.num_variables = 2
population = Population()
population.evaluate_population(function)
select_tournament(population,100)
# for c in select_tournament(population,20):
#     print(c.fitness)

