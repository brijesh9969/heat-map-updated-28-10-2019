# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PC_6\Desktop\heatmap\final working heat map\gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

# import fsr_printing_left as p
from report_gui import Ui_Form1 as r
import intfinalspatial as fs
import sys as s
import sys
import abc as a

class Ui_GATTII(object):
    file_name1=""
    def setupUi(self, GATTII):
        self.file_name=""
        ###################################################
        ########### All inputs variable ###################
        self.name=""
        self.date1=""
        self.age1=""
        self.foot_lenght_left1=""
        self.foot_lenght_right1=""
        self.foot_width_left1=""
        self.foot_width_right1=""
        self.weight1=""
        self.walk_lenght1=""
        self.gender1=""
        self.play_back_file_name1=""

        ################################
        GATTII.setObjectName("GATTII")
        GATTII.setEnabled(True)
        GATTII.resize(677, 431)
        GATTII.setMinimumSize(QtCore.QSize(677, 431))
        GATTII.setMaximumSize(QtCore.QSize(677, 431))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        GATTII.setFont(font)
        GATTII.setMouseTracking(True)
        icon = QtGui.QIcon.fromTheme("GattiLogo.png")
        GATTII.setWindowIcon(icon)
        GATTII.setAutoFillBackground(False)
        self.frame = QtWidgets.QFrame(GATTII)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setStyleSheet("""
        QFrame {
            background-color: #66b3ff;
            }
        """)
        self.frame.setObjectName("frame")
        self.start_test = QtWidgets.QPushButton(self.frame)
        self.start_test.setGeometry(QtCore.QRect(480, 90, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start_test.setFont(font)
        self.start_test.setAutoFillBackground(False)
        self.start_test.setAutoDefault(True)
        self.start_test.setDefault(True)
        self.start_test.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 4px;
            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.start_test.setFlat(False)
        self.start_test.setObjectName("start_test")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("""
        QLabel {

            }
        """)
        self.label.setGeometry(QtCore.QRect(10, 150, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("""
        QLabel {
            background-color: rgba(0, 200, 200,0.1);
            }
        """)
        self.label_2.setGeometry(QtCore.QRect(10, 320, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 90, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 260, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.age = QtWidgets.QLineEdit(self.frame)
        self.age.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.age.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)##
        self.age.setGeometry(QtCore.QRect(340, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.age.setFont(font)
        self.age.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.age.setCursorWidth(3)
        self.age.setObjectName("age")
        self.stop_test = QtWidgets.QPushButton(self.frame)
        self.stop_test.setGeometry(QtCore.QRect(480, 160, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stop_test.setFont(font)
        self.stop_test.setAutoDefault(True)
        self.stop_test.setDefault(True)
        self.stop_test.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 4px;
            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.stop_test.setFlat(False)
        self.stop_test.setObjectName("stop_test")
        self.generate_report = QtWidgets.QPushButton(self.frame)
        self.generate_report.setGeometry(QtCore.QRect(480, 220, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generate_report.setFont(font)
        self.generate_report.setAutoDefault(True)
        self.generate_report.setDefault(True)
        self.generate_report.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 4px;
            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.generate_report.setFlat(False)
        self.generate_report.setObjectName("generate_report")
        self.weight = QtWidgets.QLineEdit(self.frame)
        self.weight.setGeometry(QtCore.QRect(70, 260, 121, 41))
        self.weight.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.weight.setFont(font)
        self.weight.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)##
        self.weight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.weight.setCursorWidth(3)
        self.weight.setObjectName("weight")
        self.male = QtWidgets.QRadioButton(self.frame)
        self.male.setGeometry(QtCore.QRect(80, 320, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.male.setFont(font)
        self.male.setObjectName("male")
        self.female = QtWidgets.QRadioButton(self.frame)
        # self.female.setStyleSheet("""
        # border-radius: 4px;

        # """)
        self.female.setGeometry(QtCore.QRect(150, 320, 82, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.female.setFont(font)
        self.female.setObjectName("female")
        self.generate_graph = QtWidgets.QPushButton(self.frame)
        self.generate_graph.setGeometry(QtCore.QRect(480, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generate_graph.setFont(font)
        self.generate_graph.setAutoDefault(True)
        self.generate_graph.setDefault(True)
        self.generate_graph.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;

            border-radius: 4px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.generate_graph.setFlat(False)
        self.generate_graph.setObjectName("generate_graph")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(10, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")

        self.name_2 = QtWidgets.QLineEdit(self.frame)
        self.name_2.setGeometry(QtCore.QRect(80, 30, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)

        self.name_2.setObjectName("name_2")
        self.daet = QtWidgets.QDateEdit(self.frame)
        self.daet.setGeometry(QtCore.QRect(60, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.daet.setFont(font)
        self.daet.setStyleSheet("""
        QDateEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.daet.setCalendarPopup(True)
        self.daet.setObjectName("date")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.foot_lenght_left = QtWidgets.QLineEdit(self.frame)
        self.foot_lenght_left.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.foot_lenght_left.setGeometry(QtCore.QRect(180, 150, 91, 41))
        self.foot_lenght_left.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)##
        font = QtGui.QFont()
        font.setPointSize(12)
        self.foot_lenght_left.setFont(font)
        self.foot_lenght_left.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.foot_lenght_left.setCursorWidth(3)
        self.foot_lenght_left.setObjectName("foot_lenght_left")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.foot_width_left = QtWidgets.QLineEdit(self.frame)
        self.foot_width_left.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.foot_width_left.setGeometry(QtCore.QRect(180, 200, 91, 41))
        self.foot_width_left.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.foot_width_left.setFont(font)
        self.foot_width_left.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.foot_width_left.setCursorWidth(3)
        self.foot_width_left.setObjectName("foot_width_left")
        self.calibrate = QtWidgets.QPushButton(self.frame)
        self.calibrate.setGeometry(QtCore.QRect(480, 290, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.calibrate.setFont(font)
        self.calibrate.setAutoDefault(True)
        self.calibrate.setDefault(True)
        self.calibrate.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 4px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.calibrate.setFlat(False)
        self.calibrate.setObjectName("calibrate")
        self.foot_lenght_right = QtWidgets.QLineEdit(self.frame)
        self.foot_lenght_right.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.foot_lenght_right.setGeometry(QtCore.QRect(350, 150, 91, 41))
        ############ image #################
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(480, 342, 200, 100))
        self.label1.setStyleSheet("""
        QLabel {
           image: url(GattiiLogo.png);
            }
        """)
        self.label_4.setObjectName("label1")
        ####################################
        font = QtGui.QFont()
        font.setPointSize(12)
        self.foot_lenght_right.setFont(font)
        self.foot_lenght_right.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.foot_lenght_right.setCursorWidth(3)
        self.foot_lenght_right.setObjectName("foot_lenght_right")
        self.foot_width_right = QtWidgets.QLineEdit(self.frame)
        self.foot_width_right.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.foot_width_right.setGeometry(QtCore.QRect(350, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.foot_width_right.setFont(font)
        self.foot_width_right.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.foot_width_right.setCursorWidth(3)
        self.foot_width_right.setObjectName("foot_width_right")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(290, 150, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(290, 200, 47, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(210, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.walk_lenght = QtWidgets.QLineEdit(self.frame)
        self.walk_lenght.setStyleSheet("""
        QLineEdit {
               border: 1px solid #ccc;
                border-radius: 4px;

            }
        """)
        self.walk_lenght.setGeometry(QtCore.QRect(320, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.walk_lenght.setFont(font)
        self.walk_lenght.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhMultiLine)
        #self.walk_lenght.setCursorWidth(3)
        self.walk_lenght.setObjectName("walk_lenght")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 352, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.select_file = QtWidgets.QPushButton(self.frame)
        self.select_file.setGeometry(QtCore.QRect(120, 360, 131, 51))
        self.select_file.setAutoDefault(True)
        self.select_file.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;
            border-radius: 12px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        self.select_file.setDefault(True)
        self.select_file.setObjectName("select_file")
        self.file_name = QtWidgets.QLabel(self.frame)
        self.file_name.setGeometry(QtCore.QRect(260, 370, 121, 31))
        self.file_name.setText("")
        self.file_name.setObjectName("file_name")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(443, 0, 31, 421))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")



        self.retranslateUi(GATTII)
        QtCore.QMetaObject.connectSlotsByName(GATTII)
        ######################### --- on click function --- #################################
                                    ######################

        self.start_test.clicked.connect(self.start_graph)
        self.stop_test.clicked.connect(self.stop_graph)
        self.generate_report.clicked.connect(self.generate_report1)
        self.generate_graph.clicked.connect(self.play_back)
        self.calibrate.clicked.connect(self.calibrate1)
        self.select_file.clicked.connect(self.openFileNameDialog)
    ###########################################################################################
    ####################------------- called function --------- ##############################
    def openFileNameDialog(self):
        self.fname2 = QFileDialog.getOpenFileName(None, 'Open file')[0]
        self.file_n2=''.join(self.fname2)
        self.play_back_file_name1=self.file_n2

        self.file_name.setText(''.join(self.play_back_file_name1.split("/")[-1]))
        self.file_name.adjustSize()
    def start_graph(self):
        #g.main()
        print('start graph')
        self.name=self.name_2.text()
        self.date1=self.daet.text()
        self.age1=self.age.text()
        self.foot_lengtht_left1=self.foot_lenght_left.text()
        self.foot_lenght_right1=self.foot_lenght_right.text()
        self.foot_width_left1=self.foot_width_left.text()
        self.foot_width_left1=self.foot_width_left.text()
        self.foot_width_right1=self.foot_width_right.text()
        self.weight1=self.weight.text()
        self.walk_lenght1=self.walk_lenght.text()
        self.gender_male=""
        self.gender_female=""
        ###########################################--------------------------->>

        if self.name=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Name should not be empty !")
            msg.setWindowTitle("You Forgoted!")
            msg.setDetailedText("Name parameter is use to identify the patient Name")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        ############################################------------------------->>

        elif self.date1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Date should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Date parameter is use to identify the Test Date")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        #############################################------------------------>>

        elif self.age1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Age should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Date Parameter is use to identify the patient Age")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        ##############################################----------------------->>

        elif self.foot_lengtht_left1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot Length should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot Length parameter is use to identify the patient foot length")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        ################################################--------------------->>

        elif self.foot_lenght_right1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot Length should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot Length parameter is use to identify the patient foot length")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        #################################################-------------------->>

        elif self.foot_width_left1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot width should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot width of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        #################################################-------------------->>

        elif self.foot_width_right1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot width should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot width of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        #################################################--------------------->>

        elif self.weight1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("weight should not be empty and contains number only!")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("weight of patient in kg")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        #################################################--------------------->>

        elif self.walk_lenght1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Walk length should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("walk length of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        ################################################---------------------->>

        elif self.male.isChecked() == False and self.female.isChecked() == False :
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Select the gender !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("gender is identifyy the patient gender")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        elif self.male.isChecked():
            self.gender_male=self.male.text()
        elif self.female.isChecked()== True:
            self.gender_female=self.female.text()
            print(self.gender_female)
        #else:
        print("***************")
        print(self.gender_male)

        print(self.walk_lenght1)
        print(self.weight1)
        print(self.foot_width_right1)
        print(self.foot_width_left1)
        print(self.foot_lenght_right1)
        print(self.foot_lengtht_left1)
        print(self.age1)
        print(self.date1)
        print(self.name)
        #################################################------------------->>
        #################################################------------------->>
    def stop_graph(self):
        #g.winow_close1()
        p.window_close1()
        print('stop')
    ##################################################
    ###############################################

    ##############################################
    #############################################
    def generate_report1(self):
        # self.ui1 = rg.Form1
        # self.ui1.show()
        # print("generate report")
        self.name=self.name_2.text()
        self.date1=self.daet.text()
        self.age1=self.age.text()
        self.foot_lengtht_left1=self.foot_lenght_left.text()
        self.foot_lenght_right1=self.foot_lenght_right.text()
        self.foot_width_left1=self.foot_width_left.text()
        self.foot_width_left1=self.foot_width_left.text()
        self.foot_width_right1=self.foot_width_right.text()
        self.weight1=self.weight.text()
        self.walk_lenght1=self.walk_lenght.text()
        self.gender_male=""
        self.gender_female=""
        ###########################################--------------------------->>

        if self.name=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Name should not be empty !")
            msg.setWindowTitle("You Forgoted!")
            msg.setDetailedText("Name parameter is use to identify the patient Name")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        ############################################------------------------->>


        elif self.date1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Date should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Date parameter is use to identify the Test Date")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # #############################################------------------------>>

        elif self.age1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Age should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Date Parameter is use to identify the patient Age")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # ##############################################----------------------->>

        elif self.foot_lengtht_left1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot Length should not be empty !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot Length parameter is use to identify the patient foot length")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # ################################################--------------------->>

        elif self.foot_lenght_right1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot Length should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot Length parameter is use to identify the patient foot length")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # #################################################-------------------->>

        elif self.foot_width_left1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot width should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot width of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # #################################################-------------------->>

        elif self.foot_width_right1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Foot width should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Foot width of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # #################################################--------------------->>

        elif self.weight1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("weight should not be empty and contains number only!")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("weight of patient in kg")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # #################################################--------------------->>

        elif self.walk_lenght1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Walk length should not be empty and contains number only !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("walk length of patient")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        # ################################################---------------------->>

        elif self.male.isChecked() == False and self.female.isChecked() == False :
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText("Select the gender !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("gender is identifyy the patient gender")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        elif self.male.isChecked():
            self.gender_male=self.male.text()
        elif self.female.isChecked():
            self.gender_female=self.female.text()
        #else:
        print("*****************")
        print(self.gender_female)
        print(self.gender_male)
        print(self.gender_female)
        print(self.walk_lenght1)
        print(self.weight1)
        print(self.foot_width_right1)
        print(self.foot_width_left1)
        print(self.foot_lenght_right1)
        print(self.foot_lengtht_left1)
        print(self.age1)
        print(self.date1)
        print(self.name)
        # a=ab.demo()
        # a.setupUi()
        second.setup()




        #################################################------------------->>

    def play_back(self):

        self.play_back_file_name1=self.play_back_file_name1
        if self.play_back_file_name1=="":
            msg = QtWidgets.QMessageBox()
            #msg.setText("rohit")
            msg.setInformativeText(" select The File First !")
            msg.setWindowTitle("You Forgoted !")
            msg.setDetailedText("Select the file for play back than clivk on button")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok )
            #msg.buttonClicked.connect(self.msgbtn)
            msg.exec_()
        else:
            file_name1=self.play_back_file_name1

            #print(file_name1)
            p.main()


        print('play_back')
    def calibrate1(self):
        print('calibrating....')





    #############################################################################################
        ##########################################################################################


    def retranslateUi(self, GATTII):
        _translate = QtCore.QCoreApplication.translate
        GATTII.setWindowTitle(_translate("GATTII", "GATTII"))
        self.start_test.setText(_translate("GATTII", "Start Test"))
        self.label.setText(_translate("GATTII", "Foot Lenght (cm) : Left"))
        self.label_2.setText(_translate("GATTII", "Gender :"))
        self.label_3.setText(_translate("GATTII", "Age :"))
        self.label_4.setText(_translate("GATTII", "Weight :"))
        self.stop_test.setText(_translate("GATTII", "Stop Test"))
        self.generate_report.setText(_translate("GATTII", "Generate Report"))
        self.male.setText(_translate("GATTII", "Male"))
        self.female.setText(_translate("GATTII", "Female"))
        self.generate_graph.setText(_translate("GATTII", "Generate Heat Map"))
        self.name.setText(_translate("GATTII", "Name :"))
        self.label_5.setText(_translate("GATTII", "Date :"))
        self.label_6.setText(_translate("GATTII", "Foot Width (cm) :  Left"))
        self.calibrate.setText(_translate("GATTII", "Calibrate"))
        self.label_7.setText(_translate("GATTII", "Right"))
        self.label_8.setText(_translate("GATTII", "Right"))
        self.label_9.setText(_translate("GATTII", "Walk Lenght:"))
        self.label_10.setText(_translate("GATTII", "PlayBack File:"))
        self.select_file.setText(_translate("GATTII", "Select File"))
        self.label1.setText(_translate("GATTII",""))

class second:
    def setup():
        global Dialog
        file1_name=""
        file2_name=""
        # app2 = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        Dialog.setStyleSheet("""
        QDialog {
            background-color: #66b3ff;
            }
        """)
    # ui = Ui_Dialog()
    # ui.setupUi(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        label = QtWidgets.QLabel(Dialog)
        label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        label.setFont(font)
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(Dialog)
        label_2.setGeometry(QtCore.QRect(280, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        label_2.setFont(font)
        label_2.setObjectName("label_2")
        left_leg = QtWidgets.QPushButton(Dialog)
        left_leg.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;

            border-radius: 4px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        left_leg.setGeometry(QtCore.QRect(120, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        left_leg.setFont(font)
        left_leg.setAutoDefault(True)
        left_leg.setDefault(True)
        left_leg.setObjectName("left_leg")
        right_leg = QtWidgets.QPushButton(Dialog)
        right_leg.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;

            border-radius: 4px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        right_leg.setGeometry(QtCore.QRect(400, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        right_leg.setFont(font)
        right_leg.setAutoDefault(True)
        right_leg.setDefault(True)
        right_leg.setObjectName("right_leg")
        result = QtWidgets.QPushButton(Dialog)
        result.setStyleSheet("""
        QPushButton {
            background-color: DodgerBlue;
            border: none;
            color: white;
            padding: 12px 16px;
            font-size: 16px;

            border-radius: 4px;

            }

            QPushButton:hover {
                background-color: RoyalBlue;
            }
        """)
        result.setGeometry(QtCore.QRect(160, 150, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        result.setFont(font)
        result.setAutoDefault(True)
        result.setDefault(True)
        result.setObjectName("result")
        left_file_name = QtWidgets.QLabel(Dialog)
        left_file_name.setGeometry(QtCore.QRect(30, 70, 241, 31))
        left_file_name.setText("")
        left_file_name.setObjectName("left_file_name")
        right_file_name = QtWidgets.QLabel(Dialog)
        right_file_name.setGeometry(QtCore.QRect(280, 70, 241, 31))
        right_file_name.setText("")
        right_file_name.setObjectName("right_file_name")

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        label.setText(_translate("Form", "Left  Leg File:"))
        label_2.setText(_translate("Form", "Right Leg File"))
        left_leg.setText(_translate("Form", "Select File"))
        right_leg.setText(_translate("Form", "Select File"))
        result.setText(_translate("Form", "Generate Report"))
        # retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ###########################################################################
            ####################################################################

        ###########################################################################
            ###################################################################
        def left_file2():
            fname1 = QFileDialog.getOpenFileName(None, 'Open file')[0]
            file_n1=''.join(fname1)
            file1_name=file_n1
            left_file_name.setText(''.join(file1_name.split("/")[-1]))
            left_file_name.adjustSize()
            #store_value()
        def right_file2():
            fname2 = QFileDialog.getOpenFileName(None, 'Open file')[0]
            file_n2=''.join(fname2)
            file2_name=file_n2
            right_file_name.setText(''.join(file2_name.split("/")[-1]))
            right_file_name.adjustSize()
            #print(file_n)
            #def store_value():

        def result2():
            ##############################
            print("report goes here")
            f1=file1_name
            f2=file2_name
            fs.generate(f1,f2)
        # left_leg.clicked.connect(left_file2)
        # right_leg.clicked.connect(right_file2)
        # result.clicked.connect(result2)

        Dialog.show()
        # app2.exec_()
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 250)
        Dialog.setMinimumSize(QtCore.QSize(550, 250))
        Dialog.setMaximumSize(QtCore.QSize(550, 250))
        left_leg.clicked.connect(left_file2)
        right_leg.clicked.connect(right_file2)
        result.clicked.connect(result2)
    #######################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GATTII = QtWidgets.QWidget()
    ui = Ui_GATTII()
    ui.setupUi(GATTII)
    GATTII.show()
    sys.exit(app.exec_())
