from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.config import maximize
class Population:
    def __init__(self, population_size, num_variables,bits_per_variable,min_value = -5,max_value = 5):
        self.population_size = population_size
        self.num_variables = num_variables
        self.bits_per_variable = bits_per_variable
        self.min_value = min_value
        self.max_value = max_value
        self.chromosomes = [Chromosome(self.num_variables,self.bits_per_variable,min_value=self.min_value,max_value=self.max_value) for _ in range(population_size)]
    def calculate_fitness(self,chromosome:Chromosome,fitness_function):
        decoded_variables = chromosome.decode()
        fitness_value = fitness_function(*decoded_variables)
        return fitness_value
    def evaluate_population(self,fitness_funciton):
        for chromosome in self.chromosomes:
            chromosome.fitness = self.calculate_fitness(chromosome,fitness_funciton)

    def select_best(self,percent_to_select):
        """
        :param percent_to_select - procent najlepszych osobnikow 
        """
        num_to_select = int(percent_to_select/100*self.population_size)
        return sorted(self.chromosomes,key = lambda c: c.fitness, reverse=maximize )[:num_to_select]