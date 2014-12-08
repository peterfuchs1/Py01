"""
Created on 07.12.2014

@author: uhs374h
"""
__author__ = 'uhs374h'
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qt.mvc import MyView, MyModel
from random import shuffle


class MyController(QWidget):
    """ MVC pattern: Creates a controller with the mvc pattern.

    """
    def __init__(self, parent=None):
        """ Create a new controller with a MyView object
        using the MVC pattern

        :param parent:
        :return: None
        """
        super().__init__(parent)
        self.current = 0
        self.myForm = MyView.Ui_Form()
        self.myForm.setupUi(self)

        # collect all buttons in a list
        self.liste = [
            self.myForm.pButton0,
            self.myForm.pButton1,
            self.myForm.pButton2,
            self.myForm.pButton3,
            self.myForm.pButton4,
            self.myForm.pButton5,
            self.myForm.pButton6,
            self.myForm.pButton7,
            self.myForm.pButton8,
            self.myForm.pButton9,
            self.myForm.pButton10,
            self.myForm.pButton11,
            self.myForm.pButton12,
            self.myForm.pButton13,
            self.myForm.pButton14
        ]

        self.myModel = MyModel.MyModel(len(self.liste))

        # connect the buttons with the clicked signal
        self.connectButtons()
        # start a new game
        self.start()

    def start(self):
        """ Start a new game

        :return: None
        """
        self.initiate()
        self.myForm.lGames.setText(self.myModel.gamesStr())
        self.setButtonsEnabled()

    def closeGUI(self):
        """ The active QWidget will be closed

        :return: None
        """
        self.close()
    @staticmethod
    def closeApplication():
        """ The whole application will be closed

        :return: None
        """
        QCoreApplication.instance().quit()

    def connectButtons(self):
        """ Connect the clicked signal with the buttons

        :return: None
        """
        for b in self.liste:
            b.clicked.connect(self.buttonClicked)

        self.myForm.pNew.clicked.connect(self.start)
        # the designer creates the code!
        # self.myForm.pExit.clicked.connect(self.closeGUI)

    def writeLabel(self):
        """ print the text of the sender into a label only once
        :return: None
        """
        b = self.sender()
        self.myForm.label.setText(b.text())
        b.clicked.disconnect(self.writeLabel)

    def initiate(self):
        """ initiate all to begin a new game

        :return: None
        """
        self.myModel.newGame()
        # create a new sequence
        shuffle(self.liste)
        # update the text of the buttons
        z = 0
        for actual in self.liste:
            actual.setText(str(z))
            z += 1
        self.current = 0
        self.printScores()

    def buttonClicked(self):
        """ evaluate the clicked PushButton

        :raise TypeError: If the sender is not a instance of QPushButton
        :return: None
        """
        button = self.sender()
        if isinstance(button, QPushButton):
            value = int(button.text())
        else:
            raise TypeError('QPushButton expected, but '+type(button)+' was given')
        if self.current == int(value):
            button.setEnabled(False)
            self.myModel.correctClick()
            self.current += 1
        else:
            self.myModel.wrongClick()

        self.printScores()
        # print a MessagesBox for the winner
        if self.myModel.open == 0:
            q = QMessageBox()
            q.setWindowTitle("Gewonnen")
            q.setText("<b><center>Gratulation!<center></b>")
            q.setTextFormat(Qt.RichText)
            q.setInformativeText("Du hast die Lösung in %s Schritten gefunden." % self.myModel.sumStr())
            q.exec()

    def printScores(self):
        """ print the current Scores

        :return: None
        """
        _model = self.myModel
        self.myForm.lCorrect.setText(_model.correctStr())
        self.myForm.lOPen.setText(_model.openStr())
        self.myForm.lWrong.setText(_model.wrongStr())
        self.myForm.lSum.setText(_model.sumStr())
        self.myForm.lGames.setText(_model.gamesStr())


    def setButtonsEnabled(self):
        """ Enables all Buttons

        :return: None
        """
        for button in self.liste:
            button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = MyController()
    c.show()
    sys.exit(app.exec_())

