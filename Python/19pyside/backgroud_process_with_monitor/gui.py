import sys
import os
from functools import partial
import html
import glob
import multiprocessing as mp
import queue
import threading
import logging
from logging.handlers import QueueHandler
import configparser
import time

try:
    from PySide import QtGui, QtCore
    from PySide.QtCore import Qt
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
        pyqt = True
    except ImportError:
        pyqt = False

if not (pyside or pyqt):
    sys.exit("Error: Dependency missing. Either PySide or PyQt4 must be installed")

from autoval.app import run

try:
    __IPYTHON__
    ipython = True
except NameError as e:
    ipython = False

CONFIG = './config'
LOG = './log'

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# Note that the worker process will use the same FileHandler, which may cause 
# some problem
fh = logging.FileHandler(LOG)
fh.setLevel(logging.DEBUG)
log_file_fmt = logging.Formatter(
        '[{levelname}] {processName} - {asctime} - {message}', style='{')
fh.setFormatter(log_file_fmt)
log.addHandler(fh)


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG)
    return config

def write_config(config):
    with open(CONFIG, 'w') as f:
        config.write(f)

def run(in_files, out_file):
    log.info("in_files: {}".format(in_files))
    log.info("out_file: {}".format(out_file))
    time.sleep(3)
    log.warn("oops")
    log.error("boom")

class MonitorLogHandler(QueueHandler):
    def enqueue(self, record):
        msg = record.getMessage()
        # if we want debug output:
        #if record.exc_text:
        #    if msg[-1:] != "\n":
        #        msg = msg + "\n"
        #    msg = (msg + '<pre style="font-family:monospace">{}</pre>'
        #            .format(record.exc_text))
        if record.levelno >= logging.ERROR:
            self.queue.put(('log', 'error', msg))
        elif record.levelno >= logging.WARN:
            self.queue.put(('log', 'warn', msg))
        elif record.levelno >= logging.INFO:
            self.queue.put(('log', 'info', msg))

    def emit(self, record):
        if record.levelno >= logging.INFO:
            try:
                self.enqueue(self.prepare(record))
            except Exception:
                self.handleError(record)

def run_with_gui_monitor(in_files, out_tpl, monitor_q):
    ml = MonitorLogHandler(monitor_q)
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    ml.setLevel(logging.INFO)
    root.addHandler(ml)

    run(in_files, out_tpl)
    #from time import sleep
    #sleep(5)

    monitor_q.put(('finish',))

class Monitor(QtCore.QObject):
    log_signal = QtCore.Signal(tuple)
    finish_signal = QtCore.Signal()

    def __init__(self, thread):
        super().__init__()
        self._thread = thread

        app = QtGui.QApplication.instance()
        #print('main thread:', app.thread())

        self.moveToThread(thread)
        thread.started.connect(self._run)
        self.finish_signal.connect(thread.quit)
        self.finish_signal.connect(self.deleteLater)
        thread.finished.connect(thread.deleteLater)

    @QtCore.Slot()
    def _run(self):
        self.run()
        self.finish_signal.emit()

    def run(self):
        pass

class Runner(Monitor):
    def __init__(self, thread, in_files, out_tpl):
        super().__init__(thread)

        self.in_files = in_files
        self.out_tpl = out_tpl
        self._worker_process = None
        self._end_event = None

    def run(self):
        #print("run() in thread:", QtCore.QThread.currentThread())
        q = mp.Queue()
        p = mp.Process(target=run_with_gui_monitor, name="MonthlyReportWorker",
                args=(self.in_files, self.out_tpl, q), daemon=True)
        p.start()
        self._worker_process = p
        app = QtGui.QApplication.instance()
        while True:
            try:
                data = q.get(timeout=0.05)
            except queue.Empty:
                if pyside:
                    # shit, a huge pyside bug
                    app.processEvents()
                #self.log_signal.emit(('info', 'ping'))
                continue
            cmd = data[0]
            if cmd == 'log':
                self.log_signal.emit(data[1:])
            elif cmd == 'finish':
                break

