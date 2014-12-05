# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'printHello.ui'
#
# Created: Fri Dec  5 11:02:56 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

class Ui_Form(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 359)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bPrintHello = QPushButton(Form)
        self.bPrintHello.setObjectName("bPrintHello")
        self.verticalLayout.addWidget(self.bPrintHello)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Super Hello"))
        self.bPrintHello.setText(_translate("Form", "Print Hello"))
        self.bPrintHello.clicked.connect(self.printHello)

    def printHello(self):
        print ("Hello!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())
