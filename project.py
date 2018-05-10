#!/usr/bin/env python

#############################################################################

import sys
import re

from PyQt5.QtCore import QCoreApplication, QFile, QFileInfo, QRect, Qt, QTextCodec, QMetaObject

from PyQt5.QtWidgets import (QDialogButtonBox, QGroupBox, QLineEdit, QComboBox, QFontComboBox,
                             QPushButton, QFileDialog)

import data

if sys.platform.startswith('darwin'):
    rsrcPath = ":/images/mac"
else:
    rsrcPath = ":/images/win"#    public static void readOptions() {

class project :
    versionName = ""
    paratextFolder = ""
    audioFolderName = ""
    textFont = ""
    textSize = 0
    fileType = ""
    bBook = False
    currentBook = 1
    currentChapter = 1

    def project(self):
        pass

    def readProject(self, currentProject):
        try:
            print("Reading project " + currentProject)
            refMatcher = re.compile("^CurrentReference=([^ ]+) (\\d+)$")
            for line in open(currentProject + '.prj'):
                line = line.strip()
                mtch = refMatcher.match(line)
                if mtch:
                    self.currentBook = mtch.group(1)
                    # bk = mtch.group(1)
                    # for i, b in enumerate(data.data.book):
                    #    if b.equals(bk):
                    #         self.currentBook = i
                    #         break
                    self.currentChapter = mtch.group(2)
                elif line.startswith("VersionName="):
                    self.versionName = line[len("VersionName="):]
                elif line.startswith("ParatextFolder="):
                    self.paratextFolder = line[len("ParatextFolder="):]
                elif line.startswith("SoundFolder="):
                    self.audioFolderName = line[len("SoundFolder="):]
                elif line.startswith("AudioFolder="):
                    self.audioFolderName = line[len("AudioFolder="):]
                elif line.startswith("Font="):
                    self.textFont = line[len("Font="):]
                elif line.startswith("FontSize="):
                    self.textSize = int(line[len("FontSize=")])
                elif line.startswith("FileType="):
                    self.fileType = line[len("FileType="):]
                    self.bBook = self.fileType == "Book";
                else:
                    print("Unknown project option: ", line)
        except FileNotFoundError:
            print("Failed to open project file")
            self.writeProject(currentProject)
            pass
        except Exception as detail:
            print("Exception reading project file: ", detail)
            pass


    def writeProject(self, currentProject):
        print("Writing project file")
        try :
            fh = open(currentProject + ".prj", "w+")
            fh.write("CurrentReference==" + data.book[self.currentBook] + " " + str(self.currentChapter) + "\n")
            fh.write("VersionName=" + self.versionName + "\n")
            fh.write("ParatextFolder=" + self.paratextFolder + "\n")
            fh.write("AudioFolder=" + self.audioFolderName + "\n")
            fh.write("Font=" + self.textFont + "\n")
            fh.write("FontSize=" + str(self.textSize) + "\n")
            fh.write("FileType=" + self.fileType + "\n")
            fh.close()
        except Exception as detail:
            print("IOException writing project file: ", detail)
            pass

