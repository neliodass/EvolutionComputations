import random
import genetic_algorithm.config as config
def bit_flip_mutation(c,mutation_rate = 0.1):
    if not (0<=mutation_rate<=1):
        raise ValueError("Mutation rate must be between 0 and 1.")
    for i in range(len(c.genes)):
        if random.random()<mutation_rate:
            c.genes[i] = 1- c.genes[i]
def edge_bit_mutation(c,mutation_rate = 0.1):
    for gene in range(config.num_variables):
        gene_start = gene*config.bits_per_variable
        gene_end = gene_start+config.bits_per_variable-1
        if random.random()<mutation_rate:
            c.genes[gene_start] = 1-c.genes[gene_start]
        if random.random()<mutation_rate:
            c.genes[gene_end] = 1-c.genes[gene_end]
        