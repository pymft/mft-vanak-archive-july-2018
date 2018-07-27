#!/usr/bin/python3                                                                                                                                            
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from mw import Ui_Dialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        print(dir(self))
        self.ui.setupUi(self)
        self.show()


    def keyPressEvent(self, e):
        print(e.key())



app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())




