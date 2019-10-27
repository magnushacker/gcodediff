from fbs_runtime.application_context import ApplicationContext
from PySide2 import QtCore, QtWidgets

import sys
import os

from profilefile import ProfileCollection
from gcodediff import Ui_MainWindow

class ProfileModel(QtCore.QAbstractTableModel):
    def __init__(self, settings, parent = QtCore.QObject() ):
        super(ProfileModel, self).__init__(parent)
        self._parent = parent
        self._profiles = ProfileCollection()

    def rowCount(self, index=QtCore.QModelIndex()):
        return self._profiles.parameterCount()

    def columnCount(self, index=QtCore.QModelIndex()):
        return self._profiles.profileCount() + 1 

    def headerData(self, column, orientation, role):
        if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
            if column == 0:
                return "Parameter"
            else:
                return self._profiles.profileName(column - 1)

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            if column == 0:
                return self._profiles.parameterName(row)
            else:
                return self._profiles.data(column-1, row)

    def addFile(self, filename):
        self._profiles.addFile(filename)
        self.layoutChanged.emit()

    def setFilters(self, hideIdentical, hideSingle):
        self._profiles.setFilters(hideIdentical, hideSingle)
        self.layoutChanged.emit()

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.profiles = ProfileCollection()
        self.profileModel = ProfileModel(self.profiles)
        self.ui.dataView.setModel(self.profileModel)

    def openFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open')
        if fname[0]:
            self.profileModel.addFile(fname[0])

    def setFilters(self):
        self.profileModel.setFilters(self.ui.actionHide_identical.isChecked(), self.ui.actionHide_singles.isChecked())


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    window = MainWindow()
    window.resize(250, 150)
    window.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)