# Form implementation generated from reading ui file 'design_user_interface.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1000, 740)
        Form.setMinimumSize(QtCore.QSize(1000, 740))
        Form.setMaximumSize(QtCore.QSize(1000, 740))
        self.label_A2 = QtWidgets.QLabel(parent=Form)
        self.label_A2.setGeometry(QtCore.QRect(820, 610, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_A2.setFont(font)
        self.label_A2.setWordWrap(True)
        self.label_A2.setObjectName("label_A2")
        self.buttonEdit = QtWidgets.QPushButton(parent=Form)
        self.buttonEdit.setGeometry(QtCore.QRect(500, 560, 181, 71))
        self.buttonEdit.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:10px;\n"
"border: 2px solid white;\n"
"color: white\n"
"}")
        self.buttonEdit.setObjectName("buttonEdit")
        self.boxName = QtWidgets.QLineEdit(parent=Form)
        self.boxName.setGeometry(QtCore.QRect(30, 620, 211, 51))
        self.boxName.setObjectName("boxName")
        self.label_A1 = QtWidgets.QLabel(parent=Form)
        self.label_A1.setGeometry(QtCore.QRect(460, 50, 91, 21))
        self.label_A1.setObjectName("label_A1")
        self.label_B1 = QtWidgets.QLabel(parent=Form)
        self.label_B1.setGeometry(QtCore.QRect(730, 30, 231, 31))
        self.label_B1.setObjectName("label_B1")
        self.label_A3 = QtWidgets.QLabel(parent=Form)
        self.label_A3.setGeometry(QtCore.QRect(400, 420, 221, 31))
        self.label_A3.setObjectName("label_A3")
        self.label_B2 = QtWidgets.QLabel(parent=Form)
        self.label_B2.setGeometry(QtCore.QRect(120, 40, 271, 31))
        self.label_B2.setObjectName("label_B2")
        self.boxEmail = QtWidgets.QLineEdit(parent=Form)
        self.boxEmail.setGeometry(QtCore.QRect(30, 520, 211, 51))
        self.boxEmail.setObjectName("boxEmail")
        self.label_C2 = QtWidgets.QLabel(parent=Form)
        self.label_C2.setGeometry(QtCore.QRect(40, 580, 61, 31))
        self.label_C2.setObjectName("label_C2")
        self.label_C3 = QtWidgets.QLabel(parent=Form)
        self.label_C3.setGeometry(QtCore.QRect(280, 480, 71, 31))
        self.label_C3.setObjectName("label_C3")
        self.label_C4 = QtWidgets.QLabel(parent=Form)
        self.label_C4.setGeometry(QtCore.QRect(280, 580, 81, 31))
        self.label_C4.setObjectName("label_C4")
        self.scrollArea = QtWidgets.QScrollArea(parent=Form)
        self.scrollArea.setGeometry(QtCore.QRect(110, 80, 791, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 789, 319))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.boxPhone = QtWidgets.QLineEdit(parent=Form)
        self.boxPhone.setGeometry(QtCore.QRect(270, 620, 201, 51))
        self.boxPhone.setObjectName("boxPhone")
        self.boxPassword = QtWidgets.QLineEdit(parent=Form)
        self.boxPassword.setGeometry(QtCore.QRect(270, 520, 201, 51))
        self.boxPassword.setObjectName("boxPassword")
        self.label_C1 = QtWidgets.QLabel(parent=Form)
        self.label_C1.setGeometry(QtCore.QRect(40, 480, 71, 31))
        self.label_C1.setObjectName("label_C1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Личный кабинет"))
        self.label_A2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">sys</span></p></body></html>"))
        self.buttonEdit.setText(_translate("Form", "Сохранить изменения"))
        self.label_A1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Заказы</span></p></body></html>"))
        self.label_B1.setText(_translate("Form", "<html><head/><body><p align=\"right\"><br/></p></body></html>"))
        self.label_A3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Редактировать данные</span></p></body></html>"))
        self.label_B2.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label_C2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">ФИО</span></p></body></html>"))
        self.label_C3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Пароль</span></p></body></html>"))
        self.label_C4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Телефон</span></p></body></html>"))
        self.label_C1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Email</span></p></body></html>"))
