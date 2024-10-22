import random
import numpy as np
import genetic_algorithm.config as config
from genetic_algorithm.chromosome import Chromosome
def one_point_crossover(c1,c2):
    crossover_points = [random.randrange(0,config.bits_per_variable) for _ in range(config.num_variables)]
    
    new_genes_1 = np.empty_like(c1.genes)
    new_genes_2 = np.empty_like(c2.genes)
    for gene_num in range(config.num_variables):

        gene_start=gene_num*config.bits_per_variable
        gene_end = gene_start+config.bits_per_variable
        crossover_point = crossover_points[gene_num]+gene_start
        
        new_genes_1[gene_start:crossover_point] = c1.genes[gene_start:crossover_point]
        new_genes_1[crossover_point:gene_end] = c2.genes[crossover_point:gene_end]
        new_genes_2[gene_start:crossover_point] = c2.genes[gene_start:crossover_point]
        new_genes_2[crossover_point:gene_end] = c1.genes[crossover_point:gene_end]
    return Chromosome(new_genes_1),Chromosome(new_genes_2)


def multi_point_crossover(c1,c2,points = 2):
    if points >= config.bits_per_variable: points = config.bits_per_variable-1
    new_genes_1 = np.copy(c1.genes)
    new_genes_2 = np.copy(c2.genes)
    crossover_mask = np.zeros(config.bits_per_variable * config.num_variables, dtype=bool)
    for gene_num in range(config.num_variables):
        gene_start = gene_num*config.bits_per_variable
        gene_end = gene_start+config.bits_per_variable
        crossover_points = sorted(random.sample(range(gene_start,gene_end),points))
        if points%2!=0: crossover_points.append(gene_end)
        for i in range(0,len(crossover_points),2):
            crossover_mask[crossover_points[i]:crossover_points[i + 1]] = True
    new_genes_2[crossover_mask] = c1.genes[crossover_mask]
    new_genes_1[crossover_mask] = c2.genes[crossover_mask]
    return Chromosome(new_genes_1),Chromosome(new_genes_2)   

        

def uniform_crossover(chromosome1,chromosome2,chance = 0.5):
    """
    :param chance - szansa z jaką bity zostaną zamienione między chromosomami
    """
    new_genes_1 = np.copy(chromosome1.genes)
    new_genes_2 = np.copy(chromosome2.genes)
    crossover_mask = np.random.rand(config.bits_per_variable*config.num_variables)>chance
    new_genes_2[crossover_mask] = chromosome1.genes[crossover_mask]
    new_genes_1[crossover_mask] = chromosome2.genes[crossover_mask]
    return Chromosome(new_genes_1),Chromosome(new_genes_2)
def discrete_crossover(chromosome1,chromosome2,chance = 0.5):
    """
    :param chance - szansa z jaką bit zostanie z chromosomu 1
    """
    new_genes = np.copy(chromosome1.genes)
    crossover_mask = np.random.rand(config.bits_per_variable*config.num_variables)>chance
    new_genes[crossover_mask] = chromosome2.genes[crossover_mask]

    return Chromosome(new_genes)