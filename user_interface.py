import PyQt6 as Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
import psycopg2
import design_user_interface

class SecondWindow(Qt.QtWidgets.QMainWindow, design_user_interface.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.connect_to_db()     # Подключение к базе данных

        regex1 = QRegularExpression('[A-Za-z0-9]+')
        regex2 = QRegularExpression(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        regex3 = QRegularExpression(r'^\+\d{11}$')
        regex4 = QRegularExpression(r'^[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)? [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$')
        validator1 = QRegularExpressionValidator(regex1)  # Валидатор англ. алф. и цифры
        validator2 = QRegularExpressionValidator(regex2)
        validator3 = QRegularExpressionValidator(regex3)
        validator4 = QRegularExpressionValidator(regex4)

        self.show_package()
        self.buttonEdit.clicked.connect(self.set_changes)

        self.boxName.setValidator(validator4)
        self.boxEmail.setValidator(validator2)
        self.boxPassword.setValidator(validator1)
        self.boxPhone.setValidator(validator3)


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


    def show_package(self):
        try:
            with open('data.txt', 'r') as file:
                data = file.read()
            cursor = self.connection.cursor()
            cursor.execute("SELECT a.barcode, a.contain, a.status, b.name, b.email, b.password, b.phone from pvz.package_rec a, pvz.users b where a.id = b.id and b.login like '" + str(data) + "'")
            rows = cursor.fetchall()
            self.label_B1.setText(str(rows[0][3]))
            self.boxName.setText(str(rows[0][3]))
            self.boxEmail.setText(str(rows[0][4]))
            self.boxPassword.setText(str(rows[0][5]))
            self.boxPhone.setText(str(rows[0][6]))

            count = 0

            self.scrollArea.setWidget(QWidget())
            scroll_widget = self.scrollArea.widget()
            scroll_layout = QVBoxLayout(scroll_widget)

            for row in rows:
                count += 1
                row_label1 = QLabel("Заказ " + str(row[0]), self)
                row_label2 = QLabel(str(row[1]), self)
                row_label3 = QLabel(str(row[2]), self)

                row_layout = QVBoxLayout()
                row_layout.addWidget(row_label1)
                row_layout.addWidget(row_label2)
                row_layout.addWidget(row_label3)

                row_widget = QWidget()
                row_widget.setLayout(row_layout)

                scroll_layout.addWidget(row_widget)

            self.label_B2.setText("Всего посылок: " + str(count))

        except Exception as e:
            self.label_A2.setText('')

    def set_changes(self):
        try:
            t = self.label_B1.text()
            a = self.boxName.text()
            b = self.boxEmail.text()
            c = self.boxPassword.text()
            d = self.boxPhone.text()

            cursor = self.connection.cursor()
            cursor.execute("UPDATE pvz.users SET name = '" + str(a) + "', email = '" + str(b) + "', password = '" + str(c) + "', phone = '" + str(d) + "' where users.name = '" + str(t) + "'")
            self.connection.commit()
            self.show_package()


        except Exception as e:
            self.label_A2.setText('')


    def open_first_window(self):
        from authorization import Authorization
        self.first_window = Authorization()
        self.first_window.show()
        self.close()



