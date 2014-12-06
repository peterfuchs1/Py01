__author__ = 'uhs374h'
import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtSql
from . import MyView
#import Model

FIRST, LAST, PREVIOUS, NEXT = range(4)

class Controller(QtWidgets.QDialog):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.current=0;
        self.myDlg = MyView.Ui_Dialog()
        self.myDlg.setupUi(self)
        self.myButtons = {
            self.myDlg.pButton0: 0,
            self.myDlg.pButton1: 1,
            self.myDlg.pButton2: 2,
            self.myDlg.pButton3: 3,
            self.myDlg.pButton4: 4,
            self.myDlg.pButton5: 5,
            self.myDlg.pButton6: 6,
            self.myDlg.pButton7: 7,
            self.myDlg.pButton8: 8,
            self.myDlg.pButton9: 9,
            self.myDlg.pButton10: 10,
            self.myDlg.pButton11: 11,
            self.myDlg.pButton12: 12,
            self.myDlg.pButton13: 13,
            self.myDlg.pButton14: 14
        }
        self.connectButtons()
        """
        self.dbModel = Model.DBModel("mydb", "localhost", "root", "", "person")

        # create a model that reads from "Person" table in db "MyDB"
        self.tblRowCount = self.dbModel.modelRowCount

        self.modelRowCount = self.dbModel.getModelRowCount()
        """
        # map the dlg fields to the db fields
        self.mapper = QtWidgets.QDataWidgetMapper(self)
        self.mapper.setSubmitPolicy(QtWidgets.QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.dbModel.model)
        self.mapper.addMapping(self.myDlg.lineEdit, 0)
        self.mapper.addMapping(self.myDlg.lineEdit_2, 1)
        self.mapper.addMapping(self.myDlg.lineEdit_3, 2)
        self.mapper.toFirst()

        self.setButtonsEnabled()

    def connectButtons(self):
        for buttons in self.myButtons.keys():
            buttons.clicked.connect(lambda: self.navigate(self.myButtons[buttons]))

    def initiate(self):

        """ initiate all to begin a new game

        """
        buttons = set()
        for button in self.myButtons.keys():
            buttons.add(button)
        listAll = [x for x in buttons]
        # Alle Buttons entfernt
        for button in self.myButtons.keys():
            self.myDlg.gridLayout_2.removeWidget(button)

        count = len(self.myButtons.keys())
        columns = 3
        rows = count / 5
        z = 0
        for i in range(rows):
            for j in range(columns):
                actual = listAll[z]
                self.myButtons[actual] = z
                self.myDlg.gridLayout_2.addWidget(actual, i, j)
                z += 1


    def navigate(self, value):

        clicked=self


        self.setButtonsEnabled()

    def setButtonsEnabled(self):
        intCurrentIndex = self.mapper.currentIndex()

        if self.modelRowCount == 1:
            self.myDlg.pbPrevious.setEnabled(False)
            self.myDlg.pbNext.setEnabled(False)
            self.myDlg.pbLast.setEnabled(False)
            self.myDlg.pbFirst.setEnabled(False)
        if intCurrentIndex == 0:
            self.myDlg.pbPrevious.setEnabled(False)
            self.myDlg.pbNext.setEnabled(True)
            self.myDlg.pbLast.setEnabled(True)
            self.myDlg.pbFirst.setEnabled(False)
        elif intCurrentIndex == self.modelRowCount - 1:
            self.myDlg.pbPrevious.setEnabled(True)
            self.myDlg.pbNext.setEnabled(False)
            self.myDlg.pbLast.setEnabled(False)
            self.myDlg.pbFirst.setEnabled(True)
        else:
            self.myDlg.pbPrevious.setEnabled(True)
            self.myDlg.pbNext.setEnabled(True)
            self.myDlg.pbLast.setEnabled(True)
            self.myDlg.pbFirst.setEnabled(True)

    def quit(self):
        self.mapper.submit()
        QtWidgets.QDialog.accept(self.myDlg)

    def addRecord(self):
        self.mapper.submit()
        self.dbModel.insertRow()
        self.mapper.setCurrentIndex(self.modelRowCount + 1)

        self.modelRowCount += 1
        self.myDlg.lineEdit.setText(str(self.modelRowCount + 1))
        self.myDlg.lineEdit_2.setText("")
        self.myDlg.lineEdit_3.setText("")
        self.setButtonsEnabled()

        self.myDlg.lineEdit_2.setFocus()

        self.dbModel.getMaxId()

    def deleteRecord(self):
        intCrntRow = self.mapper.currentIndex()

        if QtWidgets.QMessageBox.question(self, "Confirmation", """Are you sure you want to delete             the person
            {0} {1} ?""".format(self.lineEdit_2.text(), self.lineEdit_3.text())) == QtWidgets.QMessageBox.No:
           return

        self.dbModel.deleteRowByIndex(intCrntRow)

        if intCrntRow - 1 < 0:
            intCrntRow += 1
        else:
            intCrntRow -= 1

        self.mapper.setCurrentIndex(intCrntRow)

        self.setButtonsEnabled()

    def openId(self):
        self.dbModel.getDataForId(7)
        self.mapper.toFirst()