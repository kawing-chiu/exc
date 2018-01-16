"""An example of embedding a RichJupyterWidget with an in-process kernel.

We recommend using a kernel in a separate process as the normal option - see
embed_qtconsole.py for more information. In-process kernels are not well
supported.

To run this example:

    python3 inprocess_qtconsole.py
"""
import os

from qtconsole.qt import QtGui
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


def print_process_id():
    print('Process ID is:', os.getpid())

def show():
    global ipython_widget  # Prevent from being garbage collected
    print_process_id()

    # Create an in-process kernel
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel(show_banner=False)
    kernel = kernel_manager.kernel
    kernel.gui = 'qt'
    kernel.shell.push({'foo': 43, 'print_process_id': print_process_id, 'kernel': kernel})

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    ipython_widget = RichJupyterWidget()
    ipython_widget.kernel_manager = kernel_manager
    ipython_widget.kernel_client = kernel_client
    ipython_widget.show()

    return kernel


if __name__ == "__main__":
    app = QtGui.QApplication([])
    kernel = show()
    app.exec_()

    if hasattr(kernel, 'abc'):
        print("kernel.abc:", kernel.abc)




