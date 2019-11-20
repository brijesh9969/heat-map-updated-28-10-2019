# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PC_6\Desktop\heatmap\final working heat map\report_file.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import intfinalspatial as fs
import sys as s

class Ui_Form1(object):
    def setupUi1(self, Form1):
        Form1.setObjectName("Form")
        Form1.resize(551, 289)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form1.setFont(font)
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form1)
        self.label_2.setGeometry(QtCore.QRect(280, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.left_leg = QtWidgets.QPushButton(Form1)
        self.left_leg.setGeometry(QtCore.QRect(120, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.left_leg.setFont(font)
        self.left_leg.setAutoDefault(True)
        self.left_leg.setDefault(True)
        self.left_leg.setObjectName("left_leg")
        self.right_leg = QtWidgets.QPushButton(Form1)
        self.right_leg.setGeometry(QtCore.QRect(400, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.right_leg.setFont(font)
        self.right_leg.setAutoDefault(True)
        self.right_leg.setDefault(True)
        self.right_leg.setObjectName("right_leg")
        self.result = QtWidgets.QPushButton(Form1)
        self.result.setGeometry(QtCore.QRect(160, 150, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.result.setAutoDefault(True)
        self.result.setDefault(True)
        self.result.setObjectName("result")
        self.left_file_name = QtWidgets.QLabel(Form1)
        self.left_file_name.setGeometry(QtCore.QRect(30, 70, 241, 31))
        self.left_file_name.setText("")
        self.left_file_name.setObjectName("left_file_name")
        self.right_file_name = QtWidgets.QLabel(Form1)
        self.right_file_name.setGeometry(QtCore.QRect(280, 70, 241, 31))
        self.right_file_name.setText("")
        self.right_file_name.setObjectName("right_file_name")

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)
    ###########################################################################
        ####################################################################
        self.left_leg.clicked.connect(self.left_file1)
        self.right_leg.clicked.connect(self.right_file1)
        self.result.clicked.connect(self.result1)
    ###########################################################################
        ###################################################################
    def left_file1(self):
        self.fname1 = QFileDialog.getOpenFileName(None, 'Open file')[0]
        self.file_n1=''.join(self.fname1) 
        self.file1_name=self.file_n1
        self.left_file_name.setText(''.join(self.file1_name))
        self.left_file_name.adjustSize()
        #store_value()
    def right_file1(self):
        self.fname2 = QFileDialog.getOpenFileName(None, 'Open file')[0]    
        self.file_n2=''.join(self.fname2)
        self.file2_name=self.file_n2
        self.right_file_name.setText(''.join(self.file2_name))
        self.right_file_name.adjustSize()
        #print(file_n)
        #def store_value():
            
    def result1(self):
        ##############################
        print("report goes here")
        f1=self.file1_name
        f2=self.file2_name
        fs.generate(f1,f2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Left  Leg File:"))
        self.label_2.setText(_translate("Form", "Right Leg File"))
        self.left_leg.setText(_translate("Form", "Select File"))
        self.right_leg.setText(_translate("Form", "Select File"))
        self.result.setText(_translate("Form", "Generate Report"))

if __name__ == "__main__":
        
    app1 = QtWidgets.QApplication(s.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi1(Form1)
    Form1.show()
    s.exit(app1.exec_())



   

