import genetic_algorithm.config as config
import random
def select_best(population,percent_to_select):
    """
    :param percent_to_select - procent najlepszych osobnikow 
    :return array of best percentage of entities
    """
    num_to_select = int(percent_to_select/100*population.population_size)
    return sorted(population.chromosomes,key = lambda c: c.fitness, reverse=config.maximize )[:num_to_select]

def select_tournament(population,tournament_size = 3):
        idx_array = list(range(len(population.chromosomes)))
        random.shuffle(idx_array)
        idx_chunks = [idx_array[i:i+tournament_size] for i in range(0,len(idx_array),tournament_size)]
        chunks = [[population.chromosomes[idx] for idx in idx_chunk] for idx_chunk in idx_chunks] 
        chosen_chromosomes =[]
        for chunk in chunks:
           chosen = sorted(chunk,key = lambda c: c.fitness,reverse=config.maximize)[0]
           chosen_chromosomes.append(chosen)
        return chosen_chromosomes
def prepare_roulette_wheel(population):
    print(config.maximize)
    if config.maximize:
        wheel_sum = sum([c.fitness for c in population.chromosomes])
        probabilities = [c.fitness/wheel_sum for c in population.chromosomes]
    else:
        adjusted_fitness = [1/c.fitness if c.fitness!=0 else 1e-6 for c in population.chromosomes]
        wheel_sum = sum(adjusted_fitness)
        probabilities = [af/wheel_sum for af in adjusted_fitness]
    cumulative_sum = 0
    wheel_cumulative = []
    for p in probabilities:
        cumulative_sum+=p
        wheel_cumulative.append(cumulative_sum)
    return wheel_cumulative

def select_roulette_wheel(population,percent_to_select):
    num_to_select = int(percent_to_select/100*population.population_size)
    wheel_cumulative = prepare_roulette_wheel(population)
    chosen_chromosomes = []
    for _ in range(num_to_select):
        r = random.random()
        for idx,c in enumerate(population.chromosomes):
            if r<= wheel_cumulative[idx]:
                chosen_chromosomes.append(c)
                break
    return chosen_chromosomes
    