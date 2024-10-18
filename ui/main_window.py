from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox, QGridLayout,QSpinBox,QComboBox
)
import sys
from qt_material import apply_stylesheet

class GeneticAlgorithmApp(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Genetic Algorithm Optimization")
        self.setGeometry(100, 100, 600, 400)
        apply_stylesheet(self,theme='dark_lightgreen.xml')
        # Wywołujemy metodę tworzącą elementy interfejsu
        self.initUI()

    def initUI(self):
        # Główny widget centralny, aby pomieścić inne elementy
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout główny
        main_layout = QVBoxLayout()

        # Layout dla ustawień algorytmu
        func_config_layout = QGridLayout()
        population_config_layout = QGridLayout()
        algorithm_config_layout = QVBoxLayout()
        
        # Pola wejściowe dla parametrów
        self.num_vars_input = QSpinBox()
        self.num_vars_input.setMinimum(1)
        self.num_vars_input.setMaximum(100)
        self.precision_input = QLineEdit()
        self.epochs_input = QSpinBox()
        self.epochs_input.setMinimum(10)
        self.epochs_input.setMaximum(10000)
        self.epochs_input.setSingleStep(10)
        self.pop_size_input = QSpinBox()
        self.epochs_input.setMinimum(1)
        self.epochs_input.setMaximum(10000)
        self.crossover_prob_input = QLineEdit()
        self.mutation_prob_input = QLineEdit()

        self.selection_type_combo = QComboBox()
        self.selection_type_combo.addItems(["Best selection", "Wheel of fortune selection", "Tournament selection"])

        self.params_label = QLabel("Parametry:")
        self.param_input = QSpinBox()
        
        self.selection_type_combo.currentIndexChanged.connect(self.on_selection_type_change)
        

        population_config_layout.addWidget(QLabel("Number of Variables:"), 0, 0)
        population_config_layout.addWidget(self.num_vars_input, 0, 1)
        
        population_config_layout.addWidget(QLabel("Precision:"), 1, 0)
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
        algorithm_config_layout.addWidget(self.params_label)
        algorithm_config_layout.addWidget(self.param_input)
        # Checkbox dla wyboru, czy maksymalizować funkcję
        self.maximize_checkbox = QCheckBox("Maximize")
        func_config_layout.addWidget(self.maximize_checkbox, 6, 0, 1, 2)

        # Dodaj layout konfiguracyjny do głównego layoutu
        main_layout.addLayout(func_config_layout)
        main_layout.addLayout(population_config_layout)
        main_layout.addLayout(algorithm_config_layout)

        # Przycisk do uruchomienia algorytmu
        self.run_button = QPushButton("Run Algorithm")
        self.run_button.clicked.connect(self.run_algorithm)
        main_layout.addWidget(self.run_button)

        # Miejsce na wykresy (placeholder)
        self.results_widget = QWidget()
        main_layout.addWidget(self.results_widget)

        # Ustaw główny layout dla centralnego widgetu
        central_widget.setLayout(main_layout)

    def on_selection_type_change(self):
        selected_type = self.selection_type_combo.currentText()
        
        # Dostosowanie etykiety i pola wejściowego w zależności od wybranej metody selekcji
        if selected_type == "Best selection":
            self.params_label.setText("Enter best percentage to select:")
            self.param_input.setMinimum(1)
            self.param_input.setMaximum(99)

        elif selected_type == "Wheel of fortune selection":
            self.params_label.setText("Enter best percentage to select:")
            self.param_input.setMinimum(1)
            self.param_input.setMaximum(99)
    

        elif selected_type == "Tournament selection":
            self.params_label.setText("Enter tournament size:")
            self.param_input.setMinimum(1)
            self.param_input.setMaximum(10000)
    def run_algorithm(self):
        # Pobieranie danych z formularzy
        num_vars = int(self.num_vars_input.text())
        precision = float(self.precision_input.text())
        epochs = int(self.epochs_input.text())
        pop_size = int(self.pop_size_input.text())
        crossover_prob = float(self.crossover_prob_input.text())
        mutation_prob = float(self.mutation_prob_input.text())
        maximize = self.maximize_checkbox.isChecked()

        # Wyświetl dane w konsoli (dla testów)
        print(f"Running algorithm with: num_vars={num_vars}, precision={precision}, epochs={epochs}, "
              f"pop_size={pop_size}, crossover_prob={crossover_prob}, mutation_prob={mutation_prob}, maximize={maximize}")

        # Tutaj można uruchomić algorytm genetyczny i wygenerować wykresy