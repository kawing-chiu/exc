import sys

try:
    from PySide import QtGui, QtCore
    from PySide.QtCore import Qt
    from PySide.QtGui import QTreeWidget, QTreeWidgetItem
    pyside = True
except ImportError:
    pyside = False

#pyside = False
if pyside:
    pyqt = False
else:
    try:
        from PyQt4 import QtGui, QtCore
        from PyQt4.QtCore import Qt
        QtCore.Signal = QtCore.pyqtSignal
        QtCore.Slot = QtCore.pyqtSlot
        from PyQt4.QtGui import QTreeWidget, QTreeWidgetItem
        pyqt = True
    except ImportError:
        pyqt = False


def fill_item(item, value, level):
    item.setExpanded(True)
    if type(value) is dict:
        for key, val in sorted(value.items()):
            child = QTreeWidgetItem()
            child.setText(level, str(key))
            item.addChild(child)
            fill_item(child, val, level+1)
    elif type(value) is list:
        for val in value:
            child = QTreeWidgetItem()
            item.addChild(child)
            if type(val) is dict:            
                child.setText(level, '[dict]')
                fill_item(child, val, level+1)
            elif type(val) is list:
                child.setText(level, '[list]')
                fill_item(child, val, level+1)
            else:
                child.setText(level, str(val))                            
            child.setExpanded(True)
    else:
        child = QTreeWidgetItem()
        child.setText(level, str(value))
        item.addChild(child)

def fill_widget(widget, value):
    widget.clear()
    fill_item(widget.invisibleRootItem(), value, 0)

app = QtGui.QApplication.instance()
if app is None:
    app = QtGui.QApplication(sys.argv)

d = { 'key1': 'value1', 
  'key2': 'value2',
  'sub_list': [1,2,3, ['good', 'test'], {'abc': 3, 'cde': 9}],
  'key4': object(),
  'sub_dict': {'key1': 'value1',
            'key2': 'value2'}}

widget = QTreeWidget()
widget.setHeaderLabels(['level0', 'level1', 'level2', 'level3'])
fill_widget(widget, d)
widget.show()

sys.exit(app.exec_())

