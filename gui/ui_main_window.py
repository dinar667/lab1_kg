# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dinar667\PycharmProjects\pointInSpace_v2\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.aWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aWidget.sizePolicy().hasHeightForWidth())
        self.aWidget.setSizePolicy(sizePolicy)
        self.aWidget.setMinimumSize(QtCore.QSize(0, 250))
        self.aWidget.setObjectName("aWidget")
        self.verticalLayout_8.addWidget(self.aWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.cWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cWidget.sizePolicy().hasHeightForWidth())
        self.cWidget.setSizePolicy(sizePolicy)
        self.cWidget.setMinimumSize(QtCore.QSize(0, 250))
        self.cWidget.setObjectName("cWidget")
        self.verticalLayout_9.addWidget(self.cWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.coordinatesGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.coordinatesGroupBox.setObjectName("coordinatesGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.coordinatesGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.xField = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.xField.setMinimumSize(QtCore.QSize(35, 20))
        self.xField.setMaximumSize(QtCore.QSize(35, 20))
        self.xField.setAlignment(QtCore.Qt.AlignCenter)
        self.xField.setReadOnly(True)
        self.xField.setObjectName("xField")
        self.verticalLayout_4.addWidget(self.xField)
        self.yField = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.yField.setMinimumSize(QtCore.QSize(35, 20))
        self.yField.setMaximumSize(QtCore.QSize(35, 20))
        self.yField.setAlignment(QtCore.Qt.AlignCenter)
        self.yField.setReadOnly(True)
        self.yField.setObjectName("yField")
        self.verticalLayout_4.addWidget(self.yField)
        self.zField = QtWidgets.QLineEdit(self.coordinatesGroupBox)
        self.zField.setMinimumSize(QtCore.QSize(35, 20))
        self.zField.setMaximumSize(QtCore.QSize(35, 20))
        self.zField.setAlignment(QtCore.Qt.AlignCenter)
        self.zField.setReadOnly(True)
        self.zField.setObjectName("zField")
        self.verticalLayout_4.addWidget(self.zField)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.xSlider = QtWidgets.QSlider(self.coordinatesGroupBox)
        self.xSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.xSlider.setMinimum(-100)
        self.xSlider.setMaximum(100)
        self.xSlider.setOrientation(QtCore.Qt.Horizontal)
        self.xSlider.setInvertedAppearance(False)
        self.xSlider.setInvertedControls(False)
        self.xSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.xSlider.setObjectName("xSlider")
        self.verticalLayout.addWidget(self.xSlider)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.ySlider = QtWidgets.QSlider(self.coordinatesGroupBox)
        self.ySlider.setMinimum(-100)
        self.ySlider.setMaximum(100)
        self.ySlider.setOrientation(QtCore.Qt.Horizontal)
        self.ySlider.setInvertedAppearance(False)
        self.ySlider.setInvertedControls(False)
        self.ySlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ySlider.setObjectName("ySlider")
        self.verticalLayout_2.addWidget(self.ySlider)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.coordinatesGroupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.zSlider = QtWidgets.QSlider(self.coordinatesGroupBox)
        self.zSlider.setMinimum(-100)
        self.zSlider.setMaximum(100)
        self.zSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zSlider.setInvertedAppearance(False)
        self.zSlider.setInvertedControls(False)
        self.zSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.zSlider.setObjectName("zSlider")
        self.verticalLayout_3.addWidget(self.zSlider)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.coordinatesGroupBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.angleComboBox = QtWidgets.QGroupBox(self.centralwidget)
        self.angleComboBox.setObjectName("angleComboBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.angleComboBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.angleComboBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_11 = QtWidgets.QLabel(self.angleComboBox)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.label_14 = QtWidgets.QLabel(self.angleComboBox)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.angleComboBox)
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.label_16 = QtWidgets.QLabel(self.angleComboBox)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.xAngleSlider = QtWidgets.QSlider(self.angleComboBox)
        self.xAngleSlider.setMinimumSize(QtCore.QSize(250, 0))
        self.xAngleSlider.setMinimum(0)
        self.xAngleSlider.setMaximum(360)
        self.xAngleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.xAngleSlider.setInvertedAppearance(False)
        self.xAngleSlider.setInvertedControls(False)
        self.xAngleSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.xAngleSlider.setObjectName("xAngleSlider")
        self.verticalLayout_11.addWidget(self.xAngleSlider)
        self.verticalLayout_10.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_17 = QtWidgets.QLabel(self.angleComboBox)
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_8.addWidget(self.label_17)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_18 = QtWidgets.QLabel(self.angleComboBox)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_8.addWidget(self.label_18)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.yAngleSlider = QtWidgets.QSlider(self.angleComboBox)
        self.yAngleSlider.setMinimum(0)
        self.yAngleSlider.setMaximum(360)
        self.yAngleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.yAngleSlider.setInvertedAppearance(False)
        self.yAngleSlider.setInvertedControls(False)
        self.yAngleSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.yAngleSlider.setObjectName("yAngleSlider")
        self.verticalLayout_12.addWidget(self.yAngleSlider)
        self.verticalLayout_10.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_19 = QtWidgets.QLabel(self.angleComboBox)
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_9.addWidget(self.label_19)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.label_20 = QtWidgets.QLabel(self.angleComboBox)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.zAngleSlider = QtWidgets.QSlider(self.angleComboBox)
        self.zAngleSlider.setMinimum(0)
        self.zAngleSlider.setMaximum(360)
        self.zAngleSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zAngleSlider.setInvertedAppearance(False)
        self.zAngleSlider.setInvertedControls(False)
        self.zAngleSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.zAngleSlider.setObjectName("zAngleSlider")
        self.verticalLayout_13.addWidget(self.zAngleSlider)
        self.verticalLayout_10.addLayout(self.verticalLayout_13)
        self.gridLayout_2.addLayout(self.verticalLayout_10, 0, 1, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.xAngleField = QtWidgets.QLineEdit(self.angleComboBox)
        self.xAngleField.setMinimumSize(QtCore.QSize(35, 20))
        self.xAngleField.setMaximumSize(QtCore.QSize(35, 20))
        self.xAngleField.setAlignment(QtCore.Qt.AlignCenter)
        self.xAngleField.setReadOnly(True)
        self.xAngleField.setObjectName("xAngleField")
        self.verticalLayout_14.addWidget(self.xAngleField)
        self.yAngleField = QtWidgets.QLineEdit(self.angleComboBox)
        self.yAngleField.setMinimumSize(QtCore.QSize(35, 20))
        self.yAngleField.setMaximumSize(QtCore.QSize(35, 20))
        self.yAngleField.setAlignment(QtCore.Qt.AlignCenter)
        self.yAngleField.setReadOnly(True)
        self.yAngleField.setObjectName("yAngleField")
        self.verticalLayout_14.addWidget(self.yAngleField)
        self.zAngleField = QtWidgets.QLineEdit(self.angleComboBox)
        self.zAngleField.setMinimumSize(QtCore.QSize(35, 20))
        self.zAngleField.setMaximumSize(QtCore.QSize(35, 20))
        self.zAngleField.setAlignment(QtCore.Qt.AlignCenter)
        self.zAngleField.setReadOnly(True)
        self.zAngleField.setObjectName("zAngleField")
        self.verticalLayout_14.addWidget(self.zAngleField)
        self.gridLayout_2.addLayout(self.verticalLayout_14, 0, 2, 1, 1)
        self.horizontalLayout_6.addWidget(self.angleComboBox)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.xSlider.valueChanged['int'].connect(MainWindow.on_x_changed)
        self.ySlider.valueChanged['int'].connect(MainWindow.on_y_changed)
        self.zSlider.valueChanged['int'].connect(MainWindow.on_z_changed)
        self.xAngleSlider.valueChanged['int'].connect(MainWindow.on_x_angle_changed)
        self.zAngleSlider.valueChanged['int'].connect(MainWindow.on_z_angle_changed)
        self.yAngleSlider.valueChanged['int'].connect(MainWindow.on_y_angle_changed)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Точка в пространстве"))
        self.label_12.setText(_translate("MainWindow", "Аксонометрическая система плоскостей"))
        self.label_13.setText(_translate("MainWindow", "Комплексный чертеж"))
        self.coordinatesGroupBox.setTitle(_translate("MainWindow", "Координаты точки T"))
        self.xField.setText(_translate("MainWindow", "0"))
        self.yField.setText(_translate("MainWindow", "0"))
        self.zField.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "X:"))
        self.label_2.setText(_translate("MainWindow", "Y:"))
        self.label_3.setText(_translate("MainWindow", "Z:"))
        self.label_5.setText(_translate("MainWindow", "-100"))
        self.label_6.setText(_translate("MainWindow", "100"))
        self.label_7.setText(_translate("MainWindow", "-100"))
        self.label_8.setText(_translate("MainWindow", "100"))
        self.label_9.setText(_translate("MainWindow", "-100"))
        self.label_10.setText(_translate("MainWindow", "100"))
        self.angleComboBox.setTitle(_translate("MainWindow", "Угол поворота"))
        self.label_4.setText(_translate("MainWindow", "X:"))
        self.label_11.setText(_translate("MainWindow", "Y:"))
        self.label_14.setText(_translate("MainWindow", "Z:"))
        self.label_15.setText(_translate("MainWindow", " 0°"))
        self.label_16.setText(_translate("MainWindow", "360°"))
        self.label_17.setText(_translate("MainWindow", " 0°"))
        self.label_18.setText(_translate("MainWindow", "360°"))
        self.label_19.setText(_translate("MainWindow", " 0°"))
        self.label_20.setText(_translate("MainWindow", "360°"))
        self.xAngleField.setText(_translate("MainWindow", "0"))
        self.yAngleField.setText(_translate("MainWindow", "0"))
        self.zAngleField.setText(_translate("MainWindow", "0"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.actionExit.setText(_translate("MainWindow", "Выход"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
