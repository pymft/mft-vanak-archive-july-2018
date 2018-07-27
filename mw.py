from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
	self.widget = QtWidgets.QWidget(Dialog)
	self.widget.setGeometry(QtCore.QRect(30, 10, 251, 111))
        self.widget.setObjectName("widget")
        self.retranslateUi(Dialog)
	QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
	_translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))











