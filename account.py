# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'account.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_account(object):
    def setupUi(self, account):
        account.setObjectName("account")
        account.resize(800, 614)
        font = QtGui.QFont()
        font.setFamily("Arial")
        account.setFont(font)
        account.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(account)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 821, 641))
        self.frame.setStyleSheet("#frame{\n"
"background: white;\n"
"}\n"
"#frame_2{\n"
"background: #FAF5E4;\n"
"border-radius: 25px;\n"
"}\n"
"#label{\n"
"font-family: oswald;\n"
"font-size: 35px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_2{\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_3{\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_4{\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_5{\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_6{\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"#label_7{\n"
"background: white;\n"
"border: 3px solid #E0DBCB;\n"
"border-radius: 15px;\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #F8B400;\n"
"}\n"
"#label_8{\n"
"background: white;\n"
"border: 3px solid #E0DBCB;\n"
"border-radius: 15px;\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #F8B400;\n"
"}\n"
"#label_9{\n"
"background: white;\n"
"border: 3px solid #E0DBCB;\n"
"border-radius: 15px;\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #F8B400;\n"
"}\n"
"#label_10{\n"
"background: white;\n"
"border: 3px solid #E0DBCB;\n"
"border-radius: 15px;\n"
"font-family: oswald;\n"
"font-size: 25px;\n"
"font-style: bold;\n"
"color: #F8B400;\n"
"}\n"
"QPushButton{\n"
"border: 0px;\n"
"background: none;\n"
"margin: 20px auto;\n"
"text-align: center;\n"
"border: 2px solid #04374A;\n"
"padding: 14px 50px;\n"
"outline: none;\n"
"color: #04374A;\n"
"border-radius: 24px;\n"
"font-style: bold;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #04374A;\n"
"color: white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 10, 261, 61))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 70, 161, 121))
        self.widget.setStyleSheet("Image: url(:/img/avatar.svg)")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 200, 131, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(200, 80, 461, 441))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(60, 70, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(60, 140, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 111, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(70, 290, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(190, 60, 261, 41))
        font = QtGui.QFont()
        font.setFamily("oswald")
        font.setPointSize(-1)
        font.setUnderline(False)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(190, 130, 261, 41))
        font = QtGui.QFont()
        font.setFamily("oswald")
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(190, 200, 261, 41))
        font = QtGui.QFont()
        font.setFamily("oswald")
        font.setPointSize(-1)
        font.setUnderline(False)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(190, 280, 261, 41))
        font = QtGui.QFont()
        font.setFamily("oswald")
        font.setPointSize(-1)
        font.setUnderline(False)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(520, 410, 261, 221))
        self.widget_2.setStyleSheet("Image: url(:/img/profile.svg)")
        self.widget_2.setObjectName("widget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(-20, 310, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # we have to connect to the openWindow3 method to connect to the update page:
        self.pushButton_2.clicked.connect(self.openWindow3)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(-20, 400, 241, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStatusTip("")
        self.pushButton_3.setWhatsThis("")
        self.pushButton_3.setAccessibleName("")
        self.pushButton_3.setAccessibleDescription("")
        self.pushButton_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_3.setObjectName("pushButton_3")

        # we have to connect to the delete method to delete user account:
        self.pushButton_3.clicked.connect(self.delete)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(530, -10, 281, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icons8-sign-out-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(51, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        # we have to connect to the openWindow method to change page to mainPage window:
        self.pushButton_4.clicked.connect(self.openWindow)

        account.setCentralWidget(self.centralwidget)

        self.retranslateUi(account)
        QtCore.QMetaObject.connectSlotsByName(account)

    def retranslateUi(self, account):
        _translate = QtCore.QCoreApplication.translate
        account.setWindowTitle(_translate("account", "MainWindow"))
        self.label.setText(_translate("account", "Inventory System"))
        self.label_2.setText(_translate("account", "Name"))
        self.label_3.setText(_translate("account", "Name :"))
        self.label_4.setText(_translate("account", "E-mail :"))
        self.label_5.setText(_translate("account", "Password :"))
        self.label_6.setText(_translate("account", "Age :"))
        self.label_7.setText(_translate("account", "jpg"))
        self.label_8.setText(_translate("account", "jpg"))
        self.label_9.setText(_translate("account", "jpg"))
        self.label_10.setText(_translate("account", "jpg"))
        self.pushButton_2.setText(_translate("account", "Update"))
        self.pushButton_3.setToolTip(_translate("account", "your account will be deleted"))
        self.pushButton_3.setText(_translate("account", "Delete"))
        self.pushButton_4.setText(_translate("account", "Logout"))


    # constructor used for switching pages:
    def __init__(self, window):
        self.window = window

    # used for passing information from other pages also for viewing the information inside labels:
    def name(self, name, password):
        self.label_2.setText(str(name))
        self.label_9.setText(str(password))
        conn = sqlite3.connect("inventory.bd")
        res = conn.execute("select * from users where username=? AND password=?", (name, password))
        conn.commit()
        for i in res:
            self.label_7.setText(str(i[1]))
            self.label_8.setText(str(i[2]))
            self.label_9.setText(str(i[3]))
            self.label_10.setText(str(i[4]))
        self.name = name
        self.password = password

    # opens main page
    def openWindow(self):
        self.window.close()
        from mainPage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.ui.name(self.name, self.password)
        self.window.show()

    # opens sign up page
    def openWindow2(self):
        self.window.close()
        from signup import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog(self.window)
        self.ui.setupUi(self.window)
        self.window.show()

    # opens update page:
    def openWindow3(self):
        self.window.close()
        from update import Ui_Dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog(self.window)
        self.ui.setupUi(self.window)
        self.ui.name(self.name, self.password)
        self.window.show()

    # delete users from the database:
    def delete(self):
        conn = sqlite3.connect("inventory.bd")
        email = self.label_8.text()
        conn.execute("Delete from users where email=?", (email,))
        conn.commit()
        self.openWindow2()


import sources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    account = QtWidgets.QMainWindow()
    ui = Ui_account()
    ui.setupUi(account)
    account.show()
    sys.exit(app.exec_())
