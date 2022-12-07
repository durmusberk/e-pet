# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pet_owner_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PetOwnerWindow(object):
    def setupUi(self, PetOwnerWindow):
        PetOwnerWindow.setObjectName("PetOwnerWindow")
        PetOwnerWindow.resize(896, 622)
        PetOwnerWindow.setStyleSheet("background: #23B7C8;")
        self.centralwidget = QtWidgets.QWidget(PetOwnerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.petOwnerTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.petOwnerTabs.setGeometry(QtCore.QRect(0, 0, 896, 622))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.petOwnerTabs.setFont(font)
        self.petOwnerTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.petOwnerTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.petOwnerTabs.setElideMode(QtCore.Qt.ElideNone)
        self.petOwnerTabs.setObjectName("petOwnerTabs")
        self.myPetsTab = QtWidgets.QWidget()
        self.myPetsTab.setObjectName("myPetsTab")
        self.myPetsList = QtWidgets.QListWidget(self.myPetsTab)
        self.myPetsList.setGeometry(QtCore.QRect(0, 0, 891, 591))
        self.myPetsList.setObjectName("myPetsList")
        self.petInfoWidget = QtWidgets.QWidget(self.myPetsTab)
        self.petInfoWidget.setGeometry(QtCore.QRect(0, 0, 891, 591))
        self.petInfoWidget.setObjectName("petInfoWidget")
        self.petListWidget1 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget1.setGeometry(QtCore.QRect(100, 40, 241, 501))
        self.petListWidget1.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget1.setObjectName("petListWidget1")
        self.petInfoBackButton = QtWidgets.QPushButton(self.petInfoWidget)
        self.petInfoBackButton.setGeometry(QtCore.QRect(10, 20, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.petInfoBackButton.setFont(font)
        self.petInfoBackButton.setStyleSheet("background: #03e8fc;")
        self.petInfoBackButton.setObjectName("petInfoBackButton")
        self.petListWidget2 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget2.setGeometry(QtCore.QRect(370, 40, 481, 231))
        self.petListWidget2.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget2.setObjectName("petListWidget2")
        self.petListWidget3 = QtWidgets.QListWidget(self.petInfoWidget)
        self.petListWidget3.setGeometry(QtCore.QRect(370, 310, 481, 231))
        self.petListWidget3.setStyleSheet("background:white;\n"
"border: 2px solid black;\n"
"border-radius: 10px;")
        self.petListWidget3.setObjectName("petListWidget3")
        self.petInfoWidget.raise_()
        self.myPetsList.raise_()
        self.petOwnerTabs.addTab(self.myPetsTab, "")
        self.appointmentBookTab = QtWidgets.QWidget()
        self.appointmentBookTab.setObjectName("appointmentBookTab")
        self.label = QtWidgets.QLabel(self.appointmentBookTab)
        self.label.setGeometry(QtCore.QRect(60, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.myAppointmentsTable = QtWidgets.QTableWidget(self.appointmentBookTab)
        self.myAppointmentsTable.setGeometry(QtCore.QRect(60, 90, 781, 461))
        self.myAppointmentsTable.setStyleSheet("background: white;\n"
"border: 4px solid black;")
        self.myAppointmentsTable.setObjectName("myAppointmentsTable")
        self.myAppointmentsTable.setColumnCount(0)
        self.myAppointmentsTable.setRowCount(0)
        self.petOwnerTabs.addTab(self.appointmentBookTab, "")
        PetOwnerWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PetOwnerWindow)
        self.petOwnerTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(PetOwnerWindow)

    def retranslateUi(self, PetOwnerWindow):
        _translate = QtCore.QCoreApplication.translate
        PetOwnerWindow.setWindowTitle(_translate("PetOwnerWindow", "e-Pet"))
        self.petInfoBackButton.setText(_translate("PetOwnerWindow", "Back"))
        self.petOwnerTabs.setTabText(self.petOwnerTabs.indexOf(self.myPetsTab), _translate("PetOwnerWindow", "My Pets"))
        self.label.setText(_translate("PetOwnerWindow", "My Appointments"))
        self.petOwnerTabs.setTabText(self.petOwnerTabs.indexOf(self.appointmentBookTab), _translate("PetOwnerWindow", "Appointment Book"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PetOwnerWindow = QtWidgets.QMainWindow()
    ui = Ui_PetOwnerWindow()
    ui.setupUi(PetOwnerWindow)
    PetOwnerWindow.show()
    sys.exit(app.exec_())
