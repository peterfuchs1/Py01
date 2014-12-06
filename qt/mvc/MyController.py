__author__ = 'uhs374h'
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qt.mvc import MyView


FIRST, LAST, PREVIOUS, NEXT = range(4)

class Controller(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.current = 0
        self.myForm = MyView.Ui_Form()
        self.myForm.setupUi(self)
        self.myButtons = {
            self.myForm.pButton0: 0,
            self.myForm.pButton1: 1,
            self.myForm.pButton2: 2,
            self.myForm.pButton3: 3,
            self.myForm.pButton4: 4,
            self.myForm.pButton5: 5,
            self.myForm.pButton6: 6,
            self.myForm.pButton7: 7,
            self.myForm.pButton8: 8,
            self.myForm.pButton9: 9,
            self.myForm.pButton10: 10,
            self.myForm.pButton11: 11,
            self.myForm.pButton12: 12,
            self.myForm.pButton13: 13,
            self.myForm.pButton14: 14
        }
        self.myForm.pButton0.clicked.connect(lambda: self.navigate(self.myForm.pButton0))
        self.myForm.pButton1.clicked.connect(lambda: self.navigate(self.myForm.pButton1))
        self.myForm.pButton2.clicked.connect(lambda: self.navigate(self.myForm.pButton2))
        self.myForm.pButton3.clicked.connect(lambda: self.navigate(self.myForm.pButton3))
        self.myForm.pButton4.clicked.connect(lambda: self.navigate(self.myForm.pButton4))
        self.myForm.pButton5.clicked.connect(lambda: self.navigate(self.myForm.pButton5))
        self.myForm.pButton6.clicked.connect(lambda: self.navigate(self.myForm.pButton6))
        self.myForm.pButton7.clicked.connect(lambda: self.navigate(self.myForm.pButton7))
        self.myForm.pButton8.clicked.connect(lambda: self.navigate(self.myForm.pButton8))
        self.myForm.pButton9.clicked.connect(lambda: self.navigate(self.myForm.pButton9))
        self.myForm.pButton10.clicked.connect(lambda: self.navigate(self.myForm.pButton10))
        self.myForm.pButton11.clicked.connect(lambda: self.navigate(self.myForm.pButton11))
        self.myForm.pButton12.clicked.connect(lambda: self.navigate(self.myForm.pButton12))
        self.myForm.pButton13.clicked.connect(lambda: self.navigate(self.myForm.pButton13))
        self.myForm.pButton14.clicked.connect(lambda: self.navigate(self.myForm.pButton14))

        self.myForm.pOk.clicked.connect(self.start)
        self.myForm.pCancel.clicked.connect(QCoreApplication.instance().quit)
        self.start()
        #self.connectButtons()

    def start(self):
        self.initiate()
        print("start")
        self.setButtonsEnabled()

    def connectButtons(self):
        for button in self.myButtons.keys():
            z = lambda: self.navigate(button)
            button.clicked.connect(z)

    def initiate(self):

        """ initiate all to begin a new game

        """
        buttons = set()
        for button in self.myButtons.keys():
            buttons.add(button)

        listAll = [x for x in buttons]

        z = 0
        for actual in listAll:
            actual.setText(str(z))
            z += 1

        self.current = 0

    def navigate(self, key):
        value = int(key.text())
        print("key: %s value %s" %(key, value))
        if self.current == int(value):
            key.setEnabled(False)
            self.current += 1


    def setButtonsEnabled(self):

        for button in self.myButtons.keys():
            button.setEnabled(True)
        self.current = 0





if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())

