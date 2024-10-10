

from genetic_algorithm.population import Population
import genetic_algorithm.config as config
from genetic_algorithm.selections import *
from genetic_algorithm.crossovers import *
from genetic_algorithm.chromosome import Chromosome

def function(x,y):
    return 2*x**2-4*x+2 +y**3

#maximize ustawia czy szukamy maksimum funkcji czy minimum
config.maximize = False
config.population_size = 1000
config.bits_per_variable = 20
config.num_variables = 4
population = Population()

chromosom1 = Chromosome()
chromosom2 = Chromosome()

multi_point_crossover(chromosom1,chromosom2,4)