# class Ui_Dialog(object):
    def setupUi(self, Dialog, proj, newProject):
        try:
            self.dialog = Dialog
            self.proj = proj
            Dialog.setObjectName("Dialog")
            Dialog.resize(400, 357)
            self.buttonBox = QDialogButtonBox(Dialog)
            self.buttonBox.setGeometry(QRect(30, 310, 341, 32))
            self.buttonBox.setOrientation(Qt.Horizontal)
            self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")
            self.groupBox = QGroupBox(Dialog)
            self.groupBox.setGeometry(QRect(10, 0, 381, 61))
            self.groupBox.setObjectName("groupBox")
            self.lineEditProjectName = QLineEdit(self.groupBox)
            self.lineEditProjectName.setGeometry(QRect(10, 30, 361, 23))
            self.lineEditProjectName.setObjectName("lineEditProjectName")
            self.groupBox_2 = QGroupBox(Dialog)
            self.groupBox_2.setGeometry(QRect(10, 60, 381, 61))
            self.groupBox_2.setObjectName("groupBox_2")
            self.comboBoxProjectType = QComboBox(self.groupBox_2)
            self.comboBoxProjectType.setGeometry(QRect(10, 30, 361, 23))
            self.comboBoxProjectType.setObjectName("comboBoxProjectType")
            self.groupBox_3 = QGroupBox(Dialog)
            self.groupBox_3.setGeometry(QRect(10, 120, 381, 61))
            self.groupBox_3.setObjectName("groupBox_3")
            self.lineEditSourcePath = QLineEdit(self.groupBox_3)
            self.lineEditSourcePath.setGeometry(QRect(10, 30, 271, 23))
            self.lineEditSourcePath.setObjectName("lineEditSourcePath")
            self.pushButtonBrowseSource = QPushButton(self.groupBox_3)
            self.pushButtonBrowseSource.setGeometry(QRect(290, 30, 80, 23))
            self.pushButtonBrowseSource.setObjectName("pushButtonBrowseSource")
            self.groupBox_4 = QGroupBox(Dialog)
            self.groupBox_4.setGeometry(QRect(10, 180, 381, 61))
            self.groupBox_4.setObjectName("groupBox_4")
            self.pushButtonBrowseAudio = QPushButton(self.groupBox_4)
            self.pushButtonBrowseAudio.setGeometry(QRect(290, 30, 80, 23))
            self.pushButtonBrowseAudio.setObjectName("pushButtonBrowseAudio")
            self.lineEditAudioFilesPath = QLineEdit(self.groupBox_4)
            self.lineEditAudioFilesPath.setGeometry(QRect(10, 30, 271, 23))
            self.lineEditAudioFilesPath.setObjectName("lineEditAudioFilesPath")
            self.groupBox_5 = QGroupBox(Dialog)
            self.groupBox_5.setGeometry(QRect(10, 240, 381, 61))
            self.groupBox_5.setObjectName("groupBox_5")
            self.comboBoxFont = QFontComboBox(self.groupBox_5)
            self.comboBoxFont.setGeometry(QRect(10, 30, 271, 23))
            self.comboBoxFont.setObjectName("comboBoxFont")
            self.lineEditFontSize = QLineEdit(self.groupBox_5)
            self.lineEditFontSize.setGeometry(QRect(290, 30, 81, 23))
            self.lineEditFontSize.setObjectName("lineEditFontSize")
            
            # set up fields
            if newProject:
                self.versionName = ""
                self.paratextFolder = "c:\\My Paratext 8 Projects"
                self.textFont = "Times New Roman"
                self.textSize = 25
                self.fileType = "Paratext"

            typeList = ("Paratext", "Book", "BART")
            # self.comboBoxProjectType.clear()
            for index, i in enumerate(typeList):
                self.comboBoxProjectType.addItem(i)
            index = self.comboBoxProjectType.findText(self.fileType, Qt.MatchFixedString)
            if index >= 0:
                self.comboBoxProjectType.setCurrentIndex(index)
            self.lineEditProjectName.setText(self.versionName)
            self.lineEditSourcePath.setText(self.paratextFolder)
            self.lineEditAudioFilesPathPath.setText(self.audioFolderName)
            index = self.comboBoxFont.findText(self.textFont, Qt.MatchFixedString)
            if index >= 0:
                self.comboBoxFont.setCurrentIndex(index)
            self.lineEditFontSize.setText(str(self.textSize))

            self.retranslateUi(Dialog)
            self.pushButtonBrowseSource.clicked.connect(self.browse_source)
            self.pushButtonBrowseAudio.clicked.connect(self.browse_audio_path)
            self.lineEditProjectName.textChanged.connect(self.lineEditProjectName_changed)
            self.comboBoxProjectType.currentTextChanged.connect(self.comboBoxProjectType_changed)
            self.buttonBox.accepted.connect(Dialog.accept)
            self.buttonBox.rejected.connect(Dialog.reject)
            QMetaObject.connectSlotsByName(Dialog)
        except Exception as detail:
            print("Exception: " + detail)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Project name"))
        self.groupBox_2.setTitle(_translate("Dialog", "Type"))
        self.groupBox_3.setTitle(_translate("Dialog", "Source"))
        self.pushButtonBrowseSource.setText(_translate("Dialog", "Browse..."))
        self.groupBox_4.setTitle(_translate("Dialog", "Audio files folder"))
        self.pushButtonBrowseAudio.setText(_translate("Dialog", "Browse..."))
        self.groupBox_5.setTitle(_translate("Dialog", "Font"))

    def accept(self):
        self.writeProject(self.versionName)
        print("OK")

    def reject(self):
        print("Cancel")

    def comboBoxProjectType_changed(self):
        self.fileType = self.comboBoxProjectType.currentText()
        # print("Changing project type to " + self.fileType)
        self.bBook = True
        if self.fileType == "Paratext":
            self.paratextFolder = "c:\\Paratext\\My Paratext 8 Projects\\" + self.lineEditProjectName.text()
            self.bBook = False
        elif self.fileType == "Book":
            self.paratextFolder = ""
        else:
            self.paratextFolder = ""
        self.lineEditSourcePath.setText(self.paratextFolder)

    def lineEditProjectName_changed(self):
        self.comboBoxProjectType_changed()
        self.lineEditSourcePath.setText(self.paratextFolder)

    def comboBoxFont_changed(self):
        self.textFont = self.comboBoxFont.currentText()

    def browse_source(self):
        try:
            my_dir = QFileDialog.getExistingDirectory(
                self.dialog,
                "Open a folder",
                self.paratextFolder,
                QFileDialog.ShowDirsOnly)
            if my_dir:
                self.paratextFolder = my_dir
            self.lineEditSourcePath.setText(self.paratextFolder)
        # except TypeError as detail:
        #     print (detail)
        except Exception:
            print("Failed choose Paratext folder: ") # + detail)

    def browse_audio_path(self):
        try:
            my_dir = QFileDialog.getExistingDirectory(
                self.dialog,
                "Open a folder",
                self.audioFolderName,
                QFileDialog.ShowDirsOnly)
            if my_dir:
                self.audioFolderName = my_dir
            self.lineEditAudioFilesPath.setText(self.audioFolderName)
        # except TypeError as detail:
        #     print (detail)
        except Exception:
            print("Failed choose audio folder: ") # + detail)
