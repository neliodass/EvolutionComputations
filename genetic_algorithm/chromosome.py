import numpy as np

class Chromosome:
    def __init__(self,num_variables,bits_per_variable = 10,precision = 0.01,min_value = -5, max_value = 5) -> None:
        """
        :param num_variables - ilosc zmiennych w chromosomie
        :param bits_per_variable - ilosc bitow reprezentujacych jedna zmienna
        :param precision - precyzja wartosci zmiennej 
        :param min_value - minimalna wartość przedziału wartości genu
        :param max_value - maksymalna wartość przedziału wartości genu
        """
        self.num_variables = num_variables
        self.bits_per_variable = bits_per_variable
        self.precision = precision
        self.min_value = min_value
        self.max_value = max_value
        self.genes = self.random_genes()
        self.fitness = None
    
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
            