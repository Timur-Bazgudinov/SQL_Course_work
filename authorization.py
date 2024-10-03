import sys
import PyQt6 as Qt
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import psycopg2
import design_authorization
from user_interface import SecondWindow


class Authorization(design_authorization.Ui_Form, Qt.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.connect_to_db() #Подключение к базе данных

        regex = QRegularExpression('[A-Za-z0-9]+')
        validator = QRegularExpressionValidator(regex)  #Валидатор англ. алф. и цифры

        self.boxA.setValidator(validator)
        self.boxB.setValidator(validator)
        self.buttonResultA.clicked.connect(self.entrance)


    def connect_to_db(self):    #Подключение к бд
        try:
            self.connection = psycopg2.connect(
                dbname='test',
                user='postgres',
                password='67Gitiba',
                host='127.0.0.1',

            )
            self.query_data()
        except Exception as e:
            self.label_A2.setText('')


    def entrance(self):     #Поиск пользователя по базе
        log = str(self.boxA.text())
        pas = str(self.boxB.text())


        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT login FROM pvz.users where login like '" + str(log) + "'")
            resulog = cursor.fetchall()[0]
            resulogf = resulog[0]
        except Exception as e:
            resulogf = "52FriendlyThug"

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT password FROM pvz.users where password like '" + str(pas) + "'")
            resupas = cursor.fetchall()[0]
            resupasf = resupas[0]
        except Exception as e:
            resupasf = "52FriendlyThug"

        if log == resulogf and pas == resupasf:
            with open('data.txt', 'w') as file:
                file.write(resulogf)
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
