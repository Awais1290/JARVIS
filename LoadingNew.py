# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadingNew.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadingNew(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1352, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, -30, 1371, 791))
        self.textBrowser.setStyleSheet("background-color: rgb(16, 15, 14);")
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 30, 821, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Downloads/ForsakenImpoliteIaerismetalmark-size_restricted.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(250, 550, 961, 261))
        self.textBrowser_2.setStyleSheet("background-color: rgb(16, 15, 14);\n"
"border:transparent;\n"
"font: 75 16pt \"Nirmala UI\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1160, 510, 161, 71))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"background-color: rgb(0, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1160, 590, 161, 71))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Nirmala UI\";\n"
"background-color: rgb(255, 0, 4);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nirmala UI\'; font-size:16pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:72pt; color:#ffaa00;\">Loading Please Wait</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Start Loading"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit Loading"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoadingNew()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
