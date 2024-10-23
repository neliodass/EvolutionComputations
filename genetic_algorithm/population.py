import random
import genetic_algorithm.config as config
from genetic_algorithm.chromosome import Chromosome
import numpy as np
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
        self.fitness_values = None

    def decode_population(self):
        decoded = np.array([chromosome.decode() for chromosome in self.chromosomes])
        return decoded


    def calculate_fitness(self,decoded_variables,fitness_function):
        #decoded_variables = chromosome.decode()
        fitness_value = np.apply_along_axis(fitness_function,1,decoded_variables)
        self.fitness_values = fitness_value
        return fitness_value
    def evaluate_population(self,fitness_function):
        """
        :param fitness_function 
        assigns fitness function value for every chromosome
        """
        decoded_variables = self.decode_population()
        fitness_values = self.calculate_fitness(decoded_variables,fitness_function)
        for chromosome,fitness_value in zip(self.chromosomes,fitness_values):
            chromosome.fitness = fitness_value
            
