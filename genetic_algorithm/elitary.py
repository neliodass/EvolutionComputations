from genetic_algorithm.selections import select_best
import genetic_algorithm.config as config
def elitary_strategy(population,number):
    best = select_best(population,number/config.population_size)
    #print(best)
    return select_best(population,number/config.population_size)

