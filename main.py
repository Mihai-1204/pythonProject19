import sys
from PyQt6 import QtWidgets
from tkinter import messagebox
from utils.gas import Gas
from utils.init_config import config
from utils.distance import Distance
from roady import Roady
from roady_gui import Ui_MainWindow
import logging


LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s- %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%Y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])





def is_input_checked():
    if ui.departure_city_lineEdit.text() and ui.destination_city_lineEdit.text():
        departure_city = ui.departure_city_lineEdit.text().capitalize()
        destination_city = ui.destination_city_lineEdit.text().capitalize()
        ui.destination_city_lineEdit.setText(destination_city)
        ui.departure_city_lineEdit.setText(departure_city)
        if ui.number_of_persons_lineEdit.text() and ui.consumption_lineEdit.text():
            if ui.number_of_persons_lineEdit.text().isnumeric() and ui.consumption_lineEdit.text().isnumeric():
                return True
            else:
                messagebox.showerror(title="Error", message="Please input numbers for persons and consumption.")
                LOGGER.error("Please input numbers for persons and consumption.")
                return False
        else:
            messagebox.showerror(title="Please add number of persons and consumption.")
            LOGGER.error("Please add number of persons and consumption.")
            return False
    else:
        messagebox.showerror(title="Please enter cities.")
        LOGGER.error("Please enter cities.")
        return False


def calculate_price():
    if is_input_checked():
        dist = Distance(departure_city=ui.departure_city_lineEdit.text(),
                        destination_city=ui.destination_city_lineEdit.text(),
                        config=config)

        if ui.fuel_type_comboBox.show() == "Gas":
            gas_price = Gas(config)
        else:
            # TODO create diesel class which inherits Fuel
            pass

        roady = Roady(dist, gas_price)
        price = roady.calculate_price(int(ui.number_of_persons_lineEdit.text()),
                                      float(ui.consumption_lineEdit.text()),
                                      ui.with_return_radioButton.isChecked(),
                                      ui.currency_comboBox.currentText())

        messagebox.showinfo(title="Pretul calculat", message=f"Fiecare persoana are de platit{int(price)}")
        LOGGER.info(f"Fiecare persoana are de platit{int(price)}")





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.calculate_btn.clicked.connect(calculate_price)
    MainWindow.show()
    sys.exit(app.exec())

