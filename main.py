

from genetic_algorithm.population import Population
from genetic_algorithm.config import maximize

def function(x):
    return 2*x**2-4*x+2

#maximize ustawia czy szukamy maksimum funkcji czy minimum
maximize = True
population = Population(7,1,10)
population.evaluate_population(function)
print([c.fitness for c in population.chromosomes])
print([c.fitness for c in population.select_best(30)])