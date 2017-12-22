import sys

import matplotlib as mpl
mpl.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import \
    FigureCanvasQTAgg as Qt5FigureCanvas
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from PyQt5 import QtWidgets, QtCore

import multiprocessing
#multiprocessing.freeze_support() # <- may be required on windows


def get_qt_app():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    return app

#def plot(datax, datay, name):
#    x = datax
#    y = datay**2
#    plt.scatter(x, y, label=name)
#    plt.legend()
#    plt.show()

def plot3d():
    #figsize = mpl.figure.figaspect(1/2)
    #fig = Figure(figsize=figsize)
    #canvas = Qt5FigureCanvas(fig)
    #ax = fig.add_subplot(121, projection='3d')

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Make data.
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=True)
    
    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    # import hunter; from hunter import Q
    # hunter.trace(Q(module_startswith='matplotlib'))

    #canvas.show()
    app = get_qt_app()
    print("id(app)2:", id(app))
    #app.exec_()
    
    plt.show()


def multiP():
    for i in range(1):
        #p = multiprocessing.Process(target=plot, args=(i, i, i))
        p = multiprocessing.Process(target=plot3d)
        p.start()

if __name__ == "__main__": 
    # XXX: this is important, otherwise on linux will not work
    multiprocessing.set_start_method('spawn')
    app = get_qt_app()
    print("id(app):", id(app))
    input('Value: ') 
    multiP()
