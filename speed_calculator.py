import sys
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton,QComboBox
from datetime import datetime

class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Speed Calculator')
        grid =QGridLayout()
        #create widgets
        distance_label = QLabel("Distance :")
        self.distance_input = QLineEdit()
        time_label = QLabel("Time( hours) :")
        self.time_input = QLineEdit()
        # option_label = QLabel("Time( hours) :")
        self.unit_option = QComboBox()
        self.unit_option.addItems(['Metric(km)', 'Imperial(miles)'])
        

        calculate_button = QPushButton("Calculate Speed")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel("")

        #add widgets to grid
        grid.addWidget(distance_label,0,0)
        grid.addWidget(self.distance_input,0,1)
        grid.addWidget(self.unit_option,0,2)
        grid.addWidget(time_label,1,0)
        grid.addWidget(self.time_input,1,1)
        grid.addWidget(calculate_button,2,1)
        grid.addWidget(self.output_label,3,0,1,2)

        self.setLayout(grid)

    
    def calculate(self):
        distance = float(self.distance_input.text())
        time = float(self.time_input.text())
        # speed calculation
        speed = distance/time

        if self.unit_option.currentText() == 'Metric(km)':
            speed = round(speed,2)
            unit = 'kmph'
        if self.unit_option.currentText() == 'Imperial(miles)':
            speed = round(speed* 0.621371,2)
            unit = 'mph'
             

        self.output_label.setText(f" Average Speed :  {speed} { unit}" )
        


app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())