# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowMaoQOY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from mplwidget import MplWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"t.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = MplWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(581, 191))

        self.verticalLayout_4.addWidget(self.widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSizeIncrement(QSize(50, 0))
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(115)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.horizontalLayoutplot_tools = QHBoxLayout()
        self.horizontalLayoutplot_tools.setObjectName(u"horizontalLayoutplot_tools")
        self.horizontalLayoutplot_tools.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(80, 40))
        icon1 = QIcon()
        icon1.addFile(u"icons/save.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_save.setIcon(icon1)

        self.horizontalLayoutplot_tools.addWidget(self.pushButton_save)

        self.pushButton_plot = QPushButton(self.centralwidget)
        self.pushButton_plot.setObjectName(u"pushButton_plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_plot.sizePolicy().hasHeightForWidth())
        self.pushButton_plot.setSizePolicy(sizePolicy2)
        self.pushButton_plot.setMinimumSize(QSize(80, 40))
        self.pushButton_plot.setSizeIncrement(QSize(5, 0))
        icon2 = QIcon()
        icon2.addFile(u"icons/plot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_plot.setIcon(icon2)

        self.horizontalLayoutplot_tools.addWidget(self.pushButton_plot)

        self.pushButton_clear = QPushButton(self.centralwidget)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(80, 40))
        icon3 = QIcon()
        icon3.addFile(u"icons/clear icon.jpeg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_clear.setIcon(icon3)

        self.horizontalLayoutplot_tools.addWidget(self.pushButton_clear)


        self.verticalLayout_3.addLayout(self.horizontalLayoutplot_tools)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_previous = QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName(u"pushButton_previous")
        self.pushButton_previous.setMinimumSize(QSize(80, 40))

        self.verticalLayout_5.addWidget(self.pushButton_previous)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_x_point = QLineEdit(self.centralwidget)
        self.lineEdit_x_point.setObjectName(u"lineEdit_x_point")
        self.lineEdit_x_point.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit_x_point)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_y_point = QLineEdit(self.centralwidget)
        self.lineEdit_y_point.setObjectName(u"lineEdit_y_point")
        self.lineEdit_y_point.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_y_point)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.labelIndex = QLabel(self.centralwidget)
        self.labelIndex.setObjectName(u"labelIndex")

        self.verticalLayout.addWidget(self.labelIndex)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_next)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.doubleSpinBox_x_scale = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_x_scale.setObjectName(u"doubleSpinBox_x_scale")
        self.doubleSpinBox_x_scale.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox_x_scale.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_x_scale, 1, 1, 1, 1)

        self.doubleSpinBox_rotate = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_rotate.setObjectName(u"doubleSpinBox_rotate")
        self.doubleSpinBox_rotate.setWrapping(True)
        self.doubleSpinBox_rotate.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox_rotate.setMinimum(-359.990000000000009)
        self.doubleSpinBox_rotate.setMaximum(360.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_rotate, 3, 1, 1, 1)

        self.doubleSpinBox_y_scale = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_y_scale.setObjectName(u"doubleSpinBox_y_scale")
        self.doubleSpinBox_y_scale.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox_y_scale.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.doubleSpinBox_y_scale, 1, 2, 1, 1)

        self.lineEdit_x_translate = QLineEdit(self.centralwidget)
        self.lineEdit_x_translate.setObjectName(u"lineEdit_x_translate")
        self.lineEdit_x_translate.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_x_translate, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.lineEdit_y_translate = QLineEdit(self.centralwidget)
        self.lineEdit_y_translate.setObjectName(u"lineEdit_y_translate")
        self.lineEdit_y_translate.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_y_translate, 2, 2, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_y = QLabel(self.centralwidget)
        self.label_y.setObjectName(u"label_y")

        self.gridLayout.addWidget(self.label_y, 0, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_x = QLabel(self.centralwidget)
        self.label_x.setObjectName(u"label_x")

        self.gridLayout.addWidget(self.label_x, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App by Taiwo", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_plot.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_previous.setText(QCoreApplication.translate("MainWindow", u"Previous Point", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_x_point.setInputMask("")
        self.lineEdit_x_point.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lineEdit_y_point.setText("")
        self.lineEdit_y_point.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.labelIndex.setText(QCoreApplication.translate("MainWindow", u"Current Index: 0", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"Next Point", None))
        self.doubleSpinBox_rotate.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0", None))
        self.lineEdit_x_translate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TRANSLATE", None))
        self.lineEdit_y_translate.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ROTATE", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Y</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SCALE", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">X</span></p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
    # retranslateUi
