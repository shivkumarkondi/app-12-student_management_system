import sys
from PyQt6.QtWidgets import QApplication \
,QLabel,QWidget,QGridLayout,QLineEdit,QPushButton,\
    QComboBox,QMainWindow,QTableWidget,QTableWidgetItem \
    ,QDialog,QVBoxLayout
from PyQt6.QtGui import QAction
from datetime import datetime
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        file_menu_item = self.menuBar().addMenu('&File')
        help_menu_item = self.menuBar().addMenu('&Help')

        add_student_action = QAction("Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
    

    def load_data(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.execute("select * from students")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        connection.close()

    def insert(self):
        dialog  = InsertDialog()
        dialog.exec()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()
        #add student Widget
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name ")
        layout.addWidget(self.student_name)

        #add combo box for courses
        self.course_name = QComboBox()
        courses = ['Biology','Math','Geology', 'Physics']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        #add mobile Widget
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile ")
        layout.addWidget(self.mobile)

        #submit button
        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)

        self.setLayout(layout)
    
    def add_student(self):
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students(name,course,mobile) values (?,?,?)",
                       (name,course,mobile))  
        connection.commit()
        cursor.close()
        connection.close()
        sms.load_data()


app = QApplication(sys.argv)
sms = MainWindow()
sms.show()
sms.load_data()
sys.exit(app.exec())