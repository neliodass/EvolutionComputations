import random
import genetic_algorithm.config as config
from genetic_algorithm.chromosome import Chromosome
class Population:
    def __init__(self):
        self.population_size = config.population_size
        self.num_variables = config.num_variables
        self.bits_per_variable = config.bits_per_variable
        self.min_value = config.min_value
        self.max_value = config.max_value
        self.roulette_wheel = None
        self.chromosomes = [Chromosome(self.num_variables,self.bits_per_variable,min_value=self.min_value,max_value=self.max_value) for _ in range(self.population_size)]
    def calculate_fitness(self,chromosome:Chromosome,fitness_function):
        decoded_variables = chromosome.decode()
        fitness_value = fitness_function(*decoded_variables)
        return fitness_value
    def evaluate_population(self,fitness_function):
        """
        :param fitness_function 
        assigns fitness function value for every chromosome
        """
        for chromosome in self.chromosomes:
            chromosome.fitness = self.calculate_fitness(chromosome,fitness_function)

    def select_best(self,percent_to_select):
        """
        :param percent_to_select - procent najlepszych osobnikow 
        :return array of best percentage of entities
        """
        num_to_select = int(percent_to_select/100*self.population_size)
        return sorted(self.chromosomes,key = lambda c: c.fitness, reverse=config.maximize )[:num_to_select]
    
    def prepare_roulette_wheel(self):
        print(config.maximize)
        if config.maximize:
            wheel_sum = sum([c.fitness for c in self.chromosomes])
            probabilities = [c.fitness/wheel_sum for c in self.chromosomes]
        else:
            adjusted_fitness = [1/c.fitness if c.fitness!=0 else 1e-6 for c in self.chromosomes]
            wheel_sum = sum(adjusted_fitness)
            probabilities = [af/wheel_sum for af in adjusted_fitness]
        cumulative_sum = 0
        wheel_cumulative = []
        for p in probabilities:
            cumulative_sum+=p
            wheel_cumulative.append(cumulative_sum)
        return wheel_cumulative

    def select_roulette_wheel(self,percent_to_select):
        num_to_select = int(percent_to_select/100*self.population_size)
        wheel_cumulative = self.prepare_roulette_wheel()
        chosen_chromosomes = []
        for _ in range(num_to_select):
            r = random.random()
            for idx,c in enumerate(self.chromosomes):
                if r<= wheel_cumulative[idx]:
                    chosen_chromosomes.append(c)
                    break
        return chosen_chromosomes