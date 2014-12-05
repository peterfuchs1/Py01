#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'uhs374h'
import sys
from PyQt5 import QtGui, uic

class MyWindow(QtGui.QWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('mywindow.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())