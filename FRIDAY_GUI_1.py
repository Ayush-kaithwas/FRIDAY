

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FRIDAY(object):
    def setupUi(self, FRIDAY):
        FRIDAY.setObjectName("FRIDAY")
        FRIDAY.resize(1194, 643)
        self.centralwidget = QtWidgets.QWidget(FRIDAY)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-4, 0, 1201, 661))
        self.label.setStyleSheet("Background-Color:rgb(0, 170, 255)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Jarvis_gui/Background_2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:none;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 150, 521, 351))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Jarvis_gui/2RNb.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(880, 60, 291, 511))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Jarvis_gui/download.gif"))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 230, 221, 131))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Jarvis_gui/Frame_1.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 351, 181))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Jarvis_gui/NearEnlightenedBushbaby-size_restricted.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(60, 280, 181, 41))
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:black;\n"
"border:none;\n"
"font-size:24px;\n"
"text-align:center;\n"
"text-decoration:bold;")
        self.textBrowser.setObjectName("textBrowser")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 350, 231, 131))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Jarvis_gui/Frame_1.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 400, 191, 41))
        self.textBrowser_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:black;\n"
"border:none;\n"
"text-align:center;\n"
"font-size:22px;\n"
"text-decoration:bold;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 470, 231, 131))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Jarvis_gui/Frame_1.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 520, 191, 41))
        self.textBrowser_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:black;\n"
"border:none;\n"
"font-size:22px;\n"
"text-decoration:bold;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(530, 310, 161, 51))
        self.textBrowser_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"border:none;\n"
"background-color:black;\n"
"text-align:center;\n"
"font-size:20px;\n"
"text-decoration:bold;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label.raise_()
        self.label_7.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.textBrowser.raise_()
        self.label_5.raise_()
        self.textBrowser_2.raise_()
        self.label_6.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        FRIDAY.setCentralWidget(self.centralwidget)

        self.retranslateUi(FRIDAY)
        QtCore.QMetaObject.connectSlotsByName(FRIDAY)

    def retranslateUi(self, FRIDAY):
        _translate = QtCore.QCoreApplication.translate
        FRIDAY.setWindowTitle(_translate("FRIDAY", "F-R-I-D-A-Y"))
        FRIDAY.setWindowIcon(QtGui.QIcon('Jarvis_gui/favicon.png'))
        self.pushButton.setText(_translate("FRIDAY", "INITIATE"))
        self.textBrowser.setHtml(_translate("FRIDAY", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("FRIDAY", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("FRIDAY", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("FRIDAY", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FRIDAY = QtWidgets.QMainWindow()
    ui = Ui_FRIDAY()
    ui.setupUi(FRIDAY)
    FRIDAY.show()
    sys.exit(app.exec_())
