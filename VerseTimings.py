#!/usr/bin/env python

#############################################################################

import sys

from os import listdir, remove
from os.path import isfile, join
from PyQt5.QtCore import QCoreApplication, QFile, QFileInfo, QMetaObject, Qt, QRect, QTextCodec, QObject
from PyQt5.QtGui import (QFont, QFontDatabase, QFontInfo, QIcon, QKeySequence,
                         QPixmap, QTextBlockFormat, QTextCharFormat, QTextCursor,
                         QTextDocumentWriter, QTextListFormat)
from PyQt5.QtWidgets import (QAction, QActionGroup, QApplication, QColorDialog,
                             QComboBox, QDialog, QFileDialog, QFontComboBox, QMainWindow, QMenu, QMenuBar, QMessageBox,
                             QStatusBar, QTextEdit, QToolBar, QApplication, QMainWindow, QVBoxLayout, QWidget)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog

import dialog
import options
import project
import sys
import data

if sys.platform.startswith('darwin'):
    rsrcPath = ":/images/mac"
else:
    rsrcPath = ":/images/win"

dirty = False
proj = None
projectfiles = []

class Ui_MainWindow(QMainWindow):
    def __init__(self, MainWindow=None, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        MainWindow = self
#        self.setWindowIcon(QIcon(':/images/logo.png'))
#        MainWindow.setObjectName("MainWindow")
        wr = opt.windowRect.split(",");
        MainWindow.move(int(wr[0]), int(wr[1]))
        MainWindow.resize(int(wr[2]), int(wr[3]))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 731, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(10, 110, 731, 101))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 751, 20))
        self.menubar.setObjectName("menubar")

        self.menuFile = QMenu("File", self.menubar)
        self.menuFile.addAction("Import from BART binary", self.import_from_BART_binary)
        self.menuFile.addAction("Export as BART binary", self.export_as_BART_binary)
        self.menuFile.addAction("Export for Scripture App Builder", self.export_for_scripture_app_builder)
        self.menuFile.addAction("Exit", self.exit)

        self.menuProject = QMenu("Project", self.menubar)
        for f in projectfiles:
            self.menuProject.addAction(f, self.choose_project)
        self.menuProject.addSeparator()
        self.menuProject.addAction("New project", self.new_project)
        self.menuProject.addAction("Edit project", self.edit_project)
        self.menuProject.addAction("Delete project", self.delete_project)

        self.menuOT = QMenu("OT", self.menubar)
        self.menuNT = QMenu("NT", self.menubar)
        self.menuChap = QMenu("Chap", self.menubar)

        self.menuHelp = QMenu("Help", self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menuHelp = QMenu("Help", self)
        # helpMenu.addAction("Help", self.about)
        self.menuHelp.addAction("About", self.about)

        self.menuBar().addMenu(self.menuFile)
        self.menuBar().addMenu(self.menuProject)
        self.menuBar().addMenu(self.menuOT)
        self.menuBar().addMenu(self.menuNT)
        self.menuBar().addMenu(self.menuChap)
        self.menuBar().addMenu(self.menuHelp)

        MainWindow.setWindowTitle("VerseTimings")
        QMetaObject.connectSlotsByName(MainWindow)

    def choose_project(self):
        # print("Name=" + QObject.sender(self).text())
        proj.readProject(QObject.sender(self).text())

    def about(self):
        QMessageBox.about(self, "About",
                          "A tool to set synchronized verse timings for use in BART Bible and Scripture App Builder.")

    def import_from_BART_binary(self):
        QMessageBox.about(self, "Import",
                          "Not yet implemented.")

    def export_as_BART_binary(self):
        QMessageBox.about(self, "Export",
                          "Not yet implemented.")

    def export_for_scripture_app_builder(self):
        QMessageBox.about(self, "Export",
                          "Not yet implemented.")

    def exit(self):
        sys.exit(app.exec_())

    def new_project(self):
        try:
            dialogWindow = QDialog()
            proj.setupUi(dialogWindow, proj, True)
            result = dialogWindow.exec_()
        except Exception as detail:
            print("Exception: " + detail)

    def edit_project(self):
        try:
            dialogWindow = QDialog()
            proj.setupUi(dialogWindow, proj, False)
            result = dialogWindow.exec_()
        except Exception as detail:
            print("Exception: " + detail)

    def delete_project(self):
        # QMessageBox.about(self, "Delete project",
        #                   "Not yet implemented.")
        print("Deleting project " + proj.versionName)
        try:
            os.remove(proj.versionName + ".prj")
        except OSError:
            pass

    def closeEvent(self, event):
        try:
            if self.maybeSave(): # not cancel
                print("Exiting")
                sys.exit(None)
            else:
                event.ignore()
        except Exception as detail:
            print("Exception: " + detail)

    def resizeEvent(self, event):
        try:
            newSize = event.size();
            wr = opt.windowRect.split(",");
            opt.windowRect = "" + wr[0] + "," + wr[1] + "," + str(newSize.width()) + "," + str(newSize.height())
            opt.writeOptions();
        except Exception as detail:
            print("Exception: " + detail)

    def moveEvent(self, event):
        try:
            newPosn = event.pos()
            wr = opt.windowRect.split(",")
            opt.windowRect = "" + str(newPosn.x() - 9) + "," + str(newPosn.y() - 38) + "," + wr[2] + "," + wr[3];
            opt.writeOptions()
        except Exception as detail:
            print("Exception: " + detail)

    def maybeSave(self):
        if dirty:
            return False
        return True

    # def center_on_the_screen(self):
    #     ag = QDesktopWidget().availableGeometry()
    #     sg = QDesktopWidget().screenGeometry()
    #
    #     widget = self.geometry()
    #     x = ag.width() - widget.width()
    #     y = 2 * ag.height() - sg.height() - widget.height()
    #     self.move(x, y)

my_data = data.data
opt = options.options()
proj = project.project()
opt.readOptions(proj)
print("Project=" + opt.currentProject)
# print("WindowRect=" + opt.windowRect)
if opt.currentProject != "":
    # proj.readProject(opt.currentProject)
    # print("read project " + opt.currentProject)
    print("current ref=" + proj.currentBook + " " + str(proj.currentChapter))
# opt.writeOptions()
mypath = "."
projectfiles = [f[:len(f)-4] for f in listdir(mypath) if isfile(join(mypath, f)) and f.endswith(".prj")]
print(projectfiles)

app = QApplication(sys.argv)
mainWindow = Ui_MainWindow()
mainWindow.show()

sys.exit(app.exec_())
