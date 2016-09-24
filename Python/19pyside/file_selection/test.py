import sys
import os
from functools import partial
import html

try:
    from PySide import QtGui, QtCore
    from PySide.QtCore import Qt
    pyside = True
except ImportError:
    pyside = False

if pyside:
    pyqt = False
else:
    try:
        from PyQt4 import QtGui, QtCore
        from PyQt4.QtCore import Qt
        QtCore.Signal = QtCore.pyqtSignal
        QtCore.Slot = QtCore.pyqtSlot
        pyqt = True
    except ImportError:
        pyqt = False

if not (pyside or pyqt):
    sys.exit("Error: Dependency missing. Either PySide or PyQt4 must be installed")

try:
    __IPYTHON__
    ipython = True
except NameError as e:
    ipython = False


def find_dialog(type='dir', combo=None):
    if type == 'dir':
        path = QtGui.QFileDialog.getExistingDirectory(None, "Choose a dir",
                os.path.expanduser("~/code_study"))
    elif type == 'file':
        if pyside:
            path, _ = QtGui.QFileDialog.getOpenFileName(None, "Choose a file",
                    os.path.expanduser("~/Downloads"))
        elif pyqt:
            path = QtGui.QFileDialog.getOpenFileName(None, "Choose a file",
                    os.path.expanduser("~/Downloads"))
        print("path:", path)
    print(type+':', path)
    if path:
        idx = combo.findText(path)
        combo.removeItem(idx)
        combo.insertItem(0, path)
        combo.setCurrentIndex(0)
    return path


class MyTab(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        group_box = QtGui.QGroupBox("File paths")
        self.group_box = group_box

        browse_button1 = QtGui.QPushButton("choose dir")
        browse_button2 = QtGui.QPushButton("choose file")

        label1 = QtGui.QLabel("Directory:")
        label2 = QtGui.QLabel("File:")

        combo1 = QtGui.QComboBox()
        combo1.setEditable(True)
        combo1.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        combo1.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        combo2 = QtGui.QComboBox()
        combo2.setEditable(True)
        combo2.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        combo2.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.combo1 = combo1
        self.combo2 = combo2

        browse_button1.clicked.connect(partial(find_dialog, 'dir', combo1))
        browse_button2.clicked.connect(partial(find_dialog, 'file', combo2))

        layout = QtGui.QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(combo1, 0, 1)
        layout.addWidget(browse_button1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(combo2, 1, 1)
        layout.addWidget(browse_button2, 1, 2)

        group_box.setLayout(layout)

        start_button = QtGui.QPushButton("start")
        start_button.clicked.connect(self.run)

        top_layout = QtGui.QHBoxLayout()
        top_layout.addWidget(group_box)
        top_layout.addWidget(start_button)

        text_area = QtGui.QPlainTextEdit()
        text_area.setReadOnly(True)
        self.text_area = text_area

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(text_area)

        self.setLayout(main_layout)

    def run(self):
        self.info("testing\n<heheh>\nlll", pre=True)
        self.error("abc\ngood <pre>testing\n<h5>eheh</h5>\nlll</pre>", escape=False)

    def info(self, text, pre=False, escape=True):
        if escape:
            text = html.escape(text)
        if pre:
            self.text_area.appendHtml('<span style="color:green">[Info] </span>'
                    '<pre>{}</pre>'
                    .format(text))
        else:
            self.text_area.appendHtml('<span style="color:green">[Info] </span>'
                    '{}'
                    .format(text))

    def error(self, text, pre=False, escape=True):
        if escape:
            text = html.escape(text)
        if pre:
            self.text_area.appendHtml('<span style="color:red">[Error] </span>'
                    '<pre>{}</pre>'
                    .format(text))
        else:
            self.text_area.appendHtml('<span style="color:red">[Error] </span>'
                    '{}'
                    .format(text))


class Test(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()

        exit = QtGui.QAction('&Quit', self)        
        exit.setStatusTip("Exit application")
        exit.triggered.connect(QtGui.qApp.closeAllWindows)

        self.status = self.statusBar()

        self.menu = self.menuBar()
        file_menu = self.menu.addMenu('&File')
        file_menu.addAction(exit)

        central_widget = QtGui.QTabWidget()
        central_widget.addTab(MyTab(), "A Tab")
        self.tabs = central_widget
        
        self.setWindowTitle("Testing")    
        self.resize(700, 500)
        self.setCentralWidget(central_widget)
        self.show()


def main():
    app = QtGui.QApplication.instance()
    if app is None:
        app = QtGui.QApplication(sys.argv)

    test = Test()
    globals()['test'] = test
    globals()['app'] = app

    if not ipython:
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()
