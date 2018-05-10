# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 357)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 310, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 381, 61))
        self.groupBox.setObjectName("groupBox")
        self.lineEditProjectName = QtWidgets.QLineEdit(self.groupBox)
        self.lineEditProjectName.setGeometry(QtCore.QRect(10, 30, 361, 23))
        self.lineEditProjectName.setObjectName("lineEditProjectName")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 60, 381, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBoxProjectType = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxProjectType.setGeometry(QtCore.QRect(10, 30, 361, 23))
        self.comboBoxProjectType.setObjectName("comboBoxProjectType")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 381, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEditSourcePath = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEditSourcePath.setGeometry(QtCore.QRect(10, 30, 271, 23))
        self.lineEditSourcePath.setObjectName("lineEditSourcePath")
        self.pushButtonBrowseSource = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButtonBrowseSource.setGeometry(QtCore.QRect(290, 30, 80, 23))
        self.pushButtonBrowseSource.setObjectName("pushButtonBrowseSource")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 180, 381, 61))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButtonBrowseSource_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtonBrowseSource_2.setGeometry(QtCore.QRect(290, 30, 80, 23))
        self.pushButtonBrowseSource_2.setObjectName("pushButtonBrowseSource_2")
        self.lineEditAudioFilesPath = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEditAudioFilesPath.setGeometry(QtCore.QRect(10, 30, 271, 23))
        self.lineEditAudioFilesPath.setObjectName("lineEditAudioFilesPath")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 240, 381, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBoxFont = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBoxFont.setGeometry(QtCore.QRect(10, 30, 271, 23))
        self.comboBoxFont.setObjectName("comboBoxFont")
        self.lineEditFontSize = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEditFontSize.setGeometry(QtCore.QRect(290, 30, 81, 23))
        self.lineEditFontSize.setObjectName("lineEditFontSize")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Project name"))
        self.groupBox_2.setTitle(_translate("Dialog", "Type"))
        self.groupBox_3.setTitle(_translate("Dialog", "Source"))
        self.pushButtonBrowseSource.setText(_translate("Dialog", "Browse..."))
        self.groupBox_4.setTitle(_translate("Dialog", "Audio files folder"))
        self.pushButtonBrowseSource_2.setText(_translate("Dialog", "Browse..."))
        self.groupBox_5.setTitle(_translate("Dialog", "Font"))

