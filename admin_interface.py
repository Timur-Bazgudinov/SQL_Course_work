import PyQt6 as Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator, QIntValidator
import psycopg2
import design_admin_interface

class SecondWindow(Qt.QtWidgets.QMainWindow, design_admin_interface.Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.connect_to_db()     # Подключение к базе данных

        regex1 = QRegularExpression('[A-Za-z0-9]+')
        regex2 = QRegularExpression(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        regex3 = QRegularExpression(r'^\+\d{11}$')
        regex4 = QRegularExpression(r'^[А-ЯЁ][а-яё]+(-[А-ЯЁ][а-яё]+)? [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+$')
        regex5 = QRegularExpression('[0-9]+')
        validator1 = QRegularExpressionValidator(regex1)  # Валидатор англ. алф. и цифры
        validator2 = QRegularExpressionValidator(regex2)
        validator3 = QRegularExpressionValidator(regex3)
        validator4 = QRegularExpressionValidator(regex4)
        validator5 = QIntValidator(1, 20100, self)
        validator6 = QIntValidator(1, 150, self)
        validator7 = QRegularExpressionValidator(regex5)

        self.boxID.setValidator(validator5)
        self.boxLogin.setValidator(validator1)
        self.boxPassword.setValidator(validator1)
        self.boxEmail.setValidator(validator2)
        self.boxPhone.setValidator(validator3)
        self.boxAge.setValidator(validator6)
        self.boxName.setValidator(validator4)
        self.boxBarCode.setValidator(validator7)
        self.boxIdPac.setValidator(validator5)
        self.boxWeight.setValidator(validator5)

        self.show_package()
        self.show_users()
        self.buttonEditUs.clicked.connect(self.set_changes_us)
        self.buttonEditPac.clicked.connect(self.set_changes_pac)
        self.buttonDelUs.clicked.connect(self.del_us)
        self.buttonDelPac.clicked.connect(self.del_pac)
        self.buttonAddUs.clicked.connect(self.add_us)
        self.buttonAddPac.clicked.connect(self.add_pac)





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
            cursor = self.connection.cursor()
            cursor.execute("SELECT * From pvz.package_rec")
            rows = cursor.fetchall()

            count = 0

            self.scrollArea.setWidget(QWidget())
            scroll_widget = self.scrollArea.widget()
            scroll_layout = QVBoxLayout(scroll_widget)

            for row in rows:
                count += 1
                row_label1 = QLabel("Заказ " + str(row), self)

                row_layout = QVBoxLayout()
                row_layout.addWidget(row_label1)

                row_widget = QWidget()
                row_widget.setLayout(row_layout)

                scroll_layout.addWidget(row_widget)

            self.label_A3.setText("Всего посылок: " + str(count))

        except Exception as e:
            self.label_A2.setText('')

    def show_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * From pvz.users")
            rows = cursor.fetchall()

            count = 0

            self.scrollArea2.setWidget(QWidget())
            scroll_widget = self.scrollArea2.widget()
            scroll_layout = QVBoxLayout(scroll_widget)

            for row in rows:
                count += 1
                row_label1 = QLabel(str(row), self)

                row_layout = QVBoxLayout()
                row_layout.addWidget(row_label1)

                row_widget = QWidget()
                row_widget.setLayout(row_layout)

                scroll_layout.addWidget(row_widget)

            self.label_A4.setText("Всего пользователей: " + str(count))

        except Exception as e:
            self.label_A2.setText('')

    def set_changes_us(self):
        try:
            a = self.boxID.text()
            b = self.boxLogin.text()
            c = self.boxPassword.text()
            d = self.boxEmail.text()
            e = self.boxPhone.text()
            f = self.boxAge.text()
            g = self.boxName.text()

            cursor = self.connection.cursor()
            cursor.execute("UPDATE pvz.users SET login = '" + str(b) + "', password = '" + str(c) + "', email = '" + str(d) + "', phone = '" + str(e) + "',age = '" + str(f) + "', name = '" + str(g) + "' where users.id = '" + str(a) + "'")
            self.connection.commit()
            self.show_users()

        except Exception as e:
            self.label_A2.setText('')

    def set_changes_pac(self):
        try:
            a = self.boxBarCode.text()
            b = self.boxIdPac.text()
            c = self.boxCont.text()
            d = self.boxStatus.text()
            e = self.boxWeight.text()


            cursor = self.connection.cursor()
            cursor.execute(
                "UPDATE pvz.package_rec SET id = '" + str(b) + "', contain = '" + str(c) + "', status = '" + str(d) + "', weight = '" + str(e) + "' where package_rec.barcode = '" + str(a) + "'")
            self.connection.commit()
            self.show_package()

        except Exception as e:
            self.label_A2.setText('')


    def del_us(self):
        try:
            a = self.boxID.text()

            cursor = self.connection.cursor()
            cursor.execute(
                "DELETE FROM pvz.users WHERE users.id = " + str(a))
            self.connection.commit()
            self.show_users()

        except Exception as e:
            self.label_A2.setText('')


    def del_pac(self):
        try:
            a = self.boxBarCode.text()

            cursor = self.connection.cursor()
            cursor.execute(
                "DELETE FROM pvz.package_rec WHERE barcode = " + str(a))
            self.connection.commit()
            self.show_package()

        except Exception as e:
            self.label_A2.setText('')


    def add_us(self):
        try:
            a = self.boxID.text()
            b = self.boxLogin.text()
            c = self.boxPassword.text()
            d = self.boxEmail.text()
            e = self.boxPhone.text()
            f = self.boxAge.text()
            g = self.boxName.text()

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO pvz.users VALUES (" + str(a) + ", '" + str(b) + "', '" + str(c) + "', '" + str(d) + "', '" + str(e) + "', " + str(f) + ", '" + str(g) + "')")
            self.connection.commit()
            self.show_users()

        except Exception as e:
            self.label_A2.setText('')


    def add_pac(self):
        try:
            a = self.boxBarCode.text()
            b = self.boxIdPac.text()
            c = self.boxCont.text()
            d = self.boxStatus.text()
            e = self.boxWeight.text()

            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO pvz.package_rec VALUES (" + str(a) + ", " + str(b) + ", '" + str(c) + "', '" + str(d) + "', '" + str(e) + "')")
            self.connection.commit()
            self.show_package()

        except Exception as e:
            self.label_A2.setText('')


    def open_first_window(self):
        from admin_access import Authorization
        self.first_window = Authorization()
        self.first_window.show()
        self.close()
