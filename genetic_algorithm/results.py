import numpy as np
import genetic_algorithm.config as config
import matplotlib.pyplot as plt
from datetime import datetime
import os
class Results:
    def __init__(self):
        self.stats = np.zeros((config.generations_num, 3))  
    def get_fitness_stats(self,population,generation):
        fitness_values = population.fitness_values
        mean_fitness = np.mean(fitness_values)
        std_fitness = np.std(fitness_values)
        top_fitness = np.max(fitness_values) if config.maximize else np.min(fitness_values)
        self.stats[generation] = [mean_fitness,std_fitness,top_fitness]
        return top_fitness
    def save_stats_to_file(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"results_{date_str}.txt"
        file_path = os.path.join(current_directory, filename)
        np.savetxt(file_path,self.stats,delimiter=",",header= "Mean_Fitness,Std_Dev,Top_1_Fitness")
    def plot_top_fitness(self,):
   
        num_generations = self.stats.shape[0]
        top_fitness = self.stats[:, 2]
        plt.figure(figsize=(10, 6))
        plt.plot(top_fitness, label="Najlepszy wynik fitness", color='g')

        plt.title("Najlepszy wynik fitness na przestrzeni generacji")
        plt.xlabel("Generacje")
        plt.ylabel("Fitness")
        plt.legend()
        plt.grid(True)
        plt.show()
    def plot_fitness_mean_and_std(self):
   
        num_generations = self.stats.shape[0]
        fitness_mean = self.stats[:, 0]
        fitness_std = self.stats[:, 1]

        plt.figure(figsize=(10, 6))
        plt.plot(fitness_mean, label="Średnia fitness", color='b')
        plt.fill_between(range(num_generations),
                     fitness_mean - fitness_std,
                     fitness_mean + fitness_std,
                     color='b', alpha=0.2, label="Odchylenie standardowe")
        plt.title("Średnia wartość fitness i odchylenie standardowe")
        plt.xlabel("Generacje")
        plt.ylabel("Fitness")
        plt.legend()
        plt.grid(True)
        plt.show()
    #def top_fitness(self):
        