def find_dialog(type='dir', combo=None):
    if combo and combo.currentText():
        default = combo.currentText()
    else:
        default = os.path.expanduser('~')

    if type == 'dir':
        path = QtGui.QFileDialog.getExistingDirectory(None, "选择目录",
                default)
    elif type == 'file':
        if pyside:
            path, _ = QtGui.QFileDialog.getOpenFileName(None, "选择文件",
                    default)
        elif pyqt:
            path = QtGui.QFileDialog.getOpenFileName(None, "选择文件",
                    default)
    if path:
        idx = combo.findText(path)
        combo.removeItem(idx)
        combo.insertItem(0, path)
        combo.setCurrentIndex(0)
    return path

class MonthlyReportTab(QtGui.QWidget):
    CONFIG_SECNAME = 'MyTab'

    def __init__(self):
        super().__init__()

        self._running = False
        self._worker_process = None
        self._runner_thread = None
        self._runner = None
        self._init_ui()


    def _init_ui(self):
        group_box = QtGui.QGroupBox("文件路径")
        self.group_box = group_box

        browse_button1 = QtGui.QPushButton("选择目录")
        browse_button2 = QtGui.QPushButton("选择文件")
        browse_button3 = QtGui.QPushButton("选择文件")

        label1 = QtGui.QLabel("数据文件目录：")
        label2 = QtGui.QLabel("输出文件：")
        label3 = QtGui.QLabel("配置文件：")

        config = get_config()
        secname = self.CONFIG_SECNAME
        if secname in config:
            sec = config[secname]
        else:
            sec = {}
        combo1_his = sec.get('数据文件目录', '').split('|')
        combo2_his = sec.get('输出文件', '').split('|')
        combo3_his = sec.get('配置文件', '').split('|')
        combo1 = self._create_combo(combo1_his)
        combo2 = self._create_combo(combo2_his)
        combo3 = self._create_combo(combo3_his)

        browse_button1.clicked.connect(partial(find_dialog, 'dir', combo1))
        browse_button2.clicked.connect(partial(find_dialog, 'file', combo2))
        browse_button3.clicked.connect(partial(find_dialog, 'file', combo3))

        layout = QtGui.QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(combo1, 0, 1)
        layout.addWidget(browse_button1, 0, 2)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(combo2, 1, 1)
        layout.addWidget(browse_button2, 1, 2)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(combo3, 2, 1)
        layout.addWidget(browse_button3, 2, 2)

        group_box.setLayout(layout)

        start_button = QtGui.QPushButton("开始执行")
        start_button.clicked.connect(self.run)

        top_layout = QtGui.QHBoxLayout()
        top_layout.addWidget(group_box)
        top_layout.addWidget(start_button)

        text_area = QtGui.QPlainTextEdit()
        text_area.setReadOnly(True)

        main_layout = QtGui.QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(text_area)

        self.setLayout(main_layout)

        self.combo1 = combo1
        self.combo2 = combo2
        self.combo3 = combo3
        self.start_button = start_button
        self.text_area = text_area

    def _create_combo(self, hist):
        combo = QtGui.QComboBox()
        combo.setEditable(True)
        combo.setInsertPolicy(QtGui.QComboBox.InsertAtCurrent)
        combo.setSizePolicy(QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Preferred)
        combo.setSizeAdjustPolicy(
                QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        combo.setMinimumContentsLength(15)
        if hist:
            hist = [h for h in hist if h]
            combo.addItems(hist)
            #combo.setCurrentIndex(0)
        return combo

    @QtCore.Slot()
    def _process_finish(self):
        self._running = False
        self.start_button.setEnabled(True)

    @QtCore.Slot(tuple)
    def _monitor_log(self, data):
        type, msg = data 
        if type == 'info':
            self.info(msg)
        elif type == 'warn':
            self.warn(msg)
        elif type == 'error':
            self.error(msg)

    def run(self):
        self.clear_log()
        self.start_button.setEnabled(False)
        app = QtGui.QApplication.instance()
        app.processEvents()

        data_dir = self.combo1.currentText()
        if not data_dir:
            self.error("未指定数据文件目录")
            self.start_button.setEnabled(True)
            return
        out_tpl = self.combo2.currentText()
        if not out_tpl:
            self.error("未指定输出文件")
            self.start_button.setEnabled(True)
            return
        config_file = self.combo3.currentText()
        if not config_file:
            self.error("未指定配置文件")
            self.start_button.setEnabled(True)
            return

        in_files = glob.glob(os.path.join(data_dir, '*/*'))
        #in_files.extend(glob.glob(os.path.join(data_dir, '*/*.xlsx')))
        #config_dir = os.path.dirname(config_file)
        #if config_dir not in sys.path:
        #    sys.path.append(config_dir)

        self._running = True
        runner_thread = QtCore.QThread()
        runner = Runner(runner_thread, in_files, out_tpl)

        runner.finish_signal.connect(self._process_finish)
        runner.log_signal.connect(self._monitor_log)

        runner_thread.start()
        # this also works in pyqt, but not in pyside                                                                                
        #QtCore.QMetaObject.invokeMethod(runner, '_run', Qt.QueuedConnection) 

        self._runner_thread = runner_thread
        self._runner = runner

    def info(self, text, escape=False):
        if escape:
            text = html.escape(text)
        self.text_area.appendHtml(
                '<span style="color:green">[Info] </span>'
                '{}'
                .format(text))

    def warn(self, text, escape=False):
        if escape:
            text = html.escape(text)
        self.text_area.appendHtml('<span style="color:gold">[Warning] </span>'
                '{}'
                .format(text))

    def error(self, text, escape=False):
        if escape:
            text = html.escape(text)
        self.text_area.appendHtml('<span style="color:red">[Error] </span>'
                '{}'
                .format(text))

    def clear_log(self):
        self.text_area.clear()

    def save_config(self):
        combo1_his = [self.combo1.itemText(i) for i in range(self.combo1.count())][:7]
        combo2_his = [self.combo2.itemText(i) for i in range(self.combo2.count())][:7]
        combo3_his = [self.combo3.itemText(i) for i in range(self.combo3.count())][:7]

        secname = self.CONFIG_SECNAME
        config = get_config()
        if secname not in config:
            config[secname] = {}
        sec = config[secname]
        if combo1_his:
            sec['数据文件目录'] = '|'.join(combo1_his)
        if combo2_his:
            sec['输出文件'] = '|'.join(combo2_his)
        if combo3_his:
            sec['配置文件'] = '|'.join(combo3_his)
        write_config(config)


class Window(QtGui.QMainWindow):
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
        central_widget.addTab(MonthlyReportTab(), 'MyTab')
        self.tabs = central_widget
        
        self.setWindowTitle("A very useful tool")    
        self.resize(700, 500)
        self.setCentralWidget(central_widget)
        self.show()

    def closeEvent(self, event):
        tabs = self.tabs
        for i in range(tabs.count()):
            if tabs.tabText(i) == 'MyTab':
                tab = tabs.widget(i)
                tab.save_config()

def _on_exit():
    log.debug("GUI退出")


def main():
    app = QtGui.QApplication.instance()
    if app is None:
        app = QtGui.QApplication(sys.argv)

    app.lastWindowClosed.connect(_on_exit)

    font_db = QtGui.QFontDatabase()
    fonts = ['Microsoft JhengHei UI', 'Microsoft JhengHei']
    #print(font_db.families())
    for font_name in fonts:
        if font_name in font_db.families():
            new_font = QtGui.QFont(font_name)
            app.setFont(new_font)
            break

    log.debug("GUI启动")
    window = Window()

    if not ipython:
        sys.exit(app.exec_())
    else:
        globals()['window'] = window
        globals()['app'] = app

if __name__ == '__main__':
    main()


