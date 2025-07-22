from PyQt5.QtWidgets import QWidget, QVBoxLayout

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavToolbar
import matplotlib
import matplotlib.style as style

style.use('seaborn-darkgrid')
matplotlib.use('QT5Agg')

class MplCanvas(Canvas):
    def __init__(self): #parent=None, width=5, height=4, dpi=100
        self.fig = Figure()
        self.fig.set_tight_layout(True)
        #figsize=(width, height), dpi=dpi
        self.axes = self.fig.add_subplot(111)
        Canvas.__init__(self, self.fig)
        Canvas.updateGeometry(self)

class MplWidget(QWidget):
    def __init__(self, parent):#parent=None
        QWidget.__init__(self, parent)
        self.canvas = MplCanvas()
        self.vbl = QVBoxLayout()
        self.toolbar = NavToolbar(self.canvas, self)
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.second_axis =False
        '''top=0.95, bottom=0.15, left=0.16, right=0.95, hspace=0.2, wspace=0.2'''

    def tight(self):
        self.canvas.fig.set_tight_layout(True)

    def plot(self,x,y, *args, **kwargs):
        return self.canvas.axes.plot(x,y, *args, **kwargs)

    def clear_canvas(self):
        '''clear canvas'''
        self.canvas.axes.clear()

    def show_plot(self):
        '''call draw on canvas'''
        self.canvas.draw()

    def label(self, xlabel, ylabels):
        self.canvas.axes.set_xlabel(str(xlabel))

    def grid(self, *args, **kwargs):
        '''toggle grid and pass arguments as is'''
        self.canvas.axes.grid(*args, **kwargs)
