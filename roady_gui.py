# Form implementation generated from reading ui file '.\roady.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(737, 380)
        MainWindow.setFixedSize(700, 400)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.departure_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.departure_label.setGeometry(QtCore.QRect(10, 10, 101, 41))
        self.departure_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.departure_label.setObjectName("departure_label")
        self.departure_city_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.departure_city_lineEdit.setGeometry(QtCore.QRect(130, 10, 141, 41))
        self.departure_city_lineEdit.setObjectName("departure_city_lineEdit")
        self.departure_city_lineEdit.setStyleSheet("""
            QLineEdit {
                font: 12pt 'Arial';  /* Fontul textului */
                border: 2px solid #7A7A7A;  /* Bordura gri în jurul câmpului */
                border-radius: 5px;  /* Colțuri ușor rotunjite */
                padding: 5px;  /* Spațiu între text și marginea câmpului */
                background-color: #f0f0f0;  /* Culoare de fundal deschisă */
                color: #333333;  /* Culoare text întunecată */
            }

            QLineEdit:focus {
                border: 2px solid #4CAF50;  /* Culoare de bordură verde la focus */
                background-color: #ffffff;  /* Culoare de fundal albă la focus */
            }
        """)
        self.destination_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.destination_label.setGeometry(QtCore.QRect(400, 10, 121, 41))
        self.destination_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.destination_label.setObjectName("destination_label")
        self.destination_city_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.destination_city_lineEdit.setGeometry(QtCore.QRect(530, 10, 151, 41))
        self.destination_city_lineEdit.setObjectName("destination_city_lineEdit")
        self.with_return_radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.with_return_radioButton.setGeometry(QtCore.QRect(20, 70, 121, 41))
        self.with_return_radioButton.setStyleSheet("""
            QRadioButton {
                font: 10pt "MS Shell Dlg 2";
                background-color: #e0e0e0;
                border-radius: 5px;
                padding: 10px;
                color: #333;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                background-color: #ff6347;  /* Roșu de exemplu */
            }
            QRadioButton::indicator:checked {
                background-color: #32cd32;  /* Verde când este selectat */
            }
        """)
        self.with_return_radioButton.setObjectName("with_return_radioButton")
        self.currency_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.currency_comboBox.setGeometry(QtCore.QRect(160, 70, 71, 31))
        self.currency_comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.currency_comboBox.setObjectName("currency_comboBox")
        self.currency_comboBox.addItem("")
        self.currency_comboBox.addItem("")
        self.fuel_type_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.fuel_type_comboBox.setGeometry(QtCore.QRect(20, 140, 121, 31))
        self.fuel_type_comboBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.fuel_type_comboBox.setObjectName("fuel_type_comboBox")
        self.fuel_type_comboBox.addItem("")
        self.fuel_type_comboBox.addItem("")
        self.persons_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.persons_label.setGeometry(QtCore.QRect(20, 200, 121, 41))
        self.persons_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.persons_label.setObjectName("persons_label")
        self.number_of_persons_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.number_of_persons_lineEdit.setGeometry(QtCore.QRect(170, 200, 151, 41))
        self.number_of_persons_lineEdit.setObjectName("number_of_persons_lineEdit")
        self.number_of_persons_lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0; 
                border: 2px solid #888888;
                border-radius: 5px;
                padding: 5px;
                font: 14pt "Arial";
                color: #333;
            }
            QLineEdit:focus {
                border-color: #32cd32;  /* Verde când câmpul este selectat */
            }
        """)
        self.consumption_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.consumption_label.setGeometry(QtCore.QRect(20, 270, 121, 41))
        self.consumption_label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.consumption_label.setObjectName("consumption_label")
        self.consumption_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.consumption_lineEdit.setGeometry(QtCore.QRect(170, 270, 151, 41))
        self.consumption_lineEdit.setObjectName("consumption_lineEdit")
        self.consumption_lineEdit.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0; 
                border: 2px solid #888888;
                border-radius: 5px;
                padding: 5px;
                font: 14pt "Arial";
                color: #333;
            }
            QLineEdit:focus {
                border-color: #ff6347;  /* Roșu când câmpul este selectat */
            }
        """)
        self.calculate_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_btn.setGeometry(QtCore.QRect(510, 240, 171, 71))
        self.calculate_btn.setStyleSheet("""
            QPushButton {
                font: 14pt 'MS Shell Dlg 2'; 
                background-color: #4CAF50;  /* Culoare verde pentru fundal */
                color: white;  /* Culoare albă pentru text */
                border-radius: 10px;  /* Colțuri rotunjite */
                padding: 10px;  /* Margini interne */
                border: none;  /* Fără bordură */
            }

            QPushButton:hover {
                background-color: #45a049;  /* Culoare mai închisă la hover */
            }

            QPushButton:pressed {
                background-color: #388e3c;  /* Culoare și mai închisă la apăsare */
            }
        """)
        self.calculate_btn.setObjectName("calculate_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 737, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.departure_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Departure</p></body></html>"))
        self.destination_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Destination</p></body></html>"))
        self.with_return_radioButton.setText(_translate("MainWindow", "With/Return"))
        self.currency_comboBox.setItemText(0, _translate("MainWindow", "RON"))
        self.currency_comboBox.setItemText(1, _translate("MainWindow", "EURO"))
        self.fuel_type_comboBox.setItemText(0, _translate("MainWindow", "Gas"))
        self.fuel_type_comboBox.setItemText(1, _translate("MainWindow", "Diesel"))
        self.persons_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Persons</p></body></html>"))
        self.consumption_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Consumption</p></body></html>"))
        self.calculate_btn.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
