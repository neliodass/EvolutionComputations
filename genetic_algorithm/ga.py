import genetic_algorithm.config as config
from genetic_algorithm.selections import *
from genetic_algorithm.crossovers import *
from genetic_algorithm.mutations import *
from genetic_algorithm.inversions import *
from genetic_algorithm.elitary import *
from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.population import Population
from copy import deepcopy
def genetic_algorithm():
    config.bits_per_variable = config.solve_for_bits_per_var()
    population = Population()
    fitness_function = config.f
    population.evaluate_population(fitness_function=fitness_function)
    best_chromosomes = []
    for generation in range(config.generations_num):
       # print(f"Generation {generation + 1}/{config.generations_num}")
        elite_chromosomes = deepcopy(elitary_strategy(population,1))
        top = elite_chromosomes[0]
        offspring = []
        remaining_chromosomes = select_roulette_wheel(population,0.3)
        while len(offspring)<population.population_size - len(elite_chromosomes):
            parent1,parent2 = random.sample(remaining_chromosomes,2)
            if random.random()<config.crossover_chance:
                child1,child2 = multi_point_crossover(parent1,parent2,5)
                offspring.extend([child1,child2])
            else:
                offspring.extend([parent1,parent2])
        for child in offspring:
            edge_bit_mutation(child,0.4)
            inversion(child,chance_rate=0.2)
        offspring = offspring[:population.population_size - len(elite_chromosomes)]
        new_population = elite_chromosomes+offspring
        population.chromosomes = deepcopy(new_population)
        population.evaluate_population(fitness_function)
        best = elitary_strategy(population, 4)[0]
        best_chromosomes.append(best)
        #print(f"Best fitness in this generation: {best.fitness:.6f}")
    print(best_chromosomes[-1].genes)
    print(f"{best_chromosomes[-1].fitness:.6f}")
    # print("\nBest chromosomes across all generations:")
    # for generation, best in enumerate(best_chromosomes):
    #     print(f"Generation {generation + 1}: {[c.fitness for c in best]}")