import sys
import os
from PySide import QtGui, QtCore
from PySide.QtCore import Qt

try:
    __IPYTHON__
    ipython = True
except NameError as e:
    ipython = False


def find_dir_dialog():
    dir_ = QtGui.QFileDialog.getExistingDirectory(None, "Choose a dir",
            os.path.expanduser("~/code_study"))
    print("dir_:", dir_)


class MyTab(QtGui.QWidget):
    def __init__(self):
        super().__init__()

        group_box = QtGui.QGroupBox("File paths")
        self.group_box = group_box

        browse_button1 = QtGui.QPushButton("choose dir")
        browse_button2 = QtGui.QPushButton("choose file")
        browse_button1.clicked.connect(find_dir_dialog)

        label1 = QtGui.QLabel("Directory:")
        label2 = QtGui.QLabel("File:")

        combo1 = QtGui.QComboBox()
        combo1.setEditable(True)
        combo1.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        combo2 = QtGui.QComboBox()
        combo2.setEditable(True)
        combo2.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        self.combo1 = combo1
        self.combo2 = combo2

        layout = QtGui.QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(combo1, 0, 1)
        layout.addWidget(browse_button1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(combo2, 1, 1)
        layout.addWidget(browse_button2, 1, 2)

        group_box.setLayout(layout)

        start_button = QtGui.QPushButton("start")

        top_layout = QtGui.QHBoxLayout()
        top_layout.addWidget(group_box)
        top_layout.addWidget(start_button)

        text_area = QtGui.QPlainTextEdit()
        text_area.setReadOnly(True)
        text_area.appendPlainText('hehe')
        text_area.appendHtml('<span style="color:red">[Error] </span>blahblah')
        self.text_area = text_area

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(text_area)

        self.setLayout(main_layout)


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
        #self.setGeometry(300, 300, 300, 200)
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
