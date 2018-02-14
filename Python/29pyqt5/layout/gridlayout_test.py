from PyQt5 import QtWidgets, QtCore

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot


w = QtWidgets.QWidget()
grid = QtWidgets.QGridLayout()
w.setLayout(grid)

def create_button(text):
    button = QtWidgets.QPushButton(text)
    button.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                         QtWidgets.QSizePolicy.Preferred)
    return button

b1 = create_button("Test 1")
b2 = create_button("Test 2")
grid.addWidget(b1, 0, 0, 2, 2)
grid.addWidget(b2, 1, 1)

# grid.count()
# grid.itemAt(0)
# grid.takeAt(0)
# grid.itemAt(1).widget().deleteLater()
# b1.deleteLater()

w.show()
