# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\pcs-utils\scripts\Python\PySide2\constraint_tool\constraint_tool_ui.ui',
# licensing of 'D:\pcs-utils\scripts\Python\PySide2\constraint_tool\constraint_tool_ui.ui' applies.
#
# Created: Fri Nov  2 15:23:10 2018
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setAcceptDrops(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_object1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_object1.setObjectName("lineEdit_object1")
        self.horizontalLayout_7.addWidget(self.lineEdit_object1)
        self.button_object1 = QtWidgets.QPushButton(Dialog)
        self.button_object1.setAcceptDrops(True)
        self.button_object1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f_open_folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_object1.setIcon(icon)
        self.button_object1.setObjectName("button_object1")
        self.horizontalLayout_7.addWidget(self.button_object1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_object2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_object2.setObjectName("lineEdit_object2")
        self.horizontalLayout_6.addWidget(self.lineEdit_object2)
        self.button_object2 = QtWidgets.QPushButton(Dialog)
        self.button_object2.setText("")
        self.button_object2.setIcon(icon)
        self.button_object2.setObjectName("button_object2")
        self.horizontalLayout_6.addWidget(self.button_object2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_dopnet = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_dopnet.setObjectName("lineEdit_dopnet")
        self.horizontalLayout_3.addWidget(self.lineEdit_dopnet)
        self.button_dopnet = QtWidgets.QPushButton(Dialog)
        self.button_dopnet.setText("")
        self.button_dopnet.setIcon(icon)
        self.button_dopnet.setObjectName("button_dopnet")
        self.horizontalLayout_3.addWidget(self.button_dopnet)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(20, 0))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "rbd constraint tool", None, -1))
        self.lineEdit_object1.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "object1", None, -1))
        self.lineEdit_object2.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "object2", None, -1))
        self.lineEdit_dopnet.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "dopnet", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "constraint type", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("Dialog", "glue constraint", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("Dialog", "pin constraint", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("Dialog", "cone constraint", None, -1))

