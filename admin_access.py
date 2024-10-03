import sys
import PyQt6 as Qt
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import psycopg2
import design_admin_access
from admin_interface import SecondWindow


class Authorization(design_admin_access.Ui_Form, Qt.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        regex = QRegularExpression('[A-Za-z0-9]+')
        validator = QRegularExpressionValidator(regex)  #Валидатор англ. алф. и цифры

        self.boxA.setValidator(validator)
        self.boxB.setValidator(validator)
        self.buttonResultA.clicked.connect(self.entrance)


    def entrance(self):     #Поиск пользователя по базе
        log = str(self.boxA.text())
        pas = str(self.boxB.text())

        if log == "admin" and pas == "admin123":
            self.go_to_lk()
        else:
            QMessageBox.about(self, "Ошибка", "Неправильно введен логин или пароль!")



    def go_to_lk(self):      #Открытие окна с интерфейсом пользователя
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()



if __name__ == '__main__':
    app = Qt.QtWidgets.QApplication(sys.argv)
    aut = Authorization()
    aut.show()
    sys.exit(app.exec())

