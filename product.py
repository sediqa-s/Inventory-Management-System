# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from typing import List

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-40, -60, 931, 721))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setStyleSheet("#frame{\n"
"background: white;\n"
"}\n"
"#label{\n"
"font-family: oswald;\n"
"font-size: 35px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"QPushButton{\n"
"border: 0px;\n"
"background: none;\n"
"text-align: center;\n"
"border: 2px solid #04374A;\n"
"color: #04374A;\n"
"border-radius: 24px;\n"
"font-style: bold;\n"
"font-size: 16px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #04374A;\n"
"color: white;\n"
"}\n"
"QLabel{\n"
"font-family: oswald;\n"
"font-size: 20px;\n"
"font-style: bold;\n"
"color: #04374A;\n"
"}\n"
"QLineEdit{\n"
"font-family: oswald;\n"
"font-size: 16px;\n"
"color: #F8B400;\n"
"border: 3px solid #E0DBCB;\n"
"border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 70, 261, 61))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(740, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icons8-sign-out-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 30))
        self.pushButton.setObjectName("pushButton")

        # we have to connect to the openWindow method to change page to mainPage window:
        self.pushButton.clicked.connect(self.openWindow)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 80, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/stats.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(46, 47))
        self.pushButton_2.setObjectName("pushButton_2")

        # we have to connect to the openWindow2 method to change page to statistics window:
        self.pushButton_2.clicked.connect(self.openWindow2)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 170, 123, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(210, 167, 160, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 340, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # we have to connect to the inserting method to insert data:
        self.pushButton_3.clicked.connect(self.inserting)

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 340, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        # we have to connect to the viewing method to view data:
        self.pushButton_4.clicked.connect(self.viewing)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 410, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")

        # we have to connect to the updating method to update data:
        self.pushButton_5.clicked.connect(self.updating)

        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(240, 410, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")

        # we have to connect to the deleting method to delete data:
        self.pushButton_6.clicked.connect(self.deleting)

        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(160, 480, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")

        # we have to connect to the searching method to search data:
        self.pushButton_7.clicked.connect(self.searching)

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(390, 170, 471, 461))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(60)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe MDL2 Assets")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(-30, 370, 251, 391))
        self.widget.setStyleSheet("image: url(:/img/prod2.svg)")
        self.widget.setObjectName("widget")
        self.widget.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Inventory System"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))
        self.pushButton_2.setText(_translate("MainWindow", "Statistics"))
        self.label_2.setText(_translate("MainWindow", "Product Name : "))
        self.label_3.setText(_translate("MainWindow", "Price : "))
        self.label_4.setText(_translate("MainWindow", "Quantity : "))
        self.pushButton_3.setText(_translate("MainWindow", "Insert"))
        self.pushButton_4.setToolTip(_translate("MainWindow", "This button will view all the records"))
        self.pushButton_4.setText(_translate("MainWindow", "View"))
        self.pushButton_5.setText(_translate("MainWindow", "Update"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quantity"))

    # constructor used for switching pages:
    def __init__(self, window):
        self.window = window

    # used for passing information from other pages:
    def name(self, name, password):
        self.name = name
        self.password = password

    # opens main page:
    def openWindow(self):
        self.window.close()
        from mainPage import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.window)
        self.ui.setupUi(self.window)
        self.ui.name(self.name, self.password)
        self.window.show()

    # insert the data entered by user into database
    def inserting(self):
        conn = sqlite3.connect("inventory.bd")
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        quantity = self.lineEdit_3.text()
        res = conn.execute("select * from products where pname=?", (name,))
        if name == "" or price == "" or quantity == "":
            QMessageBox.about(self.window, "warning", "Please make sure that you have filled all the information")
        elif len(res.fetchall()) > 0:
            QMessageBox.about(self.window, "warning", "The product that you have entered already exists")
        else:
            conn.execute("insert into products(pname,price,quantity) values(?, ?, ?)", (name, price, quantity))
            conn.commit()
            conn.close()
            QMessageBox.about(self.window, 'Thank you', 'The product has been added successfully')
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")


    def viewing(self):
        conn = sqlite3.connect("inventory.bd")
        res = conn.execute("select * from products")
        self.tableWidget.setRowCount(0)
        # row number contains number of rows and row data contains the whole row qnd enumerate keeps count of iterations
        for row_number, row_data in enumerate(res):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        conn.close()

    def updating(self):
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        quantity = self.lineEdit_3.text()
        conn = sqlite3.connect("inventory.bd")
        res = conn.execute("select * from products where pname=?", (name,))
        if len(res.fetchall()) > 0:
            if name != "":
                if price != "":
                    conn.execute("update products set price=? WHERE pname=?",
                             (price, name))
                    conn.commit()
                    self.lineEdit_2.setText("")
                if quantity != "":
                    conn.execute("update products set quantity=? WHERE pname=?",
                             (quantity, name))
                    conn.commit()
                    self.lineEdit_3.setText("")
        else:
            QMessageBox.about(self.window, "warning", "The product name that you have entered does not exists or is empty")

    def deleting(self):
        conn = sqlite3.connect("inventory.bd")
        name = self.lineEdit.text()
        res = conn.execute("select * from products where pname=?", (name,))
        if len(res.fetchall()) > 0:
            conn.execute("Delete from products where pname=?", (name,))
            conn.commit()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            QMessageBox.about(self.window, "Informative",
                              "The product has been deleted successfully!")
        else:
            QMessageBox.about(self.window, "warning", "The product name that you have entered does not exists or is empty")

    def searching(self):
        conn = sqlite3.connect("inventory.bd")
        name = self.lineEdit.text()
        price = self.lineEdit_2.text()
        quantity = self.lineEdit_3.text()
        res1 = conn.execute("select * from products where pname=?", (name,))
        res2 = conn.execute("select * from products where price=?", (price,))
        res3 = conn.execute("select * from products where quantity=?", (quantity,))
        if len(res1.fetchall()) > 0 or len(res2.fetchall()) or len(res3.fetchall()):
            res = conn.execute("select * from products where pname=? or price=? or quantity=?", (name, price, quantity))
            self.tableWidget.setRowCount(0)
            # row number contains number of rows and row data contains the whole row qnd enumerate keeps count of iterations
            for row_number, row_data in enumerate(res):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(column_data)))
            conn.close()
        else:
            QMessageBox.about(self.window, "warning", "The information you have entered does not exists!")

    # shows the pie chart for total products:
    def openWindow2(self):
        conn = sqlite3.connect("inventory.bd")
        res = conn.execute("select quantity from products")
        names = conn.execute("select pname from products")

        res1 = []
        names1 = []

        for row_data in res:
            res1.append(int(row_data[0]))
        for row_data in names:
            names1.append(str(row_data[0]))

        plt.pie(res1, labels=names1, autopct='%0.1f%%')
        plt.show(self.window)


# create the products table:
conn = sqlite3.connect("inventory.bd")
conn.execute('''CREATE TABLE IF NOT EXISTS products(
                            id integer primary key AUTOINCREMENT,
                            pname text not null unique,
                            price integer not null,
                            quantity integer not null
                            )''')

import sources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
