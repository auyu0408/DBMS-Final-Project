# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 588)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 490, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(220, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(220, 130, 271, 121))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 130, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(220, 280, 271, 191))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "查詢"))
        self.comboBox.setItemText(0, _translate("Form", "SELECT-FROM-WHERE"))
        self.comboBox.setItemText(1, _translate("Form", "DELETE"))
        self.comboBox.setItemText(2, _translate("Form", "INSERT"))
        self.comboBox.setItemText(3, _translate("Form", "UPDATE"))
        self.comboBox.setItemText(4, _translate("Form", "IN"))
        self.comboBox.setItemText(5, _translate("Form", "NOT IN"))
        self.comboBox.setItemText(6, _translate("Form", "EXISTS"))
        self.comboBox.setItemText(7, _translate("Form", "NOT EXISTS"))
        self.comboBox.setItemText(8, _translate("Form", "COUNT"))
        self.comboBox.setItemText(9, _translate("Form", "SUM"))
        self.comboBox.setItemText(10, _translate("Form", "MAX"))
        self.comboBox.setItemText(11, _translate("Form", "MIN"))
        self.comboBox.setItemText(12, _translate("Form", "AVG"))
        self.comboBox.setItemText(13, _translate("Form", "HAVING"))
        self.comboBox.setItemText(14, _translate("Form", "MySQL"))
        self.label.setText(_translate("Form", "查詢關鍵字"))
        self.label_2.setText(_translate("Form", "查詢工具"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
