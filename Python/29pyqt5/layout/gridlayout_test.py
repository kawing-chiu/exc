from PyQt5 import QtWidgets, QtCore

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


w = QtWidgets.QWidget()
grid = QtWidgets.QGridLayout()
# grid.setOriginCorner(QtCore.Qt.TopRightCorner)
w.setLayout(grid)

def create_button(text):
    button = QtWidgets.QPushButton(text)
    button.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                         QtWidgets.QSizePolicy.Preferred)
    return button

# some useful functions
def _remove_all_widgets(g):
    for i in reversed(range(g.count())):
        g.takeAt(i).widget().setParent(None)

def _remove_stretch(g):
    if self._grid_limit is not None:
        for i in range(self._grid_limit[0]):
            g.setRowStretch(i, 0)
        for i in range(self._grid_limit[1]):
            g.setColumnStretch(i, 0)

def _apply_stretch(g):
    if self._grid_limit is not None:
        for i in range(self._grid_limit[0]):
            g.setRowStretch(i, 1)
        for i in range(self._grid_limit[1]):
            g.setColumnStretch(i, 1)


b1 = create_button("Test 1")
b2 = create_button("Test 2")
b3 = create_button("Test 3")
grid.addWidget(b1, 0, 0, 2, 2)
grid.addWidget(b2, 3, 3)

# grid.count()
# grid.itemAt(0)
# grid.takeAt(0)
# grid.itemAt(1).widget().deleteLater()
# b1.deleteLater()

def main():
    w.resize(1248, 763)
    w.show()


if __name__ == '__main__':
    main()
