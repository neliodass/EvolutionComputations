

from genetic_algorithm.population import Population
import genetic_algorithm.config as config
from genetic_algorithm.selections import *
from genetic_algorithm.crossovers import *
from genetic_algorithm.mutations import *
from genetic_algorithm.inversions import *
from genetic_algorithm.chromosome import Chromosome
from genetic_algorithm.ga import genetic_algorithm
import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import GeneticAlgorithmApp
def f(*args):
    return np.sum(np.array(args)**2)

#maximize ustawia czy szukamy maksimum funkcji czy minimum


# pop = Population()
# pop.evaluate_population(config.f)
# for x in pop.chromosomes:
#     print(x)
# print("++++++++++++++")
# print(select_best(pop,0.2))
#genetic_algorithm()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GeneticAlgorithmApp()
    window.show()
    sys.exit(app.exec_())