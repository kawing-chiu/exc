from PyQt5 import QtWidgets, QtCore

from gridlayout_test import create_button

QtCore.Signal = QtCore.pyqtSignal
QtCore.Slot = QtCore.pyqtSlot

w = QtWidgets.QWidget()
v = QtWidgets.QSplitter(QtCore.Qt.Vertical)
h = QtWidgets.QSplitter(QtCore.Qt.Horizontal)
# grid_object = QtWidgets.QWidget() 
grid_object = create_button('grid')
grid = QtWidgets.QGridLayout()
grid_object.setLayout(grid)
preview = create_button('preview')
text = create_button('text')
w_layout = QtWidgets.QHBoxLayout()
w_layout.addWidget(h)
w.setLayout(w_layout)

def remove_all_widgets(splitter):
    for i in reversed(range(splitter.count())):
        splitter.widget(i).setParent(None)

def recreate_layout(h_stretch, v_stretch):
    remove_all_widgets(v)
    remove_all_widgets(h)
    h.addWidget(v)
    h.addWidget(text)
    h.setSizes([h_stretch*10000, 10000])
    v.addWidget(grid_object)
    v.addWidget(preview)
    v.setSizes([v_stretch*10000, 10000])

recreate_layout(3.8, 3.8)

def main():
    w.resize(1248, 763)
    w.show()


if __name__ == '__main__':
    main()
