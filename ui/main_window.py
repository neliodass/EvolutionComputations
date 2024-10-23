from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QGridLayout,QSpinBox,QComboBox,QGroupBox,QDoubleSpinBox,QProgressBar)
from qt_material import apply_stylesheet
import genetic_algorithm.config as config
from genetic_algorithm.ga import genetic_algorithm
import genetic_algorithm.ga as ga
import time
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


    def update_progress(self,progress):
        self.progress_bar.setValue(progress)

    def function_config_part(self):
        #FUNC CONFIG LAYOUT
        self.function_combo = QComboBox()
        self.function_combo.addItems(["Rastrigin", "Rosenbrock"])
        self.num_vars_input = QSpinBox()
        self.num_vars_input.setMinimum(1)
        self.num_vars_input.setMaximum(100)
        self.maximize_checkbox = QCheckBox("Maximize")
        self.min_value_input = QDoubleSpinBox()
        self.min_value_input.setMinimum(-10000.0)
        self.min_value_input.setDecimals(2)
        self.max_value_input = QDoubleSpinBox()
        self.max_value_input.setDecimals(2)


        self.func_config_layout.addWidget(QLabel("Function:"),0,0)
        self.func_config_layout.addWidget(self.function_combo,1,0)
        self.func_config_layout.addWidget(QLabel("Number of Variables:"),0,1)
        self.func_config_layout.addWidget(self.num_vars_input,1,1)
        self.func_config_layout.addWidget(QLabel("Minimal value:"),2,0)
        self.func_config_layout.addWidget(self.min_value_input,3,0)
        self.func_config_layout.addWidget(QLabel("Maximal value:"),2,1)
        self.func_config_layout.addWidget(self.max_value_input,3,1)
        self.func_config_layout.addWidget(self.maximize_checkbox,4,0)
        
    def population_config_part(self):
         # Parametry populacji
        self.precision_input = QSpinBox()
        self.precision_input.setMinimum(1)
        self.precision_input.setMaximum(10)
        self.epochs_input = QSpinBox()
        self.epochs_input.setMinimum(10)
        self.epochs_input.setMaximum(100000)
        self.epochs_input.setSingleStep(10)
        self.pop_size_input = QSpinBox()
        self.pop_size_input.setMinimum(1)
        self.pop_size_input.setMaximum(100000)
        


        self.population_config_layout.addWidget(QLabel("Precision(number of decimal places):"), 0, 0)
        self.population_config_layout.addWidget(self.precision_input, 1, 0)
        self.population_config_layout.addWidget(QLabel("Number of Epochs:"), 0, 1)
        self.population_config_layout.addWidget(self.epochs_input, 1, 1)
        self.population_config_layout.addWidget(QLabel("Population Size:"), 2, 0)
        self.population_config_layout.addWidget(self.pop_size_input, 3, 0)

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
        self.crossover_prob_input.show()
        self.crossover_prob_label.show()
        selected_type = self.crossover_type_combo.currentText()
        if selected_type == "One point crossover":
            self.crossover_param_input.hide()
            self.crossover_params_label.hide()
        elif selected_type == "Multi point crossover":
            self.crossover_param_input.setMinimum(1)
            self.crossover_param_input.setMaximum(99999)
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
            self.crossover_prob_input.hide()
            self.crossover_prob_label.hide()
    def on_mutation_type_change(self):
        self.mutation_params_label.show()
        self.mutation_param_input.show()
        self.mutation_prob_label.show()
        self.mutation_prob_input.show()
        selected_type = self.mutation_type_combo.currentText()
        if selected_type == "Bit flip mutation":
            self.mutation_params_label.setText("Chance of each bit flip fe.30%")
        elif selected_type=="Edge mutation":
            self.mutation_params_label.setText("Chance of each edge bit flip fe.30%")
        else:
            self.mutation_params_label.hide()
            self.mutation_param_input.hide()
            self.mutation_prob_label.hide()
            self.mutation_prob_input.hide()
    def algorithm_config_part(self):
        self.selection_type_combo = QComboBox()
        self.selection_type_combo.addItems(["Choose option..","Best selection", "Wheel of fortune selection", "Tournament selection"])
        self.selection_type_combo.currentIndexChanged.connect(self.on_selection_type_change)
        self.selection_params_label = QLabel("Params:")
        self.selection_param_input = QSpinBox()


        self.selection_layout = QGridLayout()
        self.selection_layout.addWidget(QLabel("Choose selection method:"),0,0)
        self.selection_layout.addWidget(self.selection_type_combo,1,0)
        self.selection_layout.addWidget(self.selection_params_label,0,1)
        self.selection_layout.addWidget(self.selection_param_input,1,1)
        self.selection_param_input.hide()
        self.selection_params_label.hide()
        self.algorithm_config_layout.addLayout(self.selection_layout)

        self.crossover_layout = QGridLayout()
        self.crossover_type_combo = QComboBox()
        self.crossover_type_combo.addItems(["Choose option..","One point crossover", "Multi point crossover", "Uniform crossover","Discrete crossover"])
        self.crossover_type_combo.currentIndexChanged.connect(self.on_crossover_type_change)
        self.crossover_prob_label = QLabel("Crossover Probability f.e 30%:")
        self.crossover_params_label = QLabel("Params:")
        self.crossover_param_input = QSpinBox()
        self.crossover_prob_input = QSpinBox()
        self.crossover_prob_input.setMinimum(1)
        self.crossover_prob_input.setMaximum(100)
        self.crossover_layout.addWidget(QLabel("Choose crossover method:"),0,0)
        self.crossover_layout.addWidget(self.crossover_type_combo,1,0)
        self.crossover_layout.addWidget(self.crossover_params_label,2,0)
        self.crossover_layout.addWidget(self.crossover_param_input,3,0)
        self.crossover_layout.addWidget(self.crossover_prob_label,0,1)
        self.crossover_layout.addWidget(self.crossover_prob_input,1,1)
        self.crossover_params_label.hide()
        self.crossover_param_input.hide()
        self.crossover_prob_input.hide()
        self.crossover_prob_label.hide()
        self.algorithm_config_layout.addLayout(self.crossover_layout)

        self.mutation_layout = QGridLayout()
        self.mutation_type_combo = QComboBox()
        self.mutation_type_combo.addItems(["Choose option..","Bit flip mutation", "Edge mutation"])
        self.mutation_type_combo.currentIndexChanged.connect(self.on_mutation_type_change)
        self.mutation_params_label = QLabel("Params:")
        self.mutation_param_input = QSpinBox()
        self.mutation_prob_label = QLabel("Mutation probability f.e 30%:")
        self.mutation_prob_input = QSpinBox()
        self.mutation_param_input.setMinimum(1)
        self.mutation_param_input.setMaximum(100)
        self.mutation_layout.addWidget(QLabel("Choose mutation method:"),0,0)
        self.mutation_layout.addWidget(self.mutation_type_combo,1,0)
        self.mutation_layout.addWidget(self.mutation_prob_label,0,1)
        self.mutation_layout.addWidget(self.mutation_prob_input,1,1)
        self.mutation_layout.addWidget(self.mutation_params_label,2,0)
        self.mutation_layout.addWidget(self.mutation_param_input,3,0)
        self.mutation_params_label.hide()
        self.mutation_param_input.hide()
        self.mutation_prob_label.hide()
        self.mutation_prob_input.hide()
        self.algorithm_config_layout.addLayout(self.mutation_layout)

        self.inversion_layout=QGridLayout()
        self.inversion_prob_label = QLabel("Inversion chance f.e. 30%:")
        self.inversion_prob_input = QSpinBox()
        self.inversion_prob_input.setMinimum(1)
        self.inversion_prob_input.setMaximum(100)
        self.inversion_param_Label = QLabel("Inversion chance for each gene f.e.30%")
        self.inversion_param_input = QSpinBox()
        self.inversion_param_input.setMinimum(1)
        self.inversion_param_input.setMaximum(100)
        self.inversion_layout.addWidget(self.inversion_prob_label,0,0)
        self.inversion_layout.addWidget(self.inversion_prob_input,1,0)
        self.inversion_layout.addWidget(self.inversion_param_Label,0,1)
        self.inversion_layout.addWidget(self.inversion_param_input,1,1)
        self.algorithm_config_layout.addLayout(self.inversion_layout)


        self.elitary_method_label = QLabel("Number of elitary chromosomes")
        self.elitary_method_input = QSpinBox()
        self.elitary_method_input.setMinimum(1)
        self.elitary_method_input.setMaximum(999)
        self.algorithm_config_layout.addWidget(self.elitary_method_label)
        self.algorithm_config_layout.addWidget(self.elitary_method_input)

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        left_layout = QVBoxLayout()
        
        self.func_config_layout = QGridLayout()
        self.func_config_group = QGroupBox("Function config")
        self.function_config_part()
        self.func_config_group.setLayout(self.func_config_layout)
        self.population_config_layout = QGridLayout()
        self.population_config_group = QGroupBox("Population config")
        self.population_config_part()
        self.population_config_group.setLayout(self.population_config_layout)
        self.algorithm_config_layout = QVBoxLayout()
        self.algorithm_config_part()
        left_layout.addWidget(self.func_config_group)
        left_layout.addWidget(self.population_config_group)
        left_layout.addLayout(self.algorithm_config_layout)

       
        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_algorithm)
        left_layout.addWidget(self.run_button)

        right_layout = QVBoxLayout()
        self.timer_label = QLabel()
        self.timer_label.setText("Czas: 0 s")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0,config.generations_num)
        self.plot1_button = QPushButton("Generate plot 1")
        self.plot2_button = QPushButton("Generate plot 2")
        right_layout.addWidget(self.timer_label)
        right_layout.addWidget(self.progress_bar)
        right_layout.addWidget(self.plot1_button)
        right_layout.addWidget(self.plot2_button)
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)        
        main_layout.addLayout(right_layout)
        central_widget.setLayout(main_layout)

 

    def set_config(self):
        if self.function_combo.currentText() == "Rastrigin":
            config.f = config.rastrigin
        else:
            config.f = config.rosenbrock
        config.num_variables = int(self.num_vars_input.text())
        config.min_value = self.min_value_input.value()
        config.max_value = self.max_value_input.value()
        config.maximize = self.maximize_checkbox.isChecked()

        precision = int(self.precision_input.text())
        config.precision = float(f"1e-{precision}")
        config.generations_num = int(self.epochs_input.text())
        config.population_size = int(self.pop_size_input.text())
        selection_method = self.selection_type_combo.currentText()
        
        if selection_method == "Best selection":
            config.selection_method = 1
            config.selection_percentage = float(self.selection_param_input.text())/100
        elif selection_method == "Wheel of fortune selection":
            config.selection_method = 2
            config.selection_percentage = float(self.selection_param_input.text())/100

        elif selection_method == "Tournament selection":
            config.selection_method = 3
            config.tournament_size = int(self.selection_param_input.text())
        else:
            print("select")
            return 0
    
        crossover_method = self.crossover_type_combo.currentText()
        config.crossover_chance = float(self.crossover_prob_input.text())/100
        if crossover_method == "One point crossover":
            config.crossover_method = 1
        elif crossover_method == "Multi point crossover":
            config.crossover_method = 2
            config.crossover_param = int(self.crossover_param_input.text())
        elif crossover_method == "Uniform crossover":
            config.crossover_method = 3
            config.crossover_param = float(self.crossover_param_input.text())/100
        elif crossover_method == "Discrete crossover":
            config.crossover_method = 4
            config.crossover_param = float(self.crossover_param_input.text())/100
        else:
            print("cross")
            return 0

        mutation_method = self.mutation_type_combo.currentText()
        config.mutation_chance = float(self.mutation_prob_input.text())/100
        config.mutation_param = float(self.mutation_param_input.text())/100
        if mutation_method == "Bit flip mutation":
            config.mutation_method =1
        elif mutation_method=="Edge mutation":
            config.mutation_method =2
        else:
            print("mutation")

            return 0
        
        config.inversion_chance = float(self.inversion_prob_input.text())/100
        config.inversion_param = float(self.inversion_param_input.text())/100
        config.elitary_num = int(self.elitary_method_input.text())
        config.ui_enabled = True
        return 1
    def run_algorithm(self):
        ga.window_instance = self
        
        if self.set_config() == 0:
            return
        self.progress_bar.setRange(0,config.generations_num)
        print(f"Running algorithm with: num_vars={config.num_variables},epochs={config.generations_num}, "
              f"pop_size={config.population_size}, crossover_prob={config.crossover_chance}, mutation_prob={config.mutation_chance}, maximize={config.maximize}")

        start_time = time.time()
        genetic_algorithm()
        end_time = time.time()
        elapsed_time = end_time - start_time
        self.timer_label.setText(f"Czas: {elapsed_time:.2f} s \n Top fitness:")
        self.plot1_button.clicked.connect(config.results.plot_fitness_mean_and_std)
        self.plot2_button.clicked.connect(config.results.plot_top_fitness)
        config.results.save_stats_to_file()
        
        