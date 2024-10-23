import genetic_algorithm.config as config
from genetic_algorithm.results import Results
from genetic_algorithm.selections import *
from genetic_algorithm.crossovers import *
from genetic_algorithm.mutations import *
from genetic_algorithm.inversions import *
from genetic_algorithm.elitary import *
from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.population import Population

from copy import deepcopy
window_instance = None




def genetic_algorithm():
    results = Results()
    config.results = results
    config.bits_per_variable = config.solve_for_bits_per_var()
    population = Population()
    fitness_function = config.f
    population.evaluate_population(fitness_function=fitness_function)
    results.get_fitness_stats(population,0)
    for generation in range(config.generations_num-1):
        elite_chromosomes = deepcopy(elitary_strategy(population,config.elitary_num))
        #top = elite_chromosomes[0]
        offspring = []
        remaining_chromosomes = list()
        if config.selection_method ==1:
            remaining_chromosomes = select_best(population,config.selection_percentage)
        elif config.selection_method == 2:
            remaining_chromosomes = select_roulette_wheel(population,config.selection_percentage)
        else:
            remaining_chromosomes = select_tournament(population,config.tournament_size)
    
        while len(offspring)<population.population_size - len(elite_chromosomes):
            parent1,parent2 = random.sample(remaining_chromosomes,2)
            child1,child2 = None,None
            if random.random()<config.crossover_chance:
                if config.crossover_method == 1:
                    child1,child2 = one_point_crossover(parent1,parent2)
                elif config.crossover_chance == 2:
                    child1,child2 = multi_point_crossover(parent1,parent2,config.crossover_param)
                elif config.crossover_chance ==3:
                    child1,child2 = uniform_crossover(parent1,parent2,config.crossover_param)
                else:
                    child1 = discrete_crossover(parent1,parent2,config.crossover_param)
                    offspring.extend([child1])
                    continue
                offspring.extend([child1,child2])
            
        for child in offspring:
            if random.random()<config.mutation_chance:
                if config.mutation_method ==2:
                    edge_bit_mutation(child,config.mutation_param)
                else:
                    bit_flip_mutation(child,config.mutation_param)
            if random.random()<config.inversion_chance:
                inversion(child,chance_rate=config.inversion_param)
        offspring = offspring[:population.population_size - len(elite_chromosomes)]
        new_population = elite_chromosomes+offspring
        population.chromosomes = deepcopy(new_population)
        population.evaluate_population(fitness_function)
        best1 = results.get_fitness_stats(population,generation+1)
        if config.ui_enabled and generation%(config.generations_num//100) == 0:
            window_instance.update_progress(generation)

        #if generation%100==0:
        print(f"Best fitness in this generation {generation}: {best1:.6f}")

    # print(best_chromosomes[-1].genes)
    # print(f"{best_chromosomes[-1].fitness:.6f}")
    # print("\nBest chromosomes across all generations:")
    # for generation, best in enumerate(best_chromosomes):
    #     print(f"Generation {generation + 1}: {[c.fitness for c in best]}")