#!/usr/bin/python3                                                                                                                                            
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt

from form import Ui_Dialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()

        self.ui.setupUi(self)
        self.show()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Down:
            self.ui.down()
        else:
            print(e.key())
    #


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())




