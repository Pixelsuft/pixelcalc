from clear_cache import clear as clear_cache
from PyQt5 import QtWidgets as qt_widgets
from pixelcalc import Ui_MainWindow as ui_mainwindow
from sys import exit as return_and_exit
from random import choice as reand_pick


def add_num(num_to_add):
    full = ui.resultText.text()
    if full == '' or full == 'Idiot!':
        full = str(num_to_add)
    elif full == 'Error Cyka Blyat!' or full == '0':
        full = str(num_to_add)
    else:
        if str(num_to_add) == 'clear':
            full = full[:-1]
        else:
            full += str(num_to_add)
    ui.resultText.setText(full)


def calc_result():
    str_to_calc = ui.resultText.text()
    result = None
    try:
        result = str(eval(str_to_calc))
    except (ZeroDivisionError, NameError, SyntaxError):
        result = reand_pick(['Error Cyka Blyat!', 'Idiot!'])
    ui.resultText.setText(result)


def attack_clicks():
    ui.num0.clicked.connect(lambda: add_num(0))
    ui.num1.clicked.connect(lambda: add_num(1))
    ui.num2.clicked.connect(lambda: add_num(2))
    ui.num3.clicked.connect(lambda: add_num(3))
    ui.num4.clicked.connect(lambda: add_num(4))
    ui.num5.clicked.connect(lambda: add_num(5))
    ui.num6.clicked.connect(lambda: add_num(6))
    ui.num7.clicked.connect(lambda: add_num(7))
    ui.num8.clicked.connect(lambda: add_num(8))
    ui.num9.clicked.connect(lambda: add_num(9))
    ui.plus.clicked.connect(lambda: add_num('+'))
    ui.minus.clicked.connect(lambda: add_num('-'))
    ui.umnoz.clicked.connect(lambda: add_num('*'))
    ui.razdel.clicked.connect(lambda: add_num('/'))
    ui.clear.clicked.connect(lambda: add_num('clear'))
    ui.calculate.clicked.connect(calc_result)


if __name__ == "__main__":
    app = qt_widgets.QApplication([__name__])
    MainWindow = qt_widgets.QMainWindow()
    ui = ui_mainwindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    attack_clicks()
    code_to_return = app.exec_()
    clear_cache()
    return_and_exit(code_to_return)
