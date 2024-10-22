from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QGridLayout,QSpinBox,QComboBox
)
import sys
from qt_material import apply_stylesheet
import genetic_algorithm.config as config
class GeneticAlgorithmApp(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Genetic Algorithm Optimization")
        self.setGeometry(100, 100, 800, 600)
        extra = {
            "primaryTextColor":"#FFFFFF",
            "secondaryTextColor":"#FFFFFF"
        }
        apply_stylesheet(self,theme='dark_lightgreen.xml',extra=extra)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        func_config_layout = QGridLayout()
        population_config_layout = QGridLayout()
        algorithm_config_layout = QVBoxLayout()

        #FUNC CONFIG LAYOUT
        self.function_combo = QComboBox()
        self.function_combo.addItems(["Funkcja1", "Funkcja2", "Funkcja3"])
        func_config_layout.addWidget(QLabel("Number of Variables:"), 0, 0)
        func_config_layout.addWidget(self.function_combo,0,1,0,2)
        self.maximize_checkbox = QCheckBox("Maximize")
        func_config_layout.addWidget(self.maximize_checkbox, 0, 4)


        
        # Parametry populacji
        self.num_vars_input = QSpinBox()
        self.num_vars_input.setMinimum(1)
        self.num_vars_input.setMaximum(100)
        self.precision_input = QSpinBox()
        self.precision_input.setMinimum(1)
        self.precision_input.setMaximum(10)
        self.epochs_input = QSpinBox()
        self.epochs_input.setMinimum(10)
        self.epochs_input.setMaximum(10000)
        self.epochs_input.setSingleStep(10)
        self.pop_size_input = QSpinBox()
        self.epochs_input.setMinimum(1)
        self.epochs_input.setMaximum(10000)
        self.crossover_prob_input = QLineEdit()
        self.crossover_prob_input.setMinimum(1)
        self.crossover_prob_input.setMaximum(100)
        self.mutation_prob_input = QLineEdit()
        self.mutation_prob_input.setMinimum(1)
        self.mutation_prob_input.setMaximum(100)

        self.selection_type_combo = QComboBox()
        self.selection_type_combo.addItems(["Choose option..","Best selection", "Wheel of fortune selection", "Tournament selection"])
        

        self.selection_params_label = QLabel("Params:")
        self.selection_param_input = QSpinBox()

        self.crossover_type_combo = QComboBox()
        self.crossover_type_combo.addItems(["Choose option..","One point crossover", "Multi point crossover", "Uniform crossover","Discrete crossover"])
        
        self.crossover_params_label = QLabel("Params:")
        self.crossover_param_input = QSpinBox()

        self.selection_type_combo.currentIndexChanged.connect(self.on_selection_type_change)
        self.crossover_type_combo.currentIndexChanged.connect(self.on_crossover_type_change)
        

        population_config_layout.addWidget(QLabel("Number of Variables:"), 0, 0)
        population_config_layout.addWidget(self.num_vars_input, 0, 1)
        
        population_config_layout.addWidget(QLabel("Precision(number of decimal places):"), 1, 0)
        population_config_layout.addWidget(self.precision_input, 1, 1)
        
        population_config_layout.addWidget(QLabel("Number of Epochs:"), 2, 0)
        population_config_layout.addWidget(self.epochs_input, 2, 1)
        
        population_config_layout.addWidget(QLabel("Population Size:"), 3, 0)
        population_config_layout.addWidget(self.pop_size_input, 3, 1)
        
        population_config_layout.addWidget(QLabel("Crossover Probability:"), 4, 0)
        population_config_layout.addWidget(self.crossover_prob_input, 4, 1)
        
        population_config_layout.addWidget(QLabel("Mutation Probability:"), 5, 0)
        population_config_layout.addWidget(self.mutation_prob_input, 5, 1)
        
        algorithm_config_layout.addWidget(QLabel("Choose selection method:"))
        algorithm_config_layout.addWidget(self.selection_type_combo)
        algorithm_config_layout.addWidget(self.selection_params_label)
        algorithm_config_layout.addWidget(self.selection_param_input)
        self.selection_param_input.hide()
        self.selection_params_label.hide()
        algorithm_config_layout.addWidget(QLabel("Choose crossover method:"))
        algorithm_config_layout.addWidget(self.crossover_type_combo)
        algorithm_config_layout.addWidget(self.crossover_params_label)
        algorithm_config_layout.addWidget(self.crossover_param_input)
        self.crossover_params_label.hide()
        self.crossover_param_input.hide()

        main_layout.addLayout(func_config_layout)
        main_layout.addLayout(population_config_layout)
        main_layout.addLayout(algorithm_config_layout)

       
        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_algorithm)
        main_layout.addWidget(self.run_button)

       
        self.results_widget = QWidget()
        main_layout.addWidget(self.results_widget)

        central_widget.setLayout(main_layout)

    def on_selection_type_change(self):
        selected_type = self.selection_type_combo.currentText()
        self.selection_param_input.show()
        self.selection_params_label.show()
        
        if selected_type == "Best selection":
            self.selection_params_label.setText("Enter best percentage to select:")
            self.selection_param_input.setMinimum(1)
            self.selection_param_input.setMaximum(99)

        elif selected_type == "Wheel of fortune selection":
            self.selection_params_label.setText("Enter best percentage to select:")
            self.selection_param_input.setMinimum(1)
            self.selection_param_input.setMaximum(99)
    

        elif selected_type == "Tournament selection":
            self.selection_params_label.setText("Enter tournament size:")
            self.selection_param_input.setMinimum(1)
            self.selection_param_input.setMaximum(10000)
        else:
            self.selection_param_input.hide()
            self.selection_params_label.hide()
    def on_crossover_type_change(self):
        self.crossover_param_input.show()
        self.crossover_params_label.show()
        selected_type = self.crossover_type_combo.currentText()
        if selected_type == "One point crossover":
            self.crossover_param_input.hide()
            self.crossover_params_label.hide()
        elif selected_type == "Multi point crossover":
            self.crossover_param_input.setMinimum(1)
            self.crossover_param_input.setMaximum(config.bits_per_variable-1)
            self.crossover_params_label.setText("The number of points at which the chromosomes will be crossed over.")
        elif selected_type == "Uniform crossover":
            self.crossover_param_input.setMinimum(1)
            self.crossover_param_input.setMaximum(100)
            self.crossover_params_label.setText("The percentage chance that bits will be exchanged between chromosomes.")
        elif selected_type == "Discrete crossover":
            self.crossover_param_input.setMinimum(1)
            self.crossover_param_input.setMaximum(100)
            self.crossover_params_label.setText("The percentage chance with which a bit will not be taken from the second chromosome")
        else:
            self.crossover_param_input.hide()
            self.crossover_params_label.hide()
    def run_algorithm(self):
        
        config.maximize = self.maximize_checkbox.isChecked()
        config.num_variables = int(self.num_vars_input.text())
        
        precision = int(self.precision_input.text())
        config.precision = float(f"1e-{precision}")
        config.generations_num = int(self.epochs_input.text())
        config.population_size = int(self.pop_size_input.text())
        config.crossover_chance= float(self.crossover_prob_input.text())/100
        config.mutation_chance = float(self.mutation_prob_input.text())/100
        

        
        print(f"Running algorithm with: num_vars={config.num_variables}, precision={precision}, epochs={config.generations_num}, "
              f"pop_size={config.population_size}, crossover_prob={config.crossover_chance}, mutation_prob={config.mutation_chance}, maximize={config.maximize}")

        