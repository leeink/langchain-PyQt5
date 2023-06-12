# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Practice\Personal\Python venvs\llmBackend\PyQt\pj.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from llms import *


class Ui_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(MainWindow)
        self.summarizer = summarizer()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 608)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QTabsWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.QTabsWidget.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.QTabsWidget.setObjectName("QTabsWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Summary1 = QtWidgets.QPushButton(self.tab)
        self.Summary1.setGeometry(QtCore.QRect(350, 510, 75, 23))
        self.Summary1.setObjectName("Summary1")
        self.Summary1.clicked.connect(self.summaryDoc)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(430, 80, 321, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SummarizedTxtField = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.SummarizedTxtField.setEnabled(True)
        self.SummarizedTxtField.setReadOnly(True)
        self.SummarizedTxtField.setObjectName("SummarizedTxtField")
        self.verticalLayout_3.addWidget(self.SummarizedTxtField)
        self.OpenFile1 = QtWidgets.QPushButton(self.tab)
        self.OpenFile1.setGeometry(QtCore.QRect(570, 480, 75, 23))
        self.OpenFile1.setObjectName("OpenFile1")
        self.OpenFile1.clicked.connect(self.openFile)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 321, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RawFIleField = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.RawFIleField.setEnabled(True)
        self.RawFIleField.setReadOnly(True)
        self.RawFIleField.setObjectName("RawFIleField")
        self.verticalLayout.addWidget(self.RawFIleField)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(310, 10, 151, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 480, 321, 22))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(160, 60, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(560, 60, 71, 16))
        self.label_3.setObjectName("label_3")
        self.QTabsWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(310, 30, 151, 31))
        self.label_4.setObjectName("label_4")
        self.SummarizedPdfField = QtWidgets.QTextEdit(self.tab_2)
        self.SummarizedPdfField.setEnabled(True)
        self.SummarizedPdfField.setGeometry(QtCore.QRect(230, 70, 319, 391))
        self.SummarizedPdfField.setReadOnly(True)
        self.SummarizedPdfField.setObjectName("SummarizedPdfField")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 480, 319, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.OpenFile2 = QtWidgets.QPushButton(self.tab_2)
        self.OpenFile2.setGeometry(QtCore.QRect(560, 480, 75, 23))
        self.OpenFile2.setObjectName("OpenFile2")
        self.OpenFile2.clicked.connect(self.openFile2)
        self.Summary2 = QtWidgets.QPushButton(self.tab_2)
        self.Summary2.setGeometry(QtCore.QRect(360, 510, 75, 23))
        self.Summary2.setObjectName("Summary2")
        self.Summary2.clicked.connect(self.summaryPdf)
        self.QTabsWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(280, 30, 201, 31))
        self.label_5.setObjectName("label_5")
        self.SummarizedMPdfField = QtWidgets.QTextEdit(self.tab_3)
        self.SummarizedMPdfField.setEnabled(True)
        self.SummarizedMPdfField.setGeometry(QtCore.QRect(230, 70, 319, 391))
        self.SummarizedMPdfField.setReadOnly(True)
        self.SummarizedMPdfField.setObjectName("SummarizedMPdfField")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 480, 319, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.OpenFolder3 = QtWidgets.QPushButton(self.tab_3)
        self.OpenFolder3.setGeometry(QtCore.QRect(560, 480, 75, 23))
        self.OpenFolder3.setObjectName("OpenFolder3")
        self.OpenFolder3.clicked.connect(self.openFolder3)
        self.Summary3 = QtWidgets.QPushButton(self.tab_3)
        self.Summary3.setGeometry(QtCore.QRect(350, 510, 75, 23))
        self.Summary3.setObjectName("Summary3")
        self.Summary3.clicked.connect(self.summaryMPdf)
        self.QTabsWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(280, 30, 201, 31))
        self.label_6.setObjectName("label_6")
        self.PdfQueryAnswerField = QtWidgets.QTextEdit(self.tab_4)
        self.PdfQueryAnswerField.setEnabled(True)
        self.PdfQueryAnswerField.setGeometry(QtCore.QRect(50, 70, 319, 351))
        self.PdfQueryAnswerField.setReadOnly(True)
        self.PdfQueryAnswerField.setObjectName("PdfQueryAnswerField")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 470, 319, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.OpenFolder4 = QtWidgets.QPushButton(self.tab_4)
        self.OpenFolder4.setGeometry(QtCore.QRect(560, 470, 75, 23))
        self.OpenFolder4.setObjectName("OpenFolder4")
        self.OpenFolder4.clicked.connect(self.openFolder4)
        self.QueryInputField = QtWidgets.QTextEdit(self.tab_4)
        self.QueryInputField.setEnabled(True)
        self.QueryInputField.setGeometry(QtCore.QRect(420, 110, 319, 111))
        self.QueryInputField.setReadOnly(False)
        self.QueryInputField.setObjectName("QueryInputField")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(550, 70, 41, 31))
        self.label_7.setObjectName("label_7")
        self.QueryButton = QtWidgets.QPushButton(self.tab_4)
        self.QueryButton.setGeometry(QtCore.QRect(540, 240, 75, 23))
        self.QueryButton.setObjectName("QueryButton")
        self.QueryButton.clicked.connect(self.pdfQuery)
        self.QTabsWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.QTabsWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Summary1.setText(_translate("MainWindow", "Summary"))
        self.SummarizedTxtField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OpenFile1.setText(_translate("MainWindow", "Open File"))
        self.RawFIleField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Summary TXT Document"))
        self.label_2.setText(_translate("MainWindow", "Raw File"))
        self.label_3.setText(_translate("MainWindow", "Summarized"))
        self.QTabsWidget.setTabText(self.QTabsWidget.indexOf(self.tab), _translate("MainWindow", "txt"))
        self.label_4.setText(_translate("MainWindow", "Summary PDF Document"))
        self.SummarizedPdfField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OpenFile2.setText(_translate("MainWindow", "Open File"))
        self.Summary2.setText(_translate("MainWindow", "Summary"))
        self.QTabsWidget.setTabText(self.QTabsWidget.indexOf(self.tab_2), _translate("MainWindow", "pdf"))
        self.label_5.setText(_translate("MainWindow", "Summary Multiple PDF Document"))
        self.SummarizedMPdfField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OpenFolder3.setText(_translate("MainWindow", "Open Folder"))
        self.Summary3.setText(_translate("MainWindow", "Summary"))
        self.QTabsWidget.setTabText(self.QTabsWidget.indexOf(self.tab_3), _translate("MainWindow", "pdfs"))
        self.label_6.setText(_translate("MainWindow", "Multiple PDF Document Query"))
        self.PdfQueryAnswerField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OpenFolder4.setText(_translate("MainWindow", "Open Folder"))
        self.QueryInputField.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "Query"))
        self.QueryButton.setText(_translate("MainWindow", "Query Enter"))
        self.QTabsWidget.setTabText(self.QTabsWidget.indexOf(self.tab_4), _translate("MainWindow", "pdfs query"))


    #callback function for PushButton

    ## Open File or Folder
    def openFile(self) -> None:
        fname=QFileDialog.getOpenFileName(self)
        self.lineEdit.setText(fname[0])
        f=open(fname[0],'r',encoding='UTF-8')
        with f:
            data=f.read()
            self.RawFIleField.setText(data)

    def openFile2(self) -> None:
        fname=QFileDialog.getOpenFileName(self)
        self.lineEdit_2.setText(fname[0])
        f=open(fname[0],'r',encoding='UTF-8')

    def openFolder3(self) -> None:
        fname=QFileDialog.getExistingDirectory(self,"Select Directory")
        self.lineEdit_3.setText(fname)
        
    def openFolder4(self) -> None:
        fname=QFileDialog.getExistingDirectory(self,"Select Directory")
        self.lineEdit_4.setText(fname)

    ## File Summary
    def summaryDoc(self) -> None:
        text = self.RawFIleField.toPlainText()
        res = self.summarizer.summary(text)
        self.SummarizedTxtField.setText(res)

    def summaryPdf(self) -> None:
        path = self.lineEdit_2.text()
        res = self.summarizer.summaryPdf(path)
        self.SummarizedPdfField.setText(res[0])

    def summaryMPdf(self) -> None:
        summary = ""
        path = self.lineEdit_3.text()
        res = self.summarizer.summarize_pdfs_from_folder(path)
        for i in res:
            summary += i
        self.SummarizedMPdfField.setText(summary)

    ## Query
    def pdfQuery(self) -> None:
        query = self.QueryInputField.toPlainText()
        path = self.lineEdit_4.text()
        res = self.summarizer.QueryPdfs_fromFolder(path, query)
        self.PdfQueryAnswerField.setText(res)

# Main Structure
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
