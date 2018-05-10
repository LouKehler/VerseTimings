# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import dialog2

class Ui_Dialog(object):
    def setupUi(self, dialog):
        self.dialog = dialog
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.textEdit.setFontFamily("Jameel Noori Nastaleeq")
        self.textEdit.setFontPointSize(36)
        self.textEdit.setText("میں کراچی جانا چاہتا ہُوں۔")

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def accept(self):
        self.textEdit.setFontFamily("Awami Nastaliq")
        self.textEdit.setFontPointSize(36)
        self.textEdit.setText("میں کراچی جانا چاہتا ہُوں۔")

        dialogWindow = QtWidgets.QDialog()
        window = dialog2.Ui_Dialog()
        window.setupUi(dialogWindow)
        result = dialogWindow.exec_()
        # QtWidgets.QMessageBox.about(self.dialog, "Title", "accept")
        # self.dialog.close()

    def reject(self):
        # QtWidgets.QMessageBox.about(self.dialog, "Title", "reject")
        self.dialog.close()

    def setText(self, msg):
        self.textEdit.setText(msg)
