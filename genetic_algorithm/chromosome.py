import numpy as np
import genetic_algorithm.config as config
class Chromosome:
    def __init__(self,genes = None) -> None:
        """
        :param num_variables - ilosc zmiennych w chromosomie
        :param bits_per_variable - ilosc bitow reprezentujacych jedna zmienna
        :param precision - precyzja wartosci zmiennej 
        :param min_value - minimalna wartość przedziału wartości genu
        :param max_value - maksymalna wartość przedziału wartości genu
        """
        
        self.num_variables = config.num_variables
        self.bits_per_variable = config.bits_per_variable
        self.min_value = config.min_value
        self.max_value = config.max_value
        if self.min_value>self.max_value:
            raise ValueError("min_value must be less than max_value")
        if genes is None:
            self.genes = self.random_genes()
        else: self.genes = genes
        self.fitness = None
    def __repr__(self):
        return f"Chromosome({self.fitness})"
        #return f"Chromosome(genes={self.genes}, fitness={self.fitness})"
    def random_genes(self):
        """
        Tworzy losowy binarny ciąg genów dla chromosomu
        :return int(ciag binarnych wartosci 1,0)
        """
        return np.random.randint(2,size=self.num_variables*self.bits_per_variable)
    
    def binary_to_dec(self,binary_segment):
        return self.min_value + int(''.join(binary_segment.astype(str)),2)*(self.max_value-self.min_value)/(2**self.bits_per_variable-1)
        

    def decode(self):
        variables = []
        for i in range(self.num_variables):
            start = i*self.bits_per_variable
            end = start + self.bits_per_variable
            binary_segmnet = self.genes[start:end]
            real_value = self.binary_to_dec(binary_segmnet)
            variables.append(real_value)
        return np.array(variables)
            