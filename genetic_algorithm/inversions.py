import genetic_algorithm.config as config
import random
def inversion(c,chance_rate=0.05):
    for gene_num in range(config.num_variables):
        if random.random()<chance_rate:
            gene_start = gene_num*config.bits_per_variable
            gene_end = gene_start+config.bits_per_variable  
            point1,point2 = sorted(random.sample(range(gene_start,gene_end),2))
            c.genes[point1:point2] = c.genes[point1:point2][::-1]