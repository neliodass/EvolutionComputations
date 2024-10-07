from genetic_algorithm.chromosome import Chromosome
class Population:
    def __init__(self, population_size, num_variables,bits_per_variable,min_value = -5,max_value = 5):
        self.population_size = population_size
        self.num_variables = num_variables
        self.bits_per_variable = bits_per_variable
        self.min_value = min_value
        self.max_value = max_value
        self.chromosomes = [Chromosome(self.num_variables,self.bits_per_variable,min_value=self.min_value,max_value=self.max_value) for _ in range(population_size)]
        