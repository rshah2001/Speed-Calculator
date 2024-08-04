import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, \
    QGridLayout, QPushButton


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Creating widgets
        distance_label = QLabel('Distance')
        self.distance_input = QLineEdit()

        time_label = QLabel("Time in Hours")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric(km)', 'Imperial(miles)'])

        calculator_button = QPushButton("Calculate")
        calculator_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculator_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())

        speed = distance/time

        if self.unit_combo.currentText() == "Metric(km)":
            speed = round(speed, 2)
            unit = "km/hr"

        if self.unit_combo.currentText() == "Imperial(miles)":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.result_label.setText(f"Average Speed is {speed} {unit}")


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())



