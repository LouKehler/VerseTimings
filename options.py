#!/usr/bin/env python

#############################################################################

import sys

from PyQt5.QtCore import QFile, QFileInfo, Qt, QTextCodec

import project


if sys.platform.startswith('darwin'):
    rsrcPath = ":/images/mac"
else:
    rsrcPath = ":/images/win"#    public static void readOptions() {

class options:

    currentProject = ""
    windowRect = "0,0,50,100"

    # def options(self):
    #     readOptions()

    def readOptions(self, proj):
        try:
            print("Reading options")
            for line in open('VerseTimings.opt'):
                line = line.strip()
                if line.startswith("CurrentProject=") :
                    self.currentProject = line[len("CurrentProject="):]
                    if self.currentProject != "":
                        # proj = project.project()
                        proj.readProject(self.currentProject)
                elif line.startswith("WindowRect="):
                    self.windowRect = line[len("WindowRect="):]
            else:
                self.writeOptions()
        except Exception as detail:
            print("Exception reading options file: ", detail)
            pass
        except FileNotFoundError:
            print("Failed to open options file")
            pass


    def writeOptions(self):
        # print("Writing options file")
        try :
            fh = open("VerseTimings.opt", "w+")
            fh.write("CurrentProject=" + self.currentProject + "\n")
            fh.write("WindowRect=" + self.windowRect + "\n")
            fh.close()
        except Exception as detail:
            print("IOException writing options file: ", detail)
            pass
