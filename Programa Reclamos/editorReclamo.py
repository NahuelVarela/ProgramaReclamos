# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editorReclamo.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(369, 375)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 220, 341, 121))
        self.textEdit.setObjectName("textEdit")
        self.botonGuardar = QtWidgets.QPushButton(Dialog)
        self.botonGuardar.setGeometry(QtCore.QRect(280, 350, 75, 23))
        self.botonGuardar.setObjectName("botonGuardar")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(90, 160, 271, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 271, 20))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 271, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 70, 271, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 90, 17))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 100, 271, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 130, 261, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3.setBuddy(self.lineEdit_3)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_4.setBuddy(self.comboBox)
        self.label_5.setBuddy(self.comboBox_2)
        self.label_6.setBuddy(self.lineEdit_4)
        self.label_7.setBuddy(self.textEdit)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Direccion:"))
        self.label_2.setText(_translate("Dialog", "Nombre:"))
        self.botonGuardar.setText(_translate("Dialog", "Guardar"))
        self.label_4.setText(_translate("Dialog", "Estado:"))
        self.label_5.setText(_translate("Dialog", "Devolucion:"))
        self.label_6.setText(_translate("Dialog", "DNI"))
        self.comboBox.setItemText(0, _translate("Dialog", "Buscando Remplazo"))
        self.comboBox.setItemText(1, _translate("Dialog", "Esperando Devolucion"))
        self.comboBox.setItemText(2, _translate("Dialog", "Esperando Pago Diferencia"))
        self.comboBox.setItemText(3, _translate("Dialog", "Enviado"))
        self.comboBox.setItemText(4, _translate("Dialog", "Solucionado"))
        self.label_7.setText(_translate("Dialog", "Nota:"))
        self.label.setText(_translate("Dialog", "Venta:"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "No"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Si"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "Terminal"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "OCA"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "C.A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

