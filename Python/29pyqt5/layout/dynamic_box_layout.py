from PyQt5 import QtWidgets, QtCore

from gridlayout_test import create_button

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

w = QtWidgets.QWidget()
v = QtWidgets.QVBoxLayout()
h = QtWidgets.QHBoxLayout()
# grid_object = QtWidgets.QWidget() 
grid_object = create_button('grid')
grid = QtWidgets.QGridLayout()
grid_object.setLayout(grid)
preview = create_button('preview')
text = create_button('text')
w.setLayout(h)

def remove_all_widgets(layout):
    widgets = []
    for i in reversed(range(layout.count())):
        item = layout.takeAt(i)
        if item.widget() is not None:
            item.widget().setParent(None)
        if item.layout() is not None:
            item.layout().setParent(None)

def recreate_layout(h_stretch, v_stretch):
    remove_all_widgets(v)
    remove_all_widgets(h)
    h.addLayout(v, h_stretch)
    h.addWidget(text, 1)
    v.addWidget(grid_object, v_stretch)
    v.addWidget(preview, 1)

recreate_layout(4, 4)

def main():
    w.resize(1248, 763)
    w.show()


if __name__ == '__main__':
    main()
