# Form implementation generated from reading ui file 'design_authorization.ui'
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
        self.label_A2.setGeometry(QtCore.QRect(410, 520, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_A2.setFont(font)
        self.label_A2.setWordWrap(True)
        self.label_A2.setObjectName("label_A2")
        self.buttonResultA = QtWidgets.QPushButton(parent=Form)
        self.buttonResultA.setGeometry(QtCore.QRect(350, 250, 181, 71))
        self.buttonResultA.setStyleSheet("QPushButton{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:10px;\n"
"border: 2px solid white;\n"
"color: white\n"
"}")
        self.buttonResultA.setObjectName("buttonResultA")
        self.boxA = QtWidgets.QLineEdit(parent=Form)
        self.boxA.setGeometry(QtCore.QRect(340, 80, 211, 51))
        self.boxA.setObjectName("boxA")
        self.boxB = QtWidgets.QLineEdit(parent=Form)
        self.boxB.setGeometry(QtCore.QRect(340, 160, 211, 51))
        self.boxB.setObjectName("boxB")
        self.label_A2_2 = QtWidgets.QLabel(parent=Form)
        self.label_A2_2.setGeometry(QtCore.QRect(410, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_A2_2.setFont(font)
        self.label_A2_2.setWordWrap(True)
        self.label_A2_2.setObjectName("label_A2_2")
        self.label_A2_3 = QtWidgets.QLabel(parent=Form)
        self.label_A2_3.setGeometry(QtCore.QRect(410, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_A2_3.setFont(font)
        self.label_A2_3.setWordWrap(True)
        self.label_A2_3.setObjectName("label_A2_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вход"))
        self.label_A2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:6pt;\">sys</span></p></body></html>"))
        self.buttonResultA.setText(_translate("Form", "Войти"))
        self.label_A2_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Логин</span></p></body></html>"))
        self.label_A2_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Пароль</span></p></body></html>"))
