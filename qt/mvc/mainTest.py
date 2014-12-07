__author__ = 'uhs374h'

from qt.mvc.MyController import MyController
import sys
from PyQt5.QtWidgets import *
if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())

