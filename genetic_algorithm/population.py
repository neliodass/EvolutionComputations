import random
import genetic_algorithm.config as config
from genetic_algorithm.chromosome import Chromosome
class Population:
    def __init__(self):
        random.seed()
        self.population_size = config.population_size
        self.num_variables = config.num_variables
        self.bits_per_variable = config.bits_per_variable
        self.min_value = config.min_value
        self.max_value = config.max_value
        self.roulette_wheel = None
        self.chromosomes = [Chromosome() for _ in range(self.population_size)]
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
    
