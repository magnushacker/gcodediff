# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\Magnus\Documents\QT projects\gcodediff\src\main\python\gcodediff.ui',
# licensing of 'd:\Users\Magnus\Documents\QT projects\gcodediff\src\main\python\gcodediff.ui' applies.
#
# Created: Sun Oct 27 21:09:54 2019
#      by: pyside2-uic  running on PySide2 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setBaseSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.dataView = QtWidgets.QTableView(self.centralwidget)
        self.dataView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.dataView.setAlternatingRowColors(False)
        self.dataView.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.dataView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.dataView.setSortingEnabled(False)
        self.dataView.setCornerButtonEnabled(False)
        self.dataView.setObjectName("dataView")
        self.dataView.horizontalHeader().setDefaultSectionSize(120)
        self.dataView.horizontalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.dataView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setToolTip("")
        self.statusbar.setStatusTip("")
        self.statusbar.setAccessibleName("")
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setShortcutVisibleInContextMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHide_identical = QtWidgets.QAction(MainWindow)
        self.actionHide_identical.setCheckable(True)
        self.actionHide_identical.setShortcutVisibleInContextMenu(False)
        self.actionHide_identical.setObjectName("actionHide_identical")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionHide_singles = QtWidgets.QAction(MainWindow)
        self.actionHide_singles.setCheckable(True)
        self.actionHide_singles.setObjectName("actionHide_singles")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuOptions.addAction(self.actionHide_identical)
        self.menuOptions.addAction(self.actionHide_singles)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL("triggered()"), MainWindow.openFile)
        QtCore.QObject.connect(self.actionHide_identical, QtCore.SIGNAL("triggered()"), MainWindow.setFilters)
        QtCore.QObject.connect(self.actionHide_singles, QtCore.SIGNAL("triggered()"), MainWindow.setFilters)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "GCode Diff", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuOptions.setTitle(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open file...", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+F4", None, -1))
        self.actionHide_identical.setText(QtWidgets.QApplication.translate("MainWindow", "Hide identical", None, -1))
        self.actionHide_identical.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Hide lines where all columns are identical", None, -1))
        self.actionHide_identical.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+I", None, -1))
        self.actionClose.setText(QtWidgets.QApplication.translate("MainWindow", "Close file", None, -1))
        self.actionClose.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+E", None, -1))
        self.actionHide_singles.setText(QtWidgets.QApplication.translate("MainWindow", "Hide single values", None, -1))
        self.actionHide_singles.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Hide lines where only one column has a value", None, -1))
        self.actionHide_singles.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
